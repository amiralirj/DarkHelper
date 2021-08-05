from ..MainBase import Sql_group as Sql 

def insert_players(id,group,name):
    row=Sql('insert into players (user_id,Group_id,alive,Role,name,Pretended_Role) values (:user_id,:Group_id,:alive,:Role,:name,:Pretended_Role)',
    {'Role':'none','alive':1,'user_id':int(id),'Group_id':int(group),'name':name,'Pretended_Role':'none'})


def Show_Players(group):
    row=Sql('SELECT user_id,alive,Role,name,Pretended_Role FROM players WHERE Group_id=:gap',{'gap':int(group)})
    return row

def Delete_All_Players(group):
    row=Sql('DELETE FROM players WHERE Group_id=:gap',{'gap':int(group)})

def Player_Dead(user_id,group,Role):
    row=Sql('UPDATE players SET alive=0 , Role =:PlRole WHERE Group_id=:gap AND user_id=:user',{'user':int(user_id),'gap':int(group),'PlRole':Role})

def Set_Pretended_Role(user_id,group,Role):
    row=Sql('UPDATE players SET Pretended_Role=rl  WHERE Group_id=:gap AND user_id=:user',{'user':int(user_id),'gap':int(group),'rl':Role})

def Show_Pretended_Role(group,user_id):
    row=Sql('SELECT Pretended_Role FROM players WHERE Group_id=:gap AND user_id=:user',{'gap':int(group),'user':int(user_id)})
    return row

def Show_Dead_Players_Name(group):
    row=Sql('SELECT name,user_id FROM players WHERE Group_id=:gap and NOT Role=:o',{'gap':int(group),'o':'none'})
    return row