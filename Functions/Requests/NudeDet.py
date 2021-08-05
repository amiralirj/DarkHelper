#--------------------------------------------------------------------------| » Import Nudenet For Detect  Or using Rest-Api
from aiohttp_requests import requests  #requests-async---------------------|
from random import choice                                                #-|
#--------------------------------------------------------------------------|


async def Is_Nude(path):
    api=choice(['3b072b65-29b2-4653-a678-8ab819b99f83','8e851b97-c53d-4821-b62b-5e85faecb037','7c16b029-29f9-482a-9099-b92696071475','2a72c814-948a-4888-84b0-a0966142223e'])
    r =await requests.post(
    "https://api.deepai.org/api/nsfw-detector",
    data={
        'image': open(path, 'rb'),
    },
    headers={'api-key': api})
    x=await r.json()
    return dict(x)


