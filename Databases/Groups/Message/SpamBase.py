from ...MainBase import Sql_Cheak as Sql 
def Add_User_message(user_id :int , Chat_id : int ):
    hsh=f'{Chat_id}{user_id}'
    row=Sql('insert OR ignore into spam (user_id,Group_id,hash,times) values (:user_id,:Group_id,:hash,:times)',
        {'user_id':int(user_id),'Group_id':int(Chat_id),'hash':hsh, 'times':0})
    row=Sql('UPDATE spam SET times=times+1 WHERE hash=:hash',{'hash':hsh})

    return True

def Show_User_Messages(user_id :int , Chat_id : int ):
    hsh=f'{Chat_id}{user_id}'
    row=Sql('SELECT times FROM spam WHERE hash=:hash',{'hash':hsh})
    row=row
    try:
        return int(row[0][0])
    except:
        return 0

def Set_Zero_All_Message_Spams():
    row=Sql('DROP TABLE spam ')

    row=Sql('CREATE TABLE IF NOT EXISTS spam ( user_id  INT , Group_id INT ,  hash TEXT PRIMARY KEY , times INT)')

    return True