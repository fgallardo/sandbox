#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import SpiceyPy as spi
import pdb
from mpl_toolkits.mplot3d import Axes3D


def main():
	N=10000 #Precision 
	spi.kclear() #Limpiamos el pool de los kernels.
	#MetaKernel con los datos.
	#spi.furnsh("./meta.fgl")
	spi.furnsh("./pruebas/naif0011.tls")
	spi.furnsh("./pruebas/030201AP_SK_SM546_T45.bsp")
	spi.furnsh("./pruebas/earthstns_itrf93_050714.bsp")
	spi.furnsh("./pruebas/earth_assoc_itrf93.tf") 
	spi.furnsh("./pruebas/pck00008.tpc")
	spi.furnsh("./pruebas/de421.bsp")
	
	tiempos=spi.str2et(["Jun 20 2004","Dec 1, 2005"]) #Segundos desde J2000 a cada uno de esos epochs.
	tiempos=np.linspace(tiempos[0],tiempos[1],N) 
	a=spi.spkpos("Cassini",tiempos,"J2000","None","SATURN BARYCENTER")

	a=np.array(a)
	x=list()
	y=list()
	z=list()
	for k in a[0]:
		x.append(k[0])
		y.append(k[1])
		z.append(k[2])
	plt.figure()
	plt.subplot(211)
	plt.plot(x,y)
	plt.xlabel("x [Km]")
	plt.ylabel("y [Km]")
	plt.subplot(212)
	plt.plot(y,z)
	#Axes3D.plot(x,y)
	plt.xlabel("y Km")
	plt.ylabel("z Km")
	plt.figure()
	plt.plot(dist(x,y,z),a[1])
	plt.title("One Way distance between observer and target")
	plt.ylabel("Minutes")
	plt.xlabel("Km")
	fig=plt.figure()
	ax=fig.add_subplot(111,projection='3d')
	
	ax.plot(x,y,z,label="Cassini to Saturn Barycenter")
	plt.legend()
	plt.show()
	
	print a


def dist(x,y,z):
	x=np.array(x)
	y=np.array(y)
	z=np.array(z)
	return np.sqrt((x**2)+(y**2)+(z**2))

if __name__=="__main__":	
	main()
