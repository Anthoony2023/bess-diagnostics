#!/usr/bin/env python3
"""Check the published case files and summary arithmetic; not the raw analysis.

Python 3.10+; standard library only. By default this command is read-only.
--write-manifest intentionally updates MANIFEST.csv after local edits.
--json writes a deterministic report, preferably outside the case directory.
"""
from __future__ import annotations

import argparse
import calendar
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import unquote, urlsplit

IGNORED_PARTS = {'.git', '__pycache__', '.DS_Store', 'Thumbs.db'}
MANIFEST = 'MANIFEST.csv'
REQUIRED = {
    'data/operating_profile_2022_2024.csv': ['year', 'charge_MWh', 'discharge_MWh', 'abs_throughput_MWh', 'command_abs_MWh', 'actual_abs_over_command_abs'],
    'data/power_vi_unit_validation_2017_2025.csv': ['year', 'VI_over_raw_power_median', 'raw_as_kW_error_median_pct', 'raw_as_W_error_median_pct', 'sign_agreement_pct'],
    'data/coverage_quality_2017_2025.csv': ['year', 'stream', 'screened_valid_power_hours', 'calendar_year_fraction_pct', 'gap_gt5_intervals'],
    'data/dcir_summary_2017_2025.csv': ['year', 'all_events', 'soc_match_pct', 'common_events', 'common_R_string_mohm_p25', 'common_R_string_mohm_p50', 'common_R_string_mohm_p75', 'common_R_per_cell_mohm_p50', 'common_R_vs_2018_pct'],
    'data/dcir_direction_check_2017_2025.csv': ['year', 'common_c2d_events', 'common_d2c_events', 'common_c2d_R_string_mohm_p50', 'common_d2c_R_string_mohm_p50'],
    'data/matched_tracking_support_2022_2024.csv': ['year', 'paired_timestamp_mismatch_rows', 'valid_pq_command_hours', 'common_condition_hours', 'slow_common_condition_hours'],
    'data/matched_tracking_common_condition_slow_ramp_2022_2024.csv': ['year', 'direction', 'setpoint_bin_kW', 'hours', 'tracking_ratio_projected', 'same_sign_pct', 'under90_pct', 'within10_pct'],
    'data/residual_discharge_decomposition_2022_2024.csv': ['year', 'setpoint_band_kW', 'common_cells', 'matched_support_hours', 'ac_tracking_ratio', 'dc_to_setpoint_ratio', 'ac_over_dc_ratio', 'ac_MAE_kW', 'mean_cell_voltage_V', 'mean_current_A'],
    'evidence/counter_anomaly_examples.csv': ['year', 'pre_value', 'spike_value', 'post_value', 'swap16_of_pre_value', 'spike_equals_16bit_word_swap', 'return_seconds', 'source_locator_status'],
    'evidence/evidence_matrix.csv': ['evidence_id', 'claim', 'public_evidence'],
    'evidence/data_trust_table.csv': ['signal', 'trust_assessment', 'evidence', 'caveat'],
}


def distributed_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob('*') if p.is_file()
                  and not any(x in IGNORED_PARTS for x in p.relative_to(root).parts))


def read_table(path: Path, required: list[str] | None = None) -> list[dict[str, str]]:
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        if len(fields) != len(set(fields)):
            raise ValueError(f'{path.name}: duplicate column names')
        if required and not set(required).issubset(fields):
            raise ValueError(f'{path.name}: missing required columns')
        rows = list(reader)
        if not rows or any(None in row or any(v is None for v in row.values()) for row in rows):
            raise ValueError(f'{path.name}: empty or malformed CSV')
        return rows


def number(row: dict[str, str], key: str) -> float:
    value = float(row[key])
    if not math.isfinite(value):
        raise ValueError(f'Non-finite value in {key}')
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def near(a: float, b: float, tolerance: float, message: str) -> None:
    require(abs(a - b) <= tolerance, f'{message}: {a} vs {b}')


def unique(rows: list[dict[str, str]], keys: tuple[str, ...]) -> None:
    identities = [tuple(row[k] for k in keys) for row in rows]
    require(len(identities) == len(set(identities)), f'Duplicate records for {keys}')


def write_manifest(root: Path) -> None:
    """Rebuild hashes after intentional edits; this is not scientific approval."""
    with (root / MANIFEST).open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=['path', 'bytes', 'sha256'], lineterminator='\n')
        writer.writeheader()
        for path in distributed_files(root):
            if path.relative_to(root).as_posix() == MANIFEST:
                continue
            require(not path.is_symlink(), f'Symlink is not supported: {path.name}')
            content = path.read_bytes()
            writer.writerow({'path': path.relative_to(root).as_posix(), 'bytes': len(content),
                             'sha256': hashlib.sha256(content).hexdigest()})


def validate(root: Path) -> dict[str, Any]:
    root = root.resolve()
    checks: list[dict[str, Any]] = []
    metrics: dict[str, Any] = {}
    tables: dict[str, list[dict[str, str]]] = {}

    def check(name: str, fn: Any) -> None:
        try:
            detail = fn()
            checks.append({'check': name, 'passed': True, 'detail': detail})
        except (ValueError, OSError, KeyError, TypeError, ZeroDivisionError, csv.Error) as exc:
            checks.append({'check': name, 'passed': False, 'detail': str(exc)})

    def manifest_check() -> str:
        rows = read_table(root / MANIFEST, ['path', 'bytes', 'sha256'])
        listed = [r['path'] for r in rows]
        require(len(listed) == len(set(listed)), 'Duplicate manifest paths')
        expected = {p.relative_to(root).as_posix() for p in distributed_files(root)} - {MANIFEST}
        require(set(listed) == expected, 'Manifest coverage differs: ' + str(sorted(set(listed) ^ expected)))
        for row in rows:
            path = (root / row['path']).resolve()
            require(path.is_relative_to(root), 'Manifest path escapes case root')
            require(not (root / row['path']).is_symlink(), 'Symlink in release')
            content = path.read_bytes()
            require(len(content) == int(row['bytes']), f'Size mismatch: {row["path"]}')
            require(hashlib.sha256(content).hexdigest() == row['sha256'], f'Hash mismatch: {row["path"]}')
        return f'{len(rows)} files covered; all sizes and SHA-256 hashes match'
    check('manifest_integrity_and_coverage', manifest_check)

    def links_check() -> str:
        count = 0
        for path in distributed_files(root):
            if path.suffix != '.md':
                continue
            text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
            for raw in re.findall(r'\]\(([^)\n]+)\)', text):
                target = raw.strip().split(' "', 1)[0].strip('<>')
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve()
                require(resolved.is_relative_to(root), f'Local link leaves case folder: {target}')
                require(resolved.is_file(), f'Broken local link in {path.name}: {target}')
                count += 1
        return f'{count} local Markdown file links resolve; remote URLs and heading anchors not tested'
    check('local_markdown_file_links', links_check)

    def schemas() -> str:
        for rel, fields in REQUIRED.items():
            tables[rel] = read_table(root / rel, fields)
        return f'{len(tables)} evidence/data CSVs parsed with required columns'
    check('csv_structure', schemas)

    def table(name: str) -> list[dict[str, str]]:
        return tables[name]

    def annual() -> str:
        rows = table('data/operating_profile_2022_2024.csv')
        unique(rows, ('year',))
        by = {r['year']: r for r in rows}
        require(set(by) == {'2022', '2023', '2024'}, 'Annual years differ')
        for row in rows:
            near(number(row, 'charge_MWh') + number(row, 'discharge_MWh'),
                 number(row, 'abs_throughput_MWh'), 2e-6, 'Charge + discharge throughput')
            near(number(row, 'abs_throughput_MWh') / number(row, 'command_abs_MWh'),
                 number(row, 'actual_abs_over_command_abs'), 1e-6, 'Annual energy quotient')
        for field, label, expected in [('abs_throughput_MWh', 'actual_energy_change_pct', -78.0),
                                       ('command_abs_MWh', 'command_energy_change_pct', -77.4)]:
            value = 100 * (number(by['2024'], field) / number(by['2022'], field) - 1)
            require(round(value, 1) == expected, 'Headline energy percentage differs')
            metrics[label] = round(value, 8)
        return 'Annual totals, quotients, and rounded headline changes agree'
    check('annual_energy_arithmetic', annual)

    def coverage() -> str:
        rows = table('data/coverage_quality_2017_2025.csv')
        unique(rows, ('year', 'stream'))
        require(len(rows) == 18, 'Expected nine years and two streams')
        for row in rows:
            h = number(row, 'screened_valid_power_hours')
            denom = 8784 if calendar.isleap(int(row['year'])) else 8760
            require(0 <= h <= denom, 'Coverage hours outside calendar year')
            near(h / denom * 100, number(row, 'calendar_year_fraction_pct'), 0.00006, 'Calendar fraction')
            require(number(row, 'gap_gt5_intervals') >= 0, 'Negative gap count')
        return '18 reported coverage fractions agree with calendar-year denominators'
    check('coverage_arithmetic', coverage)

    def dcir() -> str:
        rows = table('data/dcir_summary_2017_2025.csv')
        dirs = table('data/dcir_direction_check_2017_2025.csv')
        unique(rows, ('year',)); unique(dirs, ('year',))
        by = {r['year']: r for r in rows}; dby = {r['year']: r for r in dirs}
        require(set(by) == set(dby) == {str(y) for y in range(2017, 2026)}, 'DCIR year coverage differs')
        baseline = number(by['2018'], 'common_R_string_mohm_p50')
        for year, row in by.items():
            p25, p50, p75 = [number(row, 'common_R_string_mohm_' + x) for x in ('p25', 'p50', 'p75')]
            require(0 < p25 <= p50 <= p75, 'Invalid DCIR quartile order')
            require(0 < number(row, 'common_events') <= number(row, 'all_events'), 'Invalid event counts')
            require(0 <= number(row, 'soc_match_pct') <= 100, 'Invalid SOC match percentage')
            require(int(dby[year]['common_c2d_events']) + int(dby[year]['common_d2c_events']) == int(row['common_events']), 'Direction counts do not sum')
            near(p50 / baseline * 100, number(row, 'common_R_vs_2018_pct'), 5e-6, '2018 index')
            if year != '2023':
                divisor = 300 if int(year) < 2023 else 299
                near(p50 / divisor, number(row, 'common_R_per_cell_mohm_p50'), 1e-6, 'Per-cell normalization')
        change = 100 * (number(by['2024'], 'common_R_string_mohm_p50') / number(by['2022'], 'common_R_string_mohm_p50') - 1)
        require(round(change, 1) == 15.1, 'DCIR headline differs')
        for direction in ('c2d', 'd2c'):
            key = f'common_{direction}_R_string_mohm_p50'
            require(number(dby['2024'], key) > number(dby['2022'], key), 'Direction rise does not hold')
        metrics['string_dcir_change_pct'] = round(change, 8)
        return 'Counts, quartiles, 2018 indices, two directions, and non-mixed-year normalization agree; 2023 mixed normalization not reconstructed'
    check('dcir_summary_consistency', dcir)

    def tracking() -> str:
        rows = table('data/matched_tracking_common_condition_slow_ramp_2022_2024.csv')
        support = table('data/matched_tracking_support_2022_2024.csv')
        unique(rows, ('year', 'direction', 'setpoint_bin_kW')); unique(support, ('year',))
        require(len(rows) == 33, 'Unexpected broad-bin row count')
        fractions = {}
        for s in support:
            relevant = [r for r in rows if r['year'] == s['year']]
            near(sum(number(r, 'hours') for r in relevant), number(s, 'slow_common_condition_hours'), 4e-6, 'Tracking support sum')
            require(0 <= number(s, 'slow_common_condition_hours') <= number(s, 'common_condition_hours') <= number(s, 'valid_pq_command_hours'), 'Support nesting violated')
            fractions[s['year']] = round(100 * number(s, 'slow_common_condition_hours') / number(s, 'valid_pq_command_hours'), 8)
        for row in rows:
            require(number(row, 'hours') > 0, 'Non-positive support')
            number(row, 'tracking_ratio_projected')
            for field in ('same_sign_pct', 'under90_pct', 'within10_pct'):
                require(0 <= number(row, field) <= 100, 'Invalid tracking percentage')
        metrics['slow_subset_pct_of_valid_pq_command_hours'] = fractions
        ranges = {}
        for year in ('2022', '2024'):
            values = [100 * number(r, 'tracking_ratio_projected') for r in rows if r['year'] == year and r['setpoint_bin_kW'] in {'50-100','100-150','150-200','200-300'}]
            ranges[year] = [round(min(values), 2), round(max(values), 2)]
        require(ranges == {'2022':[95.24,99.88], '2024':[97.20,99.75]}, 'Headline bin range differs')
        metrics['projected_tracking_bin_ranges_pct'] = ranges
        sparse = {}
        for row in rows:
            if row['year'] in {'2023','2024'} and row['direction'] == 'discharge' and row['setpoint_bin_kW'] == '450-700':
                seconds = number(row, 'hours') * 3600
                require(round(seconds) == (27 if row['year']=='2023' else 26), 'Sparse support differs')
                sparse[row['year']] = round(seconds, 4)
        metrics['sparse_high_power_support_seconds'] = sparse
        return '33 broad-bin rows, support sums, nested reported support, bin ranges, and sparse-hour conversions agree'
    check('tracking_support_and_headlines', tracking)

    def residual() -> str:
        rows = table('data/residual_discharge_decomposition_2022_2024.csv')
        unique(rows, ('year','setpoint_band_kW'))
        require(len(rows)==6, 'Unexpected residual row count')
        cols = ['ac_tracking_ratio','dc_to_setpoint_ratio','ac_over_dc_ratio','ac_MAE_kW','mean_cell_voltage_V','mean_current_A']
        for band in ('100-200','200-450','100-450'):
            pair = [r for r in rows if r['setpoint_band_kW']==band]
            require(len(pair)==2, 'Residual pair missing')
            near(number(pair[0],'matched_support_hours'),number(pair[1],'matched_support_hours'),1e-6,'Residual paired support')
            require(pair[0]['common_cells']==pair[1]['common_cells'],'Residual bin counts differ')
            for r in pair:
                require(number(r,'matched_support_hours')+1e-6 >= number(r,'common_cells')*0.05, 'Minimum common support inconsistent')
        for year in ('2022','2024'):
            parts = [r for r in rows if r['year']==year and r['setpoint_band_kW']!='100-450']
            total = next(r for r in rows if r['year']==year and r['setpoint_band_kW']=='100-450')
            h = sum(number(r,'matched_support_hours') for r in parts)
            near(h,number(total,'matched_support_hours'),2e-6,'Residual support addition')
            require(sum(int(r['common_cells']) for r in parts)==int(total['common_cells']),'Residual bin addition')
            for col in cols:
                weighted = sum(number(r,col)*number(r,'matched_support_hours') for r in parts)/h
                near(weighted,number(total,col),2e-6,'Residual weighted aggregation '+col)
        metrics['residual_above_unity_ac_dc_rows'] = sum(number(r,'ac_over_dc_ratio')>1 for r in rows)
        return 'Band supports, bin counts, and published weighted aggregates agree; above-unity AC/DC remains an unresolved flag'
    check('residual_summary_aggregation', residual)

    def counters() -> str:
        rows = table('evidence/counter_anomaly_examples.csv')
        require(len(rows)==4,'Expected four counter excerpts')
        for row in rows:
            n=int(row['pre_value'])
            require(0<=n<2**32,'Counter outside uint32')
            swapped=((n & 0xffff)<<16)|(n>>16)
            require(swapped==int(row['spike_value'])==int(row['swap16_of_pre_value']),'Word-swap arithmetic differs')
            require(n==int(row['post_value']),'Counter does not return in excerpt')
            require(row['spike_equals_16bit_word_swap'].lower()=='true','Word-swap flag differs')
            require(number(row,'return_seconds')==1.0,'Published return duration differs')
            require('partial' in row['source_locator_status'].lower(),'Locator disclosure missing')
        return '4/4 excerpt word-swap equalities and return values agree; occurrence dates are not verified'
    check('counter_excerpt_arithmetic', counters)

    def unit_table() -> str:
        rows=table('data/power_vi_unit_validation_2017_2025.csv')
        unique(rows,('year',))
        require({r['year'] for r in rows}=={str(y) for y in range(2017,2026)},'Unit-audit year coverage differs')
        for row in rows:
            require(1.001<number(row,'VI_over_raw_power_median')<1.006,'Unit ratio outside reported range')
            require(0.17<number(row,'raw_as_kW_error_median_pct')<0.47,'kW error outside headline range')
            require(99.89<number(row,'raw_as_W_error_median_pct')<99.91,'W error outside headline range')
            require(99.99<number(row,'sign_agreement_pct')<=100,'Sign agreement outside reported range')
        return '9 yearly unit-summary values match the headline ranges; raw samples and calibration not checked'
    check('unit_summary_ranges', unit_table)

    def evidence_links() -> str:
        rows=table('evidence/evidence_matrix.csv')
        unique(rows,('evidence_id',))
        require({r['evidence_id'] for r in rows}=={f'E{i:02d}' for i in range(1,8)},'Evidence IDs differ')
        for row in rows:
            p=(root/row['public_evidence']).resolve()
            require(p.is_relative_to(root) and p.is_file(),'Missing evidence-matrix file')
        return '7 evidence IDs point to existing local files'
    check('evidence_matrix_targets', evidence_links)

    def release_files() -> str:
        version=(root/'VERSION').read_text().strip()
        require(version=='3.2','Unexpected package version')
        pdf=root/'Case-003_Technical_Brief.pdf'
        require(pdf.read_bytes().startswith(b'%PDF-'),'Missing/invalid PDF signature')
        for name in ('figure_01_dispatch_vs_throughput.png','figure_02_common_condition_dcir.png'):
            require((root/'figures'/name).read_bytes().startswith(b'\x89PNG\r\n\x1a\n'),'Invalid figure signature')
        return 'Version 3.2, one technical-brief PDF signature, and two PNG signatures present; visual appearance is not checked'
    check('release_artifact_signatures', release_files)

    return {
        'package_version':'3.2',
        'scope':'Package integrity and published-summary consistency only; not raw-data reproduction, causal validation, or operational certification.',
        'passed':all(c['passed'] for c in checks),
        'checks_passed':sum(c['passed'] for c in checks),
        'checks_total':len(checks),
        'distributed_file_count':len(distributed_files(root)),
        'checks':checks,
        'metrics_recalculated_from_published_tables':metrics,
        'limitations':[
            'Counter examples have partial source locators; full UTC dates are not published.',
            'Original raw analysis, sensor calibration, row-level masks, and fine-cell/event data are not reproduced.',
            '2023 mixed-cell normalization and the precise bypass cutoff are not independently verified.',
            'AC/DC above 1 remains unresolved; no efficiency or battery-loss attribution is validated.',
            'The standard-library checker does not test PDF layout, remote URL availability, or parent-repository settings.',
        ]
    }


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--write-manifest',action='store_true',help='Intentionally rebuild MANIFEST.csv after edits')
    parser.add_argument('--json',type=Path,help='Save report, preferably outside the case directory')
    args=parser.parse_args()
    if not args.root.is_dir():
        parser.error('Case root is not a directory')
    if args.json and args.json.resolve().is_relative_to(args.root.resolve()):
        parser.error('--json must point outside the case directory to avoid changing manifested files')
    try:
        if args.write_manifest:
            write_manifest(args.root)
        result=validate(args.root)
        if args.json:
            args.json.parent.mkdir(parents=True,exist_ok=True)
            args.json.write_text(json.dumps(result,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
    except (OSError,ValueError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr)
        return 2
    for item in result['checks']:
        print(('PASS' if item['passed'] else 'FAIL')+' '+item['check']+': '+item['detail'])
    print(f"{result['checks_passed']}/{result['checks_total']} checks passed. Scope: published summaries and package files only.")
    return 0 if result['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
