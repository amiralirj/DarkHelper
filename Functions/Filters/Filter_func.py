import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2\Classes')
from Classes.Admin import Admin
from Classes.Group import Group
from Config.Info.bot.api_bot import bot_id
from Config.Texts.Persian import on , off
from Classes.User import User
def Wrapper(_, __, msg_qry):
    try:
        chat_id=int(msg_qry.message.chat.id)
    except:
        chat_id=int(msg_qry.chat.id)
    try:
        gp=Group(chat_id)
    except:
        return False
    user=Admin(int(msg_qry.from_user.id),gp.Main)
    return bool(user.is_admin)


def Wrapper2(_, __, msg_qry):
    try:
        chat_id=int(msg_qry.message.chat.id)
    except:
        chat_id=int(msg_qry.chat.id)
    try:
        gp=Group(chat_id)
    except:return False
    user=Admin(int(msg_qry.from_user.id),gp.Main)
    return bool(user.is_nazer(msg_qry.chat.is_creator))


def Wrapper3(_, __, msg):
    if msg.reply_to_message :
        if int(msg.reply_to_message.from_user.id) == int(bot_id):
            chat_id=int(msg.chat.id)
            gap=Group(chat_id)
            return bool(gap.is_Question_Sended)
    
    return False


def Wrapper4(_, __, msg):
    if msg.new_chat_members:
        for i in msg.new_chat_members:
            if int(i.id)==int(bot_id):
                return True
    return False

def Wrapper5(_, __, msg):
    ID=int(msg.from_user.id)
    try:Chat=int(msg.chat.id)
    except:Chat=int(msg.message.chat.id)
    return User(ID).is_Shekar(Chat_Id=Chat)
            

def Get_Turn(Rj):
    if Rj:return on
    else :return off

def Get_Turn_Emoji(Rj):
    if Rj:return '🟢'
    else :return '🔴'

def Get_Turn_Bot_Emoji(Rj):
    li=['','','']
    li[Rj]='🟢'
    return li