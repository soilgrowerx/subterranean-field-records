#!/usr/bin/env python3
"""
Validate and summarize Subterranean Field Intervention Records.
Computes aggregate Critical Root Zone (CRZ) area, decompacted square footage,
specimen counts, and watershed distribution directly from field_records_manifest.json.
"""

import json
from pathlib import Path
from collections import Counter


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    manifest_path = repo_root / "data" / "field_records_manifest.json"
    geojson_path = repo_root / "data" / "central_texas_interventions.geojson"

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson = json.load(f)

    projects = manifest.get("projects", [])
    features = geojson.get("features", [])

    assert len(projects) == len(features), "Mismatch between manifest and GeoJSON feature count"

    total_trees = 0
    total_crz_sqft = 0
    total_decompacted_sqft = 0
    watersheds = Counter()
    categories = Counter()

    for p in projects:
        scope = p.get("ecological_scope", {})
        total_trees += int(scope.get("trees_treated", 0))
        total_crz_sqft += int(scope.get("crz_sqft", 0))
        total_decompacted_sqft += int(scope.get("decompacted_area_sqft", 0))
        watersheds[p.get("watershed", "Unknown")] += 1
        categories[p.get("category", "Unknown")] += 1
        assert p["coordinates"].get("privacy_offset_applied") is True, f"Missing privacy offset on {p['record_id']}"

    print("=== Subterranean Field Records Verification Summary ===")
    print(f"Verified Field Interventions : {len(projects)} parcels")
    print(f"GeoJSON Spatial Features     : {len(features)} points (CRS84)")
    print(f"Summed Parcel CRZ Evaluated  : {total_crz_sqft:,} sq ft")
    print(f"Summed Pneumatic Decompaction: {total_decompacted_sqft:,} sq ft")
    print(f"Specimen Trees Documented    : {total_trees} trees")
    print("\nWatershed Distribution:")
    for ws, count in watersheds.most_common():
        print(f"  - {ws}: {count} intervention(s)")


if __name__ == "__main__":
    main()
