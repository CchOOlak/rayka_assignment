import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseServerError, HttpResponseNotFound

from rayka_assignment import settings
from device import forms, models, repository

if settings.DEBUG:
    deviceRepo = repository.DeviceMockRepo()
else:
    deviceRepo = repository.DeviceDynamoRepo()

@csrf_exempt
@require_http_methods(['POST'])
def device_add(request):
    body = json.loads(request.body)
    dataForm = forms.DeviceAddForm(body or None)
    if dataForm.is_valid():
        try:
            dataForm.save(deviceRepo)
            return HttpResponse(status=201)
        except Exception as e:
            # log (e)
            print(e)
            return HttpResponseServerError()
    return HttpResponseBadRequest()


@require_http_methods(['GET'])
def device_get(request, deviceId):
    try:
        device = deviceRepo.get(f"/devices/{deviceId}")
        if device:
            return JsonResponse(device, safe=False)
        return HttpResponseNotFound()
    except Exception as e:
        print(e)
        return HttpResponseServerError()
