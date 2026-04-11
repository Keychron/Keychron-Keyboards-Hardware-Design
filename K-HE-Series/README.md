# K HE Series — Hardware Design Files

> Hall Effect magnetic switch variants of the K-series. Adjustable actuation, rapid trigger, and wireless connectivity for gaming and enthusiast use.

Part of the [Keychron Keyboards Hardware Design](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design) repository.

## Available Models

| Model | Layout | Size | Versions | Firmware | Status |
|---|---|---|---|---|---|
| [K2 HE](./K2%20HE/README.md) | 75% | 84-key | Standard / Special Edition / ISO / Resin Edition / All-Wood Special Edition | [Link](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground/keyboards/keychron/k2_he) | Files published |
| [K4 HE](./K4%20HE/README.md) | 96% | 100-key | Standard / Special Edition | [Link](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground/keyboards/keychron/k4_he) | Files published |
| [K6 HE](./K6%20HE/README.md) | 65% | 68-key | Standard / Special Edition | [Link](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground/keyboards/keychron/k6_he) | Folder only |
| [K8 HE](./K8%20HE/README.md) | TKL | 87-key | Standard / Special Edition | [Link](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground/keyboards/keychron/k8_he) | Files published |
| [K10 HE](./K10%20HE/README.md) | Full-size | 104-key | Standard / Special Edition | [Link](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground/keyboards/keychron/k10_he) | Files published |

`Folder only` means the model directory exists, but design files have not been uploaded yet.

## Current Product Lineup

The current K HE collection on Keychron includes the following K-series Hall Effect models and variants:

- [K2 HE](https://www.keychron.com/products/keychron-k2-he-wireless-magnetic-switch-keyboard)
- [K2 HE Resin Edition](https://www.keychron.com/products/keychron-k2-he-wireless-magnetic-switch-custom-keyboard-resin-edition)
- [K2 HE All-Wood Special Edition](https://www.keychron.com/products/keychron-k2-he-wireless-magnetic-switch-custom-keyboard-all-wood-special-edition)
- [K4 HE](https://www.keychron.com/products/keychron-k4-he-wireless-magnetic-switch-custom-keyboard)
- [K6 HE](https://www.keychron.com/products/keychron-k6-he-wireless-magnetic-switch-custom-keyboard)
- [K8 HE](https://www.keychron.com/products/keychron-k8-he-wireless-magnetic-switch-custom-keyboard)
- [K10 HE](https://www.keychron.com/products/keychron-k10-he-wireless-magnetic-switch-keyboard)

For repository organization, K2 HE variant-specific design files are grouped under the [K2 HE](./K2%20HE/README.md) directory rather than split into separate folders.

## Download Files

| File | Description | Format |
|---|---|---|
| **Top Case and Bottom Case** | 3D CAD model of the keyboard enclosure | STEP |
| **Plate** | Switch mounting plate with cutout dimensions (ANSI) | DWG / PDF |
| **US Full Model** | Complete assembled 3D model — case + plate + keycaps (ANSI) | STEP |
| **Stabilizer** | Stabilizer housing and wire specifications | STEP |
| **Keycap** | Keycap 3D models specific to this series | STEP |

## Opening the Files

| Format | Free Software | Commercial Software |
|---|---|---|
| `.stp` | FreeCAD, Onshape (browser) | Fusion 360, SolidWorks |
| `.dwg` | LibreCAD (limited), QCAD | AutoCAD, DraftSight |
| `.pdf` | Any PDF viewer | — |

## Directory Structure

```
K-HE-Series/
├── K2 HE/
├── K4 HE/
├── K6 HE/
├── K8 HE/
├── K10 HE/
└── README.md
```

## License

This project is **source-available**. Personal and educational use is allowed, and commercial use is allowed for original compatible accessories within the limits of the license.

**You may not use these files to copy, manufacture, sell, or distribute Keychron keyboards or mice, or substantially similar products, and you may not use Keychron trademarks as your own branding.**

See the [LICENSE](../LICENSE) file for full terms.

## Links

- [Open Source Design Center](https://www.keychron.com/collections/keychron-open-source)
- [K HE Series Firmware (QMK Hall Effect branch)](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground/keyboards/keychron)
- [Main Repository](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)
