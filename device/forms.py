from django.forms import ModelForm

from device.models import *

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = []
