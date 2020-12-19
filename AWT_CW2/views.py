from .models import ClassModel
from django.shortcuts import render

def stats(request):
    stats =ClassModel.objects.all()
    return render(request, 'stats.html',{'statistics':stats})

def upload(request):
    return render(request, 'upload.html')

