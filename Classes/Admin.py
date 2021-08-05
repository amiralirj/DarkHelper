import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\2\V2')
from Databases.Users import AdminsBase
from Databases.Stats import AdminStatsBase
class Admin :
    def __init__(self , User_id:int , Chat_id:int):
        self.user_id=int(User_id)
        self.chat_id = int(Chat_id)
        

    def is_nazer(self, Is):
        if Is : 
            return True
        chk=AdminsBase.Cheak_Main_Admin( self.user_id , self.chat_id )
        return chk
        
    @property
    def is_admin(self):
        chk=AdminsBase.admin_cheak( self.user_id , self.chat_id )
        return chk
    
    def Add_Point( self , join=0 , tag=0 , afk=0 ):
        AdminStatsBase.Add_Admin_Point(self.user_id , self.chat_id , join , tag , afk)
        return True
    
    def stats(self):
        return AdminStatsBase.Show_Admin_Point(self.user_id , self.chat_id )
    
    def Set_Admin(self):
        try:
            AdminsBase.add_admins(self.user_id , self.chat_id)
            return True
        except:
            False

    def Set_Nazer(self):
        AdminsBase.Add_Owner(self.user_id , self.chat_id)
        return True
            
    def Delete_Admin(self):
        AdminsBase.Delete_Admin(self.user_id , self.chat_id)


    def show_gap(self,user_id):
        return AdminsBase.Show_Admin_Group(user_id)
