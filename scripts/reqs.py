import functools
import asyncio
import aiohttp

async def fetch(session, url, params):
    async with session.get(url, params=params) as response:
        return await response.json()

async def main(params):
    root = 'https://min-api.cryptocompare.com/data/price?'
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, root, params)
        return html


queries = [
    {'fsym':'BTC', 'tsyms':['USD', 'JPY', 'EUR']},
    {'fsym':'UBQ', 'tsyms':['USD', 'JPY', 'EUR']}
]        
loop = asyncio.get_event_loop()
for query in queries:
    tasks = loop.call_soon(functools.partial(main, query))
loop.run_until_complete(asyncio.gather(tasks))
loop.close()