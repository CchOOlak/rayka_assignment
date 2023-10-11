import json
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.forms.models import model_to_dict
from django.core import serializers

from device import forms, models

@csrf_exempt
@require_http_methods(['POST'])
def device_add(request):
    body = json.loads(request.body)
    payload = forms.DeviceForm(body or None)
    if payload.is_valid():
        try:
            payload.save()
            return HttpResponse(status=201)
        except Exception as e:
            # log (e)
            return HttpResponseServerError()
    return HttpResponseBadRequest()


@require_http_methods(['GET'])
def device_get(request, deviceId):
    try:
        device = get_object_or_404(models.Device, pk=f"/devices/{deviceId}")
        return JsonResponse(model_to_dict(device), safe=False)
    except Exception as e:
        # log (e)
        print(e)
        return HttpResponseServerError()
