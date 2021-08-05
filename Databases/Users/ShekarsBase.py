from ..MainBase import Sql_User as Sql

def Add_Shekar( User_id : int , Chat_id: int):
    try:
        row=Sql(f"insert  into shekar (user_id,main) values (:user_id  , :main )",
        {'user_id':int(User_id),'main':int(Chat_id)})
    
    except:
        row=Sql(f"update shekar set user_id =:user where main =:main ",{'user':int(User_id) , 'main':int(Chat_id)})
    

def Show_Shekar(Chat_id: int):
    row=Sql('SELECT user_id FROM shekar WHERE main=:main', {'main':int(Chat_id)})
    row=row
    return row[0][0]

def Delete_Shekar(Chat_Id):
    Sql('DELETE FROM shekar WHERE main=:main', {'main':int(Chat_Id)})

def Shekar_Cheak(User_id : int , Chat_id: int ):
    row=Sql('SELECT * FROM shekar WHERE main=:main AND user_id=:user ', {'main':int(Chat_id) , 'user':int(User_id) })
    row=row
    try:
        x= row[0][0]
        return True
    except:
        return False


    