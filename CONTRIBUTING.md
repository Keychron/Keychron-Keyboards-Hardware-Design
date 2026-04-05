# Contributing to Keychron Hardware Design

Thank you for contributing to Keychron's source-available hardware project! Whether you're fixing a tolerance, adding an ISO plate variant, or improving documentation, every contribution helps.

**Important:** This project is source-available with no commercial use permitted. By submitting a contribution, you agree that your contribution will be licensed under the same Keychron Source-Available License.

## Types of Contributions

### Bug Fixes / Corrections
- Dimensional errors in STEP models
- Incorrect screw hole positions or sizes
- Plate cutout misalignment for specific switch types
- Broken or corrupted files

### New Content
- ISO layout plate variants (currently missing)
- Alternative plate materials (FR4, POM, polycarbonate)
- Community case mods and accessories
- 3D printing profiles and slicing presets
- Additional keycap profile models

### Documentation
- Better file-format guides
- Improved 3D printing instructions
- Compatibility notes for specific CAD software

## File Standards

### Naming Convention

Official files follow the pattern:
```
{Model}-{Variant}-{Component}-{Date}.{ext}
```
Examples from the repo:
- `Q1-Top-Case.stp`
- `K8-Max-US-Aluminum-Plate-20240924.dwg`
- `V2-Max-US-Full-Model-20240812.stp`
- `Stabilizer-6.25u.stp`

For community contributions, use Title-Case with hyphens, matching the model prefix:
- `Q1-ISO-Plate.dxf`
- `K8-Max-POM-Plate.stp`
- `Q5-FR4-Plate.dxf`

### Formats
- **3D models:** STEP (.stp) preferred. IGES (.iges) accepted.
- **2D drawings:** DXF (.dxf) preferred. Include a PDF export for reference.
- **Units:** Millimeters (mm). Always.
- **Origin:** Center of the PCB footprint, top surface.

### Quality Checklist
Before submitting:
- [ ] File opens without errors in FreeCAD or Fusion 360
- [ ] Dimensions are in millimeters
- [ ] File is named following the convention above
- [ ] Model is watertight (for 3D-printable components)
- [ ] No proprietary software lock-in (no .f3d-only submissions)

## How to Submit

1. **Fork** this repository
2. **Create a branch:** `git checkout -b fix/q1-plate-tolerance`
3. **Add/modify files** following the standards above
4. **Commit** with a clear message:
   ```
   fix(q1): correct plate cutout width for Cherry MX
   add(q5): ISO plate variant
   docs: add FreeCAD import guide
   ```
5. **Push** and open a **Pull Request**
6. Include a screenshot or dimension comparison in the PR description

## Large Files

This repo uses **Git LFS** for binary CAD files. Make sure you have it installed:
```bash
git lfs install
```
The repository's [`.gitattributes`](.gitattributes) file tracks the main CAD and document artifacts through LFS, including `.stp`, `.step`, `.dwg`, `.dxf`, `.pdf`, and `.zip` files.

## Code of Conduct

All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md). Be respectful, constructive, and welcoming.
