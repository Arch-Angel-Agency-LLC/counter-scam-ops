#!/usr/bin/env python3
"""Utility: hash files and extract limited metadata from DOCX / PDF for logging.
Usage: ./scripts_doc_processing.py <path1> [<path2> ...]
Appends rows to evidence_log.csv (create from template first).
"""
import argparse
import hashlib
import zipfile
import json
import csv
import datetime
import pathlib
from typing import Dict

DEFAULT_LOG = pathlib.Path('counter_scam_op/evidence_log.csv')

PDF_KEYS = ["/Title","/Author","/Creator","/Producer","/CreationDate","/ModDate"]

def sha256_file(p: pathlib.Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def extract_docx_meta(p: pathlib.Path) -> Dict[str,str]:
    out={}
    try:
        with zipfile.ZipFile(p) as z:
            def read_xml(name):
                try:
                    return z.read(name).decode('utf-8','ignore')
                except KeyError:
                    return ''
            core=read_xml('docProps/core.xml')
            app=read_xml('docProps/app.xml')
            # naive tag pulls
            import re
            for tag,key in [ ('<dc:creator>(.*?)</dc:creator>','creator'),
                             ('<cp:lastModifiedBy>(.*?)</cp:lastModifiedBy>','last_modified_by'),
                             ('<cp:revision>(.*?)</cp:revision>','revision'),
                             ('<dcterms:created[^>]*>(.*?)</dcterms:created>','created'),
                             ('<dcterms:modified[^>]*>(.*?)</dcterms:modified>','modified'),
                             ('<Application>(.*?)</Application>','application'),
                             ('<AppVersion>(.*?)</AppVersion>','app_version')]:
                m=re.search(tag, core+app, re.DOTALL)
                if m:
                    out[key]=m.group(1)[:200]
    except Exception as e:
        out['error']=str(e)
    return out

def extract_pdf_meta(p: pathlib.Path) -> Dict[str,str]:
    try:
        from pypdf import PdfReader
    except ImportError:
        return {'error':'pypdf not installed'}
    out={}
    try:
        r=PdfReader(str(p))
        info=r.metadata or {}
        for k in PDF_KEYS:
            if k in info:
                out[k.strip('/').lower()]=str(info[k])[:300]
    except Exception as e:
        out['error']=str(e)
    return out

def append_log(row: Dict[str,str], log_path: pathlib.Path):
    if log_path.name.endswith('_template.csv'):
        raise ValueError('Refusing to write into a template file. Provide a working log path.')
    exists=log_path.exists()
    with log_path.open('a', newline='') as f:
        w=csv.writer(f)
        if not exists:
            w.writerow(['artifact_id','utc_timestamp','sha256','source_channel','type','original_filename','creator','last_modified_by','application','version','notes'])
        w.writerow([row.get(k,'') for k in ['artifact_id','utc_timestamp','sha256','source_channel','type','original_filename','creator','last_modified_by','application','version','notes']])

def main():
    ap=argparse.ArgumentParser(description='Hash and log DOCX/PDF metadata')
    ap.add_argument('paths', nargs='+', help='File paths to process')
    ap.add_argument('--log', default=str(DEFAULT_LOG), help='Output CSV log path (default counter_scam_op/evidence_log.csv)')
    ap.add_argument('--channel', default='whatsapp', help='Source channel label')
    args=ap.parse_args()
    log_path=pathlib.Path(args.log)
    for path in args.paths:
        p=pathlib.Path(path)
        if not p.exists():
            print('Missing', p)
            continue
        sha=sha256_file(p)
        meta={}
        ftype='other'
        if p.suffix.lower()=='.docx':
            meta = extract_docx_meta(p)
            ftype = 'docx'
        elif p.suffix.lower()=='.pdf':
            meta = extract_pdf_meta(p)
            ftype = 'pdf'
        ts=datetime.datetime.utcnow().isoformat()+'Z'
        row={
            'artifact_id': sha[:12],
            'utc_timestamp': ts,
            'sha256': sha,
            'source_channel': args.channel,
            'type': ftype,
            'original_filename': p.name,
            'creator': meta.get('creator',''),
            'last_modified_by': meta.get('last_modified_by',''),
            'application': meta.get('application',''),
            'version': meta.get('app_version', meta.get('revision','')),
            'notes': meta.get('error','')
        }
        append_log(row, log_path)
        print(json.dumps(row, indent=2))

if __name__=='__main__':
    main()
