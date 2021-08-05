import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2\Classes')
sys.path.insert(0, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2\Databases')
#--------------------------------------------------------------------------| » Import Classes
from Classes.Group import Group                                                  #-|
from Classes.User import User                                                    #-|
#--------------------------------------------------------------------------|

def Instance(func):
    async def Wrapper(_, message):
        try:
            User_id=int(message.from_user.id)
            Chat_id=int(message.chat.id)
        except:
            User_id=int(message.from_user.id)
            Chat_id=int(message.message.chat.id)
        try:
            group=Group(Chat_id)
        except:
            await message.chat.leave()
            user=False
            group=False
        try:user=User(User_id,Chat_id)
        except:pass
        # try:group=Group(Chat_id)
        # except  Exception as e:group=False
        await func(message,group,user)
    return Wrapper