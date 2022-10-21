import os
from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np
import time


def get_image(folder_path, n, file_extension):  # Load image and convert to numpy int array
    img = image.imread(os.path.join(folder_path, str(n) + file_extension))
    img = np.array(img)
    return img.astype(int)


file_extension = '.bmp'  # File extension of analyzed images
folder_path = r"D:\Experimental data\900x900 orig"  # Folder, containing images

n_images = len(os.listdir(folder_path))  # Number of images in folder
print(f'{n_images} images found in the folder')

img = get_image(folder_path, 1, file_extension)  # Load image in order to get it resolution
height, width = img.shape[0], img.shape[1]
print(f'Image resolution: {width}x{height}')

number_of_images_in_set = int(input('Enter size of set: ') or '200')   # Get size of image set to be analyzed
# (200 for instance)
m = int(input('Enter step between images: ') or '10')  # Get step between analyzed images (10 for instance)

t0 = time.process_time()  # Measure time of code execution
n_analyzed_pairs = (number_of_images_in_set//m)-1  # Number of analyzed image pairs


if n_images % number_of_images_in_set != 0:  # If total number of images is not multiple of number of images in one set,
    # reduce total number of images to be multiple
    n_images -= n_images % number_of_images_in_set


counter = 0
for n_set in range(1, n_images, number_of_images_in_set):  # Set step. For example: 1-200; 201-400; 401-600 and etc.
    counter += 1
    activity_map = np.zeros(shape=(height, width))  # Create activity map with 0
    for n in range(n_set, n_set+number_of_images_in_set-m-1, m):  # m step between images inside one set
        first_image = get_image(folder_path, n, file_extension)  # Load first image as int numpy array
        second_image = get_image(folder_path, n+m, file_extension)  # Load second image as int numpy array

        print(f'Analyzing {n}{file_extension} and {n+m}{file_extension}')
        # Here is realized Modified structure function equation
        numerator = abs(np.subtract(first_image,  second_image))
        denominator = np.add(first_image, second_image)
        intermediate_map = np.divide(numerator, denominator)
        divided_map = np.divide(intermediate_map, n_analyzed_pairs)
        activity_map = np.add(activity_map, divided_map)

    plt.figure()
    a_m = plt.imshow(activity_map.astype(np.float64), cmap='turbo')  # Show calculated activity map
    plt.colorbar(a_m)
    plt.title(f'Set: {n_set}-{n_set+number_of_images_in_set-1}, m step: {m}')

print()
print(f'{n_analyzed_pairs} pairs of images in one set analyzed')
print(f'Execution time: {time.process_time() - t0}s')
