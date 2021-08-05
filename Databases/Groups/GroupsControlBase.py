from ..MainBase import Sql_group as Sql
    #--------------------------|
    # group_id INT PRIMARY KEY |
    # anti_spam INT            |
    # anti_robot INT           |
    # anti_tabchi INT          |
    # fosh_filter INT          |
    # porn INT                 |
    #--------------------------|

def Add_GroupControl(Chat_id:int):
    row=Sql('insert into groups_control (group_id,anti_spam,anti_robot,anti_tabchi,fosh_filter,lock,channel,channellock,voice_lock,sticker_lock,photo_lock,link_lock,forward_lock,video_lock,service_lock,spam_count,welcome,channel_text,porn,dick,pussy,coveredpossy,fboobs,mboobs,coveredboobs,stomack,baghal,ass,feet,coveredass,welcometurn) values (:group_id,:anti_spam,:anti_robot,:anti_tabchi,:fosh_filter,:lock,:channel,:channellock,:voice_lock,:sticker_lock,:photo_lock,:link_lock,:forward_lock,:video_lock,:service_lock,:spam_count,:welcome,:channel_text,:porn,:dick,:pussy,:coveredpossy,:fboobs,:mboobs,:coveredboobs,:stomack,:baghal,:ass,:feet,:coveredass,:welcometurn)',
    {'group_id':int(Chat_id),'anti_spam':0,'anti_robot':0,'anti_tabchi':0,'fosh_filter':0
    ,'lock':0,'channel' :'none', 'channellock' :0,'voice_lock':0,'sticker_lock':0,'photo_lock':0,
    'link_lock':0,'forward_lock':0,'video_lock':0,'service_lock':0,'spam_count':6,'welcome':'none'
    ,'channel_text':'👾','porn':0,
    'dick':0,'pussy':0,'coveredpossy':0,'fboobs':0,'mboobs':0,'coveredboobs':0,'stomack':0,'baghal':0,'ass':0,'feet':0,'coveredass':0,'welcometurn':0})





#----------------------------------------------------------------- Channel
def Show_Channel(Chat_id:int):
    row=Sql('SELECT channel FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row= row
    return row[0][0]

def set_Channel(Chat_id:int , Text:str):
    row=Sql(f"update groups_control set channel = :chnl where group_id =:group_id ",{'group_id':int(Chat_id) , 'chnl':str(Text)})




def Show_Channel_Lock(Chat_id:int):
    row=Sql('SELECT channellock FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row= row
    return row[0][0]

def Turn_On_Channel_Lock(Chat_id:int):
    row=Sql(f"update groups_control set channellock = 1 where group_id =:group_id ",{'group_id':int(Chat_id)})


def Turn_Off_Channel_Lock(Chat_id:int):
    row=Sql(f"update groups_control set channellock =0  where group_id =:group_id",{'group_id':int(Chat_id)})


#----------------------------------------------------------------- Anti Spam
def Show_Anti_spam(Chat_id:int):
    row=Sql('SELECT anti_spam FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row= row
    return row[0][0]

def Turn_On_Anti_spam(Chat_id:int):
    row=Sql(f"update groups_control set anti_spam = 1 where group_id =:group_id ",{'group_id':int(Chat_id)})


def Turn_Off_Anti_spam(Chat_id:int):
    row=Sql(f"update groups_control set anti_spam =0  where group_id =:group_id",{'group_id':int(Chat_id)})


#----------------------------------------------------------------- Anti Robot
def Show_Anti_robot(Chat_id:int):
    row=Sql('SELECT anti_robot FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row= row
    return row[0][0]

def Turn_On_Anti_robot(Chat_id:int):
    row=Sql(f"update groups_control set anti_robot = 1 where group_id =:group_id ",{'group_id':int(Chat_id)})


def Turn_Off_Anti_robot(Chat_id:int):
    row=Sql(f"update groups_control set anti_robot =0  where group_id =:group_id",{'group_id':int(Chat_id)})


#----------------------------------------------------------------- Anti Tabchi
def Show_Anti_tabchi(Chat_id:int):
    row=Sql('SELECT anti_tabchi FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row= row
    return row[0][0]

def Turn_On_Anti_tabchi(Chat_id:int):
    row=Sql(f"update groups_control set anti_tabchi = 1 where group_id =:group_id ",{'group_id':int(Chat_id)})


def Turn_Off_Anti_tabchi(Chat_id:int):
    row=Sql(f"update groups_control set anti_tabchi =0  where group_id =:group_id",{'group_id':int(Chat_id)})


#----------------------------------------------------------------- Anti NFSW
def Show_Fosh_filter(Chat_id:int):
    row=Sql('SELECT fosh_filter FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row= row
    return row[0][0]

def Turn_On_Fosh_filter(Chat_id:int):
    row=Sql(f"update groups_control set fosh_filter = 1 where group_id =:group_id ",{'group_id':int(Chat_id)})


def Turn_Off_Fosh_filter(Chat_id:int):
    row=Sql(f"update groups_control set fosh_filter =0  where group_id =:group_id",{'group_id':int(Chat_id)})


#----------------------------------------------------------------- Anti New Member
def Show_Lock(Chat_id:int):
    row=Sql('SELECT lock FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row= row
    return row[0][0]

def Turn_On_Lock(Chat_id:int):
    row=Sql(f"update groups_control set lock = 1 where group_id =:group_id ",{'group_id':int(Chat_id)})


def Turn_Off_Lock(Chat_id:int):
    row=Sql(f"update groups_control set lock =0  where group_id =:group_id",{'group_id':int(Chat_id)})




#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------




def Change_Group_Control_Feature( Chat_id : int , row_type : str , Amount ):
    row_type=(row_type.strip())
    row=Sql(f"UPDATE groups_control SET {row_type} =:Amount   WHERE group_id =:group_id ",{'group_id':int(Chat_id),'Amount':Amount})



def Show_Group_Control_Features( Chat_id : int ):
    row=Sql('SELECT * FROM groups_control WHERE group_id=:group_id',{'group_id':int(Chat_id)})
    row=row[0]
    return {'anti_spam':row[1],'anti_robot':row[2],'anti_tabchi':row[3],
    'fosh_filter':row[4],'lock':row[5],'channel':row[6],
    'channellock':row[7],'voice_lock':row[8],'sticker_lock':row[9],
    'photo_lock':row[10],'link_lock':row[11],'forward_lock':row[12], 
    'video_lock':row[13],'service_lock':row[14],'spam_count':row[15],'welcome':row[16],'channel_text':row[17],'porn':row[18]
    ,'Filters':{'dick':row[19],'pussy':row[20],'coveredpossy':row[21],'fboobs':row[22],'mboobs':row[23],'coveredboobs':row[24],'stomack':row[25],'baghal':row[26],'ass':row[27],'feet':row[28],'coveredass':row[29]},'welcometurn':row[30]}