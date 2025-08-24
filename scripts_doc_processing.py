#!/usr/bin/env python3
"""Utility: hash files and extract limited metadata from DOCX / PDF for logging.
Usage: ./scripts_doc_processing.py <path1> [<path2> ...]
Appends rows to evidence_log.csv (create from template first).
"""
import sys
import hashlib
import zipfile
import json
import csv
import datetime
import pathlib
from typing import Dict

EVIDENCE_LOG = pathlib.Path('counter_scam_op/evidence_log_template.csv')

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

def append_log(row: Dict[str,str]):
    exists=EVIDENCE_LOG.exists()
    with EVIDENCE_LOG.open('a', newline='') as f:
        w=csv.writer(f)
        if not exists:
            w.writerow(['artifact_id','utc_timestamp','sha256','source_channel','type','original_filename','creator','last_modified_by','application','version','notes'])
        w.writerow([row.get(k,'') for k in ['artifact_id','utc_timestamp','sha256','source_channel','type','original_filename','creator','last_modified_by','application','version','notes']])

def main():
    if len(sys.argv)<2:
        print('Provide at least one file path.')
        return
    for path in sys.argv[1:]:
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
            'source_channel': 'whatsapp',
            'type': ftype,
            'original_filename': p.name,
            'creator': meta.get('creator',''),
            'last_modified_by': meta.get('last_modified_by',''),
            'application': meta.get('application',''),
            'version': meta.get('app_version', meta.get('revision','')),
            'notes': meta.get('error','')
        }
        append_log(row)
        print(json.dumps(row, indent=2))

if __name__=='__main__':
    main()
