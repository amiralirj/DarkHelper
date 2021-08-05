import sys 
from random import choice
sys.path.insert(2, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2') 
from Databases.Groups.Message.SpamBase import Set_Zero_All_Message_Spams
from Databases.Users.AfksBase import Set_All_AFK_Zero
from Databases.Stats import UsersRanksBase , GroupStatsBase
from Databases.Users.UsersBase import Show_All_user_Points  , Show_All_user_Coins , Set_0_All_PC
from Databases.Groups import GroupsBase,GroupsControlBase  
from Errors.Error import error
from Config.Texts.Question.questions import Question_Dict
from Databases.MainBase import Create_Spam
class Robot:
    def __init__(self) -> None:
        self.Question=Question_Dict
    
    def Set_Spam_0(self):
        # con = sqlite3.connect("helper.db" , detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
        # c=con.cursor()
        Set_Zero_All_Message_Spams()
        Create_Spam()
        return

    def Set_AFK_0(self):
        # con = sqlite3.connect("helper.db" , detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
        # c=con.cursor()
        return Set_All_AFK_Zero()
    
    def Kill_Ranks(self):
        # con = sqlite3.connect("helper.db" , detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
        # c=con.cursor()
        Users_Point=Show_All_user_Points()
        rank=1
        for i in Users_Point[::-1]:
            try:
                UsersRanksBase.Kill_Ranks(int(i[0]),rank)
                rank+=1
            except Exception as e:
                error(f'{e} Classes-Robot-28')

        rank=1
        Users_Coin=Show_All_user_Coins()
        for i in Users_Coin[::-1]:
            try:
                UsersRanksBase.Insert_User_Ranks(int(i[0]),rank)
                rank+=1
            except Exception as e:
                error(f'{e} Classes-Robot-37')
        Set_0_All_PC()

    @property
    def All_Groups_Game(self):
        return GroupStatsBase.Show_All_Groups_States()
    
    def Add_Gap(self,Chat_id:int , Support : int , date=30):
        GroupsControlBase.Add_GroupControl(Chat_id)
        GroupsBase.Add_Group(Chat_id , Support , date)
        return True

    def Same_Groups(self,kind):
        return GroupsBase.Show_All_Groups_IN_Kind(kind)
        
    @property
    def All_Gaps(self):
        return GroupsBase.Show_All_GroupIds()

    @property
    def Random_Question(self):
        Ques=choice(list(self.Question.items()))
        return Ques[0]

     #-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0|
    def Add_Gap(self,Chat_Id:int,Support : int ,Date=30):                                      #0|
        GroupsBase.Add_Group(Chat_Id , Support , Date)             #0|
        GroupsControlBase.Add_GroupControl(Chat_Id)
        return                                                     #0|
    #-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0|
        
