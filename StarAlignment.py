import astroalign as aa
import glob
from astropy.io import fits
import numpy as np

source_list_B = glob.glob(r"C:\Users\astro\OneDrive\NGC4831\Fundamentals_of_Oberservational_Astronomy\lights\calibrated*hv300s.fits")
#print(source_list_B)

im1 = fits.getdata(source_list_B[0])
im1 = im1.byteswap().newbyteorder()

for name in source_list_B:
    im2 = fits.getdata(name)
    im2 = im2.byteswap().newbyteorder()
    im21, footprint = aa.register(im2, im1)
    fits.writeto("aligned_"+name[92:], im21, fits.getheader(name), overwrite=True)
