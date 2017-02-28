from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from documentation.models import Network
from documentation.forms import NetworkForm

def home(request):
    return render(request, "home.html")

def network(request):
    context = {}
    context["network_names"] = Network.objects.all()
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

def delete(request):
    context = {}
    context["network_names"] = Network.objects.all()
    if request.method == 'POST':
        form = NetworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/delete')
    else:
        form = NetworkForm()
    context["form"] = form
    return render(request, 'delete.html', context)