class FailedRequestError(Exception):
    def __init__(self, status, url, message):
        self.status = status
        self.url = url
        self.message = message

class NotGettableException(Exception):
    def __init__(self, endpoint):
        self.endpoint = endpoint
        
