#!/usr/bin/python
'''This is a test to read a complex 64 bits binary file from GNU Radio.
Details can be found here: https://www.nutaq.com/blog/gnu-radio-file-source-and-sink '''
import numpy as np
import matplotlib.pyplot as plt
import pdb
file_input="USRP.bin"
max_samples=1000#400#5000
reduce_flag=True
def main():
        data=np.fromfile(file_input, dtype=np.complex64)#f.readlines()
        print "File in memory"
        if reduce_flag:
                print "Reduction requested"
                data=data[0:max_samples]
        real_data=list()
        imag_data=list()
        mag=list()
        for point in data:
                real_data.append(np.real(point))
                imag_data.append(np.imag(point))
                mag.append(point)
        print "Plotting"
        plt.figure()
        plt.subplot(211)
        plt.plot(real_data[0:max_samples])
        plt.title("Real part")
        plt.subplot(212)
        plt.plot(imag_data[0:max_samples])
        plt.title("Imaginary part")
        plt.show()

if __name__=="__main__":
        main()
