# Subterranean Field Records & Spatial Root Zone Interventions

**Lead Practitioner:** George Steward, ISA Certified Arborist (`TX-362025A`, Oak Wilt Qualified)  
**Practice:** [Soil Grower](https://soilgrower.com) | **Interactive GIS Map & Photo Chronology:** [soilgrower.com/showcase](https://soilgrower.com/showcase/)

---

## Overview

Ecological restoration in working landscapes and urban forests begins beneath the soil surface. This repository contains the open spatial dataset (`GeoJSON`), JSON Schema specifications, and soil-physics primers backing the [Soil Grower Spatial Showcase](https://soilgrower.com/showcase/).

Every record documents a verified field intervention across Central Texas watersheds (San Gabriel River Basin, Shoal Creek, Brushy Creek, Barton Creek / Edwards Recharge Zone, and the Colorado and Brazos River basins), covering supersonic pneumatic soil fracturing (`AirSpade 2000` at `90 PSI`), surgical root collar excavations (`RCX`), stem-girdling root remediation, and rhizosphere carbon sponge establishment.

---

## Programmatic & Dataset Metrics

| Metric | Program Aggregate (`showcase_manifest`) | Open Spatial Dataset (`17 Parcel Records`) |
| :--- | :--- | :--- |
| **Critical Root Zone (CRZ) Evaluated** | `36,800+ sq ft` (Program baseline) | `55,050 sq ft` (Summed across 17 case records) |
| **Pneumatic Soil Decompaction Area** | `465 cu yd` subsurface fractured | `48,050 sq ft` (`6 to 18 in` depth) |
| **Biological & Carbon Amendments** | `108.5 cu yd` thermal compost & humates | `85,000 gal` stormwater infiltration capacity |
| **Specimen Trees Stabilized** | `74` mature canopy specimens | `45` primary documented specimens |
| **Diagnostic Compaction Standard** | `ASTM D3441` (`> 300 PSI` pre-treatment) | `< 150 PSI` post-treatment target (`80 to 95 PSI` typical) |

*(Note: All spatial coordinates in `data/central_texas_interventions.geojson` carry a corridor-level privacy offset to protect private landowner identities while preserving watershed and soil-series fidelity.)*

---

## First Principles: Why Root Flares Must Breathe

1. **Soil Compaction & Bulk Density (`> 300 PSI` / `> 1.6 g/cm3`):**  
   Feeder root elongation slows sharply above `150 PSI` and arrests when soil penetrometer resistance exceeds `300 PSI`. Supersonic pneumatic excavation (`90 PSI`) fractures compacted clay and calcareous hardpan along natural cleavage planes, restoring macropore gas exchange without tearing non-woody absorbing roots (`> 2 mm`).
2. **Root Collar Lenticel Aeration (`8 to 14 inches` Buried Fill):**  
   Trunk bark tissue lacks the waterproof suberin barriers found in true root epidermis. Grade fill or mulch volcanoes trap anaerobic moisture against the trunk, suffocating phloem tissue, inviting fungal pathogens (*Phytophthora*, *Armillaria*, *Ganoderma*), and inducing adventitious stem-girdling roots (`SGRs`).
3. **Soil Carbon Sponge & Karst/Vertisol Hydrology:**  
   Incorporating screened thermal compost, humates, and porous biochar into pneumatic radial trenches builds stable soil aggregate structure, buffering root zones against sustained summer heat domes (`> 100°F`) and increasing stormwater infiltration across both Edwards Plateau karst and Blackland Prairie shrinking-swelling vertisols.

Read the full technical primer in [`primers/01_PHYSICS_OF_SOIL_SUFFOCATION.md`](primers/01_PHYSICS_OF_SOIL_SUFFOCATION.md).

---

## Repository Structure

```text
subterranean-field-records/
├── data/
│   ├── central_texas_interventions.geojson   # OGC CRS84 GeoJSON point layer (QGIS / ArcGIS / GitHub Map ready)
│   └── field_records_manifest.json           # Full structured case records with pre/post PSI & amendment volumes
├── primers/
│   └── 01_PHYSICS_OF_SOIL_SUFFOCATION.md     # Soil mechanics, ASTM D3441 thresholds, and RCX field methodology
├── schemas/
│   └── subterranean-field-record.schema.json # JSON Schema (Draft 2020-12) for root zone intervention records
└── scripts/
    └── verify_records.py                     # Deterministic verification script computing dataset totals
```

---

## Selected Field Case Summaries

* **`SG-REC-012` (San Gabriel River Basin, Georgetown, TX):**  
  *12,000 sq ft Heritage Live Oak Grove Soil Invigoration.* Site tree survey and Texas A&M AgriLife Soil Testing Laboratory analysis (Report `691815`) confirmed adequate mineral reserves and `4.91%` organic matter, proving that canopy decline was driven by physical pore compaction (`390 PSI`) and root-zone hypoxia rather than chemical nutrient deficiency. Remediated via pneumatic fracturing (`390 PSI` to `80 PSI`), `13 cu yd` compost incorporation, and `35 cu yd` native hardwood mulch cap.
* **`SG-REC-001` (Georgetown Institutional Campus Corridor, TX):**  
  *Educational Campus Heritage Oak Grove Restoration (`9,300 sq ft` CRZ).* Relieved severe student foot-traffic compaction (`360 PSI` to `85 PSI`) across four heritage *Quercus virginiana* specimens using half-CRZ pneumatic radial aeration blended with `7 cu yd` thermal compost and `10 cu yd` hardwood mulch sponge.
* **`SG-REC-004` (Central Austin Commercial Corridor, Shoal Creek Watershed):**  
  *Surgical Hardscape Conflict Resolution (`Carya illinoinensis`).* Prevented cambial necrosis and bark shockwaves on a `34-inch` legacy pecan by rejecting mechanical jackhammers; utilized supersonic AirSpade excavation to clear the root lip (`480 PSI` to `110 PSI`) prior to vertical grapple slab lift and mycorrhizal backfill.
* **`SG-REC-007` (Brazos River Basin, Waco, TX):**  
  *Blackland Vertisol Heritage Live Oak Recovery (`4,500 sq ft` CRZ).* Addressed drought-hardened smectitic clay shrink-swell shearing (`420 PSI` to `95 PSI`) by excavating `18-inch` vertical aeration columns backfilled with mineral basalt fines, humates, and `10 cu yd` organic compost.

---

## Verification

Run the zero-dependency Python verification script to validate schema invariants and recompute spatial metrics:

```bash
python3 scripts/verify_records.py
```
