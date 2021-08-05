from ..MainBase import Sql_group as Sql
import datetime

    #--------------------------|
 #--| group_id INT PRIMARY KEY |
 #--| support_id INT           |
 #--| tamdid_date TEXT         |
 #--| davazdah INT             |
 #--| auto_tag INT             |
 #--| auto_del INT             |
 #--| auto_tag_sup INT         |
 #--| auto_del_sup INT         | 
 #--| alarm INT                | 
 #--| bet INT                  | 
 #--| state INT                | 
 #--| warn  INT                | 
 #--| bot_kind INT             |
 #--| fun_mute INT             |
 #--| state_lock INT           |
 #--| auto_next_game INT       |
 #--| next_game_response INT   |
 #--| emoji1 TEXT              |
 #--| emoji2 TEXT              |
 #--| emoji3 TEXT              |
 #--| sooti INT                |
 #--| admin_Alarm INT          | 
 #--| ghaleb TEXT              |
 #--| jointime_sup INT         |
 #--| dead_next INT            |
 #--| pin_shekar INT           |
 #--| pin_nazer INT            |
 #--| role_saver INT           |
 #--| questions INT            |
    #--------------------------|

#--------------------------------------------------------------------- ADD 
def Add_Group( Chat_id : int , Support : int , date=30 ):
    tamdid=str(datetime.date.today() + datetime.timedelta(days=date))
    row=Sql("""insert or ignore into groups (group_id,support_id,tamdid_date,davazdah,auto_tag,auto_del,auto_tag_sup,auto_del_sup,alarm,bet,state,warn,bot_kind,fun_mute,state_lock,auto_next_game,auto_next_message_id,next_game_response,emoji1,emoji2,emoji3,sooti,admin_Alarm,ghaleb,jointime_sup,dead_next,pin_shekar,pin_nazer,pin_list,role_saver,questions,bors,message_state,question_sended,auto_start,afk_warn,join_time,is_tagging,Its_Question_Time,players_state_lock) 
    values 
    (:group_id,:support_id,:tamdid_date,:davazdah,:auto_tag,:auto_del,:auto_tag_sup,:auto_del_sup,:alarm,:bet,:state,:warn,:bot_kind,:fun_mute,:state_lock,:auto_next_game,:auto_next_message_id,:next_game_response,:emoji1,:emoji2,:emoji3,:sooti,:admin_Alarm,:ghaleb,:jointime_sup,:dead_next,:pin_shekar,:pin_nazer,:pin_list,:role_saver,:questions,:bors,:message_state,:question_sended,:auto_start,:afk_warn,:join_time,:is_tagging,:Its_Question_Time,:players_state_lock)
    """,{
        'group_id':int(Chat_id),'support_id':int(Support),'tamdid_date':'none','davazdah':0,'auto_tag':0,'auto_del':0,'auto_tag_sup':0,
        'auto_del_sup':0,'alarm':0,'bet':0,'state':0,'warn':7,'bot_kind':1,'fun_mute':0,'state_lock':0,'auto_next_game':0,'auto_next_message_id':2,
        'next_game_response':0,'emoji1':'💎','emoji2':'💵','emoji3':'💰','sooti':0,'admin_Alarm':0,'ghaleb':'none',
        'jointime_sup':0,'dead_next':0,'pin_shekar':0,'pin_nazer':0,'pin_list':0,'role_saver':0,'questions':0 , 'bors':1 ,'message_state':0,
        'question_sended':0,'auto_start':0,'afk_warn':0,'join_time':0,'is_tagging':0,
        'Its_Question_Time':0,'players_state_lock':0})

    row=Sql("UPDATE groups SET tamdid_date=:tamdid ,davazdah =0  WHERE group_id =:group_id ",{'group_id':int(Chat_id),'tamdid':tamdid})


def Delete_Group( Chat_id : int):
    row=Sql('DELETE FROM groups WHERE group_id=:group_id',{'group_id':int(Chat_id)})


#--------------------------------------------------------------------- Membership 
def Have_Membership( Chat_id : int ):
    row=Sql('SELECT tamdid_date,davazdah FROM groups WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row=row
    another_day = datetime.datetime.now().strptime(str(row[0]), "%Y-%m-%d")
    if datetime.datetime.now() >another_day:
        if int(row[1])==0:
            row=Sql("UPDATE groups SET davazdah =1  WHERE group_id =:group_id ",{'group_id':int(Chat_id)})
        
            return 24 
        else :
            return False
    else:
        return True

#--------------------------------------------------------------------- Membership 
def Show_Group_Features( Chat_id : int ):
    rows=Sql('SELECT * FROM groups WHERE group_id=:group_id OR support_id=:group_id ',{'group_id':int(Chat_id)})
    row=rows[0]
    return {
        'group_id':row[0],'support_id':row[1],
        'tamdid_date':row[2],'davazdah': row[3],'auto_tag':row[4],
        'auto_del':row[5],'auto_tag_sup':row[6],
        'auto_del_sup':row[7],'alarm':row[8],
        'bet':row[9],'state':row[10],'warn':row[11],'bot_kind':row[12],
        'fun_mute':row[13],'state_lock':row[14],
        'auto_next_game':row[15],'auto_next_message_id':row[16],'next_game_response':row[17],
        'emoji1':row[18],'emoji2':row[19],'emoji3':row[20],
        'sooti':row[21],'admin_Alarm':row[22],'ghaleb':row[23],'jointime_sup':row[24],
        'dead_next':row[25],'pin_shekar':row[26],'pin_nazer':row[27],'pin_list':row[28],
        'role_saver':row[29],'questions':row[30] , 'bors':row[31], 'message_state':row[32],
        'question_sended':row[33],'auto_start':row[34],'afk_warn':row[35],'join_time':row[36],
        'is_tagging':row[37],'Its_Question_Time':row[38],'players_state_lock':row[39]}

def Change_Group_Feature( Chat_id : int , row_type : str , Amount ):
    row_type=(row_type.strip())
    row=Sql(f"UPDATE groups SET {row_type} =:Amount   WHERE group_id =:group_id OR support_id=:group_id ",{'group_id':int(Chat_id),'Amount':Amount})

def Show_one_feature(row,chat_id):
    row=Sql(f'SELECT {row} FROM groups WHERE group_id=:group_id OR support_id=:group_id ',{'group_id':int(chat_id)})
    return row[0][0]
#-------------------------------------------------------------------- Gaps
def Show_All_GroupIds():
    rows=Sql('SELECT group_id,support_id FROM groups ')
    return rows

def Show_All_Groups_IN_Kind(kind):
    rows=Sql('SELECT group_id,support_id FROM groups WHERE bot_kind=:bot ',{'bot':kind})
    return rows