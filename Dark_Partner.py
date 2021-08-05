#--------------------------------------------------------------------------| » Import Informations from Config
from Config.Info.bot.partner_bot import bot                              #-|
from Config.Info.bot.api_bot import bot_username                         #-|
#--------------------------------------------------------------------------| » Import Classes
from Classes.Filters import Filters                                      #-|
from Classes.Group import Group                                         #-|
from Classes.IO import IO                                                #-|
from Classes.User import User                                            #-|
from Classes.Admin import Admin                                          #-|
#--------------------------------------------------------------------------| » Importing madules (filters , re )
import re , time , random , datetime  , asyncio                          #-|
from pyrogram import filters                                             #-|
#--------------------------------------------------------------------------| » Importing texts
from Config.Texts import Persian as texts # or English                   #-|
#--------------------------------------------------------------------------| » Instantiating From Filters Class
from Classes.Filters import Filters                                      #-|
MyFilters = Filters()                                                    #-|
#--------------------------------------------------------------------------| » Importing Decorator
from Functions.Decorators.Aditionals import Instance                     #-|
from Functions.Decorators.DeCode import Partner                          #-|
#--------------------------------------------------------------------------| » Importing Functions
from Functions.Pointing.Charts import Charts_AND_Draw                    #-|
from Functions.Pointing.Convert_Emojies import Emoji                     #-|
#--------------------------------------------------------------------------| Import Error Madule 
from Errors.Error import error , Start_Error                             #-|
#--------------------------------------------------------------------------| » Variabels
Join_Time={}                                                             #-|
Hash={}                                                                  #-|
Links={}                                                                 #-|
Next_game={}                                                             #-|
#--------------------------------------------------------------------------| » Handlers Start 
@bot.on_message(~filters.edited &MyFilters.Dark & filters.private )
@Partner
async def Dark_Helper_Messages( chat_id , text , kind ):
    if text=='Deltags':
        x=0
        async for i in bot.iter_history(chat_id , 400):
            if i.mentioned :
                try:
                    await i.delete()
                    x+=1
                except:pass
            code=IO(texts.tag_deleted(x),chat_id,'copy')
            await bot.send_message(bot_username,str(code))
    
#-----------------------------------------------------------------------------------------------------|
# 0101010101010101010101010101010101010101010101010________1010101010101010101010101010101010101010101|
# man az sarkoob arezohaye khodam sako sakhtam :) |YASTUNES|                                          | 
# 1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010|
#-----------------------------------------------------------------------------------------------------|
@bot.on_message(~filters.edited &(filters.regex(r'روستاییا تونستن همه دشمناشونو شکست بدن')|filters.regex(r'روستاییا بازی رو بردن')|filters.regex(r'طولانی حالا آرامش خاصی در روستا')|filters.regex(r'روستاییای فراموشکار بازی رو بردن')) & filters.group & MyFilters.WWBOTS & MyFilters.Filter_Feature('bet') )
@Instance
async def Game_Winner_Vilager(message,group:Group,user:User):
    group.Delete_Shekar()
    if group.Bet :
        code=IO('0',group.chat_id,'Winner')
        await bot.send_message(bot_username,str(code))

@bot.on_message(~filters.edited & (filters.regex(r'اعضای فرقه توی روستا باقی موندن')|filters.regex(r'روستا پر شده از افراد فرقه گرا')) & filters.group & MyFilters.WWBOTS)
@Instance
async def Game_Winner_Sect(message,group:Group,user:User):
    group.Delete_Shekar()
    if group.Bet :
        code=IO('1',group.chat_id,'Winner')
        await bot.send_message(bot_username,str(code))
        
@bot.on_message(~filters.edited &(filters.regex(r'تیم گرگها برنده بازی شد')|filters.regex(r'گرگا بردن')|filters.regex(r'گرگها برنده شدن')|filters.regex(r'تک گرگ برنده‌ی بازی')|filters.regex(r'تک گرگه فراموشکار برنده‌ی بازی شد')|filters.regex(r'گرگهای فراموشکار برنده شدن'))& filters.group & MyFilters.WWBOTS & MyFilters.Filter_Feature('bet') )
@Instance
async def Game_Winner_Wolf(message,group:Group,user:User):
    group.Delete_Shekar()
    if group.Bet :
        code=IO('2',group.chat_id,'Winner')
        await bot.send_message(bot_username,str(code))
        
@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'تنها کسی که توی روستا زنده مونده کسی نیست')|filters.regex(r'ایندفعه دشمنشون برنده شد')|filters.regex(r'قاتل زنجیره ای روانی زنده موند')|filters.regex(r'دشمنایی که به تنهایی کار میکردن حال'))& filters.group & MyFilters.WWBOTS & MyFilters.Filter_Feature('bet'))
@Instance
async def Game_Winner_Murder(message,group:Group,user:User):
    group.Delete_Shekar()
    if group.Bet :
        code=IO('3',group.chat_id,'Winner')
        await bot.send_message(bot_username,str(code))
        
@bot.on_message(~filters.edited &(filters.regex(r'فقط تیم ومپایر ها 🧛🏻‍♀️ باقی موند')|filters.regex('در آخر عاشقها به هم رسیدن و برنده بازی شدن')|filters.regex('عاشقا برنده شدن')) &  MyFilters.WWBOTS & MyFilters.Filter_Feature('bet') )
@Instance
async def Game_Winner_Special(message,group:Group,user:User):
    group.Delete_Shekar()
    if group.Bet :
        code=IO('4',group.chat_id,'Winner')
        await bot.send_message(bot_username,str(code))

@bot.on_message(~filters.edited &(filters.regex(r'آتش🔥 و ملکه❄️ باقی مو')|filters.regex(r'ویران شدنِ روستاست و برنده کسی نیست جز بمب‌گذار')|filters.regex(r'آتش زن باقی موند که بر روی'))& filters.group & MyFilters.WWBOTS  & MyFilters.Filter_Feature('bet'))
@Instance
async def Game_Winner_FireMan(message,group:Group,user:User):
    if group.Bet :
        code=IO('5',group.chat_id,'Winner')
        await bot.send_message(bot_username,str(code))

@bot.on_message(~filters.edited &(filters.regex(r'بابا‌ شما منافق رو اعدام کردین و اون')|filters.regex('منافق رو کشتین')| filters.regex(r'یه منافقِ فراموشکار برنده‌ی'))& filters.group & MyFilters.WWBOTS & MyFilters.Filter_Feature('bet'))
@Instance
async def Game_Winner_Monafegh(message,group:Group,user:User):
    if group.Bet :
        code=IO('6',group.chat_id,'Winner')
        await bot.send_message(bot_username,str(code))
#-----------------------------------------------------------------------------------------------
@bot.on_message((filters.regex(r'بُرد')|filters.regex(r'برنده') ) & MyFilters.WWBOTS )
@Instance
async def Game_Result_Analyz(message,group:Group,user:User):
    Teams={}
    Team_Text=''
    text=''
    try:
        User_List=[int(i.user.id) for i in message.entities if i.user]
        Result_List=[Charts_AND_Draw.Get_User_Role(str(item).split(':')[-1]) for item in str(message.text).split("\n")[1:-1] if 'زنده' or 'مرده' or 'فرار' in item]
        Result=dict(zip(User_List, Result_List))
        Winners_Count=len([i for i in Result if bool(Result[i]['win'])])
        Alives_Count=len([i for i in Result if bool(Result[i]['alive'])])
        Players_Count=len(User_List)
        for i in Result:
            try:
                # {'win':win,'point':point,'alive':alive,'naghsh':naghsh,'team':team,'win_emoji':win_txt,'alive_emoji':alive_txt}
                Winner=User(i)
                Point_Result= int(Result[i]['point']) * (Players_Count / (Winners_Count * Alives_Count ))
                Winner.Add_Points(Point_Result)
                text+=f'{Emoji.rand_moon()}|{Result[i]["win_emoji"]}|{Result[i]["alive_emoji"]}➛{(await Winner.mention(bot))}➛({int(Result[i]["point"])}{Result[i]["naghsh"]})💸<code>{Point_Result:.2f}</code>\n'
                if Result[i]['team'] in Teams:
                    Teams[(Result[i]['team'])]+=int(Result[i]['point'])
                else:
                    Teams[(Result[i]['team'])]=int(Result[i]['point'])
            except:pass
        for team in Teams:
            Team_Text+=f'{team} ⇢ {Teams[team]}\n'
        #--------------------------------------------------
        code=IO( texts.Game_Analised( text , Team_Text) , group.chat_id,'copy' )
        await bot.send_message(bot_username,str(code))
    except Exception as e:error(f'{e} Dark_Partner (Game_Result_Analyz)')
    if group.Auto_Start:
        await asyncio.sleep(7)
        await bot.send_message( group.chat_id , group.Start_Command )
    
#-----------------------------------------------------------------------------------------------
@bot.on_message(~filters.edited &(filters.regex(r'^رای‌گیری تمام شد و بر حسب آرا')| filters.regex(r'گرگ‌ها🐺بازهم دیشب به روستا حمله کردن')| filters.regex(r'صدای 💥شلیک تفنگ باعث میشه همه روستاییا جمع بشن که ببینن چی شده')| filters.regex(r'حاکم👑 با کلی شک و تردید رای خدشو صادر کرد')| filters.regex(r'^اهالی روستا با کلی شک و تردید رای خودشونو دادن')| filters.regex(r'صبح روز بعد اعضای روستا بدن تیکه تیکه شده')| filters.regex(r'دیشب گرگا زدن پیشگو رو کشتن')| filters.regex(r'چیزی نبود جز')| filters.regex(r'خودشو انداخت روی جنازش و انقدر')| filters.regex(r'صبح روز بعد، همه از خونه‌هاشون بیرون میان و متوجه قطرات خون')| filters.regex(r'با شنیدن صدای تیر، روستاییا دور تفنگدار')| filters.regex(r'آخه این روستایی ساده بدبخت')| filters.regex(r'صبح روز بعد اعضای روستا بدن تیکه تیکه شده')| filters.regex(r'همینکه همه از خونه‌هاشون بیرون میان، قطعه ای از یک تفنگ')| filters.regex(r'دیشب ناتاشا یعنی')| filters.regex(r'با خودش فکر میکرد که شب آرامی رو سپری میکنه')| filters.regex(r'همونجا متوجه شد که اون یکی از اعضای فرقه')| filters.regex(r'یکی از اهالی خبر میده که خونه‌ی')| filters.regex(r'بنظر میرسه دیشب یه شهاب سنگ یا چیزی مثل این به خونه‌ی')| filters.regex(r'صبح میشه و  اهالی روستا، جنازه‌ای رو پیدا میکنن که به راحتی نمیشه تشخیص')| filters.regex(r'چه اتفاقی افتاده که همه به وحشت افتادن')| filters.regex(r'رای‌گیری تموم شد و بر حسب آراء')) & filters.group &  MyFilters.WWBOTS  ,group=-10)
@Instance
async def User_Dead_Func(message,group:Group,user:User):
    for ent in message.entities:
        try:
            x=int(ent.user.id)
        except:
            pass
    if group.Dead_NextGame :
        await bot.send_message(bot_username,str(IO(f'{x}',group.chat_id,'Dead')))

@bot.on_message(~filters.edited &(filters.regex(r'متوالی رای نداده')| filters.regex(r'دو روز متوالی رای نداده')|filters.regex(r'دو روز متوالی رای نداده'))& filters.group &  MyFilters.WWBOTS  ,group=-10)
@Instance
async def USER_AFK_FUNC(message,group:Group,user:User):
    group.Add_Game_AFk(Hash[int(group.chat_id)])
    for ent in message.entities:
        try:
            x=int(ent.user.id)
        except:
            pass
    usr=User(x)
    try:men=(await bot.get_users(usr.user_id)).mention
    except:men=int(user)
    try:
        admin=Admin(usr.user_id,group.Main)
        if admin.is_admin:
            admin.Add_Point(afk=1)
            code=IO(texts.Admin_Afked(men),group.chat_id,'admin_alarm')
            await bot.send_message(bot_username,str(code))
    except:pass
    usr.AFK(group)
    user.Add_Coins(-100)
    user.Add_Points(-200)
    code=IO(texts.Get_AFK(men),group.chat_id,'alarm')
    await bot.send_message(bot_username,str(code))
    if group.Afk_Warn:        
        if usr.AFk_Cheak_Count(group):
            code=IO(texts.GET_WARNED(men),group.chat_id,'alarm')
            await bot.send_message(bot_username,str(code))
            usr.Add_Warn(group.chat_id)
            usr.set_Warn_0(group.chat_id)
        if usr.Show_Warn >= group.Warn :
            await bot.kick_chat_member(group.chat_id,int(usr))
            code=IO(texts.Kicked_For_WARN(men,usr.user_id),group.chat_id,'sup')
            await bot.send_message(bot_username,str(code))

@bot.on_message(~filters.edited & (filters.regex(r'برای ورود به روستا بر روی دکمه زیر کلیک کنید')   | filters.regex(r'» /modeinfo')| filters.regex(r'روی دکمه وارد شوید کلیک کنید')|filters.regex(r'نکنید که روی کادر زیر کلیک کنید')|filters.regex(r'جوین شید و حالشو ببرید'))& filters.group & MyFilters.WWBOTS)
@Instance
async def PLAYING_STOPPED_FUNC(message,group:Group,user:User):
    Next_game[group.chat_id]=True
    group.Delete_Players() 
    if group.JoinTime_Alarm:
        code=IO(str(await message.click(0)),group.chat_id , kind='JoinTime_Alarm')
        await bot.send_message(bot_username,str(code))
    group.Join_time_Started
    Join_Time[int(group.chat_id)]=[int(time.time())]
    await bot.send_message(bot_username,str(IO('Started',group.chat_id)))
    
@bot.on_message(~filters.edited &(filters.regex(r'بازی شروع شد') |filters.regex(r'بازی شروع شد') | filters.regex(r'تعداد بازیکنا به پنج') |filters.regex(r'تعداد بازیکنا کافی نیست') | filters.regex(r'چقدر کمین'))  & filters.group & MyFilters.WWBOTS,group=-10)
@Instance
async def PLAYING_STARTED_FUNC(message,group:Group,user:User):
    Join_Time[int(group.chat_id)].append(int(time.time()))
    group.Join_time_Finished
    sup_list=[]
    main_list=[]
    try:
        if group.Auto_DeleteTag:
            async for i in bot.iter_history(group.chat_id , 400):
                if i.mentioned :
                    main_list.append(int(i.message_id))
                    if len(main_list) > 80 :
                        await bot.delete_messages(group.chat_id , main_list)
                    # try:
                    #     await i.delete()
                    # except:pass
            await bot.delete_messages(group.chat_id , main_list)
    except Exception as e:print(e)
    try:
        if group.Auto_DeleteTag_Sup:
            async for i in bot.iter_history(group.Support , 400):
                if i.mentioned :
                    sup_list.append(int(i.message_id))
                    if len(sup_list) > 80 :
                        await bot.delete_messages(group.chat_id , sup_list)
                    # try:
                    #     await i.delete()
                    # except:pass
            await bot.delete_messages(group.chat_id , sup_list)
    except Exception as e:print(e)

@bot.on_message( ~filters.edited & MyFilters.WWBOTS )
@Instance
async def ALL_MSG_WW_BOTS_FUNC(message,group:Group,user:User):
    if not group:
        await message.chat.leave()
    if 'بازیکن های زنده:' in str(message.text) or 'بازیکنان زنده :' in str(message.text):
        if group.List_Pin :
            try:await message.pin()
            except:pass
        count = re.findall('(\d+)', message.text)
        if group.Auto_nextGame:
            if 0.4<((int(count[0]) / int(count[1]) ))<0.55 and Next_game[group.chat_id]==True:
                Next_game[group.chat_id]=False
                await bot.send_message(bot_username,str(IO('@amiralirj_pv :(',group.chat_id,'Next_Game')))
        if count[0] == count[1]:
            Hash[int(group.chat_id)]=int(random.randint(1,99999999999999))
            try:jointime = str(datetime.timedelta(seconds=abs(Join_Time[group.chat_id][1] - Join_Time[group.chat_id][0] )))
            except:jointime = str(datetime.timedelta(seconds=abs(Join_Time[group.chat_id][0] - int(time.time()))))
            #hash,Join_Time,players
            group.Game_Started(Hash[int(group.chat_id)],jointime,count[1])
            Players=[]
            for ent in message.entities:
                try:
                    Players.append(int(ent.user.id))
                    a=Admin(int(ent.user.id),group.Main)
                    if a.is_admin:
                        a.Add_Point(join=1)
                except:pass
            if len(Players)>4:
                print('Game Added')
                await group.Add_Players(Players,bot)
            await bot.send_message(bot_username,str(IO('Finished',group.chat_id)))
        else:
            plyrs_list=group.Show_Deads_Name 
            for i in str(message.text).split('\n')[1:]:
                if 'مرده' in i :
                    for iter in plyrs_list:
                        if str(iter[0]).strip() in i :
                            try:User(int(iter[1])).Dead(group.chat_id,(i.split(':')[-1].replace(texts.dead,'').replace('-','')))
                            except:pass
            
@bot.on_message(~filters.edited &MyFilters.admin)
@Instance
async def ALL_MSG_WW_BOTS_FUNC(message,group:Group,user:User):
    if message.mentioned:
        Admin(user.user_id,group.Main).Add_Point(tag=1)

#                                                             | Edalat Mord :) Hesadat Bord |
if __name__=='__main__':
    print('\n I Will Try To Connect : \n ')
    bot.run()
    print('\n): I am Stopped :(\n')

# 🕸 Good Luck 🕸 