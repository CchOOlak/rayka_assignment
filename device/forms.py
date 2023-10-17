from django import forms

from device.models import *
from device.repository import AbstractRepo

class DeviceAddForm(forms.Form):
    id = forms.CharField(required=True)
    deviceModel = forms.CharField(required=True)
    name = forms.CharField(required=True)
    note = forms.CharField()
    serial = forms.CharField(required=True)

    def save(self, repo: AbstractRepo):
        repo.add(self.cleaned_data)
