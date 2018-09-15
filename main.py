from core.apis import BittrexApi
from core.getters import DataFrameResponseStrategy

if __name__ == '__main__':
    api = BittrexApi(DataFrameResponseStrategy())
    print(api.get('getmarkets', 'result'))
