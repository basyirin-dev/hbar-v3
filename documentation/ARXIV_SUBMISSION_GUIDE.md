# arXiv Submission Guide for H-Bar Model Paper

This document provides step-by-step instructions for submitting the H-Bar Model paper to arXiv.

## Prerequisites

1. **arXiv Account**: Create an account at [arXiv.org](https://arxiv.org/) if you don't have one
2. **Endorsement**: As a new arXiv author, you may need endorsement from an established arXiv author
3. **LaTeX Distribution**: Ensure you have a complete LaTeX installation (TeX Live 2024 or later recommended)

## File Structure for Submission

Create a submission directory with the following structure:

```
arxiv-submission/
├── paper.tex                    # Main LaTeX file
├── references.bib               # Bibliography file
├── figures/
│   ├── fig1_hbar.tex           # TikZ figures
│   ├── fig2_phases.tex
│   ├── fig3_coupled.tex
│   ├── fig4_diagnostic.tex
│   ├── fig4_protocol.tex
│   ├── hbar_main_results.png   # PNG images
│   ├── prediction_6_comparison.png
│   └── prediction_9_inflection.png
└── README.txt                   # Optional: submission notes
```

## Pre-Submission Checklist

### 1. Update Document Metadata

Before submission, update the following in `paper.tex`:

```latex
% After submission, add your arXiv ID:
% \usepackage{arxiv}
% \arxiv{XXXX.XXXXX}  % Replace with your actual arXiv ID
```

### 2. Choose arXiv Category

Select the most appropriate primary and secondary categories:

**Primary Category Options:**
- `cs.LG` - Learning and Generalization (recommended)
- `cs.AI` - Artificial Intelligence
- `cs.NE` - Neural and Evolutionary Computing
- `q-bio.NC` - Quantitative Biology > Neurons and Cognition

**Secondary Categories:**
- `cs.CL` - Computation and Language
- `cs.HC` - Human-Computer Interaction
- `stat.ML` - Machine Learning (stat)

### 3. License Selection

arXiv supports several license options:
- **arXiv.org perpetual, non-exclusive license** (default, allows arXiv to distribute)
- **Creative Commons Attribution 4.0 International (CC BY 4.0)** (recommended for open science)
- **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**
- **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**
- **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**

**Recommendation**: Use CC BY 4.0 for maximum openness and reuse.

### 4. Compile and Test Locally

Before submitting, compile the paper locally to catch any errors:

```bash
# Using latexmk (recommended)
latexmk -pdf paper.tex

# Or manually
pdflatex paper.tex
bibtex paper.aux
pdflatex paper.tex
pdflatex paper.tex
```

**Expected output**: `paper.pdf` without errors

### 5. Check for Common Issues

- [ ] All figures are included and render correctly
- [ ] Bibliography compiles without warnings
- [ ] No missing package errors
- [ ] Cross-references work correctly
- [ ] Page numbers are correct
- [ ] No font encoding issues

## Submission Process

### Step 1: Prepare Submission Package

Create a tar.gz archive of your submission:

```bash
# From the directory containing paper.tex and figures/
tar -czf hbar-arxiv-submission.tar.gz \
    paper.tex \
    references.bib \
    figures/
```

### Step 2: Upload to arXiv

1. Log in to [arXiv.org](https://arxiv.org/)
2. Click "Submit new article"
3. Select your category (e.g., Computer Science > Learning and Generalization)
4. Upload your tar.gz file
5. Fill in the submission form:
   - **Title**: The H-Bar Model: Schema-Coherence Suppression as the Origin of Compositional Generalization Failure
   - **Authors**: Basyirin Amsyar bin Basri
   - **Abstract**: Copy from paper.tex
   - **Categories**: Select primary and secondary categories
   - **License**: Choose your preferred license
   - **Comments**: Optional field for journal information, acknowledgments, etc.

### Step 3: Review and Confirm

1. arXiv will process your submission and generate a PDF preview
2. Review the PDF carefully for any formatting issues
3. If everything looks correct, confirm the submission
4. You will receive an arXiv ID (e.g., `arXiv:2603.XXXXX`)

### Step 4: Post-Submission

After receiving your arXiv ID:

1. **Update the paper.tex** with the arXiv ID (uncomment the lines in the header)
2. **Re-compile** to include the arXiv identifier in the PDF
3. **Share the preprint** on your website, social media, etc.

## Common Issues and Solutions

### Issue 1: Missing Packages

If arXiv reports missing packages, ensure all packages used are available in TeX Live. The current paper uses:

- Standard packages: `amsmath`, `amssymb`, `graphicx`, `natbib`, `hyperref`
- TikZ/PGF: `tikz`, `pgfplots`
- Additional: `cleveref`, `enumitem`, `microtype`, `booktabs`, `geometry`

All these are included in standard TeX Live distributions.

### Issue 2: Figure Rendering Problems

If TikZ figures don't render:
- Ensure all TikZ libraries are properly loaded
- Check that PNG images are in the correct format (RGB, not CMYK)
- Verify image paths are correct relative to paper.tex

### Issue 3: Bibliography Issues

If the bibliography doesn't compile:
- Ensure `references.bib` is in the submission package
- Check that all citations in the text have corresponding entries in the .bib file
- Use `plainnat` bibliography style (already set in paper.tex)

### Issue 4: Endorsement Required

If you're a new arXiv author, you may need endorsement:
- Contact an established arXiv author in your field
- They can endorse you through the arXiv system
- Alternatively, submit to a category where you have publications

## Post-Submission Updates

To update your submission:

1. Log in to arXiv
2. Go to your user dashboard
3. Find your paper and click "Submit a new version"
4. Upload the updated files
5. arXiv will assign a new version number (v2, v3, etc.)

## Additional Resources

- [arXiv Help](https://arxiv.org/help)
- [arXiv LaTeX Guidelines](https://arxiv.org/help/latex)
- [arXiv Category List](https://arxiv.org/category_taxonomy)
- [Creative Commons Licenses](https://creativecommons.org/licenses/)

## Contact

For questions about this submission guide, contact: basyirin.basri@gmail.com

---

**Last Updated**: March 2026
**Paper Version**: 3.0+ (Full Reconstruction)
