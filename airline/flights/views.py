from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
        return HttpResponse ("Hello world")

from django.shortcuts import render
from .models import Flight

def index(request):
        return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
        })