import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2')
from Databases.Users import UsersBase , ShekarsBase , AfksBase
from Functions.Requests.Player_State import  *
from Functions.Pointing.Convert_Emojies import Emoji
from Databases.Users.MuteFun import MuteBase
from Databases.Groups.Message import SpamBase
from Config.Texts.NFSW.NFSW import NFSW_Names
from Databases.Groups import GroupsPlayersBase 
from Databases.Groups.Bet import BetBase
from Databases.Stats.UsersRanksBase import user_rank
from Config.Texts.Persian import User_ProFile , not_Reg
import datetime
class User :
    def __init__( self , User_id:int , Chat_id =123 ):
        self.user_id=int(User_id)
        try:
            Details=UsersBase.Show_User_Info(self.user_id)
        except:
            UsersBase.Add_Player(self.user_id , Chat_id) 
            Details=UsersBase.Show_User_Info(self.user_id)
        self.Point = int(Details['point'])
        self.Coin = int(Details['coin'])
        self.Diamond = float(Details['diamonds'])
        self.Laghab = str(Details['laghab'])
        self.BirthDay = str(Details['birth'])
        self.CorectBets = int(Details['corectbet'])
        self.Amount = int(Details['amount'])
        self.Group = int(Details['main'])
        self.Warn = int(Details['warn'])
        self.Ghosts = int(Details['ghost_power'])
        self.Anti_Ghosts = int(Details['anti_ghost'])
        self.Ghost_Killers = int(Details['ghost_killer'])
        if str(Details['nextgame']) == 'none':self.Next_frame=None
        else:self.Next_frame=str(Details['nextgame'])



    @property
    async def State(self) -> list:
        '''onyx , black , were'''
        return [int(await (Onyx_State_Req(self.user_id))),int(await (Black_State_Req(self.user_id))),int(await (Werewolf_State_Req(self.user_id)))]

    def __int__(self):
        return int(self.user_id)

    def Add_Points(self,Count:int):
        if int(Count) > 0:
            UsersBase.insert_point(self.user_id , int(Count))
        else:
            UsersBase.reduce_point(self.user_id , int(Count))
        return True

    def Add_Coins(self,Count:int):
        if int(Count) > 0:
            UsersBase.insert_coin(self.user_id , int(Count))
        else:
            UsersBase.reduce_coin(self.user_id , int(Count))
        return True

    def Add_Amount(self,Count:int):
        if int(Count) > 0:
            UsersBase.insert_amount(self.user_id , int(Count))
        else:
            UsersBase.reduce_amount(self.user_id , int(Count))
        return True

    def Add_Diamond(self,Count:float):
        if int(Count) > 0:
            UsersBase.insert_diamonds(self.user_id , float(Count))
        else:
            UsersBase.reduce_diamonds(self.user_id , float(Count))
        return True

    def Set_Laghab(self, laghab:str):
        UsersBase.set_laghab(self.user_id , str(laghab))
        return True
    
    def Set_Birth(self, birth:str):
        UsersBase.set_birth(self.user_id , str(birth))
        return True
    
    def Add_Correct_Bet(self):
        UsersBase.insert_corectbet(self.user_id)
    
    def Add_Ghost(self,Count:int):
        if int(Count) > 0:
            UsersBase.insert_Power(self.user_id , ghost_power=int(Count))
        else:
            UsersBase.reduce_Power(self.user_id , ghost_power=int(Count))
        return True

    def Add_Anti_Ghost(self,Count:int):
        if int(Count) > 0:
            UsersBase.insert_Power(self.user_id , anti_ghost=int(Count))
        else:
            UsersBase.reduce_Power(self.user_id , anti_ghost=int(Count))
        return True

    def Add_Ghost_Killer(self,Count:int):
        if int(Count) > 0:
            UsersBase.insert_Power(self.user_id , ghost_killer=int(Count))
        else:
            UsersBase.reduce_Power(self.user_id , ghost_killer=int(Count))
        return True
    
    def is_Enough_Coin(self , Amount ):
        if self.Coin > int(Amount):
            return True 
        else:  return False

    def is_Enough_Diamond(self , Amount ):
        if self.Diamond > int(Amount):
            return True 
        else:  return False

    def is_Enough_Point(self , Amount ):
        if self.Point > int(Amount):
            return True 
        else:  return False
    #-------------------------------------------------
    def is_Muted(self , Chat_Id : int ):
        try:
            Date=MuteBase.Show_Mute_User(self.user_id , Chat_Id)
            another_day = datetime.datetime.now().strptime(Date, "%Y-%m-%d-%H:%M:%S")
            if datetime.datetime.now() > another_day:
                return False
            else : return True
        except Exception as e:
            return False

    def is_Suspended_Mute(self , Chat_Id : int ):
        Date=MuteBase.Show_Mute_User(self.user_id , Chat_Id)
        datetime.datetime(2019, 3, 5)
        if not Date :return False
        another_day = (datetime.datetime.now()).strptime(Date, "%Y-%m-%d-%H:%M:%S")
        if datetime.datetime.now() < (another_day + datetime.timedelta(minutes=15)):
            return True
        else : return False

    def UnMute(self,Chat_id):
        MuteBase.Delete_User_Mute(self.user_id,Chat_id)
        return True

    def Mute(self , Chat_id : int ):
        MuteBase.Add_Muted(self.user_id , Chat_id )
        return True

    async def is_State_Enough(self , Group ):
        st =( await self.State)
        for i in st:
            if i >= Group.Least_State :
                return True
        return False 

    def Set_Shekar(self , Group):
        ShekarsBase.Add_Shekar(self.user_id,Group.chat_id)
        return True

    def is_Shekar(self , Group=None , Chat_Id = None ):
        if not Chat_Id:return ShekarsBase.Shekar_Cheak( self.user_id ,Group.chat_id)
        else:return ShekarsBase.Shekar_Cheak( self.user_id , Chat_Id)
#-----------------------------------------------------------
    def AFK(self , Group):
        AfksBase.Insert_AFK(self.user_id , Group.chat_id)
    
    def AFK_Count(self):
        return AfksBase.Show_User_AFKs(self.user_id)
    
    def AFk_Cheak_Count(self , Group):
        if self.Show_Warn(Group.chat_id) >= Group.AFK_Warn :
            return True
        else : False

    def Set_AFK_Zero(self , Group):
        AfksBase.Set_User_AFK_Zero(self.user_id , Group.chat_id)
        return True
    #-----------------------------------------------------------
    def Add_Warn(self,chat_id):
        UsersBase.Insert_warn(self.user_id ,chat_id)
        return True

    def Reduce_Warn(self , chat_id ):
        UsersBase.reduce_warn(self.user_id ,chat_id)
        return True
    
    def set_Warn_0(self , chat_id):
        UsersBase.Set_User_warn_Zero(self.user_id ,chat_id)
        return True
    
    def Show_Warn(self , chat_id):
        return UsersBase.Show_User_warns(self.user_id ,chat_id)
    #-----------------------------------------------------------
    def is_Spammer(self, Group):
        if int(SpamBase.Show_User_Messages(self.user_id , Group.chat_id)) >= Group.Spam_Count :
            return True
        else : return False

    def is_tabchi(self , name):
        for i in NFSW_Names:
            if i in name :
                return True
        else : return False

    def Add_Message(self,Group):
        SpamBase.Add_User_message(self.user_id , Group.chat_id )
        return True
    
    def is_Player(self,Chat_id):
        plyr_list=[int(i[0]) for i in GroupsPlayersBase.Show_Players(Chat_id)]
        if self.user_id in plyr_list:
            return True
        else:return False
    
    def Dead(self,Chat_id , Role):
        GroupsPlayersBase.Player_Dead(self.user_id , int(Chat_id), str(Role))
        return True

    def bet(self,Amount:int ,Team : int, Zarib:float ,Chat_id:int ):
        BetBase.Start_Group_Bet(self.user_id , Team , Amount , Zarib , Chat_id)
        return True

    @property
    def Last_Ranks(self):
        return user_rank(self.user_id)

    @property
    def get_Ranks(self):
        DataBase_List=UsersBase.Show_All_user_Points()
        Global_point=0
        for stat in DataBase_List[::-1]:
            Global_point+=1
            if int(self.user_id)==int(stat[0]):
                break

        DataBase_List=UsersBase.Show_All_user_Coins()
        Global_Coin=0
        for stat in DataBase_List[::-1]:
            Global_Coin+=1
            if int(self.user_id)==int(stat[0]):
                break

        DataBase_List=UsersBase.Show_Group_ALL_User_Points(self.Group)
        Local_Point=0
        for stat in DataBase_List[::-1]:
            Local_Point+=1
            if int(self.user_id)==int(stat[0]):
                break

        DataBase_List=UsersBase.Show_Group_ALL_User_Coins(self.Group)
        Local_Coin=0
        for stat in DataBase_List[::-1]:
            Local_Coin+=1
            if int(self.user_id)==int(stat[0]):
                break
        
        return {'Local':{'Coin':Local_Coin,'Point':Local_Point},'Global':{'Coin':Global_Coin,'Point':Global_point}}

    def ProFile(self , group , men , title):
        last_rank=self.Last_Ranks
        ranks=self.get_Ranks
        emj=(Emoji.show_emt(self.Amount,group.Show_Emojis))
        Frame=group.Show_Ghaleb
        laghab=self.Laghab
        birth= self.BirthDay
        if str(laghab.lower())=='none':
            laghab=not_Reg
        if str(birth).lower()=='none':
            birth=not_Reg
        if Frame == None:return User_ProFile(men , title , self.Coin , self.Coin , self.Diamond ,
        ranks['Global']['Point'],ranks['Local']['Point'],ranks['Global']['Coin'],ranks['Local']['Coin'],self.Ghosts,self.Anti_Ghosts,self.Ghost_Killers,last_rank[0],last_rank[1],emj,laghab,birth)
        else:return str(group.Show_Ghaleb).replace('{name}',men).replace('{point}',self.Point).replace('{coin}',self.Coin).replace('{title}',title).replace('{bitcoin}',self.Diamond).replace('{ghost}',self.Ghosts).replace('{antighost}',self.Anti_Ghosts).replace('{ghostkiller}',self.Ghost_Killers).replace('{Warn}',self.Show_Warn(group.chat_id)).replace('{laghab}',self.Laghab).replace('{birth}',self.BirthDay).replace('{bets}',self.CorectBets).replace('{Pointing}',f'{emj[0]}\n{emj[1]}\n{emj[2]}').replace('{last_dolar_rank}',last_rank[0]).replace('{last_litecoin_rank}',last_rank[1]).replace('{litecoin_rank_global}',ranks['Global']['Coin']).replace('{dolor_rank_global}',ranks['Global']['Point']).replace('{litecoin_rank_local}',ranks['Local']['Coin']).replace('{dolor_rank_local}',ranks['Local']['Point'])

    async def mention(self,bot):
        try:return ((await bot.get_users(self.user_id)).mention) 
        except:return self.user_id

    def Set_Next_frame(self,x):
        UsersBase.Change_User_Feature( self.user_id , 'nextgame' , x)
        return True
