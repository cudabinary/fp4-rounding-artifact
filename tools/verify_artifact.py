"""Verify artifact identity and structure without importing numerical modules."""
from pathlib import Path
import ast
import csv
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]

def main():
    manifest=json.loads((ROOT/'artifact_manifest.json').read_text(encoding='utf-8'))
    listed=set()
    for entry in manifest['files']:
        relative=entry['path'];path=(ROOT/relative).resolve()
        assert path.is_relative_to(ROOT) and relative not in listed
        listed.add(relative)
        blob=path.read_bytes()
        assert len(blob)==entry['bytes'] and hashlib.sha256(blob).hexdigest()==entry['sha256']
        if path.suffix=='.json':json.loads(blob)
        if path.suffix=='.py':ast.parse(blob,filename=relative)
        if path.suffix=='.md':
            for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',blob.decode('utf-8')):
                if '://' not in link:
                    target=(path.parent/link.split('#',1)[0]).resolve()
                    assert target.is_relative_to(ROOT) and target.exists()
        if path.suffix=='.csv':
            with path.open(newline='',encoding='utf-8') as f:
                rows=list(csv.DictReader(f))
            assert rows
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
            and '.git' not in p.relative_to(ROOT).parts
            and '__pycache__' not in p.relative_to(ROOT).parts and p.suffix!='.pyc'}
    assert actual==listed|{'artifact_manifest.json'}
    row_counts={}
    for relative,expected in [('normal45/normal45_branch_certificate.csv',2814),
                              ('subnormal49/coefficient_ledger.csv',4656),
                              ('independent_r49/all_coefficient_t_branches.csv',4656),
                              ('performance/historical_nvl_performance.csv',72)]:
        with (ROOT/relative).open(newline='',encoding='utf-8') as f:count=sum(1 for _ in csv.DictReader(f))
        assert count==expected;row_counts[relative]=count
    for relative in ['normal45/normal45_reduction_results.json',
                     'normal45/normal45_branch_certificate.csv',
                     'subnormal49/coefficient_ledger.csv']:
        assert relative in listed
    assert not (ROOT/'normal45/payload_manifest.json').exists()
    assert not (ROOT/'subnormal49/payload_manifest.json').exists()
    print(json.dumps(dict(status='PASS_ARTIFACT_IDENTITY_AND_STRUCTURE',
        files=len(actual),row_counts=row_counts,numerical_modules_imported=False,
        numerical_verifiers_executed=False,GPU_or_network_used=False),indent=2))

if __name__=='__main__':main()
