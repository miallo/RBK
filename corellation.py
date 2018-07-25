#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from glob import glob

def main():
    data = np.genfromtxt("Geschwindigkeit_notfallkorrelation.dat")
    print data[np.argmax(data[:,1]),0], np.max(data[:,1])
    f,ax = plt.subplots()
    ax.plot(data[:,0],data[:,1],'r+-')
    ax.set_xlabel(u"Zeit [s]")
    ax.set_ylabel(r"Korrelation")
    f.savefig("kor.png",dpi=300,bbox_inches="tight")
    #plt.show()

if __name__ == "__main__":
    main()
