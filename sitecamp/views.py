from django.shortcuts import render
from django.template import loader
from .models import Lieux

def index(request):
    points = Lieux.objects.all()
    context = {"points": points}
    return render(request, 'sitecamp/index.html', context)