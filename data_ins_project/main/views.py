from django.shortcuts import render
from .models import MenuItem, FooterItem


def home(request):
    menu_items = MenuItem.objects.filter(parent_id=None)
    footer_items = FooterItem.objects.all()
    return render(request, 'home.html', {'menu_items': menu_items, 'footer_items': footer_items})


def api_palette_fromurl(request):
    return render(request, 'palette_api.html',{})

