import numpy as np
import datetime as dt
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter
from matplotlib import animation
from astropy.time import Time, TimeDelta
import seaborn as sns; sns.set()
sns.set_context("talk")
params = {"text.color" : "black",
          "xtick.color" : "black",
          "ytick.color" : "black"}
matplotlib.rcParams.update(params)


ax = plt.subplot(414)
plt.subplots_adjust(hspace=0.03)

fig = plt.figure(figsize=(20, 8))


timefunc = lambda d: mdates.date2num(datetime.strptime(d, '%Y %m %d %H %M %S'))
timefunc_q = lambda s: mdates.date2num(datetime.strptime(s, '%Y %m %d %H %M %S'))

time1 = np.genfromtxt("flux_1.txt",usecols = (4),converters={0: timefunc}, dtype=None)
flux1 = np.genfromtxt("flux_1.txt",usecols = (2),converters={0: timefunc}, dtype=None)
errory1 = np.genfromtxt("flux_1.txt",usecols = (3),converters={0: timefunc}, dtype= None)
time1 = np.genfromtxt("flux_1.txt",usecols = (1),converters={0: timefunc}, dtype=None)

time2 = np.genfromtxt("flux_2.txt",usecols = (4),converters={0: timefunc}, dtype=None)
flux2 = np.genfromtxt("flux_2.txt",usecols = (2),converters={0: timefunc}, dtype=None)
errory2 = np.genfromtxt("flux_2.txt",usecols = (3),converters={0: timefunc}, dtype= None)
time2 = np.genfromtxt("flux_2.txt",usecols = (1),converters={0: timefunc}, dtype=None)

dt = 0.03
tfinal = 59200
x0 = 58200
#
dt = TimeDelta(24*3600, format='sec') # granularity of update
start = Time(55000, format='mjd')
stop = Time(56000, format='mjd')
current = start
def animate(i):
    ax = plt.subplot(212)
    plt.subplots_adjust(hspace=0.03)
    plt.tick_params(axis ='both',which='both',direction = 'in', top = True, bottom= True, left=True, labelsize=13)
    plt.xticks(rotation=45)
    plt.setp(ax.get_xticklabels(), visible=True)
    ax.yaxis.tick_right()
    plt.setp(ax.get_yticklabels(), visible=True)
    plt.xlabel('Time (MJD)', fontsize=19)
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.set_xticks([58050,58950,58100,58250,58350,58400,58450, 58500, 58550, 58600, 58650, 58700, 58750, 58800, 58850, 58900, 58950, 59000, 59050, 59100, 59150, 59200, 59250 ])
    ax.set_xlim([x0, tfinal]) # fix the x axis
    ax.set_ylim([10, 1e6]) # fix the x axis

    plt.errorbar(time1[:i], flux1[:i], errory1[:i], marker='d', linestyle='', label='detections', color='mediumblue', ecolor='mediumblue')

    plt.axhline(y=62,linestyle='--', color='y', label = 'quiescent level')
    plt.gcf().autofmt_xdate()
    plt.ylabel('Flux density \n ($\mu$Jy beam$^{-1}$)', fontsize=13)
    plt.tick_params(axis ='both',which='both',direction = 'in', top=True, right=True, labelsize=13)
    ax.set_yticks([50,9e4,80, 150, 300, 500, 900, 1800, 3600, 7200, 14400,2.3e4, 4.7e4, 7.8e4, 9.3e04])
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.set_yscale('log')
    ax.yaxis.tick_right()



    ax4 = plt.subplot(211, sharex=ax)
    plt.errorbar(time2[:i],flux2[:i], errory2[:i], marker='d', linestyle='',uplims=False, label='Swift/XRT', color='mediumpurple', ecolor='mediumpurple')
    plt.ylabel('Unabsorbed \n flux (3-9 keV) \n (erg cm$^{-2}$ sec$^{-1}$)', fontsize=13)
    ax4.set_yscale('log')
    plt.tick_params(axis ='both',which='both',direction = 'in', top=True, right=True, labelsize=13)
    ax4.yaxis.tick_right()
    ax4.xaxis.tick_top()
    plt.xticks(rotation=45)
    plt.setp(ax4.get_xticklabels(), visible=True)
    plt.axhline(y=1.65e-13,linestyle=':', color='y',label = 'quiescence level (Tremou et al. 2020)')
    ax4.set_xlim([x0, tfinal]) # fix the x axis
    ax4.set_ylim([10e-14, 10e-09]) # fix the x axis


anim = animation.FuncAnimation(fig, animate, frames = len(time) + 1, interval = 550, blit = False)
anim.save(r'timeplot.gif')
