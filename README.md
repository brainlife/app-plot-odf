[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.317-blue.svg)](https://doi.org/10.25663/brainlife.app.317)

# Generate image of ODF

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Renders PNG images of fibre orientation distribution functions (ODFs) from CSD spherical-harmonic coefficients for a chosen sub-volume, using DIPY visualisation.**

Loads the CSD FOD of the selected lmax, converts the spherical harmonics in the requested x/y/z slice ranges to ODFs on a 724-point sphere and renders them with DIPY/VTK (off-screen) as images for visual quality control. Use it to check that CSD fits look plausible, e.g. crossing fibres in the centrum semiovale; slice ranges must lie within the image.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.317](https://doi.org/10.25663/brainlife.app.317)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `csd` | `neuro/csd` | yes | Constrained spherical deconvolution FODs (one file per lmax). |

| Output | Datatype | Description |
|---|---|---|
| `images` | `generic/images` | PNG images of the ODFs in the selected sub-volume. |

| Parameter | Type | Default | Description |
|---|---|---|---|
| `lmax` | number | `8` | Spherical harmonic order of the FOD to plot (selects the lmax<N> file of the csd input). |
| `odf_scale` | string | `2` | Scale factor for the size of the rendered ODF glyphs. |
| `x_slice` | string | `121 174` | Start and end voxel indices along x of the region to render (two space-separated integers). |
| `y_slice` | string | `140 193` | Start and end voxel indices along y of the region to render (two space-separated integers). |
| `z_slice` | string | `77 78` | Start and end voxel indices along z of the region to render (two space-separated integers). |

Runtime: container `brainlife/pythonvtk:1.2`; 1 CPUs; 0.25 h walltime.

<!-- brainlife-app:end -->

This app will generate images of the fiber orientation distribution function (ODF) using Dipy.

### Authors

- Brad Caron (bacaron@utexas.edu)

### Contributors

- Soichi Hayashi (shayashi@iu.edu)

### Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations

We kindly ask that you cite the following articles when publishing papers and code using this code.

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

2. Garyfallidis E, Brett M, Amirbekian B, Rokem A, van der Walt S, Descoteaux M, Nimmo-Smith I and Dipy Contributors (2014). DIPY, a library for the analysis of diffusion MRI data. Frontiers in Neuroinformatics, vol.8, no.8.

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University

## Running the App

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.317](https://doi.org/10.25663/brainlife.app.317) via the 'Execute' tab.

### Running Locally (on your machine)

1. git clone this repo

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

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

### Sample Datasets

You can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download
```

3. Launch the App by executing 'main'

```bash
./main
```

## Output

The main output of this App is a images datatype containing png images of ODF

#### Product.json

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.   

- python3: https://www.python.org/downloads/
- dipy: https://dipy.org/
- numpy: https://numpy.org/
- nibabel: https://nipy.org/nibabel/
- xvfbwrapper: https://pypi.org/project/xvfbwrapper/

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University
