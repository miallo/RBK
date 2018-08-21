# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from glob import glob
from scipy import interpolate

Nu_T = np.array([.5,.35,.2,.1,.05])
files = sorted(glob("../T*"))
T = []
#for fi in files:
numbers = ["$Ra=10^3$","$Ra=10^4$","$Ra=10^5$","$Ra=10^6$","$Ra=10^7$"]
fmts = ['C0','C1','C2','C3','C4']
for i in range(len(files)):
    fi = files[i]
    #name = fi.split("/")[-1][:-4]
    name = numbers[i]
    T = np.genfromtxt(fi,comments="%")
    itdx,col = T.shape
    T = T.reshape(int(itdx/200),200,col)
    T = np.mean(T,axis=0)
    plt.plot(T[:,0],T[:,1],fmts[i]+"-",label=name)
    f = interpolate.interp1d(T[:,0], T[:,1])
    print(f(Nu_T[i]))
    plt.plot(Nu_T[i], f(Nu_T[i]), c=fmts[i], marker='x', ms=10)
#    plt.axvline(Nu_T[i],0,0.1,color=fmts[i])
#    plt.axvline(1.-Nu_T[i],0,0.55,color=fmts[i])
plt.legend(loc='best')
plt.xlabel(u"Höhe (normiert)")
plt.ylabel(r"Konzentration $\hat =$ $\Delta T$ [a.u.]")
plt.savefig("../../../images/T_sim.pdf",dpi=300,bbox_inches="tight")
