#encoding=utf-8
import codecs
from itertools import chain
import math
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy.optimize import curve_fit

def func1(x, a, b):
    return a * x + b

def func2(x, a, b, c):
    return np.power(x, (a - b * np.log(x))) + c

def func3(x, a, b, c, d):
    return d * np.power(x, (a - b * np.log(x))) + c

print("Ocarina frequency fitting begins!")

area = [0, 3.46, 7.62, 20.18, 36.80372685, 44.35139683, 77.5344412, 124.100659,
        171.8842429, 199.2239299, 299.5113366, 368.9090597, 417.9257177]
frequency = [444, 476.8, 505.9, 555.8, 617, 650.5, 
             730.9, 837.7, 926.2, 1003, 1099, 1231, 1298]

popt1, pcov = curve_fit(func1, area, frequency)                                   
unique_vals1 = [func1(i, popt1[0], popt1[1]) for i in area]
print(popt1[0], popt1[1])
popt2, pcov = curve_fit(func2, area, frequency)                               
unique_vals2 = [func2(i, popt2[0], popt2[1], popt2[2]) for i in area]
print(popt2[0], popt2[1], popt2[2])
try:
    popt3, pcov = curve_fit(func3, area, frequency)                         
    unique_vals3 = [func3(i, popt3[0], popt3[1], popt3[2], popt3[3]) for i in area]
    print(popt3[0], popt3[1], popt3[2], popt3[3])
except RuntimeError:
    print("hahahahahah3~")

plt.figure()
plt.title('Ocarina frequency')      
plt.plot(area, frequency, 'b', label = 'original values')
plt.scatter(area, frequency, s=30, marker = 'x', color = 'blue')
plt.plot(area, unique_vals1, 'r', label='y=a*x+b')
plt.plot(area, unique_vals2, 'y', label='y=x^(a-b*log(x))+c')
plt.plot(area, unique_vals3, 'g', label='y=d*x^(a-b*log(x))+c')
plt.xlabel('area/mm^2')
plt.ylabel('frequency/Hz')
plt.legend(loc='upper left')
plt.savefig("Distribution.png")
plt.close()

plt.figure()
plt.title('Ocarina frequency fitting dAG')       
plt.plot(area, np.sqrt(np.abs(unique_vals1)) - np.sqrt(np.abs(frequency)), 'r', label='dAG: y=a*x+b')  
plt.plot(area, np.sqrt(np.abs(unique_vals2)) - np.sqrt(np.abs(frequency)), 'y', label='dAG: y=x^(a-b*log(x))+c')
plt.plot(area, np.sqrt(np.abs(unique_vals3)) - np.sqrt(np.abs(frequency)), 'g', label='dAG: y=d*x^(a-b*log(x))+c')   
plt.plot(area, np.zeros(len(area)), 'k', label='Standard')   
plt.xlabel('area/mm^2')
plt.ylabel('dAG value')
plt.legend(loc='upper left')
plt.savefig("dAG.png")
plt.close()
print("Ocarina frequency fitting ends!")