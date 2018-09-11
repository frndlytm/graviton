import requests
import logging
logging.basicConfig(
    filename = 'basic.log',
    level = logging.DEBUG,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

def fetch(url, params):
    """Get the text from the url"""
    response = requests.get(url, params=params)
    logging.info('{} {}'.format(response.url, response.text))
    return response.text

def main(url, queries):
    responses = map(lambda query: fetch(url, query), queries)
    return list(responses)

if __name__ == '__main__':
    url = 'https://min-api.cryptocompare.com/data/price?'
    queries = [
        {'fsym':'BTC', 'tsyms':'SAT,USD,EUR'},
        {'fsym':'UBQ', 'tsyms':'SAT,USD,EUR'}
    ]  
    print(main(url, queries))