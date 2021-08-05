from requests_async  import get,post   #requests-async

async def Black_State_Req(user_id):
    try:
        a=(await get(f"http://blackwerewolf.com/Stats/PlayerStats/?pid={user_id}&json=true")).json()
        a=dict(a)
        return int(a['gamesPlayed'])
    except:
        return 0

async def Onyx_State_Req(user_id):
    token='1121419247:AAHCd4sTctw3p8RiofS3Rhp4aPkuvREtlJm'
    try:
        o= ( await post(
            url="http://api.wolfofpersia.ir:9999/api/GetState",
            data={
                "user_id": user_id,
                "token": token},timeout=4)).json()
        man=dict(o)
        return int(man['total_game'])
    except:
        return 0

async def Werewolf_State_Req(user_id):
    try:
        a=(await get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={user_id}&json=true")).json()
        a=dict(a)
        return int(a['gamesPlayed'])
    except :
        return 0
