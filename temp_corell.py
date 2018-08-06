#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
from glob import glob
from scipy.optimize import curve_fit

def gauss(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2.*sigma**2))



value = []
hoehe = np.array([0.02,0.05,0.08,0.12,0.15,0.18])
data = np.genfromtxt("18-06-06/Geschwindigkeit_notfallkorrelation.dat")
hoehe = np.array([0.02,0.05,0.08,0.12,0.15,0.18])
for i in range(1,6):
    #value.append(np.array([(hoehe[i-1]+hoehe[i])/2.,(hoehe[i]-hoehe[i-1])/data[np.argmax(data[:,i]),0]]))
    mean    = data[np.argmax(data[:,i]),0]
    mask    = (data[:,0]>mean-3.) & (data[:,0]<mean+3.)
    #fit gaussian
    popt,pcov = curve_fit(gauss,data[mask,0],data[mask,i],p0=[1.,mean,1.])

    value.append(np.array([(hoehe[i-1]+hoehe[i])/2.,(hoehe[i]-hoehe[i-1])/popt[1]]))


value = np.array(value)
plt.plot(value[:,0]*100,value[:,1]*100,'r+-')
plt.xlabel(u"Höhe [cm]")
plt.ylabel(r"Geschwindigkeit [cms$^{-1}$]")
plt.grid(True)
plt.savefig("v_hoehe.pdf", dpi=300, bbox_inches="tight")
plt.close()

for i in range(1,6):
    plt.plot(data[:,0]/(hoehe[i]-hoehe[i-1]),data[:,i],label="T{}*T{}".format(i,i+1))
plt.xlabel(r"$\tau/\Delta h$ [m$^{-1}$s]")
plt.ylabel(r"$\int(T(t)T(t-\tau)$d$t$")
plt.legend(loc="best")
plt.grid(True)
plt.savefig("tempcorell.pdf", dpi=300, bbox_inches="tight")
