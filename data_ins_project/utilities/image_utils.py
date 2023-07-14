
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import webcolors
from collections import Counter

DEFAULT_FONT = 'LiberationSans-Bold.ttf'


class Cutter:
    def __init__(self, fontname=DEFAULT_FONT):
        self._basic_font = ImageFont.truetype(fontname, size=100)
        self._dummy_draw = ImageDraw.ImageDraw(Image.new('RGBA', (1, 1)))


    def fit_font_variant(self, width, height, text, *args, 
                         align='center', fill_percent=100, **kwargs):
        """Make a font variant that fits into provided boundaries.

        Args:
            width:  boundary width
            height: boundary height
            text:   multiline text to fit
            align:  text alignment (e.g. 'left', 'center', 'right')
            fill_percent:
                    how much of a boundary space should be occupied
                    by text (i.e. leaving margins if not 100)
        """
        # rescale boundary by fill percent
        width, height = [int(i * fill_percent / 100) for i in (width, height)]

        # calculate height & width given the basic font is used
        x0, y0, x1, y1 = self._dummy_draw.multiline_textbbox(
            (0,0), *args, text=text, align=align, font=self._basic_font, **kwargs)
        w = x1 - x0
        h = y1 - y0

        # to guarantee font fits, we calculate two scaling factors,
        # the horizonal and vertical, and scale by the lowest of the two
        fit_w = width / w
        fit_h = height / h
        factor = min(fit_w, fit_h)
        newsize = int(self._basic_font.size * factor)

        return self._basic_font.font_variant(size=newsize)


    def text_cutout(self, image, text, *args,
                    bgcolor=(255, 255, 255, 127), align='center', fill_percent=100, **kwargs):
        mask = Image.new('RGBA', image.size, bgcolor)

        font = self.fit_font_variant(
            image.size[0], image.size[1], text, *args,
            align=align, fill_percent=fill_percent, **kwargs)

        draw = ImageDraw.Draw(mask)
        center = tuple(i / 2 for i in image.size)
        draw.multiline_text(center, *args,
                            align=align, anchor='mm', text=text, font=font,
                            fill=(0, 0, 0, 255), **kwargs)
        bg = Image.new('RGBA', image.size, bgcolor)
        res = Image.composite(image, bg, mask)
        return res
    


default_cutter = Cutter()

class Palette(object):

    def __init__(self, image_array: np.ndarray) -> None:
        self.image_data = image_array


    def generate(self):
        palette_hex_array = []
        first_channel, second_channel, third_channel = self.squarer(self.image_data[:,:,0]), self.squarer(self.image_data[:,:,1]), self.squarer(self.image_data[:,:,2])

        median1, median2, median3 = np.median(first_channel, axis=0), np.median(second_channel, axis=0), np.median(third_channel, axis=0)

        for i in range(median1.shape[0]):
            hex_pixel_code = webcolors.rgb_to_hex((round(median1[i]), round(median2[i]), round(median3[i])))
            palette_hex_array.append(hex_pixel_code)


        common_colors = Counter(palette_hex_array)
        common = sorted(common_colors.most_common(300)[::-1])
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
        
   