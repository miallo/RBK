import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
def messfreq(f,fm=9.1):
    return np.mod(f,fm)

data = np.genfromtxt("18-06-06/Power_SF4.dat")
plt.loglog(data[:,0], data[:,1], 'r')
plt.xlabel("Frequenz [Hz]")
plt.ylabel("Powerspektrum")
plt.grid(True,which="both")
plt.savefig("stoer.pdf",dpi=300,bbox_inches="tight")

plt.clf()

plt.loglog(messfreq(data[:,0][data[:,0]>=9.1]),data[:,1][data[:,0]>=9.1],c='r',linestyle='None', marker='.', ms=2, label="Frequenzen ohne Aliasing")
plt.loglog(data[:,0][data[:,0]<9.1],data[:,1][data[:,0]<9.1],'k-',label="Dem Aliasing unterliegende Frequenzen")
plt.xlabel("Frequenz [Hz]")
plt.ylabel("Powerspektrum")
plt.legend()
plt.grid(True,which="both")
plt.savefig("stoer_shift.pdf",dpi=300,bbox_inches="tight")
