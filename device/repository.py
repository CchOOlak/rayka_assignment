import boto3
from rayka_assignment import settings
from abc import ABC, abstractmethod

class AbstractRepo(ABC):
    @abstractmethod
    def get(self, id):
        pass
    @abstractmethod
    def add(self, data):
        pass


class DeviceDynamoRepo(AbstractRepo):
    def __init__(self):
        self._table = boto3.resource('dynamodb').Table(settings.DYNAMODB_TABLE)

    def get(self, id):
        response = self._table.get_item(
            Key={'id': id}
        )
        if "Item" not in response:
            return None

        item = response["Item"]
        return item
    
    def add(self, data):
        self._table.put_item(Item=data)


class DeviceMockRepo(AbstractRepo):
    def __init__(self):
        self.devices = {}
    
    def get(self, id):
        return self.devices.get(id, None)

    def add(self, data):
        device_id = data['id']
        self.devices[device_id] = data

def getRepo():
    if settings.DEBUG == True:
        return DeviceMockRepo()
    else:
        return DeviceDynamoRepo()