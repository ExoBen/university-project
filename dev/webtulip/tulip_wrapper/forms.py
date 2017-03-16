from django import forms
from .models import Network

class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ['network_name', 'network_file', 'network_type']

    def clean(self):

        if self.cleaned_data["network_type"] == Network.TLP_TYPE and not self.cleaned_data["network_file"].name.endswith(".tlp"):
        	self._errors["network_file"] = "Network file must be a .tlp"

        if self.cleaned_data["network_type"] == Network.IND_TYPE and not self.cleaned_data["network_file"].name.endswith(".json"):
        	self._errors["network_file"] = "Network file must be a .json"
