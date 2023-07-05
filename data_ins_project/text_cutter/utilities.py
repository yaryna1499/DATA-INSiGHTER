
from PIL import Image, ImageDraw, ImageFont
import io
import base64

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


class DataSaver(object):
    """
    1)gets PIL Image object and saves it to buffer
    2)returns encoded image data
    """
    def __init__(self, obj):
        self.obj = obj
        
    @property
    def encoded_image_data(self):
        buffer = io.BytesIO()
        buffer.seek(0)
        buffer.truncate()
        self.obj.save(buffer, format='PNG')
        buffer.seek(0)
        image_data = buffer.getvalue()
        encoded_image_data = base64.b64encode(image_data).decode('utf-8')
        return encoded_image_data
        
   