import numpy as np
import matplotlib.pyplot as plt
import astropy
from astropy.io import fits
import os

# image_file = "C:\\Users\\astro\\OneDrive\\NGC4831\\NGC4831_V_3300s.fits"
# hdu_list = fits.open(image_file)
# image_data = hdu_list[0].data

#plt.imshow(image_data, cmap='gray')
# plt.colorbar()
# plt.show()

#print('Mean:', np.mean(image_data))

# print(type(image_data.flatten()))
# print(image_data.flatten().shape)


# Set file paths for the calibration frames and the target images
bias_file = r"C:\Users\astro\OneDrive\NGC4831\mbias.fits"
dark_file = r"C:\Users\astro\OneDrive\NGC4831\mdark.fits"
flat_file = r"C:\Users\astro\OneDrive\NGC4831\mflatV.fits"
# flat_B_file = "flat.fits"
# flat_R_file = "flat.fits"
target_dir = r"C:\Users\astro\OneDrive\NGC4831\Fundamentals_of_Oberservational_Astronomy\lights"

# Open the calibration frames and flat field
bias = fits.open(bias_file)[0].data
dark = fits.open(dark_file)[0].data
flat = fits.open(flat_file)[0].data

# Normalize the flat field by its median
flat_normalized = flat / np.average(flat)

# Loop through all FITS files in the target directory and calibrate each one
for filename in os.listdir(target_dir):
    if filename.endswith("hv300s.fits"):
        target_file = os.path.join(target_dir, filename)
        target = fits.open(target_file)[0].data

        # Subtract the bias frame from the target image and dark frame
        target_bias_subtracted = target - bias
        dark_bias_subtracted = dark - bias

        # Subtract the dark frame from the target image and divide by the normalized flat field
        target_dark_subtracted = (target_bias_subtracted - dark_bias_subtracted) / flat_normalized

        # Save the calibrated image to a new FITS file
        calibrated_file = os.path.join(target_dir, "calibrated_" + filename)
        fits.writeto(calibrated_file, target_dark_subtracted, overwrite=True)
