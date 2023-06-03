from dataManager.models import Location
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    locations = Location.objects.all()
    return render(request, 'index.html', {'locations': locations})

