#!/usr/bin/env python
from astropy.io import fits
from astropy.wcs import WCS
from astropy import units as u
from astropy.coordinates import Angle
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib as mpl
import pyparsing
import math
import numpy as np
from astropy.visualization.wcsaxes.frame import EllipticalFrame
import glob
import argparse
import os
from radio_beam import Beam
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredEllipse
from astropy.wcs.utils import proj_plane_pixel_scales
from matplotlib.patches import Ellipse
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredAuxTransformBox
#from regions import DS9Parser
#from regions import read_ds9
from astropy.coordinates import SkyCoord
from astropy.nddata import Cutout2D
import timeit
from astropy.time import Time
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
mpl.use('TkAgg')



mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['image.cmap'] = 'cubehelix'
mpl.rcParams['image.origin'] = 'lower'
mpl.rcParams['axes.grid'] = False
mpl.rcParams['savefig.dpi'] = 150
mpl.rcParams['figure.figsize'] = (20, 20)
mpl.rcParams['text.usetex'] = True
params = {"text.color" : "black",
          "xtick.color" : "black",
          "ytick.color" : "black"}
mpl.rcParams.update(params)

fitslist=glob.glob('*.fits')

RA = ...
DEC = ...

def read_fits(filename):
    with fits.open(filename, memmap=True) as hdul:
        header = WCS(hdul[0].header)
        data = hdul[0].data
        #data[0, 0, :, :]
        max=np.max(data)
        min=np.min(data)
        std=np.std(data)
        return header, data, hdul[0].data[0, 0, :, :], max, min, std



def get_beam(filename):
        hdbeam=fits.getheader(filename)
        my_beam = Beam.from_fits_header(hdbeam)
        bmaj=hdbeam["BMAJ"] * u.deg
        bmin=hdbeam["BMIN"] * u.deg
        bpa=hdbeam["BPA"] * u.deg
        xcen=hdbeam["CRPIX1"]
        ycen=hdbeam["CRPIX2"]
        CDELT1=hdbeam["CDELT1"]
        CDELT2=hdbeam["CDELT2"]
        bpa=hdbeam["BPA"] * u.deg
        date=hdbeam["DATE-OBS"]
        t = Time(date, format='isot', scale='utc')
        mjd=t.mjd
        pixscale=(math.sqrt(CDELT1**2 + CDELT2**2))*u.deg
        el=Ellipse((100, 130), width=(bmaj.to(u.deg) / pixscale).to(u.dimensionless_unscaled).value, height=(bmin.to(u.deg) / pixscale).to(u.dimensionless_unscaled).value, angle=(bpa+90*u.deg).to(u.deg).value, facecolor='grey', lw=54)
        return el, mjd


for num, i in enumerate(fitslist):
    position= SkyCoord('RA  DEC', frame='fk5', unit='deg', equinox='J2000.0')
    size = u.Quantity((50, 50), u.arcsec)
    cutout =Cutout2D(read_fits(i)[2], position, size, wcs=read_fits(i)[0].celestial)
    rows = 4
    ax=plt.subplot(rows,4,num+1, projection=cutout.wcs)


    plt.subplots_adjust(bottom=0.09, right=0.83, top=0.915, left=0.06, hspace = 0.001, wspace = 0.23)


    ax.text(0.83, 0.92, "MJD:"  +str(get_beam(i)[1]), alpha= 0.8, color='white', va="center", ha="center", size=8, transform=ax.transAxes,  bbox=dict(facecolor='grey', alpha=0.1))
    ax.plot_coord(SkyCoord(RA*u.deg, DEC*u.deg, frame="fk5"), "+", color='red')
    box = AnchoredAuxTransformBox(ax.transData, loc='lower left')
    box.drawing_area.add_artist(get_beam(i)[0])
    ax.add_artist(box)
    plt.contour(cutout.data, levels=[6*read_fits(i)[5], 12*read_fits(i)[5], 24*read_fits(i)[5], 58*read_fits(i)[5], 106*read_fits(i)[5], 300*read_fits(i)[5], 900*read_fits(i)[5]], colors='blue', alpha=0.35)


    plt.imshow(cutout.data, vmin=MIN, vmax=MAX)
    cax = plt.axes([0.85, 0.1, 0.035, 0.8])
    cbar=plt.colorbar(cax=cax,anchor=False, format='%.0e')
    cbar.set_label(label='Flux (Jy beam$^{-1}$)',size=18)
    cbar.ax.tick_params(labelsize=15)
    ra = ax.coords[0]
    deg = ax.coords[1]
    deg.set_axislabel('Declination (J2000)', fontsize='8', )
    ra.set_axislabel('Right Ascension (J2000)',fontsize='8')
    ax.xaxis.labelpad = 0.02
    ax.yaxis.labelpad = 0.01

    ra.set_major_formatter('hh:mm:ss')
    deg.set_major_formatter('dd:mm:ss')
    ra.display_minor_ticks(False)
    deg.display_minor_ticks(False)
    ra.set_auto_axislabel(False)
    deg.set_auto_axislabel(False)
    ax.tick_params(axis='both', which='major', pad=1.0, labelsize=5)
    plt.savefig('grid.png')
