import requests

class FailedRequestError(Exception):
    def __init__(self, status, url, message):
        self.status = status
        self.url = url
        self.message = message


class IApi:
    def __init__(self, strategy, endpoints={}):
        self._root = None
        self._version = None
        self._group = None
        self.strategy = strategy
        self.endpoints = endpoints

    def __str__(self):
        """Return the formatted url string for the Bittrex API, like:
        
                https://bittrex.com/api/v1.1/public/{endpoint}
        """
        return '/'.join(
            [self.root, self.version, self.group]
        )

    def get(self, endpoint, path):
        """get() response, and return the data using the attached strategy.
        """ 
        url = '{}/{}'.format(str(self), str(endpoint))
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            return self.strategy.respond(response, path)
        else:
            raise FailedRequestError(
                response.status_code, url, 'cannot be found.'
            )

    def add_endpoint(self, endpoint):
        """add_endpoint() appends an Endpoint to the list of queryable
        endpoints.
        """
        self.endpoints[endpoint.get_name()] = endpoint

    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, root):
        self._root = root

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def group(self):
        return self._group
    @group.setter
    def group(self, group):
        self._group = group
    


class BittrexApi(IApi):
    """BittrexApi houses the API base info and builds the base url
    string for calls to a NULL endpoint.
    """
    root = 'https://bittrex.com/api'
    version = 'v1.1'
    group = 'public'



class CryptoCompareApi(IApi):
    """CryptoCompareApi houses the API base info and builds the url
    string for calls to the NULL endpoint. 
    """
    root = 'https://min-api.cryptocompare.com'
    group = 'data'
