from ..MainBase import Sql_User as Sql

#-------------------------------------------------------------------------- AFK 
def Show_User_AFKs(User_id : int , main:int):
    row=Sql('SELECT times FROM AFK WHERE user_id=:user  AND main=:main',{'user':int(User_id), 'main':int(main)})
    row= row
    try:
        return row[0][0]
    except:
        return 0

def reduce_AFK(user_id , main ):
    hash=str(user_id)+str(main)
    row=Sql(f"insert or ignore into AFK (user_id,times,main,hash) values (:user_id , :times , :main , :hash)",
    {'user_id':int(user_id),'times':0,'main':int(main),'hash':hash})
    row=Sql(f"update AFK set times = times-1 where user_id =:user AND main=:main ",{'user':int(user_id), 'main':int(main)})



def Insert_AFK(user_id , main ):
    hash=str(user_id)+str(main)
    row=Sql(f"insert or ignore into AFK (user_id,times,main,hash) values (:user_id , :times , :main , :hash)",
    {'user_id':int(user_id),'times':0,'main':int(main),'hash':hash})
    row=Sql(f"update AFK set times = times+1 where user_id =:user AND main=:main",{'user':int(user_id), 'main':int(main)})


def Set_All_AFK_Zero():
    row=Sql(f"update AFK set times = 0 ")


def Set_All_Group_AFK_Zero(main):
    row=Sql(f"update AFK set times = 0 WHERE main=:main ",{'main':int(main) })



def Set_User_AFK_Zero(user_id , main):
    row=Sql(f"update AFK set times = 0 WHERE user_id =:user AND main=:main",{'user':int(user_id) , 'main':int(main) })


