"""Check complete reduced normal p45 coverage using supplied residue identities."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent


def verify():
    expected = set()
    for q, lo, hi, tmax in ((18,128,191,9),(17,192,255,16)):
        for A in range(lo, hi+1):
            if A % 3 == 0:
                continue
            for t in range(1, tmax+1):
                for J in range(12,24):
                    if t*2**J < A*A+2**(46-2*q):
                        expected.update((q,A,t,J,eta) for eta in (0,1))
    result = json.loads((ROOT/'normal45_reduction_results.json').read_text())
    candidate_map = {}
    for item in result['candidates']:
        key = tuple(item[k] for k in ('q','A','t','J','eta','j'))
        assert key not in candidate_map
        candidate_map[key] = item
    seen, accounted, counts, eta_cases = set(), set(), Counter(), []
    with (ROOT/'normal45_branch_certificate.csv').open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f):
            q,A,t,J,eta = (int(row[k]) for k in ('q','A','t','J','eta'))
            key = q,A,t,J,eta
            assert key in expected and key not in seen
            seen.add(key)
            D,eps,L,u,g,cap = (int(row[k]) for k in
                               ('D','epsilon','L','u','gcd','j_cap'))
            assert 3*D == (A << q)+eps and eps in (-1,1)
            assert 2**23 <= D < 2**24 and cap == D//2**J
            assert L == 61+eta-J and u == L-2*q and 0 <= u <= q
            c,M = 3*A*A,2**u
            assert g == math.gcd(c,M)
            if eps*t % g:
                assert row['status'] == 'GCD_EXCLUSION'
                counts['gcd_exclusions'] += 1
                continue
            modulus, residue = int(row['modulus']),int(row['residue'])
            assert row['status'] == 'RECORDED_RESIDUE_CLASS'
            assert modulus == M//g and math.gcd(c//g,modulus) == 1
            assert 0 <= residue < modulus and (c*residue-eps*t)%M == 0
            start = residue if residue else modulus
            for j in range(start,cap+1,modulus):
                ckey = key+(j,)
                assert ckey in candidate_map
                item = candidate_map[ckey]
                accounted.add(ckey)
                B = t*((A << q)+eps)-3*j*A*A
                assert B % (3 << u) == 0
                X = B//(3 << u)
                assert item['X'] == X
                if not 128 <= X <= 255:
                    assert item['status'] == 'NORMALIZED_X_RANGE_EXCLUSION'
                    counts['X_range_exclusions'] += 1
                else:
                    assert int((X << 16) < D) != eta
                    assert item['status'] == 'ETA_CONSISTENCY_EXCLUSION'
                    eta_cases.append(item)
                    counts['eta_exclusions'] += 1
    assert seen == expected and accounted == set(candidate_map)
    manifest = ROOT/'payload_manifest.json'
    if manifest.exists():
        for item in json.loads(manifest.read_text())['files']:
            path = (ROOT/item['path']).resolve()
            assert path.is_relative_to(ROOT)
            data = path.read_bytes()
            assert len(data) == item['bytes']
            assert hashlib.sha256(data).hexdigest() == item['sha256']
    return dict(status='PASS_COMPLETE_NORMAL45_REDUCED_CERTIFICATE',
                branch_count=len(seen), coarse_candidates=len(accounted),
                counts=dict(counts), eta_exceptions=eta_cases,
                inversion_used=False, raw_pairs_enumerated=False,
                proof_kind='Algebraic reduction plus a complete finite certificate; pure symbolic exclusion remains open')


if __name__ == '__main__':
    print(json.dumps(verify(),indent=2))
