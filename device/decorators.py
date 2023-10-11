from device import models

def remove_if_exist_wrapper(deviceId):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                device = models.Device.objects.get(pk=f"/devices/{deviceId}")
                device.delete()
                return func(*args, **kwargs)
            except:
                return func(*args, **kwargs)
        return wrapper
    return decorator
