#!/usr/bin/python
import os
import matplotlib.pyplot as plt
import numpy as np



#f.gallardo.lopez@gmail.com
#This code was just made to check a Frequency estimator method for DSP. Based on Cagatay Candan paper "A Method For Fine Resolution Frequency Estimation From Three DFT Samples". Is just some code for DSP testing. This code is not really useful in real applications, it is just to see how the method performs. 
#http://www.eee.metu.edu.tr/~ccandan/pub_dir/FineDopplerEst_IEEE_SPL_June2011.pdf





muestra=0# If you want to see a stem plot with the FFT and half the FFT
Y2=list()
#Simulation paremeters:
#=============================
f=1000 #Sinusoid Freq
#f=1e6
fs=10*f #Fs
ini=0 #Simulation Inital Time
fin=1 #Simulation Stop time
A0=1 #Sinusoid Ampliutde
#=========================


t=np.linspace(ini,fin,int(np.round((fin-ini)*(fs))))
y=A0*np.cos(2*np.pi*f*t)
Y=np.fft.fft(y,1024) #I was interested in a 1024 points FFT for a real application.



if muestra==1:
	plt.subplot(211)
	plt.title("Just the positive freq")
	plt.stem(abs(Y[1:512][::-1])) #I just want the positive output and I want it reversed.
	plt.subplot(212)
	plt.title("Complete FFT. X[0]=CC. Positive Frequs from n=1 to n=512. Negative freq from n 513 to n=1023") #yep, numpy does it this way...
#http://docs.scipy.org/doc/numpy/reference/routines.fft.html It is always a good idea to check how FFT is performed.
	plt.stem(abs(Y))
	plt.show()

Y=np.fft.fftshift(Y)




#We first try to find the maximum value
#=======================================
liminf=(len(Y)/2) #From CC 
limmax=len(Y)    # To maximum positive frequency (This is the bin related to +fs/2)
temp=np.array(Y[liminf:limmax]) # I will just take half the sequence and zero freq value (it is a real valued sequence what we are feeding into the FFT).
temp2=abs(temp)
maximo=temp2.max()
#=======================================

for n in range(len(temp2)): #searchsorted method does not do what I expected. It just tell you where to put a particular value so array is sorted... :(
	if temp2[n]==maximo:
		maxbin=n

#What the paper ask you to calculate.
N=len(Y)
Rkp_1=temp[maxbin-1]
Rkp0=temp[maxbin]
Rkp1=temp[maxbin+1]
freqestim=((np.tan(np.pi/N))/(np.pi/N))*((Rkp_1 - Rkp1)/((2*Rkp0)-Rkp_1 - Rkp1)).real

print "##########################################"
print "This is the frequency estimated with this method:"
print ((maxbin+freqestim)*fs/(N))
print "This is the real frequency the sinousoid have"
print f
print "This would be the value we would have with a spectral resolution of %d points:"%N
print (maxbin*fs/N)
print "#########################################"

##
plt.subplot(211)
plt.plot(np.linspace(-fs/2,fs/2,len(Y)),np.abs(Y)/len(Y))
plt.xlabel("Hz")

plt.grid()

plt.title("Original")
plt.subplot(212)
plt.title("Estimated position VS real position ")
estim=[((maxbin+freqestim)*fs/(N)),((maxbin+freqestim)*fs/(N)),((maxbin+freqestim)*fs/(N)),((maxbin+freqestim)*fs/(N))]
normal=[ (maxbin*fs/N), (maxbin*fs/N), (maxbin*fs/N), (maxbin*fs/N)]
plt.plot(np.linspace(0,3,4),estim,label="Estimated Freq")
plt.plot(np.linspace(0,3,4),normal,label="Freq due to bin")
if estim[0]>normal[0]:
	minim=normal[0]-1
	maxi=estim[0]+1
else:
	minim=estim[0]-1
	maxi=normal[0]+1
plt.axis([0,3,minim,maxi])
plt.legend()
plt.grid()
plt.show()


