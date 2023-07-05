from django.shortcuts import render, redirect
from .utilities import default_cutter, DataSaver
from PIL import Image
import io

"""
TODO:
1) user can choose oriebtation of the image
2) user can choose font
3) user can choose the size of the font
4) user can download image in defferent formats
5) to add 'go back' button
"""


def process_image(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text')
        uploaded_file = request.FILES.get('image')

        if uploaded_file:
            file_content = uploaded_file.read()
            buffer = io.BytesIO(file_content)
            with Image.open(buffer) as image:
                new_image = default_cutter.text_cutout(image, user_text)
                saved_image = DataSaver(new_image)
            image_data = saved_image.encoded_image_data
            request.session['image_data'] = image_data
            return redirect('show_image')
    return redirect('text_cutter')


def show_image(request):
    image_data = request.session.get('image_data')
    return render(request, 'show_img_text_cutter.html', {'image_data': image_data})



def text_cutter(request):
    return render(request, 'upload_text_cutter.html', {})