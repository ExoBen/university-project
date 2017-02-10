from django import forms
from documentation.models import Network

class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ['name', 'network']
