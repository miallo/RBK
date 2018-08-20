# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from glob import glob

files = sorted(glob("../V*"))
V = []
numbers = ["$Ra=10^3$","$Ra=10^4$","$Ra=10^5$","$Ra=10^6$","$Ra=10^7$"]
#for fi in files:
for i in range(len(files)):
    fi = files[i]
    #name = fi.split("/")[-1][:-4]
    name = numbers[i]
    V = np.genfromtxt(fi,comments="%")
    itdx,col = V.shape
    V = V.reshape(itdx/200,200,col)
    V = np.mean(V,axis=0)
    plt.plot(V[:,0],V[:,1],label=name)
plt.legend(loc='best')
plt.xlabel(u"Höhe (normiert)")
plt.ylabel("Geschwindigkeit [a.u.]")
plt.savefig("../../../images/V_sim.pdf",dpi=300,bbox_inches="tight")
