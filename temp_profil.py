#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from glob import glob

files = sorted(glob("18-06-06/tem_*.dat"))
backup = sorted(glob("18-06-06/tem_*_b.dat"))
for ba in backup:
    files.remove(ba)
files = files[:-5]
space = []
val_mean = []
val_std = []
for fi in files:
    key = fi.split("/")[-1][4:-4]
    val = np.genfromtxt(fi)
    space.append(np.float(key)/100.)
    val_mean.append(np.mean(val[:,1]))
    val_std.append(np.std(val[:,1]))

space       = np.array(space)
val_mean    = np.array(val_mean)
val_std     = np.array(val_std)

plt.fill_between(space,val_mean-val_std,val_mean+val_std)
plt.plot(space,val_mean,'rx-')
plt.xlabel(u"Höhe [cm]")
plt.ylabel("Temperatur [$^\circ$C]")
plt.grid(True,which="both")
plt.savefig("images/temp_profil.pdf",dpi=300,bbox_inches="tight")
