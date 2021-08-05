from pyrogram.filters import create , user , regex
import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2')
from Functions.Filters.Filter_func import Wrapper , Wrapper2 , Wrapper3 , Wrapper4 , Wrapper5
from Classes.Group import Group
from Config.Info.bot.partner_bot import bot_id
from Config.Info.Supports import Owner , wwBots
from Config.Info.bot.api_bot import bot_id as main_bot
class Filters:
    def __init__(self) -> None:
        self.admin=create(Wrapper)
        self.nazer=create(Wrapper2)
        self.Question=create(Wrapper3)
        self.Dark_Helper_Added=create(Wrapper4)
        self.partner=user(int(bot_id))
        self.Owner=user(int(Owner))
        self.Dark=user(int(main_bot))
        self.WWBOTS=user(wwBots)
        self.shekar=create(Wrapper5)

    def Filter_Feature(self,row):
        def Wrapper(_, __, msg):
            chat_id=int(msg.chat.id)
            gap=Group(chat_id)
            if gap.All_Atrebeutes[row] :
                return True
            else:
                return False
        return create(Wrapper)


    # @property
    # def Nazer(self):
    #     return self.nazer

    # @property
    # def Admin(self):
    #     return self.admin
        
    # @property
    # def Question(self):
    #     return self.quest

    # @property
    # def Dark_Helper_Added(self):
    #     return self.bot