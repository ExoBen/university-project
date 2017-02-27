from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from documentation.models import Network
from documentation.forms import NetworkForm

# Create your views here.

def home(request):
	return render(request, "home.html")

def network(request):
	context = {}
	context["network_names"] = Network.objects.all()
	for data in context["network_names"]:
		print(data.name)
		print(data.network)
	return render(request, "network.html", context)

def upload(request):
	if request.method == 'POST':
		form = NetworkForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/network')
	else:
		form = NetworkForm()
	return render(request, 'upload.html', {
		'form': form
	})
