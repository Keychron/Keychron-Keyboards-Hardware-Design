# Q Series — Hardware Design Files

> The original fully customizable mechanical keyboard series with gasket mount, QMK/VIA support, and full CNC aluminum construction.

Part of the [Keychron Keyboards Hardware Design](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design) repository.

## Available Models

| Model | Layout | Size | Firmware |
|---|---|---|---|
| [Q0 Plus](./Q0%20Plus/README.md) | Numpad | — | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q0_plus) |
| [Q1](./Q1/README.md) | 75% | 82-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q1) |
| [Q2](./Q2/README.md) | 65% | 68-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q2) |
| [Q3](./Q3/README.md) | TKL | 87-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q3) |
| [Q4](./Q4/README.md) | 60% | 61-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q4) |
| [Q5](./Q5/README.md) | 96% | 97-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q5) |
| [Q6](./Q6/README.md) | Full-size | 108-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q6) |
| [Q7](./Q7/README.md) | 70% | 72-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q7) |
| [Q8](./Q8/README.md) | Alice | 69-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q8) |
| [Q9](./Q9/README.md) | 40% | 52-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q9) |
| [Q10](./Q10/README.md) | 75% Alice | 82-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q10) |
| [Q11](./Q11/README.md) | 75% Split | 84-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q11) |
| [Q12](./Q12/README.md) | 96% | 100-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q12) |
| [Q60](./Q60/README.md) | 60% | 64-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q60) |
| [Q65](./Q65/README.md) | 65% | 68-key | [Link](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron/q65) |

## Current Product Lineup

As of April 8, 2026, the Keychron Q collection includes the following Q series products:

- [Q0](https://www.keychron.com/products/keychron-q0-qmk-custom-number-pad)
- [Q0 Plus](https://www.keychron.com/products/keychron-q0-plus-qmk-custom-number-pad)
- [Q1](https://www.keychron.com/products/keychron-q1)
- [Q2](https://www.keychron.com/products/keychron-q2-qmk-custom-mechanical-keyboard)
- [Q3](https://www.keychron.com/products/keychron-q3-qmk-custom-mechanical-keyboard)
- [Q4](https://www.keychron.com/products/keychron-q4-qmk-via-custom-mechanical-keyboard)
- [Q5](https://www.keychron.com/products/keychron-q5-qmk-custom-mechanical-keyboard)
- [Q6](https://www.keychron.com/products/keychron-q6-qmk-custom-mechanical-keyboard)
- [Q7](https://www.keychron.com/products/keychron-q7-qmk-custom-mechanical-keyboard)
- [Q8](https://www.keychron.com/products/keychron-q8-alice-layout-qmk-custom-mechanical-keyboard)
- [Q9](https://www.keychron.com/products/keychron-q9-qmk-custom-mechanical-keyboard)
- [Q10](https://www.keychron.com/products/keychron-q10-alice-layout-qmk-custom-mechanical-keyboard)
- [Q11](https://www.keychron.com/products/keychron-q11-qmk-custom-mechanical-keyboard)
- [Q12](https://www.keychron.com/products/keychron-q12-qmk-custom-mechanical-keyboard)
- [Q60](https://www.keychron.com/products/keychron-q60-qmk-custom-mechanical-keyboard)
- [Q65](https://www.keychron.com/products/keychron-q65-qmk-custom-mechanical-keyboard)

If there is a Q series model or variant you would like to see added to this repository, please contact Keychron or [open a file request](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design/issues/new?template=file-request.yml).

## Download Files

| File | Description | Format |
|---|---|---|
| **Top Case and Bottom Case** | 3D CAD model of the keyboard enclosure | STEP |
| **Plate** | Switch mounting plate with cutout dimensions | DXF / PDF |
| **Encoder / Knob** | Rotary encoder housing and knob (knob models only) | STEP |
| **Full Model** | Complete assembled 3D model — case + plate + keycaps | STEP |
| **Stabilizer** | Stabilizer housing and wire specifications | STEP |
| **OSA Keycap** | OSA-profile keycap 3D models | STEP |

## Opening the Files

| Format | Free Software | Commercial Software |
|---|---|---|
| `.stp` | FreeCAD, Onshape (browser) | Fusion 360, SolidWorks |
| `.dxf` | LibreCAD, QCAD | AutoCAD, DraftSight |
| `.pdf` | Any PDF viewer | — |

## Directory Structure

```
Q-Series/
├── Q0 Plus/
├── Q1/
├── Q2/
├── Q3/
├── Q4/
├── Q5/
├── Q6/
├── Q7/
├── Q8/
├── Q9/
├── Q10/
├── Q11/
├── Q12/
├── Q60/
├── Q65/
└── README.md
```

## Board Revisions

Some Q-Series models include files for multiple board revisions, indicated by letter suffixes:

- **Q3:** Revision A (original) and B (updated)
- **Q5:** Revision A (original) and B (updated, knob version)
- **Q6:** Revision B and C

Revision differences typically involve PCB layout changes, updated stabilizer positions, or additional features (e.g., knob support). Both revisions are provided so community members can work with whichever version matches their board.

## License

This project is **source-available**. All design files are provided for personal, educational, and non-commercial use only. **Commercial use is strictly prohibited.**

See the [LICENSE](../LICENSE) file for full terms.

## Links

- [Keychron Q Series](https://www.keychron.com/collections/keychron-q-series-keyboard)
- [Open Source Design Center](https://www.keychron.com/collections/keychron-open-source)
- [Q Series Firmware (QMK)](https://github.com/Keychron/qmk_firmware/tree/master/keyboards/keychron)
- [Main Repository](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)
