# Keychron Hardware Design — Source Available

**Open keyboards. Open mice. Source-available design files.**

This repository contains the complete industrial design files for Keychron's keyboard and mouse product lines — case models, plate drawings, stabilizer specs, encoder assemblies, and keycap profiles. Free to view, learn from, and modify for personal use. Commercial use is strictly prohibited.

## What's Inside

| Series | Type | Models | Components |
|---|---|---|---|
| **Q Series** | Keyboard | Q1–Q12, Q60, Q65| Case, Plate, Encoder, Full Model, Stabilizer, OSA Keycap |
| **Q Pro Series** | Keyboard | Q1 Pro–Q14 Pro | Case, Plate, Encoder, Full Model, Stabilizer, KSA Keycap |
| **Q HE Series** | Hall Effect | Q1 HE, Q3 HE, Q5 HE, Q6 HE | Case, Plate, Full Model, Stabilizer |
| **K Pro Series** | Keyboard | K1 Pro–K17 Pro (16 models) | Case, Plate, Full Model, Stabilizer |
| **K Max Series** | Keyboard | K1 Max–K17 Max (11 models) | Case, Plate, Full Model, Stabilizer |
| **K HE Series** | Hall Effect | K2 HE–K10 HE | Case, Plate, Full Model, Stabilizer, Keycap |
| **V Max Series** | Keyboard | V1 Max–V10 Max | Case, Plate, Encoder, Full Model, Stabilizer, OSA Keycap |
| **P HE Series** | Hall Effect | P1 HE | Case, Plate, Full Model, Stabilizer |
| **Mouse Series** | Mouse | M1–M7, G1, G2 (10 models) | Shell, Full Model |

**100+ models. 500+ design files. Source-available. No commercial use.**

## Quick Start

```bash
# Clone (uses Git LFS for binary CAD files)
git clone https://github.com/Keychron/hardware-design.git

# Or grab just one model (sparse checkout)
git clone --filter=blob:none --sparse https://github.com/Keychron/hardware-design.git
cd hardware-design
git sparse-checkout set Q-Series/Q1
```

## Opening the Files

| Format | Software |
|---|---|
| `.step` / `.stp` | FreeCAD (free), Fusion 360 (free for personal), SolidWorks, Onshape |
| `.dxf` / `.dwg` | LibreCAD (free), AutoCAD, DraftSight |
| `.pdf` | Any PDF viewer — used for 2D reference drawings |

## Directory Structure

```
keyboards/
  Q-Series/Q1/          — Case, plate, encoder, stabilizer, full model
  Q-Pro-Series/Q1 Pro/  — Same structure
  ...
Mice/
  M1/                   — Shell, full model
  ...
keycaps/
  osa-profile/          — Row-by-row keycap 3D models
  ksa-profile/
docs/
  file-format-guide.md  — How to open and edit these files
  3d-printing-guide.md  — Tips for printing cases and keycaps
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Ways to contribute:**
- Fix dimensional errors or tolerances in existing models
- Add ISO layout plate variants
- Improve documentation and guides
- Report issues with downloaded files

**Note:** This project is source-available. Commercial use is prohibited. By contributing, you agree your work falls under the same license.

## License

This project is **source-available**. All hardware design files are provided for personal, educational, and non-commercial use only.

**Commercial use is strictly prohibited.** You may not use these files, or any derivative of them, to manufacture, sell, or distribute products for profit without explicit written permission from Keychron.

See the [LICENSE](LICENSE) file for full terms.

## Links

- [Keychron Website](https://www.keychron.com)
- [Open Source Design Center](https://www.keychron.com/collections/keychron-open-source)
- [Keychron Firmware (QMK)](https://github.com/Keychron/qmk_firmware)
- [Keychron Firmware (ZMK)](https://github.com/Keychron/zmk)

---

*Built by [Keychron](https://www.keychron.com) — source-available hardware design files for the community.*
