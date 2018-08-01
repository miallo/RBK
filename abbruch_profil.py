#!/usr/bin/env python
# coding: utf8
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

height = [0,5,10,15,20,25,30,35,40,45,50,60,70,80,90,100,110,120,220,320,420,520,620,720,820,920,1020]
height = np.array(height,dtype="float")/100

data = [[0.735,0.74,0.758],
        [0.995,0.978,0.896],
        [1.23,1.3,1.32],
        [1.52,1.43,1.42],
        [1.33,1.33,1.27],
        [1.48,1.47,1.35],
        [1.75,1.74,1.63],
        [1.96,2.15,1.98],
        [1.95,2.19,2.05],
        [1.88,1.9,1.88],
        [1.56,1.6,1.6],
        [1.56,1.61,1.58],
        [1.96,1.83,1.96],
        [1.78,2.11,1.84],
        [1.87,1.9,1.78],
        [1.84,1.86,1.74],
        [1.61,1.56,1.56],
        [2,2.03,1.92],
        [1.2,1.16,1.16],
        [1.34,1.29,1.3],
        [0.76,0.8,0.8],
        [0.3,0.38,0.34],
        [0.33,0.35,0.29],
        [0.26,0.31,0.26],
        [0.35,0.37,0.34],
        [0.32,0.29,0.29],
        [0.2,0.26,0.21]]
        #[1.21,1.22,1.28],
        #[1.5,1.68,1.4]]

plt.errorbar(height,np.mean(data,axis=1),yerr=np.std(data,axis=1),fmt="r-",capsize=5)
plt.xlabel(u"Höhe [cm]")
plt.ylabel("Abbruchfrequenz [Hz]")
plt.grid()
plt.savefig("abbruch_result.pdf",dpi=300,bbox_inches="tight")
