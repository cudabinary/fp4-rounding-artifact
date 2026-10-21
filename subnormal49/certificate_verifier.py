"""Check supplied residues as a finite proof certificate, without inversion."""
from pathlib import Path
import csv
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent
CLASSES = {15: (1, 255, 16, 15, 42), 16: (128, 255, 4, 15, 85),
           17: (128, 191, 1, 13, 127)}


def verify():
    expected = {(q, A, t) for q, (lo, hi, cap, _, _) in CLASSES.items()
                for A in range(lo, hi + 1) for t in range(1, cap + 1)}
    seen = set()
    survivor = []
    counts = {}
    with (ROOT / 'coefficient_ledger.csv').open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            q, A, t = (int(row[name]) for name in ('q', 'A', 't'))
            key = q, A, t
            assert key in expected and key not in seen
            seen.add(key)
            D, eps, m, jcap = (int(row[name]) for name in
                               ('D', 'epsilon', 'm', 'j_cap'))
            assert m == CLASSES[q][3]
            assert 3 * D == (A << q) + eps and eps in (-1, 0, 1)
            assert 0 < D < 2**23
            assert jcap == D // 65536 <= CLASSES[q][4]
            status = row['status']
            counts[status] = counts.get(status, 0) + 1
            if eps == 0:
                assert status == 'EXACT_SCALE_DIVISIBILITY_EXCLUSION'
                assert D % (1 << q) == 0 and jcap < (1 << q)
                continue
            assert math.gcd(A, D) == 1 and D % 2 == 1
            c, M = 3 * A * A, 1 << m
            g = math.gcd(c, M)
            assert int(row['gcd']) == g
            if (eps * t) % g:
                assert status == 'GCD_EXCLUSION'
                continue
            modulus, j = int(row['modulus']), int(row['j_residue'])
            assert modulus == M // g and math.gcd(c // g, modulus) == 1
            assert modulus > CLASSES[q][4] and 0 <= j < modulus
            assert (c * j - eps * t) % M == 0
            if 1 <= j <= jcap:
                assert status == 'COARSE_CONGRUENCE_SURVIVOR'
                survivor.append((q, A, D, eps, t, j))
            else:
                assert status == 'UNIQUE_RESIDUE_OUTSIDE_CARRY_RANGE'
    assert seen == expected and len(seen) == 4656
    assert survivor == [(16, 230, 5024427, 1, 4, 51)]
    B = 4 * ((230 << 16) + 1) - 3 * 51 * 230**2
    assert B == 52199424 == 3 * 531 * 2**15
    assert 531 > 255 and 531 % 2 == 1
    manifest = ROOT / 'payload_manifest.json'
    if manifest.exists():
        for item in json.loads(manifest.read_text(encoding='utf-8'))['files']:
            path = (ROOT / item['path']).resolve()
            assert path.is_relative_to(ROOT)
            data = path.read_bytes()
            assert len(data) == item['bytes']
            assert hashlib.sha256(data).hexdigest() == item['sha256']
    return {'status': 'PASS_COMPLETE_REDUCED_CERTIFICATE',
            'coefficient_t_branches': len(seen), 'counts': counts,
            'coarse_survivors': len(survivor), 'physical_candidates': 0,
            'method': 'Residue identity and uniqueness checks; no modular inversion',
            'raw_pair_sweep': False, 'gpu_execution': False}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
