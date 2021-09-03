from ..MainBase import Sql_Stats as Sql
import datetime

def Add_Admin_Point(User_id , Chat_id , join=0 , tag=0 , afk=0 ):
    Date=str(datetime.date.today() )
    row=Sql('SELECT user_id FROM adminstats WHERE user_id=:user AND Group_id=:Group_id AND time=:time',
    {'user':int(User_id),'Group_id':int(Chat_id),'time':Date})
    row=row
    if row==[]:
        row=Sql(f"insert into adminstats (user_id,tag,game_join,AFK,Group_id,time) values (:user_id,:tag,:game_join,:AFK,:Group_id,:time)",
        {'user_id':int(User_id),'tag':int(tag),'game_join':int(join),'AFK':int(afk),'Group_id':int(Chat_id),'time':Date})
    
    else:
        row=Sql(f'UPDATE adminstats SET tag = tag+{int(tag)} , game_join=game_join+{int(join)} ,AFK=AFK+{int(afk)}  SET WHERE ')
    

def Show_Gap_All_Admins_Points(Chat_id : int):
    row=Sql('SELECT * FROM adminstats WHERE Group_id=:group ',{'group':int(Chat_id),})
    rows=row
    return rows

def Show_Gap_All_Admins_Points_Today(Chat_id : int):
    row=Sql('SELECT * FROM adminstats WHERE Group_id=:group AND time=:date ',{'group':int(Chat_id),'date':str(datetime.date.today())})
    rows=row
    return rows
    
def Show_Admin_Point(User_id , Chat_id):
    row=Sql('SELECT * FROM adminstats WHERE user_id=:user AND Group_id=:group ',{'user':int(User_id),'group':int(Chat_id),})
    rows=row
    return rows
    