import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from glob import glob

def get_tempera():
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
        space.append(np.float(key)/10000.)
        val_mean.append(np.mean(val[:,1]))
        val_std.append(np.std(val[:,1]))

    space       = np.array(space)
    val_mean    = np.array(val_mean)
    val_std     = np.array(val_std)
    return (space,val_mean,val_std)

Nu_T = 1./(2.*np.array([.5,.35,.2,.1,.05]))
files = sorted(glob("18-06-06/Comsol/Nu*"))
Nu = []
Ra = []
for fi in files:
    name = fi.split("/")[-1][:-4]
    Nus = np.genfromtxt(fi,comments="%")
    Nu.append([np.mean(Nus[Nus[:,0]>1.][:,1]),np.std(Nus[Nus[:,0]>1.][:,1])])
    Ra.append(np.float(name[2:]))
Nu = np.array(Nu)
Ra = np.array(Ra)
nup = np.polyfit(np.log(Ra), np.log(Nu[:,0]), 1)
nup_T = np.polyfit(np.log(Ra), np.log(Nu_T), 1)

tf_sc,tf_mean,tf_std = get_tempera()

NU_IT   = 1.+(-3./2.*tf_mean[-1]+2.*tf_mean[-2]-1./2.*tf_mean[-3])/0.0005
print NU_IT,.2/(2.*0.002)

#xs = np.linspace(Ra[0],Ra[-1],100)
#xs = np.array([6e2,Ra[-1]])
xs = np.array([6e2,1e9])
plt.xscale("log", nonposx='clip')
plt.yscale("log", nonposy='clip')
plt.plot(xs,np.exp(np.polyval(nup_T,np.log(xs))),"r",
         label="$Nu=${:.02f}$Ra^{{{:.02f}}}$".format(np.exp(nup_T[1]),nup_T[0]))
plt.plot(Ra,Nu_T,'ro',label="Simulation Grenzschicht")
plt.plot(1e9,.2/(2.*0.002),'ko',label="Experimentelle Grenzschicht")
plt.plot(1e9,NU_IT,'k+',label="Experimentelles Integral ")
plt.plot(xs,np.exp(np.polyval(nup,np.log(xs))),"b",
         label="$Nu=${:.02f}$Ra^{{{:.02f}}}$".format(np.exp(nup[1]),nup[0]))
plt.errorbar(Ra,Nu[:,0],yerr=Nu[:,1],fmt='b+',capsize=4,label="Simulation Integral")
#plt.loglog(xs,np.exp(nup[1])*xs**nup[0])
plt.xlabel("$Ra$")
plt.ylabel("$Nu$")
plt.grid(True, which="both")
plt.legend(loc="best")
plt.savefig("images/Nu_Ra.pdf",dpi=300,bbox_inches="tight")
