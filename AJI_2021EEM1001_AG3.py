#1D-DWT code
#Ajinkya Dudhal_2021EEM1001_Assigment-3
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import pywt

#D:/IIT Ropar/Sem-1_Stuff/EE525-Communication and Signal Processing Lab/Assignment-3/sample_signal.wav
n=int(input("Enter '1' for logic and '2' for in-built function: "))
name=input("Enter file path: ")
level=int(input("Enter number of decomposition levels="))
fs,wav=wavfile.read(name)
plt.subplot(3,1,1)
plt.title("1D wav Signal")
plt.plot(wav)

if n==1:
    for i in range(level):
        LP=np.convolve(wav,[1/np.sqrt(2),1/np.sqrt(2)])
        down_LP=LP[::2]

        HP=np.convolve(wav,[1/np.sqrt(2),-1/np.sqrt(2)])
        down_HP=HP[::2]
        wav=down_LP
        plt.suptitle('Using Logic',fontsize='30')

else:
    coefficients=pywt.wavedec(wav,'haar',level=level)
    down_LP=coefficients[0]
    down_HP=coefficients[1]
    plt.suptitle('Using In-built Function',fontsize='30')

plt.subplot(3,1,2)
plt.title("Approximation Coefficient")
plt.plot(down_LP)
plt.subplot(3,1,3)
plt.title("Detailed Coefficient")
plt.plot(down_HP)
plt.show()