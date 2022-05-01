from django.shortcuts import render

# Create your views here.
from ToursNTravels.models import *


def index(request):
    return render(request, 'developer/index.html'),
