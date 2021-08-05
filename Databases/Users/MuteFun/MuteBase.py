from ...MainBase import Sql_Fun as Sql # muted_users ( user_id  INT , group INT , date INT)
import datetime
def Add_Muted( User_id : int , Chat_id: int):
    Date=str((datetime.datetime.now() + datetime.timedelta(minutes=4)).strftime('%Y-%m-%d-%H:%M:%S'))
    try:
        row=Sql('DELETE FROM muted_users WHERE user_id=:user AND Group_id=:main',{'user':int(User_id),'main':Chat_id})
    except:
        pass
    row=Sql(f"insert  into muted_users (user_id,Group_id,date) values (:user_id,:Group_id,:date)",
    {'user_id':int(User_id),'Group_id':int(Chat_id) , 'date':Date})



def Show_Mute_User(user_id:int ,Chat_id: int):
    row=Sql('SELECT date FROM muted_users WHERE Group_id=:main AND user_id=:user', {'main':int(Chat_id), 'user':int(user_id)})
    try:
        return row[0][0]
    except:
        return False


def Delete_User_Mute( User_id : int , main : int ):
    row=Sql('DELETE FROM muted_users WHERE user_id=:user AND Group_id=:main',{'user':int(User_id) , 'main':main})
