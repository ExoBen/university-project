from django.shortcuts import render

from tulip import *

# Create your views here.

def home(request):
	return render(request, "home.html")