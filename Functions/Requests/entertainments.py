from requests_async  import get,post   #requests-async

async def danestani():
    res=(await get('http://api.codebazan.ir/danestani/'))
    return res.text

async def story():
    res=(await get('http://api.codebazan.ir/dastan/'))
    return res.text

async def bio():
    res=(await get('https://api.codebazan.ir/bio/'))
    return res.text

async def wheather(city):
    res=( await get(f'https://api.codebazan.ir/weather/?city={city}'))
    return res.json()