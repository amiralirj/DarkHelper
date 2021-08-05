from ..MainBase import Sql_User as Sql
#    row=Sql('CREATE TABLE IF NOT EXISTS users ( user_id INT PRIMARY KEY, point INT , coin INT,  , laghab TEXT , birth TEXT , corectbet , amount INT , main INT )')
def Add_Player(user_id , chat_id ):
    row=Sql('insert or ignore into users (user_id,point,coin,laghab,birth,corectbet,amount,main,warn,ghost_power,anti_ghost,ghost_killer,diamonds,nextgame) values (:user_id,:point,:coin,:laghab,:birth,:corectbet,:amount,:main,:warn,:ghost_power,:anti_ghost,:ghost_killer,:diamonds,:nextgame)',
    {'user_id':int(user_id),'point':0,'coin':0,'laghab':'none','birth':'none','corectbet':0,'amount':0,'main':int(chat_id),'warn':0,'ghost_power':0,'anti_ghost':0,'ghost_killer':0,'diamonds':0,'nextgame':'none'})
#-------------------------------------------------------------------------- Warn 
def Show_User_Powers(User_id : int):
    row=Sql('SELECT ghost_power,anti_ghost,ghost_killer FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    return row[0]

def reduce_Power(user_id,ghost_power=0,anti_ghost=0,ghost_killer=0):
    row=Sql(f"update users set ghost_power=ghost_power-{ghost_power} ,anti_ghost=anti_ghost-{anti_ghost} ,ghost_killer=ghost_killer-{ghost_killer}  where user_id =:user ",{'user':int(user_id)})



def insert_Power(user_id,ghost_power=0,anti_ghost=0,ghost_killer=0):
    row=Sql(f"update users set ghost_power=ghost_power+{ghost_power} ,anti_ghost=anti_ghost+{anti_ghost} ,ghost_killer=ghost_killer+{ghost_killer}  where user_id =:user ",{'user':int(user_id)})

#-------------------------------------------------------------------------- Diamonds 
def Show_User_Diamonds(User_id : int):
    row=Sql('SELECT diamonds FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    return row[0][0]

def reduce_diamonds(user_id,adad):
    row=Sql(f"update users set diamonds = diamonds-{adad} where user_id =:user ",{'user':int(user_id)})



def insert_diamonds(user_id,adad):
    row=Sql(f"update users set diamonds = diamonds+{adad} where user_id =:user",{'user':int(user_id)})


#-------------------------------------------------------------------------- Warn 
def Show_User_warns(User_id : int , main:int):
    row=Sql('SELECT times FROM warn WHERE user_id=:user  AND main=:main',{'user':int(User_id), 'main':int(main)})
    row= row
    try:
        return row[0][0]
    except:
        return 0

def reduce_warn(user_id , main ):
    hash=str(user_id)+str(main)
    row=Sql(f"insert or ignore into warn (user_id,times,main,hash) values (:user_id , :times , :main , :hash)",
    {'user_id':int(user_id),'times':0,'main':int(main),'hash':hash})
    row=Sql(f"update warn set times = times-1 where user_id =:user AND main=:main ",{'user':int(user_id), 'main':int(main)})



def Insert_warn(user_id , main ):
    hash=str(user_id)+str(main)
    row=Sql(f"insert or ignore into warn (user_id,times,main,hash) values (:user_id , :times , :main , :hash)",
    {'user_id':int(user_id),'times':0,'main':int(main),'hash':hash})
    row=Sql(f"update AFK set times = times+1 where user_id =:user AND main=:main",{'user':int(user_id), 'main':int(main)})

def Set_User_warn_Zero(user_id , main):
    row=Sql(f"update warn set times = 0 WHERE user_id =:user AND main=:main",{'user':int(user_id) , 'main':int(main) })



#-------------------------------------------------------------------------- Points 
def Show_User_Points(User_id : int):
    row=Sql('SELECT point FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    return row[0][0]

def reduce_point(user_id,adad):
    row=Sql(f"update users set point = point-{adad} where user_id =:user ",{'user':int(user_id)})



def insert_point(user_id,adad):
    row=Sql(f"update users set point = point+{adad} where user_id =:user",{'user':int(user_id)})


#------------------------------------------------------------------------------------ Coin 
def Show_User_Coins(User_id : int):
    row=Sql('SELECT coin FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    return row[0][0]
    
def reduce_coin(user_id,adad):
    row=Sql(f"update users set coin = coin-{adad} where user_id =:user ",{'user':int(user_id)})


def insert_coin(user_id,adad):
    row=Sql(f"update users set coin = coin+{adad} where user_id =:user",{'user':int(user_id)})

#------------------------------------------------------------------------------------ Laghab 
def Show_User_Laghab(User_id : int):
    row=Sql('SELECT laghab FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    if row[0][0]== 'none':
        return None
    else:
        return row[0][0]

def set_laghab(user_id,text):
    row=Sql(f"update users set laghab =:txt where user_id =:user",{'user':int(user_id) , 'txt': text})

#------------------------------------------------------------------------------------ Birth 
def Show_User_Birth(User_id : int):
    row=Sql('SELECT birth FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    if row[0][0]== 'none':
        return None
    else:
        return row[0][0]

def set_birth(user_id,text):
    row=Sql(f"update users set birth =:txt where user_id =:user",{'user':int(user_id) , 'txt': text})

#------------------------------------------------------------------------------------ Corectbet
def Show_User_Corectbet(User_id : int):
    row=Sql('SELECT corectbet FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    return row[0][0]

def insert_corectbet(user_id):
    row=Sql(f"update users set corectbet = corectbet+1 where user_id =:user",{'user':int(user_id)})

#------------------------------------------------------------------------------------ Amount
def Show_User_Amount(User_id : int):
    row=Sql('SELECT amount FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    return row[0][0]

def reduce_amount(user_id,adad,main):
    row=Sql(f"update users set amount = amount-{int(adad)} where user_id =:user AND main=:main",{'user':int(user_id),'main':int(main)})


def insert_amount(user_id,adad,main):
    row=Sql(f"update users set amount = amount+{int(adad)} where user_id =:user AND main=:main",{'user':int(user_id),'main':int(main)})

#------------------------------------------------------------------------------------- main 
def Show_User_Group(User_id : int):
    row=Sql('SELECT main FROM users WHERE user_id=:user',{'user':int(User_id)})
    row= row
    return row[0][0]

def Change_main(user_id,main):
    row=Sql(f"update users set main = :main where user_id =:user ",{'user':int(user_id),'main':int(main)})


#user_id,point,coin,laghab,birth,corectbet,amount,main,warn,ghost_power,anti_ghost,ghost_killer,diamonds
def Show_User_Info( User_id : int ):
    row=Sql('SELECT * FROM users WHERE user_id=:user_id',{'user_id':int(User_id)})
    row=row[0]
    return {'user_id':row[0],'point':row[1],'coin':row[2],
    'laghab':row[3],'birth':row[4],'corectbet':row[5],
    'amount':row[6],'main':row[7],'warn':row[8],
    'ghost_power':row[9],'anti_ghost':row[10],'ghost_killer':row[11] , 
    'diamonds':row[12],'nextgame':row[13]}

def Change_User_Feature( User_id : int , row_type : str , Amount ):
    row_type=(row_type.strip())
    row=Sql(f"UPDATE users SET {row_type} =:Amount  WHERE user_id=:user_id ",{'user_id':int(User_id),'Amount':Amount})


#------------------------------------------------
def Show_All_user_Points():
    row=Sql(f'SELECT user_id,point FROM users ORDER BY point')
    q=row

    return q

def Show_All_user_Coins():
    row=Sql(f'SELECT user_id,coin FROM users ORDER BY coin')
    q=row

    return q

def Show_Group_ALL_User_Points(main):
    row=Sql(f'SELECT user_id,point FROM users WHERE main=:main ORDER BY point ',{'main':main})
    q=row
    return q

def Show_Group_ALL_User_Coins(main):
    row=Sql(f'SELECT user_id,point FROM users WHERE main=:main ORDER BY coin ',{'main':main})
    q=row
    return q
#---------------------------------------------------------------
def Set_0_All_PC():
    row=Sql('update users set coin = 100 ,point = 0  ')
