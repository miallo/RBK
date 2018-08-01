import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

data    = np.genfromtxt("18-06-06/Power_0050.dat")
data2   = np.genfromtxt("18-06-06/Powerfq_0050.dat")
mask_ab = np.logical_and(data[:,0]>3*10**(-1),data[:,0]<1.5*10**(0))
mask_no = data[:,0]>2*10**(0)

nup_ab  = np.polyfit(np.log(data[:,0][mask_ab]),np.log(data[:,1][mask_ab]),1)
nup_no  = np.polyfit(np.log(data[:,0][mask_no]),np.log(data[:,1][mask_no]),1)
print nup_ab
print nup_no

xs_ab = [0.3,2.5]
xs_no = [1.5,5.]
plt.loglog(data[:,0],data[:,1],'r',label="Powerspektrum bei z=5cm")
plt.loglog(data2[:,0],data2[:,1],'m',label="Powerspektrum mal Frequenzquadrat bei z=5cm")
plt.xlabel("Frequenz [Hz]")
plt.ylabel("Powerspektrum")
plt.plot(xs_ab,np.exp(np.polyval(nup_ab,np.log(xs_ab))),"k",
         label="Wendetangente")
plt.plot(xs_no,np.exp(np.polyval(nup_no,np.log(xs_no))),"b",
         label="Rauschpegel")
plt.plot([1.743976276],[0.00135268], "go", label="Abbruchfrequenz bei $x=1.74$Hz, $y=0.0014$")
plt.grid(True,which="both")
plt.legend(loc="best")
plt.savefig("abbruchfrequenz.pdf",dpi=300,bbox_inches="tight")
