#!/usr/bin/env python

import re
import argparse
import os,sys
import numpy as np
import nibabel as nib
from dipy.viz import actor, window, ui
from dipy.data import get_sphere
from dipy.reconst.csdeconv import AxSymShResponse
from dipy.segment.mask import applymask
from dipy.reconst.shm import sh_to_sf
from xvfbwrapper import Xvfb
import json
from dipy.segment.mask import applymask
from dipy.reconst.shm import sh_to_sf

def plot_odf_slice(odf_src,lmax,x_slice,y_slice,z_slice,odf_scale,out_png=False):

    # start virtual display
    print("starting Xvfb");
    vdisplay = Xvfb()
    vdisplay.start()

    img_odf = nib.load(odf_src)
    data_odf = img_odf.get_data()

    slice_odf = data_odf[int(x_slice[0]):int(x_slice[1]),int(y_slice[0]):int(y_slice[1]),int(z_slice[0]):int(z_slice[1])]

    sh_order = lmax
    sphere = get_sphere('symmetric724')
    data_sf = sh_to_sf(slice_odf, sphere, sh_order)

    scale_odf = odf_scale
    size_odf = (600, 600)

    ren = window.ren()
    odf_actor = actor.odf_slicer(data_sf, sphere=sphere, scale=scale_odf, norm=False,colormap='blues')
    ren.add(odf_actor)

    ren.set_camera(
        position=(-1.38, -1.05, 93.67),
        focal_point=(-1.38, -1.05, -0.50),
        view_up=(0.00, 1.00, 0.00))

    if out_png != False:
        window.record(ren, out_path=out_png, magnification=10, size=(60, 60))
    else:
        window.show(ren, reset_camera=False)
        print('Camera Settings')
        print('Position: ', '(%.2f, %.2f, %.2f)' % my_camera.GetPosition())
        print('Focal Point: ', '(%.2f, %.2f, %.2f)' % my_camera.GetFocalPoint())
        print('View Up: ', '(%.2f, %.2f, %.2f)' % my_camera.GetViewUp())

    vdisplay.stop()

# set paths
if not os.path.exists("images"):
    os.mkdir("images")

# read json file
with open('config.json') as config_json:
    config = json.load(config_json)

# set variables
lmax = config['lmax']
odf_src = config['lmax%s' %lmax]
x_slice = config['x_slice'].split(' ')
y_slice = config['y_slice'].split(' ')
z_slice = config['z_slice'].split(' ')
odf_scale = int(config['odf_scale'])
out_png = "images/odf.png"

# create png image
plot_odf_slice(odf_src,lmax,x_slice,y_slice,z_slice,odf_scale,out_png=out_png)

