from django.shortcuts import render, redirect
from utilities import Saver, Palette, read_as_np
import json


def get_palette(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')

        if uploaded_file:
            file_content = uploaded_file.read()
            buffered_file = Saver(file_content)
            request.session['image'] = buffered_file.encoded_file
            np_data = read_as_np(buffered_file)
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
