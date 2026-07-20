#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    'train': ROOT / 'data' / 'train_6150.jsonl',
    'dev': ROOT / 'data' / 'dev_600.jsonl',
    'test': ROOT / 'data' / 'test_600.jsonl',
    'challenge': ROOT / 'data' / 'challenge' / 'fresh_150_v2_4class.jsonl',
}
ALLOWED = {'supported', 'partially_supported', 'contradicted', 'unverifiable'}
REQUIRED = {'example_id', 'context_id', 'domain', 'context', 'question', 'claim', 'gold_label'}

def read_jsonl(path):
    rows=[]
    for i,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise SystemExit(f'{path}:{i}: invalid JSON: {e}')
    return rows

all_contexts={}
for split,path in FILES.items():
    rows=read_jsonl(path)
    ids=[r.get('example_id') for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit(f'{split}: duplicate example_id')
    for i,r in enumerate(rows,1):
        missing=REQUIRED-r.keys()
        if missing:
            raise SystemExit(f'{split}:{i}: missing {sorted(missing)}')
        if r['gold_label'] not in ALLOWED:
            raise SystemExit(f"{split}:{i}: invalid label {r['gold_label']}")
        if not all(isinstance(r[k],str) and r[k].strip() for k in ['example_id','context_id','domain','context','question','claim','gold_label']):
            raise SystemExit(f'{split}:{i}: empty required string')
    all_contexts[split]={r['context_id'] for r in rows}
    print(split, len(rows), dict(Counter(r['gold_label'] for r in rows)), dict(Counter(r['domain'] for r in rows)))

for a,b in [('train','dev'),('train','test'),('dev','test')]:
    overlap=all_contexts[a] & all_contexts[b]
    if overlap:
        raise SystemExit(f'{a}-{b}: {len(overlap)} context_id overlap')
print('Validation passed.')
