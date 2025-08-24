#!/usr/bin/env python3
"""Append or rebuild a rolling hash chain for a CSV evidence log.
Each line's chain_hash = SHA256(prev_chain_hash + raw_csv_line_bytes). Stored in companion JSON.
Usage: ./log_integrity_chain.py evidence_log.csv
Outputs: evidence_log.chain.json (array of objects with line_no, sha256_line, chain_hash)
"""
import sys
import pathlib
import hashlib
import json

def build_chain(csv_path: pathlib.Path):
    lines=csv_path.read_bytes().splitlines()
    chain=[]
    prev=b''
    for i, raw_line in enumerate(lines):
        if i==0 and raw_line.decode(errors='ignore').startswith('artifact_id'):  # header remains but included
            pass
        sha_line=hashlib.sha256(raw_line).hexdigest()
        chain_hash=hashlib.sha256(prev + raw_line).hexdigest()
        chain.append({'line_no':i,'sha256_line':sha_line,'chain_hash':chain_hash})
        prev=bytes.fromhex(chain_hash)
    return chain

def main():
    if len(sys.argv)<2:
        print('Provide CSV file path')
        return
    p=pathlib.Path(sys.argv[1])
    if not p.exists():
        print('Missing file')
        return
    chain=build_chain(p)
    out=p.with_suffix(p.suffix + '.chain.json')
    out.write_text(json.dumps(chain, indent=2))
    print(f'Wrote chain entries: {len(chain)} to {out.name}')

if __name__=='__main__':
    main()
