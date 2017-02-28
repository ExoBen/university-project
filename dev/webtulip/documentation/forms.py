from django import forms
from documentation.models import Network
from .models import Network



class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ['network_name', 'network_file', 'network_type']