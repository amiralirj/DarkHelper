import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2\Classes')
sys.path.insert(0, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2\Databases')
#--------------------------------------------------------------------------| » Import Classes
from Classes.IO import IO                                             #-|
#--------------------------------------------------------------------------|

def Partner(func):
    async def Wrapper(_, message):
        try:OBJ=IO(str(message.text.html))
        except:OBJ=IO(str(message.text))
        await func(int(OBJ) , str(OBJ) , OBJ.kind  )
    return Wrapper