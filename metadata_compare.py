#!/usr/bin/env python3
"""Compare metadata across multiple DOCX/PDF artifacts previously logged.
Usage: ./metadata_compare.py file1 file2 [file3 ...]
Outputs a markdown table of selected fields and notes deltas.
"""
import sys
import pathlib
import json
import hashlib
import zipfile
from typing import Dict

FIELDS = ["creator","last_modified_by","application","app_version","revision","created","modified","title","author","producer","creationdate","moddate"]

try:
    from pypdf import PdfReader  # optional
except ImportError:  # pragma: no cover
    PdfReader = None


def sha256_path(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def extract_docx(p: pathlib.Path) -> Dict[str,str]:
    out={}
    try:
        with zipfile.ZipFile(p) as z:
            def r(name):
                try:
                    return z.read(name).decode('utf-8','ignore')
                except KeyError:
                    return ''
            core = r('docProps/core.xml')
            app = r('docProps/app.xml')
            import re
            patterns=[('creator','<dc:creator>(.*?)</dc:creator>'),
                      ('last_modified_by','<cp:lastModifiedBy>(.*?)</cp:lastModifiedBy>'),
                      ('revision','<cp:revision>(.*?)</cp:revision>'),
                      ('created','<dcterms:created[^>]*>(.*?)</dcterms:created>'),
                      ('modified','<dcterms:modified[^>]*>(.*?)</dcterms:modified>'),
                      ('application','<Application>(.*?)</Application>'),
                      ('app_version','<AppVersion>(.*?)</AppVersion>')]
            blob=core+app
            for k,pat in patterns:
                m=re.search(pat, blob, re.DOTALL)
                if m:
                    out[k] = m.group(1)[:120]
    except Exception as e:
        out['error']=str(e)
    return out


def extract_pdf(p: pathlib.Path) -> Dict[str,str]:
    out={}
    if not PdfReader:
        out['error']='pypdf not installed'
        return out
    try:
        r=PdfReader(str(p))
        info=r.metadata or {}
        for k in ['/Author','/Creator','/Producer','/CreationDate','/ModDate','/Title']:
            if k in info:
                out[k.strip('/').lower()]=str(info[k])[:120]
    except Exception as e:
        out['error']=str(e)
    return out


def collect(path: pathlib.Path) -> Dict[str,str]:
    meta={}
    if path.suffix.lower()=='.docx':
        meta=extract_docx(path)
    elif path.suffix.lower()=='.pdf':
        meta=extract_pdf(path)
    meta['sha256']=sha256_path(path)
    meta['file']=path.name
    return meta


def main():
    if len(sys.argv)<3:
        print('Need at least two files to compare.')
        return
    metas=[collect(pathlib.Path(p)) for p in sys.argv[1:]]
    # Build markdown table
    header=['field']+[m['file'] for m in metas]
    lines=['|'+'|'.join(header)+'|', '|'+'|'.join(['---']*len(header))+'|']
    for f in FIELDS:
        row=[f]
        for m in metas:
            row.append(m.get(f,'') )
        lines.append('|'+'|'.join(row)+'|')
    # Delta summary
    deltas=[]
    baseline=metas[0]
    for m in metas[1:]:
        changes=[f for f in FIELDS if baseline.get(f)!=m.get(f)]
        if changes:
            deltas.append({'file':m['file'],'changed_fields':changes})
    report='\n'.join(lines)+'\n\nDelta Summary:\n'+json.dumps(deltas, indent=2)
    print(report)

if __name__=='__main__':
    main()
