from datetime import  datetime
import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\2\V2\Databases')
from Databases.Groups import GroupsPlayersBase , GroupsBase , GroupsControlBase 
from Databases.Groups.Bet import BetBase
from Databases.Users import AdminsBase 
from Databases.Users.AfksBase import  Set_All_Group_AFK_Zero
from Databases.Stats import AdminStatsBase , GroupStatsBase
from Classes.Statics import Statics
from Databases.Users.UsersBase import Show_Group_ALL_User_Points , Show_All_user_Points
from Databases.Users.ShekarsBase import Delete_Shekar

class Group:
    def __init__(self,Chat_id : int):
        Details=GroupsBase.Show_Group_Features(int(Chat_id))
        self.All_Atrebeutes=Details
        self.chat_id=int(Chat_id)
        self.Main = int(Details['group_id'])
        self.Support = int(Details['support_id'])
        self.Subscription_Date=str(Details['tamdid_date'])
        self.Deadline=int(Details['davazdah'])
        self.Auto_Tag=int(Details['auto_tag'])
        self.Auto_DeleteTag=int(Details['auto_del'])
        self.Auto_Tag_Support=int(Details['auto_tag_sup'])
        self.Auto_DeleteTag_Sup=int(Details['auto_del_sup'])
        self.Alarm=int(Details['alarm'])
        self.Bet=int(Details['bet'])
        self.Least_State=int(Details['state'])
        self.State_Lock=int(Details['state_lock'])
        self.Warn=int(Details['warn'])
        #--------------------------------------|
        # 0 - onyx                             |
        # 1 - werewolf                         |
        # 2 - black                            |
        self.Bot_Kind=int(Details['bot_kind'])#|
        #--------------------------------------|
        self.Mute_Fun=int(Details['fun_mute'])
        self.Auto_nextGame=int(Details['auto_next_game'])
        self.NextGame_Response=int(Details['next_game_response'])
        self.emoji1=str(Details['emoji1'])
        self.emoji2=str(Details['emoji2'])
        self.emoji3=str(Details['emoji3'])
        self.Sooti=int(Details['sooti'])
        self.Admin_Alarm=int(Details['admin_Alarm'])
        self.Ghaleb=str(Details['ghaleb'])
        self.JoinTime_Alarm=int(Details['jointime_sup'])
        self.Dead_NextGame=int(Details['dead_next'])
        self.Shekar_Pin=int(Details['pin_shekar'])
        self.Nazer_pin=int(Details['pin_nazer'])
        self.List_Pin=int(Details['pin_list'])
        self.Role_Saver=int(Details['role_saver'])
        self.Questions=int(Details['questions'])
        self.Bors=int(Details['bors'])
        self.Message_State=int(Details['message_state'])
        self.Next_Message_Id=int(Details['auto_next_message_id'])
        self.is_Question_Sended=int(Details['question_sended'])
        self.Auto_Start=int(Details['auto_start'])
        self.Afk_Warn=int(Details['afk_warn'])
        self.Is_Join_Time=int(Details['join_time'])
        self.Is_Tagging=int(Details['is_tagging'])
        self.Is_Time_For_Question=bool(Details['Its_Question_Time'])
        self.Players_Lock_Only=int(Details['players_state_lock'])
        #-----------------------------------------------------------
        Controls=GroupsControlBase.Show_Group_Control_Features(self.Main)
        self.All_Controls=Controls
        self.Welcome_Turn=int(Controls['welcometurn'])
        self.Anti_Spam=int(Controls['anti_spam'])
        self.Anti_Robot=int(Controls['anti_robot'])
        self.Anti_NFSW=int(Controls['fosh_filter'])
        self.Anti_Tabchi=int(Controls['anti_tabchi'])
        self.Channel =str(Controls['channel'])
        self.Channel_Lock=int(Controls['channellock'])
        self.Group_Lock=int(Controls['lock'])
        self.Voice_Lock=int(Controls['voice_lock'])
        self.Sticker_Lock=int(Controls['sticker_lock'])
        self.Photo_Lock=int(Controls['photo_lock'])
        self.Link_Lock=int(Controls['link_lock'])
        self.Forward_Lock=int(Controls['forward_lock'])
        self.Video_Lock=int(Controls['video_lock'])
        self.Service_Lock=int(Controls['service_lock'])
        self.Spam_Count=int(Controls['spam_count'])
        self.Welcome=str(Controls['welcome'])
        self.Channel_Text=str(Controls['channel_text'])
        #-----------------------------------------porn
        self.Porn=str(Controls['porn'])
        #-----------------------------
        Controls=Controls['Filters']
        self.Porn_All_Filters=Controls
        self.Porn_Dick_Filter=str(Controls['dick'])
        self.Porn_Pussy_Filter=str(Controls['pussy'])
        self.Porn_Coverd_Pussy_Filter=str(Controls['coveredpossy'])
        self.Porn_FBoobs_Filter=str(Controls['fboobs'])
        self.Porn_MBoobs_Filter=str(Controls['mboobs'])
        self.Porn_CoveredBoobs_Filter=str(Controls['coveredboobs'])
        self.Porn_Stomach_Filter=str(Controls['stomack'])
        self.Porn_ZirBaghal_Filter=str(Controls['baghal'])
        self.Porn_Ass_Filter=str(Controls['ass'])
        self.Porn_Feet_Filter=str(Controls['feet'])
        self.Porn_Covered_ASS_Filter=str(Controls['coveredass'])
    #-----------------------------------------------------------------
    @property
    def All_Players(self):
        return Show_All_user_Points()

    @property
    def All_Group_Players(self):
        return Show_Group_ALL_User_Points(self.Main)

    async def Get_Players_usernames(self,bot,lists):
        for i in lists:
            try:
                user=await bot.get_users(i)
                if user.username :
                    yield user.mention 
            except:pass

#-----------------------------------------------------------------
    def __int__(self) -> int:
        return int(self.Support)
    def __str__(self) -> str:
        return str(self.Main)
#-----------------------------------------------------------------
    @property
    def Show_Istagging(self):
        return GroupsBase.Show_one_feature('is_tagging',self.chat_id)

    @property
    def Show_JoinTime(self):
        return GroupsBase.Show_one_feature('join_time',self.chat_id)
    @property
    def Join_time_Started(self):
        GroupsBase.Change_Group_Feature(self.Main , 'join_time' , 1)
        return 1
    @property
    def Join_time_Finished(self):
        GroupsBase.Change_Group_Feature(self.Main , 'join_time' , 0)
        return 0
#-----------------------------------------------------------------
    @property
    def Show_All_Admins_Points(self):
        return AdminStatsBase.Show_Gap_All_Admins_Points(self.Main)

    @property
    def Admins(self):
        admins=AdminsBase.Show_All_Admins(self.Main)
        return [ admins , len(admins) ]

    @property
    def Show_Owner(self):
        return int(AdminsBase.Show_Owner(self.Main))
#-----------------------------------------------------------------
    @property
    def Show_Emojis(self):
        return [ self.emoji1 , self.emoji2 , self.emoji3 ]

    @property
    def Show_Welcome(self):
        wel=self.Welcome
        if wel == 'none':
            return None
        else:return wel

    @property
    def Show_Ghaleb(self):
        ghlb=self.Ghaleb
        if ghlb == 'none':
            return None
        else:return ghlb

    @property
    def Show_Channel(self):
        chnl=GroupsControlBase.Show_Channel(self.Main)
        if chnl == 'none':
            return None
        else:return chnl

    @property
    def Show_Next_Game_Text(self):
        if self.Bot_Kind ==0:return ' /nextgame@OnyxWereBetaBot '
        elif self.Bot_Kind ==1:return ' /nextgame@werewolfbot '
        elif self.Bot_Kind ==2:return ' /nextgame@Blackwwrobot \n /nextgame@blackwerewolfbot '
    #-----------------------------------------------------------------
    def Turn_Welcome_Turn(self):
        if self.Welcome_Turn:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'welcometurn' , x)
        return x 


    def Turn_Covered_Ass_Filter_Lock(self):
        if self.Porn_Covered_ASS_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'coveredass' , x)
        return x 

    def Turn_Dick_Filter_Lock(self):
        if self.Porn_Dick_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'dick' , x)
        return x 

    def Turn_pussy_Filter_Lock(self):
        if self.Porn_Pussy_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'pussy' , x)
        return x 

    def Turn_CoveredPussy_Filter_Lock(self):
        if self.Porn_CoveredBoobs_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'coveredpossy' , x)
        return x 

    def Turn_FBoobs_Filter_Lock(self):
        if self.Porn_FBoobs_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'fboobs' , x)
        return x 

    def Turn_MBoobs_Filter_Lock(self):
        if self.Porn_MBoobs_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'mboobs' , x)
        return x 

    def Turn_Covers_Boobs_Filter_Lock(self):
        if self.Porn_CoveredBoobs_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'coveredboobs' , x)
        return x 

    def Turn_Stomach_Filter_Lock(self):
        if self.Porn_Stomach_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'stomack' , x)
        return x 

    def Turn_ZirBaghal_Filter_Lock(self):
        if self.Porn_ZirBaghal_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'baghal' , x)
        return x 

    def Turn_Ass_Filter_Lock(self):
        if self.Porn_Ass_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'ass' , x)
        return x 

    def Turn_Feet_Filter_Lock(self):
        if self.Porn_Feet_Filter:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'feet' , x)
        return x 
    #-----------------------------------------------------------------
    def Turn_Video_Lock(self):
        if self.Video_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'video_lock' , x)
        return x 

    def Turn_Service_Lock(self):
        if self.Service_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'service_lock' , x)
        return x 
        
    def Turn_Voice_Lock(self):
        if self.Voice_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'voice_lock' , x)
        return x 

    def Turn_Sticker_Lock(self):
        if self.Sticker_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'sticker_lock' , x)
        return x 

    def Turn_Photo_Lock(self):
        if self.Photo_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'photo_lock' , x)
        return x

    def Turn_Link_Lock(self):
        if self.Link_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'link_lock' , x)
        return x 

    def Turn_Forward_Lock(self):
        if self.Forward_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'forward_lock' , x)
        return x 

    def Set_Anti_Spam(self,x):
        if self.Anti_Robot:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'anti_spam' , x)
        return x 

    def Turn_Anti_Robot(self):
        if self.Anti_Robot:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'anti_robot' , x)
        return x 

    def Turn_Anti_Porn(self):
        if self.Porn:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'porn' , x)
        return x 

    def Turn_Anti_NFSW(self):
        if self.Anti_NFSW:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'fosh_filter' , x)
        return x 

    def Turn_Anti_Tabchi(self):
        if self.Anti_Tabchi:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'anti_tabchi' , x)
        return x 

    def Set_Channel(self , x):
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'channel' , x)
        return x 

    def Set_Channel_text(self , x):
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'channel_text' , x)
        return x 

    def Set_Welcome(self , x):
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'welcome' , x)
        return x 

    def Set_Spam_Count(self , x):
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'spam_count' , x)
        return x 

    def Turn_Channel_Lock(self):
        if self.Channel_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'channellock' , x)
        return x 

    def Turn_Lock(self):
        if self.Group_Lock:
            x=0
        else:
            x=1
        GroupsControlBase.Change_Group_Control_Feature(self.Main , 'lock' , x)
        return x 
    #-------------------------------------------------------------------------- 
    def Change_Message_State(self):
        if self.Message_State:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'message_state' , x)
        return x 

    def Change_Bors(self):
        if self.Bors:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'bors' , x)
        return x 

    def Change_Questions(self):
        if self.Questions:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'questions' , x)
        return x 

    def Change_Role_Saver(self):
        if self.Role_Saver:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'role_saver' , x)
        return x 

    def Change_Nazer_pin(self):
        if self.Nazer_pin:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'pin_nazer' , x)
        return x 
        
    def Change_Shekar_Pin(self):
        if self.Shekar_Pin:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'pin_shekar' , x)
        return x 

    def Change_Dead_NextGame(self):
        if self.Dead_NextGame:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'dead_next' , x)
        return x 

    def Change_JoinTime_Alarm(self):
        if self.JoinTime_Alarm:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'jointime_sup' , x)
        return x 

    def Set_Ghaleb(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'ghaleb' , x)
        return x 

    def Set_Next_Message_Id(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'auto_next_message_id' , x)
        return x 

    def Change_Afk_Warn(self):
        if self.Afk_Warn:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'afk_warn' , x)
        return x 

    def Change_Admin_Alarm(self):
        if self.Admin_Alarm:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'admin_Alarm' , x)
        return x 

    def Change_Sooti(self):
        if self.Sooti:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'sooti' , x)
        return x 

    def Set_emoji1(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'emoji1' , x)
        return x 

    def Set_emoji2(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'emoji2' , x)
        return x 

    def Set_emoji3(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'emoji3' , x)
        return x 

    def Change_NextGame_Response(self):
        if self.NextGame_Response:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'next_game_response' , x)
        return x 

    def DeadLine_Ends(self):
        GroupsBase.Change_Group_Feature(self.Main , 'davazdah' , 0)
        return True


    def Change_Auto_NextGame(self):
        if self.Auto_nextGame:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'auto_next_game' , x)
        return x 

    def Change_Mute_Fun(self):
        if self.Mute_Fun:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'fun_mute' , x)
        return x 

    def Change_Bot_Kind(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'bot_kind' , x)
        return x

    def Set_Warn(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'warn' , x)
        return x 
    

    def Change_State_Lock(self,x):
        GroupsBase.Change_Group_Feature(self.Main , 'state_lock' , x)
        return x 

    def Set_State(self , x):
        GroupsBase.Change_Group_Feature(self.Main , 'state' , x)
        return x 

    def Change_Bet(self):
        if self.Bet:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'bet' , x)
        return x 

    def Change_Auto_Tag(self):
        if self.Auto_Tag:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'auto_tag' , x)
        return x 
    
    def Change_Auto_DeleteTag(self):
        if self.Auto_DeleteTag:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'auto_del' , x)
        return x 

    def Change_Auto_Tag_Support(self):
        if self.Auto_Tag_Support:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'auto_tag_sup' , x)
        return x 

    def Change_Auto_DeleteTag_Sup(self):
        if self.Auto_DeleteTag_Sup:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'auto_del_sup' , x)
        return x 

    def Change_Alarm(self):
        if self.Alarm:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'alarm' , x)
        return x 

    def Change_Auto_Start(self):
        if self.Alarm:
            x=0
        else:
            x=1
        GroupsBase.Change_Group_Feature(self.Main , 'auto_start' , x)
        return x 

    def Tag_Started(self):
        GroupsBase.Change_Group_Feature(self.Main , 'is_tagging' , 1)
        return
    
    def Tag_Stopped(self):
        GroupsBase.Change_Group_Feature(self.Main , 'is_tagging' , 0)
        return
    #------------------------------------------------------------------------|
    def Manual_Control_Change(self,row,amnt):                               #|
        if amnt:                                                            #|
            x=0                                                             #|
        else:                                                               #|
            x=1                                                             #|
        GroupsControlBase.Change_Group_Control_Feature(self.Main , row , x) #|
        return x                                                            #|
                                                                            #|
    def Manual_Change(self,row,amnt):                                       #|
        if amnt:                                                            #|
            x=0                                                             #|
        else:                                                               #|
            x=1                                                             #|
        GroupsBase.Change_Group_Feature(self.Main , row , x)                #|
        return x                                                            #|        
    #------------------------------------------------------------------------|
    def Reset_AFKS(self):
        Set_All_Group_AFK_Zero( self.Main )
        return True
    
    def END_Bet(self , team : int ):
        x=BetBase.win( team , self.Main )
        return x
    
    def Game_Started(self,hash,Join_Time,players):
        'time,players,main,hour,afk,hash,date'
        GroupStatsBase.Add_Game(Join_Time,players,self.Main,int((datetime.now()).hour),hash)
        return True
    
    def Add_Game_AFk(self , hash):
        GroupStatsBase.Add_AFK(self.Main , hash)
        return True
    @property
    def Last_Match(self):
        return GroupStatsBase.Show_Group_State_last_Game(self.Main)


    @property
    def Show_Games(self):
        return GroupStatsBase.Show_Group_State_All_Time(self.Main)

    @property
    def Show_Games_Today(self):
        return GroupStatsBase.Show_Group_State_Today(self.Main)
    
    def Is_Expired(self):
        another_day = datetime.datetime.now().strptime(self.Subscription_Date,"%Y-%m-%d")
        Day = datetime.datetime.now()
        if Day < another_day:
            return False
        else : return True
        
    #-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0|
    def Tamdid(self,Date=30):                                      #0|
        GroupsBase.Add_Group(self.Main , self.Support , Date)      #0|
        return                                                     #0|
    #-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0|

    def Question_Sended(self):
        GroupsBase.Change_Group_Feature(self.Main , 'question_sended' , 1)
        return 1 

    def Question_Answered(self):
        GroupsBase.Change_Group_Feature(self.Main , 'question_sended' , 0)
        return 0
    #----------------------------------------------------------------------------
    def Its_Question_time(self):
        GroupsBase.Change_Group_Feature(self.Main , 'Its_Question_Time' , 1)
        return 1 

    def Question_Time_Passes(self):
        GroupsBase.Change_Group_Feature(self.Main , 'Its_Question_Time' , 0)
        return 0
    #-------------------------------------------------------------------------
    @property
    def Show_Players(self):
        return GroupsPlayersBase.Show_Players(self.Main)

    def Delete_Players(self):
        GroupsPlayersBase.Delete_All_Players(self.Main )
        return True

    async def Add_Players(self,id_list,bot):
        for i in id_list:
            name=(await bot.get_users(i)).first_name
            GroupsPlayersBase.insert_players(i,self.Main,name)
        return True
    
    @property
    def Show_Deads_Name(self):
        return GroupsPlayersBase.Show_Dead_Players_Name(self.chat_id)
    
    @property
    def Zerib(self):
        plyrs=self.Show_Players
        deads=0
        alives=0
        all=len(plyrs)
        for i in plyrs:
            if int(i[1])==1:alives+=1
            else:deads+=1
        if alives>=40:
            zarib_bet=float((all+alives)/(deads+30))
        elif alives>35:
            zarib_bet=float((all+alives)/(deads+26))
        elif alives>=30:
            zarib_bet=float((all+alives)/(deads+25))
        elif alives>=25:
            zarib_bet=float((all+alives)/(deads+23))
        elif alives>=15:
            zarib_bet=float((all+alives)/(deads+21))
        elif alives>=10:
            zarib_bet=float((all+alives)/(deads+16))
        elif alives>=5:
            zarib_bet=float((all+alives)/(deads+13))
        elif alives<5:
            zarib_bet=0.01

        return zarib_bet

    @property
    def Team_Zarib(self):
        Zr=float(self.Zerib)
        return [Zr * 0.70 ,Zr * 0.80 ,Zr * 0.90 ,Zr  ,Zr * 1 ,Zr * 1.05 ,Zr * 1.5 ]
    
    @property
    def Group_Teams(self):
        if self.Bot_Kind==0:
            Role='🧛🏻‍♀️ ومپایر 🧛🏻‍♀️'
        elif self.Bot_Kind==1:
            Role='💖 لاور 💖'
        else:
            Role='💣 بمبر 💣'

        return {0:'👩🏻‍🦰👨🏻‍🦱 روستا 👩🏻‍🦰👨🏻‍🦱'
            ,1:'👥 فرقه 👥'
            ,2:'🐺 گرگ 🐺'
            ,3:'🔪 قاتل 🔪'
            ,4:Role
            ,5:'🔥 آتش 🔥'
            ,6:'👺 منافق 👺'}

    @property
    def Start_Command(self):
        if self.Bot_Kind ==0:    return '/startmighty@OnyxWereBetaBot'
        elif self.Bot_Kind ==1:  return '/startchaos@werewolfbot'
        elif self.Bot_Kind ==2:  return '/startmighty@Blackwwrobot'
        
    def delete(self):
        GroupsBase.Delete_Group(self.Main)
        return True
    
    def Delete_Shekar(self):
        Delete_Shekar(self.Main)
        return True 