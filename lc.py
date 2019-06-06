import numpy as np
import datetime as dt
import datetime
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.dates as mdates
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter

ax = plt.subplot(212)
ax.subplots_adjust(hspace=0)


timefunc = lambda d: mdates.date2num(datetime.strptime(d, '%Y %m %d %H %M %S'))
timefunc_q = lambda s: mdates.date2num(datetime.strptime(s, '%Y %m %d %H %M %S'))

time = np.genfromtxt("radio.txt",usecols = (4),converters={0: timefunc}, dtype=None)
flux = np.genfromtxt("radio.txt",usecols = (2),converters={0: timefunc}, dtype=None)
errory = np.genfromtxt("radio.txt",usecols = (3),converters={0: timefunc}, dtype= None)


time_s = np.genfromtxt("swift_bat.txt",usecols = (1),converters={0: timefunc_q}, dtype=None)
flux_s = np.genfromtxt("swift_bat.txt",usecols = (2),converters={0: timefunc_q}, dtype=None)
errory_s = np.genfromtxt("swift_bat.txt",usecols = (3),converters={0: timefunc_q}, dtype= None)


plt.errorbar(time, flux, yerr=errory, marker='d',color='blue', linestyle='', ecolor='blue', label='RADIO')#,uplims=True)
plt.gcf().autofmt_xdate()
plt.xlabel('Date (MJD)', fontsize=19)
plt.ylabel('Flux ($\mu$Jy)', fontsize=15)
plt.yscale('log')
plt.tick_params(axis ='both',which='both',direction = 'in', top=True, right=True)
plt.legend(loc=9,shadow=True,fontsize=12,fancybox=True)

ax.set_yticks([50,6.5e3,80, 150,300, 450, 900, 1800,3600])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_xticks([58050,58650,58100,58250,58350,58400,58450, 58480, 58500, 58525, 58550])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

ax2 = plt.subplot(211, sharex=ax)
plt.errorbar(time_s,flux_s, yerr=errory_s, marker='d',color='green', linestyle='', ecolor='green',uplims=False, label='swift/bat')
plt.legend(loc=9,shadow=True,fontsize=12,fancybox=True)
plt.ylabel('Counts/cm$^{2}$/sec (15-50 keV)', fontsize=15)
plt.ylim(-0.01,0.04)
plt.tick_params(axis ='both',which='both',direction = 'in', top=True, right=True)
ax2.xaxis.tick_top()
plt.xticks(rotation=45)
plt.setp(ax2.get_xticklabels(), visible=True)
plt.savefig('lightcurve.png')
plt.show()
