from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utilities import url_to_np, Palette
from rest_framework.permissions import AllowAny
import requests

class PaletteView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        image_url = request.query_params.get('image_url')
        response = requests.get(image_url)
        palette_size = request.query_params.get('palette_size')

        if not image_url:
            return Response({'error': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)


        image = url_to_np(response.content)
        palette_obj = Palette(image, palette_size)
        colors = palette_obj.generate()
        colors = [color for color, _ in colors]
        return Response({'colors': colors}, status=status.HTTP_200_OK)
