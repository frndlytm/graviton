import requests
from core.exceptions import FailedRequestError

class Api:
    """Api manages the strategies for using a Rest API
    and its available calls. The API has a few private
    members:

        . _root:    the base url.
        . _key:     the project key (DO NOT EXPOSE).
        . _path:    contains the url extensions.
        . _calls:   contains the valid endpoints.
        
    The API also has a strategy for each HTTP method:

        . getter:   configures the type of data to GET.
        . poster:   configures PUT requests with a key.
        . poster:   manages POST keys.
        . deleter: decides what data to DELETE.

    An API can be decorated to force-nullify requests
    for specific HTTP calls. For example, we can create
    a GetOnlyApi by decorating it as Gettable. This will
    be implemented at a later time.

    Endpoints can also be Getable, Putable, Postable, and
    Deletable. Need to consider how to structure the
    inheritance structure so that Api and Endpoint can
    both be decorated using these decorators.
    """
    def __init__(self, getter, poster, putter, deleter):
        self._root = None       # base url
        self._key = None        # private key
        self._path = []         # url extensions
        self._calls = {}        # endpoints by name
        self.getter = getter    # GET strategy
        self.poster = poster    # POST strategy
        self.putter = putter    # PUT strategy
        self.deleter = deleter  # DELETE strategy

    def __str__(self):
        """Return the base target url, without endpoint 
        attachments. This is to provide an easy string
        representation to append Endpoint renders later.
        """
        url = '{}/{}'.format(self.root, self.path)
        return url



    """'root' should be set by the implementation 
    so we have provided the default as None in 
    __init__ and a setter to enforce this.
    """
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, x):
        self._root = x

    """'path' /-delimits the _path members. It can
    be extend()ed and trim()med 
    """
    @property
    def path(self):
        return '/'.join(self._path)
    def extend_path(self, ext):
        self._path.append(ext)
    



    def add_endpoint(self, endpoint):
        """add_endpoint() appends an Endpoint to the 
        list of queryable endpoints.
        """
        self._calls[endpoint.get_name()] = endpoint



    def get(self, call, params={}, path=[]):
        """get() response, and return the data using 
        the attached strategy. The parameters are:

            . call:     name of Endpoint in _calls.
            . params:   for building Endpoint url. 
            . path:     path into the JSON for data.

        """ 
        # Build an endpoint using the parameters...
        endpoint = self._calls[call](params)
        url = '{}/{}'.format(str(self), str(endpoint))
        return self.getter.respond(url, path)


    def post(self, call, params={}):
        """post() response, and return the data using 
        the attached strategy. The parameters are:

            . call:     name of Endpoint in _calls.
            . params:   for building Endpoint url.  

        """ 
        # Build an endpoint using the parameters...
        endpoint = self._calls[call](params)
        url = '{}/{}'.format(str(self), str(endpoint))
        return self.poster.respond(url)   


    def put(self, call, params={}):
        """put() data using the attached strategy. 
        The parameters are:

            . call:     name of Endpoint in _calls.
            . params:   for building Endpoint url.  

        """ 
        # Build an endpoint using the parameters...
        endpoint = self._calls[call](params)
        url = '{}/{}'.format(str(self), str(endpoint))
        return self.putter.respond(url)


    def delete(self, call, params={}):
        """delete() request using the attached strategy. 
        The parameters are:

            . call:     name of Endpoint in _calls.
            . params:   for building Endpoint url.  

        """ 
        # Build an endpoint using the parameters...
        endpoint = self._calls[call](params)
        url = '{}/{}'.format(str(self), str(endpoint))
        return self.deleter.respond(url)



class ApiImp: pass

class BittrexApiImp(ApiImp):
    """BittrexApi houses the API base info and builds the base url
    string for calls to a NULL endpoint.
    """
    root = 'https://bittrex.com/api'

    version = 'v1.1'
    nodes = ['public']



class CryptoCompareApiImp(ApiImp):
    """CryptoCompareApi houses the API base info and builds the url
    string for calls to the NULL endpoint. 
    """
    root = 'https://min-api.cryptocompare.com'
    nodes = ['data']
