import sqlite3 as db 
import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\2\V2')
from Config.Info.Supports import path
def start():
    con = db.connect(f"{path}DarkHelper-Group.db"  ,check_same_thread = False)
    c=con.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS groups ( 
    group_id INT PRIMARY KEY ,
    support_id INT           ,
    tamdid_date TEXT         ,
    davazdah INT             ,
    auto_tag INT             ,
    auto_del INT             ,
    auto_tag_sup INT         ,
    auto_del_sup INT         , 
    alarm INT                , 
    bet INT                  , 
    state INT                , 
    warn  INT                , 
    bot_kind INT             ,
    fun_mute INT             ,
    state_lock INT           ,
    auto_next_game INT       ,
    auto_next_message_id INT ,
    next_game_response INT   ,
    emoji1 TEXT              ,
    emoji2 TEXT              ,
    emoji3 TEXT              ,
    sooti INT                ,
    admin_Alarm INT          , 
    ghaleb TEXT              ,
    jointime_sup INT         ,
    dead_next INT            ,
    pin_shekar INT           ,
    pin_nazer INT            ,
    pin_list INT             ,
    role_saver INT           ,
    questions INT            ,
    bors INT                 ,
    message_state INT        ,
    question_sended INT      ,
    auto_start INT           ,
    afk_warn   INT           ,
    join_time  INT           ,
    is_tagging INT           ,
    Its_Question_Time INT    ,
    players_state_lock INT    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS groups_control (  
    group_id INT PRIMARY KEY ,
    anti_spam    INT         ,
    anti_robot   INT         ,
    anti_tabchi  INT         ,
    fosh_filter  INT         ,
    lock INT                 ,
    channel      TEXT        ,
    channellock  INT         ,
    voice_lock   INT         ,
    sticker_lock INT         ,
    photo_lock   INT         ,
    link_lock    INT         ,
    forward_lock INT         ,
    video_lock   INT         ,
    service_lock INT         ,
    spam_count   INT         ,
    welcome TEXT             ,
    channel_text TEXT        ,
    porn INT                 ,
    dick INT                 ,
    pussy INT                ,
    coveredpossy INT         ,
    fboobs INT               ,
    mboobs INT               ,
    coveredboobs INT         ,
    stomack INT              ,
    baghal INT               ,
    ass INT                  ,
    feet INT                 ,
    coveredass INT           ,
    welcometurn INT          ) ''' )
    c.execute('CREATE TABLE IF NOT EXISTS hashtags (hashtag TEXT , msg_id INT ,  Group_id INT , hash TEXT )')
    c.execute('CREATE TABLE IF NOT EXISTS players ( user_id  INT , Group_id INT,alive INT , Role TEXT , name TEXT , Pretended_Role)')
    #------------------------------------------------------------------------------------------------------------------
    con = db.connect(f"{path}DarkHelper-User.db"  ,check_same_thread = False)
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users ( user_id INT PRIMARY KEY, point INT , coin INT,  laghab TEXT , birth TEXT , corectbet INT , amount INT , main INT , warn INT, ghost_power INT , anti_ghost INT , ghost_killer INT , diamonds REAL, nextgame TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS AFK (user_id INT , times , main INT , hash INT PRIMARY KEY )')
    c.execute('CREATE TABLE IF NOT EXISTS shekar (user_id INT ,  main INT PRIMARY KEY)')
    c.execute('CREATE TABLE IF NOT EXISTS warn (user_id INT , times , main INT , hash INT PRIMARY KEY )')
    c.execute('CREATE TABLE IF NOT EXISTS admins (admin INT , gap  INT,asli INT , hash TEXT PRIMARY KEY)')

    con = db.connect(f"{path}DarkHelper-Stats.db"  ,check_same_thread = False)
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS adminstats (user_id INT  ,tag INT , game_join INT , AFK INT  ,Group_id INT , time TEXT   )')
    c.execute('CREATE TABLE IF NOT EXISTS jointime (time TEXT , players  INT , main INT , hour TEXT , afk INT , hash INT , date TEXT )')
    c.execute('CREATE TABLE IF NOT EXISTS ranks ( user_id  int  , point INT , coin INT,month INT)')

    con = db.connect(f"{path}DarkHelper-Fun.db"  ,check_same_thread = False)
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS bet ( user_id INT ,amount INT,active INT,win INT,team INT,zarib REAL,main INT )')
    c.execute('CREATE TABLE IF NOT EXISTS muted_users ( user_id  INT , Group_id INT , date INT)')

    con = db.connect(f"{path}DarkHelper-Cheak.db"  ,check_same_thread = False)
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS message ( message_id  INT , Group_id INT)')
    c.execute('CREATE TABLE IF NOT EXISTS spam ( user_id  INT , Group_id INT ,  hash TEXT PRIMARY KEY , times INT)')


def Create_Spam():
    con = db.connect(f"{path}DarkHelper-Cheak.db"  ,check_same_thread = False)
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS spam ( user_id  INT , Group_id INT ,  hash TEXT PRIMARY KEY , times INT)')


def Sql_Cheak(Query,Params={}):
    with db.connect(f"{path}DarkHelper-Cheak.db"  ,check_same_thread = False) as con :
        c=con.cursor()
        c.execute(Query,Params)
        con.commit()
        q=c.fetchall()
    return q

def Sql_User(Query,Params={}):
    with db.connect(f"{path}DarkHelper-User.db"  ,check_same_thread = False) as con :
        c=con.cursor()
        c.execute(Query,Params)
        con.commit()
        q=c.fetchall()
    return q

def Sql_Stats(Query,Params={}):
    with db.connect(f"{path}DarkHelper-Stats.db"  ,check_same_thread = False) as con :
        c=con.cursor()
        c.execute(Query,Params)
        con.commit()
        q=c.fetchall()
    return q

def Sql_Fun(Query,Params={}):
    with db.connect(f"{path}DarkHelper-Fun.db"  ,check_same_thread = False) as con :
        c=con.cursor()
        c.execute(Query,Params)
        con.commit()
        q=c.fetchall()
    return q

def Sql_group(Query,Params={}):
    with db.connect(f"{path}DarkHelper-Group.db"  ,check_same_thread = False) as con :
        c=con.cursor()
        c.execute(Query,Params)
        con.commit()
        q=c.fetchall()
    return q

    
def Sql_One(Query,Params={}):
    with db.connect(f"{path}DarkHelper-Stats.db"  ,check_same_thread = False) as con :
        c=con.cursor()
        c.execute(Query,Params)
        con.commit()
        q=c.fetchone()
    return q
