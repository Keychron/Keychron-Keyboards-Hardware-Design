# Keychron Hardware Design

[![Models Uploaded](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Keychron/Keychron-Keyboards-Hardware-Design/main/.github/badges/model-count.json)](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)
[![Repo](https://img.shields.io/badge/repo-source--available-4c1)](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)
[![Docs](https://img.shields.io/badge/docs-ready-brightgreen)](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design/tree/main/docs)
[![Star this repo](https://img.shields.io/badge/GitHub-Star%20this%20repo-black?logo=github)](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)

Production-grade hardware design files for Keychron keyboards and mice.

Study real CAD. Remix plates and cases. Design compatible accessories. Learn from how real products are built.

> This project is source-available. Personal and educational use is allowed. Original compatible accessories and add-ons are not subject to the commercial-use restriction in this license, but you may not copy and sell Keychron keyboards or mice, and you may not use Keychron trademarks as your own branding.

![Keychron hardware design hero](docs/assets/hero-keychron-hardware-design.jpg)

## Latest Updates

- **2026-04-11:** Added add c3 Pro 8k, K4 HE, K8 HE, K2 QMK, Q0 HE and Q12 HE.
- **2026-04-10:** Added more K0 Max files, Q12 HE and more Q6 Max files and more keycap profiles.
- **2026-04-09:** Added K10 HE, Q6 Max and K0 Max design files. Update: make the accessories not subject to licensing.
- **2026-04:** Added Q HE and mouse design files.
- **2026-03:** Expanded K Max coverage.
- More milestone updates will be published in [GitHub Releases](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design/releases).

## Start Here

If you're new, begin with one of these paths:

- **Browse keyboard files**  
  Explore C Pro 8K, Q, Q Pro, Q HE, Q Max, Q Ultra 8K, K Pro, K Max, K HE, K QMK, V Max, and P HE models.

- **Browse mouse files**  
  Explore shell and full-model files for M and G series mice.

- **Open the files in CAD software**  
  Read the [File Format Guide](docs/file-format-guide.md) for STEP, DWG, DXF, and PDF compatibility.

- **Learn how to remix or modify a design**  
  Start with the [Getting Started Guide](docs/getting-started.md).

- **See the current filesystem inventory**  
  Open the [Repository Inventory](docs/repo-inventory.md) generated from the repo itself.

- **Contribute fixes or improvements**  
  Read [Contributing](CONTRIBUTING.md) for workflow, file standards, and submission rules.

- **Join the community**  
  Join the [Keychron Discord](https://discord.com/invite/HAYbRrTsjN) to share builds, ask questions, and help grow the hardware modding community.

- **Understand the license before building**  
  Read the [License FAQ](docs/license-faq.md).

## What You Can Do With This Repository

- Study real industrial design and hardware packaging files
- Create case, plate, and accessory remixes
- Inspect dimensions, structure, and component integration
- Build community mods and compatible add-ons
- Contribute documentation, corrections, and new variants that fit the license

## What's Inside

| Series | Type | Models | Components |
|---|---|---|---|
| **C Pro 8K Series** | Keyboard | C1 Pro 8K, C2 Pro 8K, C3 Pro 8K | Case, Plate, Full Model, Stabilizer |
| **Q Series** | Keyboard | Q0 Plus, Q1–Q12, Q60, Q65 | Case, Plate, Encoder, Full Model, Stabilizer, OSA Keycap |
| **Q Pro Series** | Keyboard | Q1 Pro–Q14 Pro (10 models) | Case, Plate, Encoder, Full Model, Stabilizer, KSA Keycap |
| **Q HE Series** | Hall Effect | Q1 HE, Q3 HE, Q5 HE, Q6 HE, Q12 HE | Plate, Full Model, selected case parts |
| **Q Max Series** | Keyboard | Q6 Max | Case, Plate, Full Model, Stabilizer |
| **Q Ultra 8K Series** | Keyboard | Q6 Ultra 8K | Plate |
| **K Pro Series** | Keyboard | K1 Pro–K17 Pro (16 models) | Case, Plate, Full Model, Stabilizer |
| **K Max Series** | Keyboard | K0 Max, K1 Max–K17 Max (12 models) | Case, Plate, Full Model, Stabilizer, Keycap on selected models |
| **K HE Series** | Hall Effect | K2 HE–K10 HE | Case, Plate, Full Model, Stabilizer, Keycap (K2 HE; other models pending) |
| **K QMK Series** | Keyboard | K2 QMK | Case, Plate, Stabilizer, Keycap |
| **L Series** | Keyboard | L1, L3 | Case, Plate, Knob, Full Model, Stabilizer |
| **V Max Series** | Keyboard | V1 Max–V10 Max | Case, Plate, Encoder, Full Model, Stabilizer, OSA Keycap |
| **P HE Series** | Hall Effect | P1 HE | Case, Plate, Full Model, Stabilizer, Keycap |
| **Mouse Series** | Mouse | M1–M7, G1, G2 (11 models) | Shell, Full Model |

**92 device models. 734+ design files. Source-available. Accessory-friendly.**
![Keychron keyboards structure design](docs/assets/keychron-keyboards-structures.webp)

## Directory Structure

```
C-Pro-8K-Series/
  C3 Pro 8K/            — Wired C Pro 8K hardware files, with C1 Pro 8K and C2 Pro 8K also present
Q-Series/
  Q0 Plus/              — Numpad files alongside Q1–Q12, Q60, and Q65
Q-HE-Series/
  Q12 HE/               — Hall Effect files alongside Q1 HE, Q3 HE, Q5 HE, and Q6 HE
Q-Pro-Series/
  Q1 Pro/               — Wireless Q-series hardware files across 10 models
Q-Max-Series/
  Q6 Max/               — Wireless Q-series case, plate, full model, and stabilizer files
Q-Ultra-8K-Series/
  Q6 Ultra 8K/          — Ultra 8K plate files
K-Pro-Series/
  K1 Pro/               — Low-profile and standard K Pro models through K17 Pro
  K8 Pro/               — Example model folder with `K8-Pro-Keycap.stp`
K-Max-Series/
  K0 Max/               — Numpad files alongside K1 Max–K17 Max keyboard models
K-HE-Series/
  K2 HE/                — Example model folder with Cherry and OSA keycap STEP files
K-QMK-Series/
  K2 QMK/               — Early K QMK hardware files with plate, case, keycap, and stabilizer assets
V-Max-Series/
  V1 Max/               — Tri-mode keyboard hardware files across V1–V10 Max
P-HE-Series/
  P1 HE/                — Lemokey Hall Effect keyboard files
L-Series/
  L1/                   — Aluminum keyboard files with plate, case, knob, and stabilizers
Mice/
  M1/                   — Shell and full model
Keycap Profiles/
  Cherry Profile/       — Reference profile docs alongside KSA, LSA, MDA, OEM, and OSA
docs/
  file-format-guide.md  — How to open and edit these files
  getting-started.md    — First-stop guide for browsing and remixing
  3d-printing-guide.md  — Practical printing guidance for compatible parts
scripts/
  repo_inventory.py     — Regenerates the repository inventory from the live tree
```

## Why This Matters

Making production hardware files available is a meaningful contribution to the broader hardware and keyboard community.

- It lowers the barrier to entry by giving hobbyists, students, and engineers real STEP and DXF files they can study, remix, and build from instead of starting from zero.
- It expands what customization can mean. With access to case, plate, and component designs, the community can explore deeper hardware changes, new materials, structural tweaks, and original variations.
- It offers real educational value. These are production-level designs, so people can learn from actual decisions around mounting systems, tolerances, and component integration.
- It helps the ecosystem grow by enabling compatible accessories, modifications, and personal projects that build around existing designs.
- It also reflects trust and transparency. Sharing internal design files signals confidence in the products and supports users as creators, not just customers.

The license is designed to support the ecosystem around Keychron products while still protecting Keychron's core hardware business. In practice, original compatible accessories and add-ons are not subject to the commercial-use restriction in this license, but copying and selling Keychron keyboards or mice, or trading on Keychron trademarks, is not allowed.

## Contributing

**Ways to contribute:**
- Fix dimensional errors or tolerances in existing models
- Add ISO layout plate variants
- Improve documentation and guides
- Report issues with downloaded files

**Note:** This project is source-available. Original compatible accessories and add-ons are not subject to the commercial-use restriction in this license. By contributing, you agree your work falls under the same license.

## License

This project is **source-available**. The files may be used for personal and educational work. Original compatible accessories and add-ons are not subject to the commercial-use restriction in this license.

**You may not use these files to copy, manufacture, sell, or distribute Keychron keyboards or mice, or substantially similar products, and you may not use Keychron trademarks as your own branding.**

See the [LICENSE](LICENSE) file for full terms.

## Links

- [Keychron Website](https://www.keychron.com)
- [Open Source Design Center](https://www.keychron.com/collections/keychron-open-source)
- [Keychron Discord Community](https://discord.com/invite/HAYbRrTsjN)
- [Keychron Firmware (QMK, main branch)](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron)
- [Keychron Firmware (Bluetooth boards)](https://github.com/Keychron/qmk_firmware/tree/bluetooth_playground/keyboards/keychron)
- [Keychron Firmware (2.4 GHz wireless boards)](https://github.com/Keychron/qmk_firmware/tree/wireless_playground/keyboards/keychron)
- [Keychron Firmware (Hall Effect boards)](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground/keyboards/keychron)
- [Keychron Firmware (ZMK)](https://github.com/Keychron/zmk)

---

*Built by [Keychron](https://www.keychron.com) — source-available hardware design files for the community.*
