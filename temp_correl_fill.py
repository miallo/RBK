#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

data = np.genfromtxt("18-06-06/tem_notfallkorrelation.dat")
value = []
hoehe = np.array([0.02,0.05,0.08,0.12,0.15,0.18])
for i in range(1,6):
    value.append(np.array([(hoehe[i-1]+hoehe[i])/2.,np.mean(data[:,i]),np.std(data[:,i])]))
value = np.array(value)

plt.fill_between(value[:,0]*100,value[:,1]-value[:,2],value[:,1]+value[:,2])
plt.plot(value[:,0]*100,value[:,1],'r+-')
plt.xlabel(u"Höhe [cm]")
plt.ylabel("Temperatur [$^\circ$C]")
plt.grid(True, which="both")
plt.savefig("images/T_kor.pdf",dpi=300,bbox_inches="tight")
