#!/usr/bin/env python3
"""Minimal portal beacon server.
Serves /logo.png and logs requester IP, UA, timestamp to session_log.csv (create from template first).
Usage: FLASK_APP=app.py flask run --host 0.0.0.0 --port 8000
"""
from flask import Flask, send_file, request, make_response
import hashlib
import datetime
import csv
import pathlib

LOG_PATH = pathlib.Path('../session_log.csv')
LOG_HEADERS = ['utc_timestamp','remote_ip','user_agent','path','referer','etag','notes']
app = Flask(__name__)

ASSET_PATH = pathlib.Path('logo.png')
if not ASSET_PATH.exists():
    # create 1x1 transparent png
    import base64
    png_bytes=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII=')
    ASSET_PATH.write_bytes(png_bytes)


def log_event(path:str, notes:str=''):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    exists=LOG_PATH.exists()
    with LOG_PATH.open('a', newline='') as f:
        w=csv.writer(f)
        if not exists:
            w.writerow(LOG_HEADERS)
        ua=request.headers.get('User-Agent','')
        ref=request.headers.get('Referer','')
        ts=datetime.datetime.utcnow().isoformat()+'Z'
        etag=hashlib.sha256(f'{request.remote_addr}{ua}{ts}'.encode()).hexdigest()[:16]
        w.writerow([ts, request.remote_addr, ua, path, ref, etag, notes])

@app.route('/logo.png')
@app.route('/l.png')
@app.route('/asset/logo')
def logo():
    log_event('/logo.png')
    resp=make_response(send_file(str(ASSET_PATH)))
    resp.headers['Cache-Control']='no-store'
    return resp

@app.route('/')
def index():
    log_event('/', 'index')
    return 'ok'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000)
