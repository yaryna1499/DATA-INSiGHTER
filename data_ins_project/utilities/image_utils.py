
import numpy as np
import webcolors
from collections import Counter




class Palette(object):

    def __init__(self, image_array: np.ndarray, palette_size=300) -> None:
        self.image_data = image_array
        self.palette_size = palette_size


    def generate(self):
        palette_hex_array = []
        first_channel, second_channel, third_channel = self.squarer(self.image_data[:,:,0]), self.squarer(self.image_data[:,:,1]), self.squarer(self.image_data[:,:,2])

        median1, median2, median3 = np.median(first_channel, axis=0), np.median(second_channel, axis=0), np.median(third_channel, axis=0)

        for i in range(median1.shape[0]):
            hex_pixel_code = webcolors.rgb_to_hex((round(median1[i]), round(median2[i]), round(median3[i])))
            palette_hex_array.append(hex_pixel_code)


        common_colors = Counter(palette_hex_array)
        common = sorted(common_colors.most_common(self.palette_size)[::-1])
        return common
    


    def squarer(self, arr):
        # Get the dimensions of the array
        n, m = arr.shape

        # Calculate the size of the largest square
        square_size = min(n, m)

        # Calculate the indices for slicing the largest square
        start_row = (n - square_size) // 2
        end_row = start_row + square_size
        start_col = (m - square_size) // 2
        end_col = start_col + square_size

        # Slice out the largest square
        largest_square = arr[start_row:end_row, start_col:end_col]
        return largest_square
        
   