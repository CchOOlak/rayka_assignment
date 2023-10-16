from django.db import models

class Device(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    deviceModel = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=50, null=False)
    note = models.TextField(blank=True)
    serial = models.CharField(max_length=100, null=False, unique=True)
