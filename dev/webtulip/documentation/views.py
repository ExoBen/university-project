from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, "home.html")

def network(request):
	return render(request, "network.html")