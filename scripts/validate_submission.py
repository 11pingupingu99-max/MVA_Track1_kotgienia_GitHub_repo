#!/usr/bin/env python3
"""Validate the frozen Track 1 CSV against the current hackathon schema constraints."""
from pathlib import Path
import argparse, csv, math

REQUIRED=["proband_id","chrom_1","pos_1","ref_1","alt_1","chrom_2","pos_2","ref_2","alt_2","epcr"]
OPTIONAL={"finding_type","notes"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("csv", nargs="?", default="submission/kotgienia_mva-mechanism-first.csv")
    a=ap.parse_args(); path=Path(a.csv)
    with path.open(encoding="utf-8-sig", newline="") as f:
        r=csv.DictReader(f); fields=r.fieldnames or []; rows=list(r)
    missing=[x for x in REQUIRED if x not in fields]
    assert not missing, f"Missing columns: {missing}"
    assert len(rows)<=10, f"Too many rows: {len(rows)}"
    ep=[]
    for i,row in enumerate(rows,1):
        x=float(row["epcr"]); assert math.isfinite(x) and 0 < x <= 1, f"row {i}: invalid epcr"
        ep.append(x)
        if "finding_type" in row and row["finding_type"]:
            assert row["finding_type"] in {"primary","secondary"}, f"row {i}: invalid finding_type"
    assert ep==sorted(ep, reverse=True), "Rows are not pre-ranked by descending EPCR"
    assert rows and rows[0]["chrom_1"]=="chr15" and rows[0]["pos_1"]=="40209701"
    assert rows[0]["chrom_2"]=="chr15" and rows[0]["pos_2"]=="40220612"
    print(f"PASS: {path} | rows={len(rows)} | top_epcr={ep[0]:.3f}")

if __name__ == "__main__": main()
