#!/usr/bin/env python3
"""Enrich session_log.csv with ASN & country for IPs lacking data.
Usage:
  ./asn_enrich.py --in session_log.csv --out session_log_enriched.csv

Behavior:
  - Reads the input CSV (header: utc_timestamp,ip,asn,country,ua,path,token,notes)
  - For any row where asn or country is blank, resolves via ipapi.co (HTTPS JSON)
  - Caches lookups in ip_cache.json to avoid repeat network calls
  - Writes a new CSV (does not overwrite source unless --out == --in)

Notes:
  - Network calls are rate-limited by the public service; heavy use may require an API key / self-hosted DB.
  - If the service fails or times out, leaves fields blank and continues.
  - Safe to re-run incrementally as new rows are appended.
"""
import argparse
import csv
import json
import pathlib
import time
import urllib.request
import urllib.error

CACHE_PATH = pathlib.Path('ip_cache.json')

def load_cache():
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text())
        except Exception:
            return {}
    return {}

def save_cache(cache):
    try:
        CACHE_PATH.write_text(json.dumps(cache, indent=2))
    except Exception:
        pass

def lookup_ip(ip: str, cache: dict, timeout: float = 4.0):
    if ip in cache:
        return cache[ip]
    url = f'https://ipapi.co/{ip}/json/'
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:  # nosec B310 (simple metadata fetch)
            data = json.loads(resp.read().decode('utf-8', 'ignore'))
            asn = data.get('asn', '')
            country = data.get('country_name') or data.get('country', '')
            cache[ip] = {'asn': asn, 'country': country}
            return cache[ip]
    except urllib.error.URLError:
        cache[ip] = {'asn': '', 'country': ''}
    except Exception:
        cache[ip] = {'asn': '', 'country': ''}
    return cache[ip]

def enrich(rows):
    cache = load_cache()
    updated = []
    for r in rows:
        ip = r.get('ip','').strip()
        # Only enrich if we have an IP and missing data
        if ip and (not r.get('asn') or not r.get('country')):
            info = lookup_ip(ip, cache)
            if not r.get('asn'):
                r['asn'] = info.get('asn','')
            if not r.get('country'):
                r['country'] = info.get('country','')
            time.sleep(0.2)  # light throttle
        updated.append(r)
    save_cache(cache)
    return updated

def main():
    ap = argparse.ArgumentParser(description='Enrich session log with ASN & country information.')
    ap.add_argument('--in', dest='inp', required=True, help='Input session_log.csv path')
    ap.add_argument('--out', dest='out', required=True, help='Output CSV path')
    args = ap.parse_args()
    inp = pathlib.Path(args.inp)
    if not inp.exists():
        ap.error('Input file does not exist')
    rows = []
    with inp.open() as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames or []
        needed = ['utc_timestamp','ip','asn','country','ua','path','token','notes']
        # basic header validation / expansion
        for n in needed:
            if n not in fieldnames:
                fieldnames.append(n)
        for row in r:
            # ensure all keys present
            for n in needed:
                row.setdefault(n,'')
            rows.append(row)
    enriched = enrich(rows)
    outp = pathlib.Path(args.out)
    with outp.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['utc_timestamp','ip','asn','country','ua','path','token','notes'])
        w.writeheader()
        for row in enriched:
            w.writerow(row)
    print(f'Wrote enriched log: {outp} (rows: {len(enriched)})')

if __name__ == '__main__':
    main()
