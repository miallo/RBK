#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from glob import glob

def main():
    matplotlib.rc('text', usetex=True)
    data = np.genfromtxt("Geschwindigkeit_notfallkorrelation.dat")
    f,ax = plt.subplots()
    for ii in range(1,5):
        ax.plot(data[:,0],data[:,ii],'+-', label=r'$Th_'+str(ii)+r'*Th_'+str(ii+1)+r'$')
        print(data[np.argmax(data[:,ii]),0])
    ax.set_xlabel(u"Zeit [s]")
    ax.set_ylabel(r"Korrelation")
    ax.legend()
    f.savefig("kor.png",dpi=300,bbox_inches="tight")
    #plt.show()

if __name__ == "__main__":
    main()
