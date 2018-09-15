import requests

class Endpoint:
    """Endpoints decorate an API to extend the get()
    method with parameters and a name
    """
    def __init__(self, name, api):
        self.name = name
        self.api = api

    def get(self, params):
        url = '/'.join([str(self.api), self.name])
        response



