from ..MainBase import Sql_Stats as Sql
import datetime


def Add_Game(time,players,main,hour,hash):
    tamdid=str(datetime.date.today() )
    row=Sql(f"insert into jointime (time,players,main,hour,afk,hash,date) values(:time,:players,:main,:hour,:afk,:hash,:date);",
    {'time':time,'players':int(players),'main':int(main),'hour':int(hour),'afk':0,'hash':hash,'date' : tamdid })


def Show_All_Groups_States():
    row=Sql(f'SELECT time,players,hour,afk,date FROM jointime ')
    q=row
    return q



def Show_Group_State_Today(main):
    tamdid=str(datetime.date.today() )
    row=Sql(f'SELECT time,players,hour,afk,date FROM jointime WHERE main=:main and date=:date',{'main':main,'date':tamdid})
    q=row
    return q


def Show_Group_State_All_Time(main):
    row=Sql(f'SELECT time,players,hour,afk,date FROM jointime WHERE main=:main',{'main':main})
    q=row
    return q

def Add_AFK(main,hash):
    row=Sql('update jointime set afk = afk+1 where main =:main AND hash=:hash',{'main':main,'hash':hash})



def Show_Group_State_last_Game(main):
    tamdid=str(datetime.date.today() )
    row=Sql(f'SELECT time,players,hour,afk,date FROM jointime WHERE main=:main and date=:date',{'main':main,'date':tamdid})
    return row[-1]
