#!/usr/bin/env python3
"""Insert or verify zero-width space watermark markers.
Usage:
  Insert:  ./zero_width_watermark.py --in input.txt --out output.txt --interval 3
  Verify:  ./zero_width_watermark.py --verify file.txt
Watermark: zero-width space (\u200b) at sentence boundaries every N sentences.
"""
import argparse
import pathlib
import re
import sys
ZW='\u200b'
SENT_END=re.compile(r'([.!?])')

def insert(text:str, interval:int)->str:
    parts = []
    count = 0
    for segment in re.split(SENT_END, text):
        if not segment:
            continue
        parts.append(segment)
        if segment in '.!?':
            count+=1
            if count % interval==0:
                parts.append(ZW)
    return ''.join(parts)

def verify(text:str):
    total=text.count(ZW)
    return total

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp')
    ap.add_argument('--out')
    ap.add_argument('--interval', type=int, default=3)
    ap.add_argument('--verify')
    args=ap.parse_args()
    if args.verify:
        data=pathlib.Path(args.verify).read_text(encoding='utf-8', errors='ignore')
        print(f"Zero-width markers: {verify(data)}")
        sys.exit(0)
    if not args.inp or not args.out:
        ap.error('Insertion mode requires --in and --out')
    raw=pathlib.Path(args.inp).read_text(encoding='utf-8', errors='ignore')
    watermarked=insert(raw, args.interval)
    pathlib.Path(args.out).write_text(watermarked, encoding='utf-8')
    print('Inserted watermark markers.')

if __name__=='__main__':
    main()
