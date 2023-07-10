from django.shortcuts import render, redirect
from text_cutter.utilities import DataSaver, Palette
import io ##переписати utilities/зробити їх універсальними!
from skimage.io import imread
from PIL import Image
import json


def get_palette(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')

        if uploaded_file:
            file_content = uploaded_file.read()
            buffer = io.BytesIO(file_content)
            with Image.open(buffer) as image:
                saved_image = DataSaver(image)
                request.session['image'] = saved_image.encoded_image_data
            np_data = imread(buffer)
            palette_obj = Palette(np_data)
            palette = palette_obj.generate()
            request.session['palette'] = palette
        return redirect('palette_show')
    return redirect('palette_upload')

def palette_upload(request):
    return render(request, 'upload_palette_gen.html', {})


def palette_show(request):
    palette = request.session.get('palette')
    image = request.session.get('image')
    palette = [color for color, amount in palette]
    palette_json = json.dumps(palette)
    return render(request, 'show_palette.html', {'palette': palette_json, 'image': image})
