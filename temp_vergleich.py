#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

def korr():
    data = np.genfromtxt("../18-06-06/tem_notfallkorrelation.dat")
    value = []
    hoehe = np.array([0.02,0.05,0.08,0.12,0.15,0.18])
    for i in range(1,6):
        value.append(np.array([(hoehe[i-1]+hoehe[i])/2.,np.mean(data[:,i]),np.std(data[:,i])]))
    value = np.array(value)
    return value

def fahrt():
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
    return np.array([space,val_mean,val_std])


def main():
    
    ko   = korr()
    fi   = fahrt()

    f,ax = plt.subplots()
    ax.errorbar(ko[:,0],ko[:,1],yerr=ko[:,2],fmt='b+-',label="Korrelation",capsize=4)
    ax.errorbar(fi[0],fi[1],yerr=fi[2],fmt='r+-',label="Fahrt",capsize=4)
    ax.set_xlabel(u"Höhe/m")
    ax.set_ylabel("Temperatur/C")
    ax.legend(loc="best")
    ax.grid('on',which="both")
    f.savefig("T_vergleich.png",dpi=300,bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()
