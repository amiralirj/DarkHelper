from threading import Timer , Thread
import sys , os 
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\2\V2')   
from Classes.Robot import Robot  
from Classes.Group import Group  
from datetime import datetime
from Config.Info.bot.api_bot import bot
# from Functions.Tag.tag import Tag
from Errors.Error import error
robot=Robot()   
 
def Every_Day():
    robot=Robot()
    if datetime.today().day==1:
        robot.Kill_Ranks()
    robot.Set_AFK_0()
    for i in robot.All_Gaps:
        gap=Group(int(i[0]))
        Day = datetime.now().strptime(gap.Subscription_Date ,"%Y-%m-%d")
        if datetime.now() > Day:
            if bool(gap.Deadline):
                gap.delete()
            else:
                gap.DeadLine_Ends()
    # call again in Next Day
    Timer(86400, Every_Day).start()

def Every_Minute():
    # call again in 60 seconds
    Timer(60, Every_Minute).start()

def Every_10_sec():
    global bot
    robot=Robot()
    #For Tagging Without Partners Message !
    # for i in robot.All_Gaps:
    #     gap=Group(int(i[0]))
    #     if gap.Is_Join_Time:
    #         if not gap.Is_Tagging:
    #             Thread(target = Tag(gap , bot),args=[]).start()
    robot.Set_Spam_0()
    # call again in 10 seconds
    Timer(9, Every_10_sec).start()

def Every_Month():
    robot=Robot()
    robot.Kill_Ranks()
    # call again in Next Month
    Timer(2678400, Every_Month).start()
    
def Every_Hour():
    try:                       # path/to/directory 
        for file in os.listdir(r'/root/helper/Dark_Helper') :
            try:
                if file.endswith('.jpg'):
                    os.remove(file) 
            except:pass
    except:pass
    robot=Robot()
    hour=int(datetime.now().hour)
    if hour > 12:
        for i in robot.All_Gaps:
            try:
                gap=Group(int(i[0]))
                if gap.Questions:
                    gap.Its_Question_time()
            except Exception as e:
                error('{e} - 51 Priodically ')
                print(e)
    # call again in Next Hour
    Timer(3600, Every_Hour).start()

def Call_Month_priod():
    Timer(2678400, Every_Month).start()