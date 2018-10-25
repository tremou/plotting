import matplotlib.pyplot as plt
from astropy import units as u
import aplpy
import pylab
from matplotlib import pyplot as plt,cm, colors as mc,patches as mpatches, colorbar as clm
from matplotlib.colors import LogNorm
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
import matplotlib.ticker as ticker

#edit accordingly below
min=x
max=x 
rms=x


fig = plt.figure(figsize=(8, 8))
gc=aplpy.FITSFigure("XXX.fits", figure=fig)

gc.recenter('ra', 'dec', radius=0.01) #ra, dec should be given in degrees and radius can be adjusted
gc.set_theme("publication")
gc.show_colorscale(cmap='viridis',vmin=min,vmax=max)
#gc.add_scalebar(0.00833333, "10\'\'")
gc.add_label('ra', 'dec', '+', color='blue', size=20, layer='point') #ra, dec should be given in degrees

#gc.show_contour("XXX.fits", levels=[5*rms, 10*rms, 15*rms] , colors='red', layer='cont')

axisf3 = fig.add_axes([0.91,0.1145,0.02,0.773])
normf3 = mc.Normalize(vmin=min, vmax=max)

cbf3 = clm.ColorbarBase(axisf3, cmap='viridis', norm=normf3, orientation='vertical', format='%0.1e')
cbf3.set_label('Flux (Jy/beam)',fontsize = 20)

gc.add_beam()
gc.beam.show()
gc.beam.set_color('blue')
gc.beam.set_edgecolor('blue')
gc.beam.set_facecolor('blue')
gc.beam.set_borderpad(0)
gc.beam.set_frame(True)

gc.axis_labels.show()
gc.tick_labels.show()
gc.tick_labels.set_xformat("hh:mm:ss.ss")
gc.tick_labels.set_yformat("dd:mm:ss.s")
gc.tick_labels.set_font(size='medium')
gc.axis_labels.set_font(size='x-large')
gc.set_title("xxx",fontsize = 25)

plt.show()
gc.save('out.png', format='png')
