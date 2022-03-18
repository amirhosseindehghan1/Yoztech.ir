from django.shortcuts import render


import json
def index(request):
    context = {}
    return render(request, 'home/main/index.html', context)