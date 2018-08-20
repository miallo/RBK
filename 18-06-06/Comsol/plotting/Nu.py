# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from glob import glob

files = sorted(glob("../Nu*"))
Nu = []
f,ax = plt.subplots()
#for fi in files:
numbers = ["$Ra=10^3$","$Ra=10^4$","$Ra=10^5$","$Ra=10^6$","$Ra=10^7$"]
for i in range(len(files)):
    fi = files[i]
    #name = fi.split("/")[-1][:-4]
    name = numbers[i]
    Nu = np.genfromtxt(fi,comments="%")
    plt.plot(Nu[:,0],Nu[:,1],label=name)
    #ax.axhline(Nu_T[i],0.,5.)
plt.legend(loc='best')
plt.xlabel("Zeit [a.u.]")
plt.ylabel("$Nu$")
plt.savefig("../../../images/Nu_sim.pdf",dpi=300,bbox_inches="tight")
