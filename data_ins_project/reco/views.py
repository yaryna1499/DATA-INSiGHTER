from django.shortcuts import render
from utilities import json_parser
import os
from data_ins_project.settings import BASE_DIR

dataset_PATH = os.path.join(BASE_DIR, 'reco/stacks.json')

def recommend_system_view(request):
    specializations = json_parser(dataset_PATH)
    if request.method == 'POST':
        user_selected = request.POST.get("specialization")
        user_tech = request.POST.get("technologies")
        print(user_tech)
    return render(request, "reco.html", {'specializations': specializations,})


