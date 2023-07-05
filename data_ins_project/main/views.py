from django.shortcuts import render
from .models import MenuItem
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


def home(request):
    menu_items = MenuItem.objects.filter(parent_id=None)
    return render(request, 'home.html', {'menu_items': menu_items})

