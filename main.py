from core.apis import Api
from core.getters import DataFrameResponseStrategy

class BittrexApiImp(JsonRestApiImp):
    """BittrexApi houses the API base info and builds the base url
    string for calls to a NULL endpoint.
    """
    root = 'https://bittrex.com/api'
    version = 'v1.1'
    nodes = ['public']



class CryptoCompareApiImp(JsonRestApiImp):
    """CryptoCompareApi houses the API base info and builds the url
    string for calls to the NULL endpoint. 
    """
    root = 'https://min-api.cryptocompare.com'
    nodes = ['data']



if __name__ == '__main__':
    api = BittrexApi(DataFrameResponseStrategy())
    print(api.get('getmarkets', 'result'))
