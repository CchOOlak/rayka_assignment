from django import forms

from device.models import *
from device.repository import AbstractRepo

class DeviceAddForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = []

    def save(self, repo: AbstractRepo):
        repo.add(self.cleaned_data)
