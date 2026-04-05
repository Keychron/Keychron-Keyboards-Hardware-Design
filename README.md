# Keychron Hardware Design

[![Models Uploaded](https://img.shields.io/badge/models%20uploaded-89-brightgreen)](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)
[![Repo](https://img.shields.io/badge/repo-source--available-4c1)](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)
[![Docs](https://img.shields.io/badge/docs-ready-brightgreen)](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design/tree/main/docs)

Production-grade hardware design files for Keychron keyboards and mice.

Study real CAD. Remix plates and cases. Design compatible accessories. Learn from how real products are built.

> This project is source-available for personal, educational, and non-commercial use. Commercial use is not allowed.

![Keychron hardware design hero](docs/assets/hero-keychron-hardware-design.jpg)

## Start Here

If you're new, begin with one of these paths:

- **Browse keyboard files**  
  Explore Q, Q Pro, Q HE, K Pro, K Max, K HE, V Max, and P HE models.

- **Browse mouse files**  
  Explore shell and full-model files for M and G series mice.

- **Open the files in CAD software**  
  Read the [File Format Guide](docs/file-format-guide.md) for STEP, DWG, DXF, and PDF compatibility.

- **Learn how to remix or modify a design**  
  Start with the [Getting Started Guide](docs/getting-started.md).

- **Contribute fixes or improvements**  
  Read [Contributing](CONTRIBUTING) for workflow, file standards, and submission rules.

- **Understand the license before building**  
  Read the [License FAQ](docs/license-faq.md).

## What You Can Do With This Repository

- Study real industrial design and hardware packaging files
- Create non-commercial case, plate, and accessory remixes
- Inspect dimensions, structure, and component integration
- Build community mods and compatible add-ons
- Contribute documentation, corrections, and new non-commercial variants

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

## Why This Matters

Making production hardware files available is a meaningful contribution to the broader hardware and keyboard community.

- It lowers the barrier to entry by giving hobbyists, students, and engineers real STEP and DXF files they can study, remix, and build from instead of starting from zero.
- It expands what customization can mean. With access to case, plate, and component designs, the community can explore deeper hardware changes, new materials, structural tweaks, and original variations.
- It offers real educational value. These are production-level designs, so people can learn from actual decisions around mounting systems, tolerances, and component integration.
- It helps the ecosystem grow by enabling compatible accessories, modifications, and personal projects that build around existing designs.
- It also reflects trust and transparency. Sharing internal design files signals confidence in the products and supports users as creators, not just customers.

The non-commercial restriction protects Keychron's business while still giving makers, learners, and enthusiasts a strong foundation for experimentation. In practice, that balance turns passive users into active contributors and helps the community learn and innovate faster.

## Contributing

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
