from ..MainBase import Sql_User as Sql

def add_admins(admin,main_gap):
    hash=str(admin)+str(main_gap)
    row=Sql(f"insert into admins (admin,gap,asli,hash) values (:id,:gap,:asli,:hash)",{'id':int(admin),'gap':main_gap,'asli':0,'hash':hash})


def Add_Owner(main_admin,main_gap):
    hash=str(main_admin)+str(main_gap)
    row=Sql(f"insert or ignore into admins (admin,gap,asli,hash) values(:id,:gap,:asli,:hash)",{'id':int(main_admin),'gap':main_gap,'asli':1,'hash':hash})
    row=Sql('UPDATE admins SET asli = 1 WHERE admin =:User_id AND gap=:Group_id',{'User_id':int(main_admin),'Group_id':main_gap})


def Delete_Admin(main_admin,main_gap):
    hashs=str(main_admin)+str(main_gap)
    row=Sql('DELETE FROM admins where hash=:hash',{'hash':hashs})


def Delete_Admin_Nazer(main_admin,main_gap):
    hashs=str(main_admin)+str(main_gap)
    row=Sql('DELETE FROM admins where hash=:hash AND asli = 0',{'hash':hashs})


def Cheak_Main_Admin(admin,main):
    '''admin asli boolian'''
    row=Sql(f'SELECT asli FROM admins WHERE admin=:admin AND gap=:gap',{'admin':int(admin),'gap':main})
    q=row
    try:
        if q[0][0]==1:
            return True
        else:
            return False
    except:
        return False

def admin_cheak(admin,main):
    '''admin  boolian'''
    row=Sql(f'SELECT asli FROM admins WHERE admin=:admin AND gap=:gap',{'admin':int(admin),'gap':main})
    q=row
    try:
        if q[0][0]==0 or q[0][0]==1:
            return True
        else:
            return False
    except:
        return False

def Show_All_Admins(main_gap):
    row=Sql(f'SELECT admin FROM admins WHERE gap={int(main_gap)}')
    q=row
    a=[]
    for i in q:
        a.append(i[0])
    return a


def Delete_Gap_Admins(main):
    row=Sql('DELETE FROM admins WHERE gap=:group AND asli=0',{'group':main})


def Delete_Gap_Admins(main):
    row=Sql('DELETE FROM admins WHERE gap=:main',{'main':main})


def Show_Owner(main : int ):
    row=Sql('SELECT admin FROM admins WHERE gap=:group AND asli=1',{'group':int(main)})
    row=row
    return row[0][0]

def Show_Admin_Group(User_id):
    row=Sql('SELECT gap FROM admins WHERE admin=:admin ',{'admin':int(User_id)})
    return row