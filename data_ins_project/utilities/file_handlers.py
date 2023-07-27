import io
import base64
from PIL import Image
from skimage.io import imread




class Saver(io.BytesIO):
    """
    Acts as default BytesIO with additional properties.
    """
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self._encoded_file = None


    def _encode(self):
        self.seek(0)
        data = self.getvalue()
        encoded_data = base64.b64encode(data).decode('utf-8')
        return encoded_data

    @property
    def encoded_file(self):
        if self._encoded_file is None:
            self._encoded_file = self._encode()
        return self._encoded_file
    



def openPIL(file):
    return Image.open(file)

    


def read_as_np(file):
    return imread(file)

    

def url_to_np(content):
    buffered_file = Saver(content)
    return read_as_np(buffered_file)


class Downloader:
    pass