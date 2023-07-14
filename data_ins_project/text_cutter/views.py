from django.shortcuts import render, redirect
from utilities import Saver, openPIL, default_cutter



def process_image(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text')
        uploaded_file = request.FILES.get('image') #<class 'django.core.files.uploadedfile.TemporaryUploadedFile'>

        if uploaded_file:
            file_content = uploaded_file.read() #<class 'bytes'>
            file_buffered = Saver(file_content)
            with openPIL(file_buffered) as image:
                new_image = default_cutter.text_cutout(image, user_text)
                saver = Saver()
                new_image.save(saver, format='PNG')
            image_data = saver.encoded_file
            request.session['image_data'] = image_data
            return redirect('show_image')
    return redirect('text_cutter')


def show_image(request):
    image_data = request.session.get('image_data')
    return render(request, 'show_img_text_cutter.html', {'image_data': image_data})



def text_cutter(request):
    return render(request, 'upload_text_cutter.html', {})