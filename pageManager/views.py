from django.shortcuts import render
from dataManager.models import Location
# Create your views here.

def index(request):
    locations = Location.objects.all()
    return render(request, 'index.html', {'locations': locations})

