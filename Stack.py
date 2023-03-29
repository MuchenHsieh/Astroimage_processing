import os
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

directory = r"C:\FAO"
files = os.listdir(directory)
imagetobestackelist = []

for i in range(1,11):
# Loop through all the files in the directory

    for filename in files:

        # Check if the file is a aligned image
        if filename.startswith("aligned"):

            # Load the image data into a NumPy array
            filepath = os.path.join(directory, filename)
            image_data = fits.getdata(filepath)

            # Add the image to a list
            imagetobestacked_list.append(image_data)

            if len(imagetobestacked_list) == i :
                average_image = np.mean(imagetobestacked_list, axis=0)
                print(len(imagetobestacked_list))
                fits.writeto(f'average_image{i}.fits', average_image, overwrite=True)
                imagetobestacked_list = []
                break
        
        


# # Calculate the average of the images
# average_image = np.mean(imagetobestacked_list, axis=0)
# print(len(imagetobestacked_list))

# # plt.imshow(average_image, cmap='gray')
# # plt.show()

# # Save the average image to a FITS file
# fits.writeto('average_image.fits', average_image, overwrite=True)

