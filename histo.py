#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

data = np.genfromtxt("18-06-06/tem_notfallkorrelation.dat")
hoehe = np.array([0.02,0.05,0.08,0.12,0.15,0.18])
for i in range(1,7):
    plt.hist(data[:,i],log=True,histtype="step",label="{}cm".format(20-100*hoehe[i-1]),bins=30)#,normed=True)
plt.legend(loc="best")
plt.xlabel("Temperatur [$^\circ$C]")
plt.ylabel(u"Häufigkeit")
plt.savefig("images/hist.pdf",dpi=300,bbox_inches="tight")

