from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
import os

from .sas_to_tlp import SasToTlp

from tulip_wrapper.models import Network
from tulip_wrapper.forms import NetworkForm

def home(request):
    context = {}
    context["network_names"] = Network.objects.all()
    return render(request, "home.html", context)

def upload(request):
    if request.method == 'POST':
        form = NetworkForm(request.POST, request.FILES)
        if form.is_valid():
            network_model = form.save()
            if network_model.network_type == Network.IND_TYPE:
                old_file_path = os.path.join(settings.MEDIA_ROOT, network_model.network_file.name)
                with open(old_file_path, "r") as uploaded_file:
                    file_content = SasToTlp.sas_to_tlp(uploaded_file.read())
                new_file_name = "networks/" + network_model.network_name+".tlp"
                with open(os.path.join(settings.MEDIA_ROOT, new_file_name), "w") as uploaded_file:
                    uploaded_file.write(file_content)
                network_model.network_file.name = new_file_name
                network_model.save()
                os.remove(old_file_path)
            return HttpResponseRedirect('/home')
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

def moreInfo(request):
    return render(request, 'moreInfo.html')
