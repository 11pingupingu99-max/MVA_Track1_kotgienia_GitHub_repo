#!/usr/bin/env python3
"""Rebuild the frozen Track 1 competition CSV from the public frozen-candidate config."""
from pathlib import Path
import argparse, csv, json

DEFAULT_FIELDS = [
    "proband_id","chrom_1","pos_1","ref_1","alt_1",
    "chrom_2","pos_2","ref_2","alt_2","epcr","finding_type","notes"
]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--config", default="config/frozen_track1_candidates.json")
    ap.add_argument("--out", default="submission/kotgienia_mva-mechanism-first.csv")
    args=ap.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding="utf-8"))
    fields=cfg.get("columns", DEFAULT_FIELDS)
    rows=cfg["rows"]
    out=Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader(); w.writerows(rows)
    print(out)

if __name__ == "__main__": main()
