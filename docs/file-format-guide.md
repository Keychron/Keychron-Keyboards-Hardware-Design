# File Format Guide

This repository includes a mix of production hardware design file types. The exact formats vary by model and series, but the most common ones are STEP, DWG, DXF, and PDF.

## STEP Files

STEP files are the main 3D exchange format used in this repository.

You can use them to:
- Inspect case and plate geometry
- Measure overall dimensions and clearances
- Import parts into other CAD tools for reference or remix work
- Build assemblies or fit-check compatible accessories

Common software that can open STEP files:
- Fusion 360
- SolidWorks
- FreeCAD
- Onshape
- Rhino

## DWG Files

DWG files are commonly used for 2D engineering drawings and production layouts.

You can use them to:
- Review drawing layouts
- Inspect dimensioned manufacturing references
- Open design data in CAD drafting tools
- Export to other formats for review or documentation

Common software that can open DWG files:
- AutoCAD
- DraftSight
- LibreCAD for limited workflows
- Fusion 360 in some workflows

## DXF Files

DXF files are widely used for 2D profile exchange, especially for plate outlines and fabrication workflows.

You can use them to:
- Inspect 2D cut profiles
- Export shapes for CNC or laser workflows
- Modify plate geometry for remixes or compatible accessories
- Share flat geometry between CAD tools

Common software that can open DXF files:
- AutoCAD
- LibreCAD
- Fusion 360
- SolidWorks
- CorelDRAW and similar vector tools for viewing only

## PDF Files

PDF files are typically provided for documentation, drawings, or reference sheets.

You can use them to:
- Review dimensions and callouts
- Share printable references
- Inspect layouts without opening a CAD program

Common software that can open PDF files:
- Adobe Acrobat
- Preview on macOS
- Any modern browser

## Recommended Workflow

If you are new to hardware files, start here:
1. Open the PDF or drawing files first to understand the part.
2. Open the STEP file to inspect the 3D model.
3. Use DXF files when working with flat plates or cut profiles.
4. Keep your work within the license: compatible accessories are allowed, but copying Keychron keyboards or mice is not.

## Compatibility Notes

- Some files may open with missing layers, units, or fonts depending on the software.
- Certain DWG and DXF files may be easier to inspect after converting or re-saving them in your preferred CAD tool.
- Imported STEP geometry may arrive as solid bodies or stitched surfaces depending on the source application.
- Always verify dimensions before fabricating any part.

## Before You Build

These files are provided under a source-available license. Review the repository license terms before manufacturing, sharing derivatives, or publishing modified files, especially if your project is commercial.
