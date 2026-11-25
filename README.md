<h1 align="center">Generate image of ODF</h1>

<p align="center">
  A PNG image of fibre orientation distribution functions (ODFs) in a chosen sub-volume, rendered from CSD spherical-harmonic coefficients with DIPY.
</p>

<p align="center">
  <a href="https://doi.org/10.25663/brainlife.app.317"><img src="https://img.shields.io/badge/brainlife.io-run%20this%20App-2b6cb0" alt="Run on brainlife.io"></a>
  <a href="https://doi.org/10.25663/brainlife.app.317"><img src="https://img.shields.io/badge/DOI-10.25663%2Fbrainlife.app.317-blue" alt="DOI"></a>
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD%20spec-v1.1-green" alt="ABCD spec v1.1"></a>
  <a href="https://dipy.org/"><img src="https://img.shields.io/badge/DIPY-orange" alt="DIPY"></a>
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT license">
</p>

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Renders PNG images of fibre orientation distribution functions (ODFs) from CSD spherical-harmonic coefficients for a chosen sub-volume, using DIPY visualisation.**

Loads the CSD FOD of the selected lmax, converts the spherical harmonics in the requested x/y/z slice ranges to ODFs on a 724-point sphere and renders them with DIPY/VTK (off-screen) as images for visual quality control. Use it to check that CSD fits look plausible, e.g. crossing fibres in the centrum semiovale; slice ranges must lie within the image.

| | |
|---|---|
| 📥 **Inputs** | `neuro/csd` |
| 📤 **Outputs** | `generic/images` |
| 🐳 **Container** | `brainlife/pythonvtk:1.2` |
| ⚙️ **Resources** | 1 CPUs · 0.25 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.317](https://doi.org/10.25663/brainlife.app.317) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `csd` | `neuro/csd` | yes | Constrained spherical deconvolution FODs (one file per lmax). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `images` | `generic/images` | PNG images of the ODFs in the selected sub-volume. |

<details>
<summary><b>⚙️ Parameters</b> (5)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `lmax` | number | `8` | Spherical harmonic order of the FOD to plot (selects the lmax<N> file of the csd input). |
| `odf_scale` | string | `2` | Scale factor for the size of the rendered ODF glyphs. |
| `x_slice` | string | `121 174` | Start and end voxel indices along x of the region to render (two space-separated integers). |
| `y_slice` | string | `140 193` | Start and end voxel indices along y of the region to render (two space-separated integers). |
| `z_slice` | string | `77 78` | Start and end voxel indices along z of the region to render (two space-separated integers). |

</details>

<!-- brainlife-app:end -->

## 🔬 How it works

The App loads the constrained spherical deconvolution (CSD) fibre orientation distribution of the chosen spherical-harmonic order (`lmax`), converts the coefficients inside the `x_slice`, `y_slice` and `z_slice` voxel ranges to ODFs on a 724-point sphere, and renders them off-screen with [DIPY](https://dipy.org/) and VTK. Use it for visual quality control of CSD fits, for example to check for crossing fibres in the centrum semiovale.

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.317](https://doi.org/10.25663/brainlife.app.317), choose a `neuro/csd` dataset from your project, set the `lmax` to plot, the glyph scale (`odf_scale`) and the voxel ranges, and press **Execute**. The image is archived to your project as a `generic/images` dataset tagged `odf`.

### 💻 Locally

You need [Singularity/Apptainer](https://apptainer.org/). `main` runs `plot_odf.py` inside the `brainlife/pythonvtk:1.2` container. Without Singularity, install Python 3 with dipy, numpy, nibabel and xvfbwrapper.

1. Clone this repository.
2. Create `config.json` with the paths to your CSD files and the region to render:

   ```json
   {
       "lmax2": "/input/csd/lmax2.nii.gz",
       "lmax4": "/input/csd/lmax4.nii.gz",
       "lmax6": "/input/csd/lmax6.nii.gz",
       "lmax8": "/input/csd/lmax8.nii.gz",
       "lmax10": "/input/csd/lmax10.nii.gz",
       "lmax12": "/input/csd/lmax12.nii.gz",
       "lmax14": "/input/csd/lmax14.nii.gz",
       "lmax": 8,
       "odf_scale": "2",
       "x_slice": "121 174",
       "y_slice": "140 193",
       "z_slice": "77 78"
   }
   ```

   Only the `lmax<N>` file that matches `lmax` is read. Each slice range is a start and end voxel index, separated by a space, and must lie within the image.

3. Run the App:

   ```bash
   ./main
   ```

### 🧪 Sample data

Download a CSD dataset from brainlife.io with the [brainlife CLI](https://github.com/brainlife/cli):

```bash
npm install -g brainlife
bl login
mkdir input
bl dataset download <dataset id>
```

## 📦 Outputs

```text
images/
└── odf.png    the rendered ODFs of the selected sub-volume
```

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Garyfallidis E, Brett M, Amirbekian B, Rokem A, van der Walt S, Descoteaux M, Nimmo-Smith I, Dipy Contributors. DIPY, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8:8 (2014).
- Generate image of ODF. brainlife.io App. [doi:10.25663/brainlife.app.317](https://doi.org/10.25663/brainlife.app.317)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## 👥 Authors

- Brad Caron

**Contributors:** Soichi Hayashi

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

MIT, Copyright (c) 2020 brainlife.io, The University of Texas at Austin and Indiana University. DIPY is distributed under its own license.
