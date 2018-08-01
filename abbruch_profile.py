#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

def main():
    files = sorted(glob("../18-06-06/tem_*.dat"))
    backup = sorted(glob("../18-06-06/tem_*_b.dat"))
    for ba in backup:
        files.remove(ba)
    files = files[:-5]
    space = []
    val_mean = []
    val_std = []
    for fi in files:
        key = fi.split("/")[-1][4:-4]
        val = np.genfromtxt(fi)
        space.append(np.float(key)/10000.)
        val_mean.append(np.mean(val[:,1]))
        val_std.append(np.std(val[:,1]))

    space       = np.array(space)
    val_mean    = np.array(val_mean)
    val_std     = np.array(val_std)

    f,ax = plt.subplots()
    ax.fill_between(space,val_mean-val_std,val_mean+val_std)
    ax.plot(space,val_mean,'r+-')
    ax.set_xlabel(u"Höhe/m")
    ax.set_ylabel("Temperatur/C")
    #ax.set_title("Temperatur Profil fuer die halbe Zelle")
    ax.grid('on',which="both")
    #f.savefig("T_fahrt.png",dpi=300,bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
