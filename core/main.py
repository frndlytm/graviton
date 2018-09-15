from model import BittrexApi
from strategies import DataFrameResponseStrategy

if __name__ == '__main__':
    api = BittrexApi(DataFrameResponseStrategy())
    print(api.get('getmarkets', 'result'))
