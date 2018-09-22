from core.apis import Api, JsonRestApiImp
from core.getters import DataFrameGetter
from core.posters import NullPoster
from core.putters import NullPutter
from core.deleters import NullDeleter

class Bittrex(Api):
    """BittrexApi houses the API base info and builds the base url
    string for calls to a NULL endpoint.
    """
    root = 'https://bittrex.com'


class CryptoCompare(Api):
    """CryptoCompareApi houses the API base info and builds the url
    string for calls to the NULL endpoint. 
    """
    root = 'https://min-api.cryptocompare.com'



if __name__ == '__main__':
    api = Bittrex(
        JsonRestApiImp(),
        DataFrameGetter(),
        NullPoster(),
        NullPutter(),
        NullDeleter()
    )
    api.extend_path('api')
    api.extend_path('v1.1')
    api.extend_path('public')
    print(str(api))
    
    
