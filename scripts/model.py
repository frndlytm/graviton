import requests

class FailedRequestError(Exception):
    def __init__(self, url, message):
        self.url = url
        self.message = message


class IApi:
    def __init__(self):
        self._root = None
        self._version = None
        self._group = None

    def get(self):
        raise NotImplementedError

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
    """BittrexMeta houses the API base info and builds the base url
    string for calls to a NULL endpoint.
    """
    root = 'https://bittrex.com/api'
    version = 'v1.1'
    group = 'public'


    def __init__(self, strategy):
        self.strategy = strategy


    def __str__(self):
        """Return the formatted url string for the Bittrex API, like:
                
                https://bittrex.com/api/v1.1/public/{endpoint}
        """
        return '/'.join([self.root, self.version, self.group])


    def get(self, endpoint, path):
        """get() response, and return the data using the attached strategy.
        """ 
        url = '{}/{}'.format(str(self), endpoint)
        response = requests.get(url)
        if response.json()['success']:
            return self.strategy.respond(response, path)
        else:
            raise FailedRequestError(url, 'cannot be found.')


        