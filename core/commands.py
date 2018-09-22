import requests
from core import exceptions

class ApiCommand:
    def __init__(self, api, endpoint):
        self.api = api
        self.endpoint = endpoint

    def execute(self):
        raise NotImplementedError

    @property
    def url(self):
        return '{}/{}'.format(
            str(self.api), str(self.endpoint)
        )



class GetCommand(ApiCommand):
    def execute(self, params=None):
        """GetCommand checks if an Endpoint is gettable
        before it performs a request, and returns the
        response.
        
        The GetCommand class will be piped by the system
        to a response handler.
        """
        if self.endpoint.gettable:  
            response = requests.get(
                self.url, params=params
            )
            # On successful response...
            if 200 <= response.status_code < 300:
                return response
            # On failed response...
            else:
                raise exceptions.FailedRequestError(
                    response.status_code,
                    self.url,
                    'request failed. See API documentation.'
                )
        # On a non-gettable endpoint...
        else:
            raise exceptions.NotGettableException(
                self.endpoint
            )


class PostCommand(ApiCommand):
    def execute(self, params=None):
        pass

class PutCommand(ApiCommand):
    def execute(self, params=None):
        pass

class DeleteCommand(ApiCommand):
    def execute(self, params=None):
        pass