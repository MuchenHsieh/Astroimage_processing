import os
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

std = []
exptime = []

#image region of interest(no star region)
X, Y, w, h = 1700, 1520, 100, 100

# Define the starting value, the common difference, and the number of terms in the sequence
start = 300
diff = 300
num_terms = 10

# Create the sequence using NumPy's arange() function
exptime = np.arange(start, start + num_terms * diff, diff)


directory = r"C:\FAO"
files = os.listdir(directory)

for filename in files:
    if filename.startswith("average"):
        filepath = os.path.join(directory, filename)
        image_data = fits.getdata(filepath)
        region = image_data[X-w:X+w, Y-h:Y+h]
        std_dividedby_exptime = np.std(region)/300
        std.append(std_dividedby_exptime)

exptime = np.concatenate((exptime[:1], exptime[2:]), axis=0)
std = np.concatenate((std[:1], std[2:]), axis=0)

#print(exptime, std)

def func(x, a, b, c):
    return a*x**b+c

popt, pcov = curve_fit(func, exptime, std, p0=[2, -0.5, 0.01])
print(popt)

i = np.linspace(200,3500,6000)
plt.plot(i, func(i, *popt), color='#873e23' , label='fitting curve')
plt.scatter(exptime, std, color='#1e81b0')


equation = '$ y = {:.2f} x^{{ {:.2f} }} {:.2f} $'.format(*popt)
print(equation)

plt.text(1500, 0.1, equation, fontsize=12, color='#873e23')
plt.xlabel("Total exposure time(s)")
plt.ylabel("Standard deviation/single exposure time(s)")

plt.show()