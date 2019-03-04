import numpy as np
import datetime as dt
import datetime
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')
#matplotlib.use('agg')
import matplotlib.dates as mdates
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter
#mydate.strftime("%B")
#fig, ax = plt.subplots()
ax = plt.subplot(212)
#mydate.strftime("%B")
#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)


timefunc = lambda d: mdates.date2num(datetime.strptime(d, '%Y %m %d %H %M %S'))
timefunc_q = lambda s: mdates.date2num(datetime.strptime(s, '%Y %m %d %H %M %S'))

time = np.genfromtxt("flux_gx.txt",usecols = (4),converters={0: timefunc}, dtype=None)
flux = np.genfromtxt("flux_gx.txt",usecols = (2),converters={0: timefunc}, dtype=None)
errory = np.genfromtxt("flux_gx.txt",usecols = (3),converters={0: timefunc}, dtype= None)

time_q = np.genfromtxt("flux_gx_q.txt",usecols = (4),converters={0: timefunc_q}, dtype=None)
flux_q = np.genfromtxt("flux_gx_q.txt",usecols = (2),converters={0: timefunc_q}, dtype=None)
errory_q = np.genfromtxt("flux_gx_q.txt",usecols = (3),converters={0: timefunc_q}, dtype= None)

time_s = np.genfromtxt("swift_bat.txt",usecols = (1),converters={0: timefunc_q}, dtype=None)
flux_s = np.genfromtxt("swift_bat.txt",usecols = (2),converters={0: timefunc_q}, dtype=None)
errory_s = np.genfromtxt("swift_bat.txt",usecols = (3),converters={0: timefunc_q}, dtype= None)

#epoch = np.genfromtxt("2808_2.txt",usecols = (0),converters={0: timefunc}, dtype=None)

#x = [dt.datetime.strptime(d,'%Y-%m-%d') for d in time]
#x_q = x = [dt.datetime.strptime(s,'%Y-%m-%d') for s in time_q]

#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y %B'))
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

#splt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

plt.errorbar(time, flux, yerr=errory, marker='d',color='blue', linestyle='', ecolor='blue', label='detections')#,uplims=True)
plt.errorbar(time_q,flux_q, yerr=errory_q, marker='d',color='red', linestyle='', ecolor='red',uplims=True, label='upper limits')

#plt.plot(x,rms, marker='+', linestyle='',label='RMS')
#plt.xlim([datetime.date(2013, 8, 01), datetime.date(2017, 1, 1)])
plt.gcf().autofmt_xdate()
plt.xlabel('Date (MJD)', fontsize=19)
plt.ylabel('Flux ($\mu$Jy)', fontsize=15)
#plt.title('GX339-4 (MeerKAT)')
plt.yscale('log')
#plt.gca().set_ylim(0,10e3)
plt.tick_params(axis ='both',which='both',direction = 'in', top=True, right=True)
#plt.xscale('log')
plt.legend(loc=9,shadow=True,fontsize=12,fancybox=True)
ax.set_yticks([50,6.5e3,80, 150,300, 450, 900, 1800,3600])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_xticks([58050,58650,58100,58250,58350,58400,58450, 58480, 58500, 58525, 58550])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2 = plt.subplot(211, sharex=ax)
plt.errorbar(time_s,flux_s, yerr=errory_s, marker='d',color='green', linestyle='', ecolor='green',uplims=False, label='swift/bat')
# make these tick labels invisible
plt.legend(loc=9,shadow=True,fontsize=12,fancybox=True)
#plt.xlabel('Date (MJD)', fontsize=22)
plt.ylabel('Counts/cm$^{2}$/sec (15-50 keV)', fontsize=15)
#plt.title('GX339-4 (Swift/BAT)')
plt.ylim(-0.01,0.04)
plt.tick_params(axis ='both',which='both',direction = 'in', top=True, right=True)
ax2.xaxis.tick_top()
plt.xticks(rotation=45)
plt.setp(ax2.get_xticklabels(), visible=True)
#plt.savefig('gx_lightcurve.png')
#plt.savefig('2888.pdf')
plt.show()
