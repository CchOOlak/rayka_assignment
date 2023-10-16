from django.test import TestCase
from django.urls import reverse

from device.models import Device
from device.forms import DeviceAddForm
from device.repository import DeviceMockRepo

class DeviceTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.deviceRepo = DeviceMockRepo()
        self.device_data_valid = {
            "id": "/devices/id1",
            "deviceModel": "/devicemodels/id1",
            "name": "Sensor",
            "note": "Testing a sensor.",
            "serial": "A02000013233"
        }
        self.device_data_invalid_null = {}
        self.device_data_invalid_id_duplicate = {
            "id": "/devices/id1",
            "deviceModel": "/devicemodels/id1",
            "name": "Sensor",
            "note": "Testing a sensor.",
            "serial": "vvvvvvv"
        }
        self.device_data_invalid_serial_duplicate = {
            "id": "/devices/id3",
            "deviceModel": "/devicemodels/id3",
            "name": "Sensor",
            "note": "Testing a sensor.",
            "serial": "A02000013233"
        }
        self.device_id_valid = 'id1'
        self.device_id_invalid_not_found = 'id12'            

    def create_device(self, device):
        payload = DeviceAddForm(device)
        if payload.is_valid():
            payload.save(self.deviceRepo)
        # print(f"create device problem: {payload.errors}\n")
    def get_device(self, id):
        return self.deviceRepo.get(id)
    
    # Forms
    def test_device_add_form_valid(self):
        payload = DeviceAddForm(self.device_data_valid)
        self.assertTrue(payload.is_valid())

    def test_device_add_form_invalid(self):
        payload = DeviceAddForm(self.device_data_invalid_null)
        self.assertFalse(payload.is_valid())

    # Repo
    def test_device_model_device_create(self):
        self.create_device(self.device_data_valid)
        device = self.deviceRepo.get(self.device_id_valid)
        self.assertDictEqual(device, self.device_data_valid)

    # Views
    def test_device_view_device_add_success(self):
        response = self.client.post(
            reverse('device_add'),
            self.device_data_valid,
            'application/json'
        )
        self.assertEqual(response.status_code, 201)
    
    def test_device_view_device_add_fail_on_null(self):
        response = self.client.post(
            reverse('device_add'),
            self.device_data_invalid_null,
            'application/json'
        )
        self.assertEqual(response.status_code, 400)
    
    def test_device_view_device_get_success(self):
        self.create_device(self.device_data_valid)
        response = self.client.get(
            reverse('device_get', kwargs={'deviceId': self.device_id_valid})
        )
        self.assertDictEqual(
            response.json(),
            self.device_data_valid
        )

    def test_device_view_device_get_fail_not_found(self):
        self.create_device(self.device_data_valid)
        response = self.client.get(
            reverse('device_get', kwargs={'deviceId': self.device_id_invalid_not_found})
        )
        self.assertEqual(response.status_code, 404)
    