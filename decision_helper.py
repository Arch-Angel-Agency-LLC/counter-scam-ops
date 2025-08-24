#!/usr/bin/env python3
"""Suggest next operational branch based on current pivot inventory.
Inputs (CLI args or prompt): counts of docx_versions, pdf_versions, portals_hit, wallet_addresses, sessions, branch_events.
Heuristics output JSON with priority ordered actions.
"""
import argparse
import json
from typing import List


def suggest(docx:int,pdf:int,portals:int,wallets:int,sessions:int,branches:int)->List[str]:
    actions=[]
    # Document leverage
    if docx<2:
        actions.append('Request editable DOCX citing formatting / signature block requirement')
    elif docx>=2 and pdf<docx:
        actions.append('Ask for consolidated final PDF after accepting tracked changes to capture new metadata')
    # Portal / IP capture
    if portals==0:
        actions.append('Send hosted logo link variant to elicit portal fetch and log IP/UA')
    elif sessions<portals:
        actions.append('Encourage revisiting earlier draft link to get repeated session for timing correlation')
    # Wallet pivot
    if wallets==0:
        actions.append('Steer toward on-chain deposit method to obtain first wallet address')
    elif wallets==1:
        actions.append('Politely claim transfer failed and request alternate wallet to build cluster')
    # Branch richness
    if branches<3:
        actions.append('Introduce low-friction delay pretext (internal review) to open another document request window')
    if sessions>=3 and wallets>=2 and docx>=2 and portals>=1:
        actions.append('Stabilize; shift to integrity packaging (hashes, chain) and prep referral dossier')
    if not actions:
        actions.append('No immediate branching needed; maintain rapport and avoid new requests')
    return actions


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--docx',type=int,default=0)
    ap.add_argument('--pdf',type=int,default=0)
    ap.add_argument('--portals',type=int,default=0)
    ap.add_argument('--wallets',type=int,default=0)
    ap.add_argument('--sessions',type=int,default=0)
    ap.add_argument('--branches',type=int,default=0)
    args=ap.parse_args()
    recs=suggest(args.docx,args.pdf,args.portals,args.wallets,args.sessions,args.branches)
    print(json.dumps({'recommendations':recs},indent=2))

if __name__=='__main__':
    main()
