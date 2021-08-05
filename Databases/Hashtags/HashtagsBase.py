from ..MainBase import Sql_group as Sql
#    row=Sql('CREATE TABLE IF NOT EXISTS hashtags (hashtag TEXT , msg_id INT ,  group INT , hash INT )')
def Add_Hashtags(hashtag ,message_id , chat_id ):
    hash=str(hashtag)+str(chat_id)
    try:
        row=Sql('insert into hashtags (hashtag,msg_id,Group_id,hash) values (:hashtag,:msg_id,:Group_id,:hash)',
        {'hashtag':str(hashtag),'msg_id':int(message_id),'Group_id':int(chat_id),'hash':hash})
    
    except:
        row=Sql(f"update hashtags set msg_id =:msg where Group_id =:group ",{'msg':int(message_id),'group':int(chat_id)})
    
#-------------------------------------------------------------------------- Warn 
def Show_Hashtag(Hashtag :  str , group  : int):
    row=Sql('SELECT msg_id FROM hashtags WHERE hashtag=:hashtg AND Group_id=:group ',{'hashtg':str(Hashtag) , 'group':int(group)})
    row= row
    return row[0][0]

def Delete_hashtag(hashtag : str , Chat_id : int):
    row=Sql(f"DELETE FROM hashtags WHERE hashtag=:tg AND  Group_id =:group ",{'tg':hashtag , 'group':int(Chat_id)})

