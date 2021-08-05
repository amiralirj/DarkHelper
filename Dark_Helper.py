#--------------------------------------------------------------------------| » Variables
from Config.Texts.Question.questions import Question_Dict                 #|
#--------------------------------------------------------------------------| » Importing Pyrogram Client
from pyrogram import filters                                              #|
from Config.Info.bot.api_bot import bot                                   #|
#--------------------------------------------------------------------------| » Starting Database Tabales Creation
from Databases import MainBase                                           #-|
MainBase.start()                                                         #-|
#--------------------------------------------------------------------------| » Import Classes & asyncio|datetime & os.remove() & Hash Getter & Taggers
import asyncio , datetime                                                #-|
from random import choice                                                #-|
from os import remove                                                    #-|
from Classes.Admin import Admin                                          #-|
from Classes.Statics import Statics                                      #-|
from Classes.Message import Message                                      #-|
from Classes.Group import Group                                          #-|
from Classes.User import User                                            #-|
from Classes.IO import IO                                                #-|
from Classes.Robot import Robot                                          #-|
from Functions.Filters.Hash import Get_hash                              #-|
from Functions.Tag.tag import Tag , Support_tag                          #-|
#--------------------------------------------------------------------------| Import Error Madule & Start Error Reg
from Errors.Error import error , Start_Error                             #-|
Start_Error()                                                            #-|
#--------------------------------------------------------------------------| » Import Config ( Buttons & Texts , Info )
from Config.Buttons import Inline_Buttons , Keyboard_Buttons             #-|
from Config.Texts import Persian as texts # or English                   #-|
from Config.Info.Supports import Channel , next_channel,Songs,Song_Channel#|
#--------------------------------------------------------------------------| » Instantiating From Filters Class
from Classes.Filters import Filters                                      #-|
MyFilters = Filters()                                                    #-|
#--------------------------------------------------------------------------| » This will run every 10 Second , Day , Month
from Functions.Treads import Priodically                                 #-|
from threading import Thread                                             #-|
thread = Thread(target = Priodically.Every_Day ,args=[])                 #-|
thread.start()                                                           #-|
thread1 = Thread(target = Priodically.Every_10_sec,args=[])              #-|
thread1.start()                                                          #-|
thread2 = Thread(target = Priodically.Every_Hour,args=[])                #-|
thread2.start()                                                          #-|
#--------------------------------------------------------------------------| » Importing Decorator
from Functions.Decorators.Aditionals import Instance                     #-|
from Functions.Decorators.DeCode import Partner                          #-|
#--------------------------------------------------------------------------| » Importing Functions
from Functions.Filters import New_members                                #-|
from Functions.Pointing.Charts import Charts_AND_Draw                    #-|
#--------------------------------------------------------------------------| » Get Bot Username as "bot_username" Variable
with bot:                                                                #-|
    bot_username = ("@" +str( ( bot.get_me()).username) )                #-|
#--------------------------------------------------------------------------| » Handlers Started » » »
@bot.on_message(~filters.edited &~filters.me & filters.command(['start',f'start{bot_username}']) & filters.private ,group=-3)
@Instance
async def Start_RoBot(message,group,user):
    await message.reply_text(texts.Start_Text(message.from_user.mention) , reply_markup=Inline_Buttons.Dark_Channel)

@bot.on_message(~filters.edited &~filters.me & filters.command(['add',f'add{bot_username}'])  & MyFilters.Owner ,group=-10)
async def Add_Group_Func( _ , message ):
    rob=Robot()
    try:date=int(message.command[3])
    except:date=30
    try:chts=int(message.command[2])
    except:chts=int(message.chat.id)
    x=rob.Add_Gap(int(chts) , int(message.command[1]) , date)
    if x:
        await message.reply_text(f'Okey Sear This Group Added to Database for {date}')
    #➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited &~filters.me &  (filters.regex('^اهنگ بفرست')|filters.regex('^send song')),group=-3)
async def Song_Func(_,message):
    await bot.copy_message( int(message.chat.id) , Song_Channel , choice(Songs))
#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited & MyFilters.partner ,group=-10)
@Partner
async def Partner_Callback_Function( chat_id , text , kind ):
    gp=Group(chat_id)
    if kind=='copy':
        await bot.send_message(chat_id,text,parse_mode='html')
        return

    elif kind=='sup':
        if gp.Alarm:
            await bot.send_message(gp.Support,text,parse_mode='html')
            return

    elif kind=='alarm':
        if gp.Alarm:
            await bot.send_message(chat_id,text,parse_mode='html')
            return

    elif kind=='admin_alarm':
        if gp.Admin_Alarm:
            await bot.send_message(gp.Support,text)
            return

    elif kind=='Winner':
        Results=gp.END_Bet(int(text))
        text=texts.bet_Title
        for i in Results[0]:
            # user_id,amount,zarib
            try:
                text+=texts.bet_Winner((await User(int(i[0])).mention(bot)),int(i[1]))
                user=User(int(i[0]))
                user.Add_Coins(          (int(float(i[2]) * float(i[1])) - int(i[1]))            )
                try:await bot.send_message( int(user) , texts.Winner_private(
                    (int(float(i[2]) * float(i[1])) - int(i[1]))    ,   (int(i[1]))
                ))
                except:pass
            except Exception as e:error(e)
        for i in Results[1]:
            # user_id,amount,zarib
            try:
                text+=texts.bet_Loser((await User(int(i[0])).mention(bot)),int(i[1]))
                user=User(int(i[0]))
                user.Add_Coins(        (  (int(float(i[2]) * float(i[1])) - int(i[1])) * -1  )          )
                try:await bot.send_message( int(user) , texts.Loser_private(
                    (  (int(float(i[2]) * float(i[1])) - int(i[1])) * -1  ) ,   (int(i[1]))
                ))
                except:pass
            except Exception as e:error(e)
        await bot.send_message( chat_id , text)

    elif kind=='JoinTime_Alarm':
        await bot.send_message(gp.Support ,texts.join_time_Started, reply_markup=Inline_Buttons.Button_JoinTime_Link_Maker(text))

    elif kind=='Next_Game':
        await bot.copy_message( chat_id , next_channel , gp.Next_Message_Id )
        return
    admin=Admin(100000,100000)
    try:
        if text=='Started' and gp.Auto_Tag_Support:await Support_tag(bot , gp)
    except:pass
    try:
        if text=='Started' and gp.Auto_Tag:
            await Tag(gp,bot)
    except Exception as e:print(f'{e} TAG ')
    if text=='Finished' and gp.JoinTime_Alarm :
        for i in gp.Show_Players :
            for cht in admin.show_gap(int(i[0])):
                try:
                    Alarmed_G=Group(int(cht[0]))
                    if Alarmed_G.Admin_Alarm :
                        if int(cht[0])!=int(gp.Main):
                            try:
                                tt=(await bot.get_chat(int(gp.Main))).title
                            except:
                                tt=cht[0]
                            try:men=(await bot.get_users(int(i))).mention
                            except:men=int(i)

                            await bot.send_message(Alarmed_G.Support , texts.Admin_Joined_Other_Group_Game(tt ,men ))
                except:pass
        mch=gp.Last_Match
        await bot.send_message(gp.Support ,texts.join_time_Filnished(mch[0], str(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')) , mch[1]))
    if kind=='Dead':
        try:
            men=(await bot.get_users(int(text))).mention
            await bot.send_message(gp.Main,texts.Next_Dead( gp.Show_Next_Game_Text ,men ))
        except Exception as e:error(e)

@bot.on_message(~filters.edited &~filters.me & MyFilters.admin & filters.command(['stop',f'stop{bot_username}']) & filters.group ,group=-3)
@Instance
async def Stop_Tag_Func(message,group:Group,user:User):
    if group.Is_Tagging :
        await message.reply_text(texts.tag_stopped)
        group.Tag_Stopped()
    else:
        await message.reply_text(texts.tag_is_Also_Stopped)

#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited &~filters.me & ( filters.regex('^پنل$') | filters.regex('(?i)^pannel$') | filters.regex('^تنظیمات$') ) & (MyFilters.admin|MyFilters.Owner)  &  filters.group  ,group=-100)
@Instance
async def Pannel_Call(message,group,user):
    await message.reply_text(texts.pannel, reply_markup=Inline_Buttons.Main_Pannel(group))

@bot.on_message(~filters.edited &~filters.me & ( filters.regex('^امار$') | filters.regex('(?i)^statics$') | filters.regex('^بازی ها$') ) & (MyFilters.admin|MyFilters.Owner)  &  filters.group  ,group=-100)
@Instance
async def Statics_Pannel_Call(message,group,user):
    await message.reply_text(texts.statics_pannel, reply_markup=Inline_Buttons.Statics_Inline)
#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited &(filters.command(['set',f'set{bot_username}'])) & MyFilters.Owner &  filters.group  ,group=-100)
@Instance      #only "Promation" XD
async def Owner_Promation_Func(message,group:Group,user:User):
    Admin(int(message.reply_to_message.from_user.id),group.Main).Set_Nazer()
    await message.reply_text(texts.Owner_Setted(f'<code>{Get_hash()}</code>'),parse_mode='html')

@bot.on_message(~filters.edited &~filters.me & MyFilters.nazer & (filters.command(['promote',f'promote{bot_username}'])|filters.regex('^ارتقا$')) &  filters.group  ,group=-3)
@Instance
async def Promote_Users_Func(message,group:Group,user:User):
    if message.reply_to_message:
        admin = Admin(int(message.reply_to_message.from_user.id) , group.Main )
        admin.Set_Admin()
        await message.reply_text(texts.admin_setted(message.reply_to_message.from_user.mention))
    else:await message.reply_text(texts.reply)

@bot.on_message(~filters.edited &~filters.me & MyFilters.nazer & (filters.command(['demote',f'demote{bot_username}'])|filters.regex('^عزل$')) &  filters.group  ,group=-3)
@Instance
async def Demote_Users_Func(message,group:Group,user:User):
    if message.reply_to_message:
        admin = Admin(int(message.reply_to_message.from_user.id) , group.Main )
        admin.Delete_Admin()
        await message.reply_text(texts.admin_deleted(message.reply_to_message.from_user.mention))
    else:await message.reply_text(texts.reply)

@bot.on_message(~filters.edited &~filters.me & MyFilters.admin & (filters.command(['adminlist',f'adminlist{bot_username}'])|filters.regex('^ادمین ها$')) &  filters.group  ,group=-3)
@Instance
async def All_Group_Admins(message,group:Group,user:User):
    admins=group.Admins
    owner=group.Show_Owner
    try:
        owner=(await bot.get_users(owner)).mention
    except:pass
    text=f'سازنده گروه \n ⇢{owner}\n▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️\n'
    for i in admins[0]:
        try:
            usr=await bot.get_users(i)
            text+=f'⍣ {usr.mention} ➟ <code> {usr.id} </code> \n'
        except:
            text+=f'⍣ ******* ➟ <code> {i} </code> \n'
    text+=f'▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️\nadmins Number : {admins[1]}'
    await message.reply_text(text, parse_mode='html')

@bot.on_message(~filters.edited &~filters.me & MyFilters.nazer & (filters.command(['AdminConfig',f'AdminConfig{bot_username}'])|filters.regex('^پیکربندی$')) &  filters.group  ,group=-3)
@Instance
async def Config_All_Admins(message,group:Group,user:User):
    x=0
    y=0
    async for usr in bot.iter_chat_members( group.Main  , filter='administrators'):
        try:
            Admin(int(usr.user.id)).Set_Admin()
            x+=1
        except:y+=1
    await message.reply_text(texts.Admin_Config(x,y,f'<code>{Get_hash()}</code>'),parse_mode='html')

@bot.on_message(~filters.edited &~filters.me & MyFilters.nazer & (filters.command(['SetFrame',f'SetFrame{bot_username}'])|filters.regex('^تنظیم قالب$')) &  filters.group  ,group=-3)
@Instance
async def Set_Group_Profile_Frame(message,group:Group,user:User):
    if message.reply_to_message:
        # Points->{point}
        # Coin->{coin}
        # Title->{title}
        # Diamond->{diamond}
        # Ghost->{ghost}s
        # Anti Ghost->{antighost}
        # Ghost Killer->{ghostkiller}
        # Warns->{Warn}
        # Laghab->{laghab}
        # Birth->{birth}
        # Correct Bets->{bets}
        # Pointing -> {Pointing}
        #...
        text=str(message.reply_to_message.text)
        if '{name}' in text and '{point}' in text and '{coin}'in text  and '{title}'in text  and '{bitcoin}' in text and '{laghab}' in text and '{birth}' in text and '{last_dolar_rank}' in text and '{last_litecoin_rank}' in text :group.Set_Ghaleb(str(message.reply_to_message.text))
        else:await message.reply_text(texts.frame_help,parse_mode='html' )
    else:await message.reply_text(texts.reply)

@bot.on_message(~filters.edited &~filters.me & MyFilters.nazer & (filters.command(['Setwel',f'Setwel{bot_username}'])|filters.regex('^تنظیم خوشامد$')) &  filters.group  ,group=-3)
@Instance
async def Set_Group_Welcome_Frame(message,group:Group,user:User):
    if message.reply_to_message:
        text=str(message.reply_to_message.text)
        # {name}
        # {title}
        # {werewolf}
        # {onyx}
        # {black}
        if '{name}' in text :
            group.Set_Welcome(text)
        else:await message.reply_text(texts.welcome_help,parse_mode='html' )
    else:await message.reply_text(texts.reply)

@bot.on_message(~filters.edited &~filters.me & MyFilters.nazer & (filters.command(['setchannel',f'setchannel{bot_username}'])) &  filters.group  ,group=-3)
@Instance
async def Set_Group_Channel(message,group:Group,user:User):
    try:message.command[1]
    except:
        await message.reply_text(texts.command)
        return
    if 'https://t.me/' in str(message.text).lower() and 'joinchat' not in str(message.text).lower() :
        group.Set_Channel(str(message.command[1]))
        await message.reply_text(texts.channel_setted)
    else:await message.reply_text(texts.how_to_reg_channel)


#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited &~filters.me & filters.regex('^پروفایل$') &  filters.group  ,group=-3)
@Instance
async def Set_Group_Profile_Ghaleb(message,group:Group,user:User):
    try:title=(await bot.get_chat(user.Group)).title
    except:title=user.Group
    await message.reply_text(user.ProFile(group , message.from_user.mention ,title ))
#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited &~filters.me  & (filters.command(['shutup',f'shutup{bot_username}'])|filters.regex('^خفه$')|filters.regex('^گودرت$')) &  filters.group & MyFilters.Filter_Feature('fun_mute')  ,group=-3)
@Instance
async def Mute_Fun_User(message,group:Group,user:User):
    if message.reply_to_message :
        if not user.user_id == int(message.reply_to_message.from_user.id):
            if not message.reply_to_message.from_user.is_self :
                if not message.reply_to_message.from_user.is_bot :
                    if not user.is_Muted(group.chat_id) :
                        if user.Coin > 301 :
                            Muted_user=User(int(message.reply_to_message.from_user.id))
                            if not Muted_user.is_Muted(group.chat_id):
                                if not Muted_user.is_Suspended_Mute(group.chat_id):
                                    Muted_user.Mute(group.chat_id)
                                    user.Add_Coins(-300)
                                    await message.reply_text(texts.Muted_Fun(message.from_user.mention , message.reply_to_message.from_user.mention),Inline_Buttons.Made_Inline(texts.taskhir_bt(message.from_user.first_name),f'taskhir {user.user_id} {Muted_user.user_id}'))
                                else:await message.reply_text(texts.Suspended_Mute)
                            else:await bot.copy_message(group.chat_id , Channel , texts.message_id_devil_sticker ,reply_to_message_id=message.message_id )
                        else:await message.reply_text(texts.not_Enough_Coin(user.Coin))
                    else:await message.reply_text(texts.do_not_Talk)
                else:await message.reply_text(texts.Bote_Muting)
            else:await bot.copy_message(group.chat_id , Channel , texts.message_id_sticker ,reply_to_message_id=message.message_id )
        else:await message.reply_text(texts.self_mute)
    else:pass

@bot.on_message(~filters.edited &~filters.me  & (filters.command(['s',f'save']))  & MyFilters.Filter_Feature('sooti') & filters.group  ,group=-3)
async def Sooti_Saver_Func(_,message):
    await message.reply_to_message.forward(Channel)
    await message.reply_text(texts.Sooti_Saved(Channel))

@bot.on_message( filters.command(['nextgame', 'nextgame@OnyxWereBetaBot' , 'nextgame@Blackwwrobot', 'nextgame@werewolfbot',f'nextgame@{bot_username}']) & filters.group , group=-10)
@Instance
async def Next_Game_Resbons_Func(message,group:Group,user:User):
    if group.NextGame_Response :
        if user.Next_frame:
            await message.reply_text(user.Next_frame,reply_markup=Inline_Buttons.Made_Inline(str(message.from_user.first_name) , 'None'))
        else:
            await message.reply_text(choice(texts.next_List(message.from_user.mention)),reply_markup=Inline_Buttons.Made_Inline(str(message.from_user.first_name) , 'None'))

@bot.on_message( filters.command(['setnext',f'setnext{bot_username}']) & filters.group , group=-3)
@Instance
async def Set_NextGame_Frame_Func(message,group:Group,user:User):
    Per=True
    for i in message.entities:
        if str(i.type) in ['url','text_link']:
            Per=False
    if len(message.command) <=1 :
        Per=False
    if Per:
        user.Set_Next_frame( (str((message.text))[9:]) )
        await message.reply_text(texts.next_setted)
    else:await message.reply_text(texts.how_to_set_next_frame)

#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message( filters.command(['ray',f'ray{bot_username}']) & MyFilters.shekar & filters.group , group=-3)
@Instance
async def Spam_Election_Func(message,group:Group,user:User):
    Players=[i for i in group.Show_Players if bool(i[1])]
    await message.reply_text(texts.Who,reply_markup=Inline_Buttons.Election_Inline( Players , group))

@bot.on_message(~filters.edited &~filters.me & (filters.regex('^#شکار$') | filters.regex('^#شکارم$') | filters.regex('^#ch$') | filters.regex('^#شکارچی$') ) &  filters.group  ,group=-3)
@Instance
async def Shekar_Detection_Func(message,group:Group,user:User):
    user.Add_Message(group)
    user.Add_Message(group)
    user.Add_Message(group)
    user.Add_Message(group)
    permission=False
    #-----------------------------------------
    if group.Anti_Spam:
        if user.is_Player(group.chat_id):
            permission=True
        else:
            await message.delete()
            await bot.kick_chat_member(user_id= user.user_id , chat_id=group.chat_id )
    else:
        permission=True
    #-----------------------------------------
    if permission :
        user.Set_Shekar(group)
        await message.reply_text(texts.shekar(message.from_user.mention))
        if group.Shekar_Pin :
            try:await message.pin()
            except:pass
        st=await user.State
        if st[0]>20 or  st[1]>20 or st[2]>20 :
            pass
        else:
            await bot.send_message(int(group) , texts.shekar_less_State(message , st))

@bot.on_message(~filters.edited &~filters.me  & (filters.regex('^#ناظر$') | filters.regex('^#شاهد$') | filters.regex('^#مکمل_شکار$') ) &  filters.group  ,group=-3)
@Instance
async def Nazer_Detection_Func(message,group:Group,user:User):
    user.Add_Message(group)
    user.Add_Message(group)
    user.Add_Message(group)
    user.Add_Message(group)
    permission=False
    if group.Anti_Spam:
        if user.is_Player(group.chat_id):
            permission=True
        else:await message.delete()
    else:
        permission=True
    #-----------------------------------------
    if permission :
        if group.Nazer_pin :
            try:await message.pin()
            except:pass
        await bot.send_message(int(str(group)) , texts.nazer)
#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited &~filters.me & filters.command(['bet',f'bet{bot_username}']) &  filters.group  ,group=-3)
@Instance
async def Bet_regestry_Func(message,group:Group,user:User):
    try:
        amount=int(message.command[1])
    except:
        amount=None
        await message.reply_text(texts.how_to_bet_correct)
    if amount:
        if int(amount) < int(user.Coin):
            if amount > 0 :
                await message.reply_text(texts.bet , reply_markup=Inline_Buttons.Bet_Inline(group , user.user_id,amount),parse_mode='html')
        else:
            print(f'{amount}{user.Coin}')
            await message.reply_text(texts.not_Enough_Coin(user.Coin))

@bot.on_message(~filters.edited &~filters.me & filters.command(['zarib',f'zarib{bot_username}']) &  filters.group  ,group=-3)
@Instance
async def Zarib_Info_Func(message,group:Group,user:User):
    text='➖➖➖➖➖➖➖➖➖➖➖➖➖'
    zarib=group.Team_Zarib
    TM=group.Group_Teams
    for i in TM:
        text+=f'➕ {TM[i]} → : {zarib[i]} \n'
    text+='➖➖➖➖➖➖➖➖➖➖➖➖➖'
    await message.reply_text(text)
#➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@bot.on_message(~filters.edited &~filters.me & filters.command(['setlaghab',f'setlaghab{bot_username}']) &  filters.group  ,group=-3)
@Instance
async def Set_Laghab_Func(message,group:Group,user:User):
    try:str(message.text)[11:]
    except:
        await message.reply_text(texts.command)
        return
    x=Message(message).is_NFSW()
    if not x :
        user.Set_Laghab(str(message.text)[11:])
        await message.reply_text(texts.laghab_setted)
    else:
        await message.reply_text(texts.have_NFSW)

@bot.on_message(~filters.edited &~filters.me & filters.command(['setbirth',f'setbirth{bot_username}']) &  filters.group  ,group=-3)
@Instance
async def Set_BirthDay_Func(message,group:Group,user:User):
    try:message.command[1]
    except:
        await message.reply_text(texts.command)
        return
    if user.BirthDay == 'none':
        if str(message.command[1]).count('-')==2:
            user.Set_Birth(message.command[1])
            await message.reply_text(texts.birth_reg)
        else:await message.reply_text(texts.birth_help)
    else:await message.reply_text(texts.set_second_birth(user.BirthDay))
#______________________________________________________________________________________________
@bot.on_message(~filters.edited &~filters.me & filters.reply & ( MyFilters.Question ) &  filters.group  ,group=-1)
@Instance
async def Question_Answering_Detection_Function(message,group:Group,user:User):
    question=str(message.reply_to_message.text).split('سوال :')[1].split('«')[0].strip()
    if Question_Dict[question] in str(message.text):
        await message.reply_text(texts.its_Correct)
        group.Question_Answered()
        user.Add_Coins(200)
        user.Add_Points(500)

# @bot.on_message(~filters.edited &~filters.user(int(Supports.Owner)) & (MyFilters.Dark_Helper_Added) &  filters.group  ,group=-3)
# @Instance
# async def Dark_Helper_Added_Func(message,group:Group,user:User):
#     await message.reply_text(texts.Membership)
#     await message.chat.leave()

@bot.on_message(~filters.edited & filters.new_chat_members &  filters.group  ,group=-3)
@Instance
async def New_Chat_members(message,group:Group,user:User):
    Title=message.chat.title
    for Joined_User in message.new_chat_members:
        usr=User(int(Joined_User.id),group.Main)
        kicked=(await New_members.New_Member_State(group , usr))
        if kicked:
            try:
                await bot.kick_chat_member(user_id= usr.user_id , chat_id=group.chat_id )
            except:
                kicked=False
        #------------------------------------------------------------------------
        if not kicked:
            if bool(group.Group_Lock):
                try:
                    await bot.kick_chat_member(user_id= usr.user_id , chat_id=group.chat_id )
                    kicked=True
                except:
                    pass
        #------------------------------------------------------------------------
        if not kicked:
            user_Fullname = Joined_User.first_name + (Joined_User.last_name if Joined_User.last_name else '')
            is_tabchi,is_bot=New_members.Locks(group , usr , user_Fullname , Joined_User.is_bot )
            if is_bot or is_tabchi:
                try:
                    await bot.kick_chat_member(user_id= user.user_id , chat_id=group.chat_id )
                    await bot.kick_chat_member(user_id= usr.user_id , chat_id=group.chat_id )
                    kicked=True
                except:
                    pass
        #------------------------------------------------------------------------
        if not kicked:
            if group.Welcome_Turn :

                if group.Show_Welcome:
                    WLC,reply=await New_members.Welcome(group , usr , Joined_User , Title , Joined_User.mention )
                    try:await message.reply_text(WLC,reply_markup=reply)
                    except:await message.reply_text(WLC)

                else:
                    if group.Show_Channel:
                        reply=Inline_Buttons.Channel_Text(group.Channel_Text , group.Channel )
                    else:
                        reply= None
                    state=list(await usr.State)
                    WLC=(texts.welcome ).replace('{name}',str(Joined_User.mention)).replace('{werewolf}',str(state[2])).replace('{onyx}',str(state[0])).replace('{black}',str(state[1])).replace('{title}',str(message.chat.title))

                try:await message.reply_text(WLC,reply_markup=reply)
                except:await message.reply_text(WLC)

@bot.on_message(~filters.edited & ~filters.me & filters.group ,group=-1 )
@Instance
async def All_Messages_Func(message,group:Group,user:User):
    if not group:
        await message.chat.leave()
        return
    robot=Robot()
    try:
        if group.Is_Time_For_Question:
            await bot.send_message(group.Main , texts.Question_text(robot.Random_Question) )
            group.Question_Sended()
            group.Question_Time_Passes()
    except:pass
    try:
        user.Add_Message(group)
        if group.Anti_Spam:
            if user.is_Spammer(group):
                await bot.kick_chat_member(user_id= user.user_id , chat_id=group.chat_id )
                await bot.send_message(group.Support , texts.banned(user.user_id))
        #--------------------------------------------------------------------------------
    except:pass
    msg=Message(message)
    x=await msg.Auto_Lock(group,user,message)
    if  x:
        await message.delete()
        if x=='NFSW':
            if group.Alarm:
                pm=await bot.copy_message(group.chat_id , Channel , texts.NFSW_sticker ,reply_to_message_id=message.message_id )
                await pm.reply_text(str(message.from_user.mention))
    else:
        if message.media and bool(group.Porn) :
            PATH=(await msg.Lock_Nude(group))
            if PATH:
                try:
                    for i in range(1,int(group.Spam_Count /2) ):
                        user.Add_Message(group)
                except:pass
                user.Add_Warn(message.chat.id)
                if group.Alarm:
                    await message.reply_text(texts.nfsw_alarm(message.from_user.mention))
                await bot.send_photo(group.Support , PATH[0] ,  caption=texts.nfsw_detected(message.from_user.mention,PATH[1] ,PATH[2] ), reply_markup=Inline_Buttons.Made_Inline(texts.ban,f'Ban {message.chat.id} {message.from_user.id}'))
                remove(PATH[0])

#------------------------------------|=(Esalat Mano Khatere Gereft (T|a) Be Eteghadatam Khateme bede)=|-----------------------------------|
#✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪⍟ |-CallBack-| ✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✮✪✮✪✮|
#✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪ |-Queries--| ✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮|

@bot.on_callback_query(filters.regex('^Setting') & MyFilters.admin )
@Instance
async def Main_Pannel_Callbacks(query,group:Group,user:User):
    kind=str(query.data).split(' ')[1]
    if kind == 'Group':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Group_Pannel(group))
    else:
        GP=(await bot.get_chat(int(group.Main)))
        SP=(await bot.get_chat(int(group.Support)))
        await query.edit_message_text( texts.werepannel,reply_markup=Inline_Buttons.Werewolf_Pannel( group ,[GP.title , SP.title]  , GP.invite_link ))

@bot.on_callback_query(filters.regex('^Pannel') & MyFilters.admin )
@Instance
async def Werewolf_Pannel_Callbacks(query,group:Group,user:User):
    kind=str(query.data).split(' ')[1]
    if kind == 'Tag':await query.edit_message_text(texts.new_pannel , reply_markup=Inline_Buttons.Pannel_Tag(group))
    elif kind == 'Notifications':await query.edit_message_text(texts.new_pannel , reply_markup=Inline_Buttons.Pannel_Notifications(group))
    elif kind == 'Pin':await query.edit_message_text(texts.new_pannel , reply_markup=Inline_Buttons.Pannel_Pin(group))
    elif kind == 'Game':await query.edit_message_text(texts.new_pannel , reply_markup=Inline_Buttons.Pannel_Game(group))
    elif kind == 'State':await query.edit_message_text(texts.new_pannel , reply_markup=Inline_Buttons.Pannel_State(group))
    elif kind == 'Fun':await query.edit_message_text(texts.new_pannel , reply_markup=Inline_Buttons.Pannel_Fun(group))
    elif kind == 'Filters':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Filters_pannel(group))
    elif kind == 'Porn':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Porn_Pannel(group))
    elif kind == 'Spam':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Pannel_Spam(group))
    elif kind == 'Warn':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_Warn(group))
    else:pass

@bot.on_callback_query(filters.regex('^Undo') & MyFilters.admin )
@Instance
async def Undo_Callbacks(query,group:Group,user:User):
    kind=str(query.data).split(' ')[1]
    if kind == 'Main':await query.edit_message_text(texts.new_pannel , reply_markup=Inline_Buttons.Main_Pannel(group))
    elif kind=='Were':
        GP=(await bot.get_chat(int(group.Main)))
        SP=(await bot.get_chat(int(group.Support)))
        await query.edit_message_text( texts.werepannel,reply_markup=Inline_Buttons.Werewolf_Pannel( group ,[GP.title , SP.title]  , GP.invite_link ))
    elif kind == 'Group':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Group_Pannel(group))

@bot.on_callback_query(filters.regex('^Turn') & MyFilters.admin )
@Instance
async def Turn_Control_Feature_Callback(query,group:Group,user:User):
    data=str(query.data).split(' ')
    row=str(data[1])
    try:
        Amount=int(data[2])
    except:
        try:Amount=int(group.All_Controls[row])
        except:Amount=int(group.Porn_All_Filters[row])
    kind=str(data[3])
    if kind=='porn':group.Turn_Anti_Porn()
    elif row=='spam_count':group.Set_Spam_Count(Amount)
    else:group.Manual_Control_Change(row,Amount)
    group=Group(group.Main)
    if kind == 'Group':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Group_Pannel(group))
    elif kind == 'Filters':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Filters_pannel(group))
    elif kind == 'Porn':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Porn_Pannel(group))
    elif kind=='Spam':await query.edit_message_text( texts.grouppannel,reply_markup=Inline_Buttons.Pannel_Spam(group))

@bot.on_callback_query(filters.regex('^Change') & MyFilters.admin )
@Instance
async def Change_Feature_Callback(query,group:Group,user:User):
    data=str(query.data).split(' ')
    row=str(data[1])
    try:
        Amount=int(data[2])
    except:
        Amount=int(group.All_Atrebeutes[row])
    kind=str(data[3])
    if row=='state':group.Set_State(Amount)
    elif row=='warn':group.Set_Warn(Amount)
    elif row=='state_lock':group.Change_State_Lock(Amount)
    elif row=='bot_kind':group.Change_Bot_Kind(Amount)
    elif row=='warn':group.Set_Warn(Amount)
    else:group.Manual_Change(row,Amount)
    group=Group(group.Main)
    if kind=='werewolf':
        try:
            GP=(await bot.get_chat(int(group.Main)))
            SP=(await bot.get_chat(int(group.Support)))
            await query.edit_message_text( texts.werepannel,reply_markup=Inline_Buttons.Werewolf_Pannel( group ,[GP.title , SP.title]  , GP.invite_link ))
        except:
            try:await query.edit_message_text( texts.werepannel,reply_markup=Inline_Buttons.Werewolf_Pannel( group ,[GP.title , SP.title]  , None ))
            except:await query.edit_message_text( texts.werepannel,reply_markup=Inline_Buttons.Werewolf_Pannel( group ,None  , None ))
    elif kind == 'Tag':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_Tag(group))
    elif kind == 'Notifications':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_Notifications(group))
    elif kind == 'Pin':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_Pin(group))
    elif kind == 'Game':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_Game(group))
    elif kind == 'State':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_State(group))
    elif kind == 'Fun':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_Fun(group))
    elif kind == 'Warn':await query.edit_message_text(texts.saved , reply_markup=Inline_Buttons.Pannel_Warn(group))

@bot.on_callback_query(filters.regex('^wwwBan') & MyFilters.admin )
@Instance
async def Ban_User_Callback(query,group:Group,user:User):
    data=str(query.data).split(' ')
    User_id=int(data[2])
    Chat_id=int(data[1])
    try:name = (await bot.get_users(user_ids=User_id)).first_name
    except:name = User_id
    try:
        await bot.kick_chat_member(user_id= User_id, chat_id=Chat_id )
        await query.edit_message_text(texts.ban_complited(name,query.from_user.mention ))
    except:
        await query.edit_message_text(texts.Error_Ocurred)

@bot.on_callback_query(filters.regex('^wwwtaskhir'))
@Instance
async def Taskhir_Callback(query,group:Group,user:User):
    data=str(query.data).split(' ')
    Muter=User(int(data[1]))
    Victam=User(int(data[2]))
    if user.user_id != Muter.user_id :
        if user.Coin > 10000 :
            Victam.UnMute(group.chat_id)
            if not user.is_Shekar(group):Muter.Mute(group.chat_id)
        else:await query.answer(texts.not_Enough_Coin(user.Coin), show_alert=True)
    else:await query.answer(texts.own_Evil, show_alert=True)

@bot.on_callback_query(filters.regex('^Close'))
async def Close_Callback( _ , q ):
    await q.edit_message_text(texts.Closed)

@bot.on_callback_query(filters.regex('^Bet'))
@Instance
async def Bet_Callback(query,group:Group,user:User):
    data=str(query.data).split(' ')
    try:
        Amount=int(data[3])
    except IndexError:
        Amount=None
        await query.edit_message_text(texts.cancel , parse_mode='html' )
        return

    if Amount:
        User_Id=int(data[2])
        Team=int(data[1])
        if user.user_id == User_Id:
            if Amount > user.Coin :
                user.bet( Amount , Team , group.Team_Zarib[Team] , group.chat_id )
                await query.edit_message_text(texts.bet_complited , parse_mode='html' )
                if float(group.Team_Zarib[Team]) <=1 : return
                await bot.send_message(User_Id ,texts.bet_Details( query.message.chat.title , group.Team_Zarib[Team] , Amount , group.Group_Teams[Team] ))
            else:
                await query.answer(texts.not_Enough_Coin(user.Coin), show_alert=True)

#----------------------------------------------------------------------------- STATS

@bot.on_callback_query(filters.regex('^Stats') & MyFilters.admin )
@Instance
async def Group_Statics_Callback(query,group:Group,user:User):
    data=str(query.data).split(' ')[1]
    if data=='Today':await query.edit_message_text(texts.Static_Dates_pannel(f'{texts.day}') , reply_markup=Inline_Buttons.Stats_Inline(f'{data}'))
    elif data=='Week':await query.edit_message_text(texts.Static_Dates_pannel(f'{texts.week}') , reply_markup=Inline_Buttons.Stats_Inline(f'{data}'))
    else :await query.edit_message_text(texts.Static_Dates_pannel(f'{texts.month}') , reply_markup=Inline_Buttons.Stats_Inline(f'{data}'))

@bot.on_callback_query(filters.regex('^Groups_Points_Statics') & MyFilters.admin )
@Instance
async def ALL_Group_Points_Callback(query,group:Group,user:User):
    Day=int(str(query.data).split(' ')[1])
    Points_list=[]
    Group_id_lists=[]
    Titels_List=[]
    for i in Robot().Same_Groups(group.Bot_Kind):
        GP=Group(i[0])
        print(group.Show_Games)
        if Day==1:Game_List=GP.Show_Games_Today
        else:Game_List=Statics(GP.Show_Games).Filter_Date(Day)
        Points_list.append(Statics(Game_List).Point)
        Group_id_lists.append(i[0])
        try:Titels_List.append((str((await bot.get_chat(int(i[0]))).title),i[0]))
        except:Titels_List.append((i[0],i[0]))
    Fname=Charts_AND_Draw.Single_Bar(Points_list,Group_id_lists,texts.Points_Title,texts.Point_Xlabel,texts.Point_Ylabel)
    await bot.send_photo(group.chat_id , Fname , caption=texts.Group_Pointing_help(Titels_List))
    import os
    os.remove(Fname)
    del os

@bot.on_callback_query(filters.regex('^AFK_Statics') & MyFilters.admin )
@Instance
async def All_AFK_Statics_Callback(query,group:Group,user:User):
    Day=int(str(query.data).split(' ')[1])
    if Day==1:Game_List=group.Show_Games_Today
    else:Game_List=Statics(group.Show_Games).Filter_Date(Day)
    Stats=Statics(Game_List)
    Fname=Charts_AND_Draw.Pie_Chart( Stats.AFK , Stats.Players , texts.afk_players_labels , texts.AFK_title  )
    await bot.send_photo(group.chat_id , Fname , caption=texts.AFK_Pie_Chart( Stats.AFK , Stats.Players))
    import os
    os.remove(Fname)
    del os

@bot.on_callback_query(filters.regex('^Average') & MyFilters.admin )
@Instance
async def Average_Statics_Callback(query,group:Group,user:User):
    Day=int(str(query.data).split(' ')[1])
    if Day==1:Game_List=group.Show_Games_Today
    else:Game_List=Statics(group.Show_Games).Filter_Date(Day)
    Games=Statics(Game_List)
    Game_Number=Games.Games_Num
    try:Afk=Games.AFK / Game_Number
    except:Afk=0
    JT=Games.Join_Time_All
    await query.message.reply_text(texts.Average_Statics(
        (Afk) , (Game_Number) , (Games.Players / Game_Number) , str(datetime.timedelta(seconds=JT[0],minutes=JT[1]))))

@bot.on_callback_query(filters.regex('^Game_AFK_Hour') & MyFilters.admin )
@Instance
async def Hourly_AFK_Statics_Callback(query,group:Group,user:User):
    Day=int(str(query.data).split(' ')[1])
    if Day==1:Game_List=group.Show_Games_Today
    else:Game_List=Statics(group.Show_Games).Filter_Date(Day)
    hours={}
    for hr in range(0,24):
        hours[hr]=0
    #--------------------------------------
    for i in (Game_List):
        hours[int(i[2])]+=i[3]
    mainlist=[[],[]]
    for plyrs in hours:
        mainlist[0].append(plyrs)
        mainlist[1].append(int(hours[plyrs]))
    Fname=Charts_AND_Draw.Normall_Bar (mainlist , texts.jointime_xlabel , texts.jointime_ylabel )
    await bot.send_photo(group.chat_id , Fname , caption=texts.Hour_Afk_Detais)
    import os
    os.remove(Fname)
    del os

@bot.on_callback_query(filters.regex('^Join_Time_Statics') & MyFilters.admin )
@Instance
async def Join_Time_Statics_Callback(query,group:Group,user:User):
    Day=int(str(query.data).split(' ')[1])
    if Day==1:Game_List=group.Show_Games_Today
    else:Game_List=Statics(group.Show_Games).Filter_Date(Day)
    list_hour=[i for i in range(0,24)]
    Fname=Charts_AND_Draw.Tree_Kind_Chart( Statics(Game_List).Join_Time_List , list_hour , texts.jointime_label)
    await bot.send_photo(group.chat_id , Fname , caption=texts.join_time_Statics(len(Game_List)))

@bot.on_callback_query(filters.regex('^َAdmins_Statics') & MyFilters.admin )
@Instance
async def Admin_Statics_Callback(query,group:Group,user:User):
    Day=int(str(query.data).split(' ')[1])
    if Day==1:Game_List=group.Show_Games_Today
    else:Game_List=Statics(group.Show_Games).Filter_Date(Day)

@bot.on_callback_query(filters.regex('^Elect') & MyFilters.shekar )
@Instance
async def Election_Spammer_Callback(query,group:Group,user:User):
    Vote=str(query.data)[6:].replace("'",'').replace('"','')
    await query.edit_message_text(texts.Votting(Vote))
    await bot.send_message( group.chat_id , texts.elaction_Spam(Vote) , reply_markup=Inline_Buttons.Made_Inline(texts.Im_hunter,'None') )
    await asyncio.sleep(5)
    await bot.send_message( group.chat_id , texts.elaction_Spam(Vote) , reply_markup=Inline_Buttons.Made_Inline(texts.Im_hunter,'None') )
    await asyncio.sleep(5)
    await bot.send_message( group.chat_id , texts.elaction_Spam(Vote) , reply_markup=Inline_Buttons.Made_Inline(texts.Im_hunter,'None') )
    await asyncio.sleep(5)
    await bot.send_message( group.chat_id , texts.elaction_Spam(Vote) , reply_markup=Inline_Buttons.Made_Inline(texts.Im_hunter,'None') )
    await asyncio.sleep(5)
    await bot.send_message( group.chat_id , texts.elaction_Spam(Vote) , reply_markup=Inline_Buttons.Made_Inline(texts.Im_hunter,'None') )
    await asyncio.sleep(5)
    await bot.send_message( group.chat_id , texts.elaction_Spam(Vote) , reply_markup=Inline_Buttons.Made_Inline(texts.Im_hunter,'None') )
    await asyncio.sleep(5)
    await bot.send_message( group.chat_id , texts.elaction_Spam(Vote) , reply_markup=Inline_Buttons.Made_Inline(texts.Im_hunter,'None') )
    await asyncio.sleep(5)


#------------------------------------------------------------------------------ INLINE
@bot.on_inline_query()
async def Inline_Query_Callback(_,query):
    user=User(query.from_user.id)
    try:title=(await bot.get_chat(user.Group)).title
    except:title=user.Group
    await Inline_Buttons.Inline_Answer(query,user.ProFile(Group(user.Group) , query.from_user.id , title ))


if __name__=='__main__':
    print('Dark Helper Has Runned ! https://www.github.com/amiralirj For More')
    #»«»«»«»«»|<<<<telegram : @AMIRALiRJ_PV  | INSTA : AMIRALIRJ >>>>|
    bot.run()#|<<<<telegram : @AMIRALiRJ_PV  | INSTA : AMIRALIRJ >>>>|
    #»«»«»«»«»|<<<<telegram : @AMIRALiRJ_PV  | INSTA : AMIRALIRJ >>>>|
    print('\n\n\n\n ok :( \n i\'m stopped , but my Threads are working :D \n » Press CTRL+Z\n\n ')

# 🕸 Good Luck 🕸  2021 :)