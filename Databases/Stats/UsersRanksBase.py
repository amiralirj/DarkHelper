from ..MainBase import Sql_Stats as Sql
import datetime

def Kill_Ranks(user_id,point):
    month=str((datetime.date.today()).strftime('%Y-%m'))
    row=Sql('insert or ignore into ranks (user_id,point,coin,month) values (:user_id,:point,:coin,:month)',{'user_id':int(user_id),'point':int(point),'coin':999999999,'month':month})


def Insert_User_Ranks(user_id,coin):
    month=str((datetime.date.today()).strftime('%Y-%m'))
    try:
        row=Sql('update ranks set coin=:coin where user_id=:user_id AND month=:mon ',{'coin':int(coin),'user_id':int(user_id) ,'mon':int(month)})
    except:
        row=Sql('insert or ignore into ranks (user_id,point,coin,month) values (:user_id,:point,:coin,:month)',{'user_id':int(user_id),'point':99999999,'coin':int(coin),'month':month})

def user_rank(user_id):
    month=str((datetime.date.today()).strftime('%Y-%m'))
    row=Sql('SELECT point,coin from ranks where user_id=:user_id AND month=:mon',{'user_id':int(user_id),'mon':(month)})
    rank=row
    try:
        return rank[0]
    except:
        return['رنکی ندارید 💩',
        'رنکی ندارید 💩']