from django.shortcuts import render

# Create your views here.
from .models import Bus

def home(request):
    bus_data = Bus.objects.all()
    context = {
        'bus_data':bus_data
    }
    return render(request, "index.html", context)