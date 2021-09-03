from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent)
import sys
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2')
from Functions.Filters.Filter_func import Get_Turn , Get_Turn_Bot_Emoji , Get_Turn_Emoji
from Config.Texts.Persian import  My_Statics 

def IO(O_F):
    if bool(O_F):
        return '✅'
    else:
        return '❌'

Button_JoinTime_Link_Maker=lambda link :InlineKeyboardMarkup([[InlineKeyboardButton(f'ᴊᴏɪɴ ᴛᴏ ɢᴀᴍᴇ', url=f'{link}')]])
Dark_Channel = InlineKeyboardMarkup([[InlineKeyboardButton('ᴅᴀʀᴋ ᴄʜᴀɴɴᴇʟ', url='https://t.me/DarkhelperNews')]])

def Channel_Text(text,url):
    return InlineKeyboardMarkup([[InlineKeyboardButton(f'{text}', url=f'{url}')]])

def Made_Inline(text,query):
    return InlineKeyboardMarkup([[InlineKeyboardButton(f'{text}', callback_data=f'www{query}')]])

def Election_Inline(List,group):
    inlines=[]
    for i in List :
        #user_id,alive,Role,name,Pretended_Role
        if i[4]=='none':rl='-'
        else:rl=i[4]
        if len(str(i[3]).encode('utf-8')) > 50 :
            continue
        if len(i[3])>20:
            if group.Role_Saver:inlines.append([InlineKeyboardButton(f'{i[3]}', callback_data=f'Elect {i[0]}'),InlineKeyboardButton(f'{rl}', callback_data=f'Elect {i[3]}')])
            else:inlines.append([InlineKeyboardButton(f'{i[3]}', callback_data=f'Elect {i[3]}')])
        else:
            if group.Role_Saver:inlines.append([InlineKeyboardButton(f'{i[3][:15]}', callback_data=f'Elect {i[0]}'),InlineKeyboardButton(f'{rl}', callback_data=f'Elect {i[3][:15]}')])
            else:inlines.append([InlineKeyboardButton(f'{i[3][:15]}', callback_data=f'Elect {i[3][:15]}')])
    inlines.append([InlineKeyboardButton(f'Wait', callback_data=f'Elect Wait')])
    inlines.append([InlineKeyboardButton('❌ بستن ❌', callback_data='ClSheKar')])
    return InlineKeyboardMarkup(inlines)
#------------------------------------------------------------------------------------------------------------------

Statics_Inline=InlineKeyboardMarkup([
    [InlineKeyboardButton('امار امروز ☀️', callback_data='Stats -1')],
    [InlineKeyboardButton('امار هفتگی  🌗', callback_data='Stats -7')],
    [InlineKeyboardButton('امار ماهانه  🌕', callback_data='Stats -31')]])

Stats_Inline=lambda Time:InlineKeyboardMarkup([
        [InlineKeyboardButton('🔥 امتیاز گپ ها 🌟', callback_data=f'Groups_Points_Statics {Time}')],
        [InlineKeyboardButton('امار افک در ساعت 📑', callback_data=f'Game_AFK_Hour {Time}')],
        [InlineKeyboardButton('امار کلی افک 💩', callback_data=f'AFK_Statics {Time}')],
        [InlineKeyboardButton('امار جوین تایم 🕑', callback_data=f'Join_Time_Statics {Time}')],
        [InlineKeyboardButton('🔍 میانگین های متنی', callback_data=f'Average {Time}')],
        [InlineKeyboardButton('امار ادمین ها 📊', callback_data=f'َAdmins_Statics {Time}')],
        [InlineKeyboardButton('❌ بستن ❌', callback_data='Close')],
    ])
#------------------------------------------------------------------------------------------------------------------
def Bet_Inline(Group,User_id,Amount):

    if Group.Bot_Kind==0:
        First_Mature='🧛🏻‍♀️ ومپایر 🧛🏻‍♀️'
        sec_Mature='🔥 آتش 🔥'
    elif Group.Bot_Kind==1:
        First_Mature='💖 لاور 💖'
        sec_Mature='🔥 آتش 🔥'
    else:
        First_Mature='💖 لاور 💖'
        sec_Mature='💣 بمب گذار 💣'
    zarib=Group.Team_Zarib
    indx=0
    for i in zarib:
        if float(i)<=1:zarib[indx]='ضریبی ندارد ❌'
        indx+=1

    zz = InlineKeyboardMarkup([
        [InlineKeyboardButton('👩🏻‍🦰👨🏻‍🦱 روستا 👩🏻‍🦰👨🏻‍🦱', callback_data= f'Bet 0 {User_id} {Amount}'),InlineKeyboardButton(f'🔝 {zarib[0]:.2f} 💲', callback_data= f'Bet 0 {User_id} {Amount}')],
        [InlineKeyboardButton('👥 فرقه 👥', callback_data=   f'Bet 1 {User_id} {Amount}'),InlineKeyboardButton(f'🔝 {zarib[1]:.2f} 💲', callback_data= f'Bet 1 {User_id} {Amount}')],
        [InlineKeyboardButton('🐺 گرگ 🐺', callback_data=    f'Bet 2 {User_id} {Amount}'),InlineKeyboardButton(f'🔝 {zarib[2]:.2f} 💲', callback_data= f'Bet 2 {User_id} {Amount}')],
        [InlineKeyboardButton('🔪 قاتل 🔪', callback_data=   f'Bet 3 {User_id} {Amount}'),InlineKeyboardButton(f'🔝 {zarib[3]:.2f} 💲', callback_data= f'Bet 3 {User_id} {Amount}')],
        [InlineKeyboardButton(f'{First_Mature}', callback_data= f'Bet 4 {User_id} {Amount}'),InlineKeyboardButton(f'🔝 {zarib[4]:.2f} 💲', callback_data= f'Bet 4 {User_id} {Amount}')],
        [InlineKeyboardButton(f'{sec_Mature}', callback_data=      f'Bet 5 {User_id} {Amount}'),InlineKeyboardButton(f'🔝 {zarib[5]:.2f} 💲', callback_data= f'Bet 5 {User_id} {Amount}')],
        [InlineKeyboardButton('👺 منافق 👺', callback_data=  f'Bet 6 {User_id} {Amount}'),InlineKeyboardButton(f'🔝 {zarib[6]:.2f} 💲', callback_data= f'Bet 6 {User_id} {Amount}')],
        [InlineKeyboardButton('⭕️ لغو ❌', callback_data=f'Bet None')]])
    return zz


def Main_Pannel(Group): 
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f'{Group.Subscription_Date} ♻️',url='https://t.me/DarkhelperNews/3')],
        [InlineKeyboardButton('تنظیمات گروه ⚙️', callback_data='Setting Group'),InlineKeyboardButton('تنظیمات گرگینه ⚙️', callback_data='Setting Werewolf')],
        [InlineKeyboardButton('❌ بستن ❌', callback_data='Close')]
    ])

def Werewolf_Pannel(Group,titles,link):
    Bot_King_List=Get_Turn_Bot_Emoji(Group.Bot_Kind)
    if link==None:
        link='https://t.me/DarkhelperNews'
    if titles==None:
        titles=['none','none']


    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f'✦ گروه اصلی',url=f'{link}'),InlineKeyboardButton(f'{titles[0]}',url=f'{link}')],
        [InlineKeyboardButton(f'✦ گروه پشتیبانی',url=f'https://t.me/DarkhelperNews'),InlineKeyboardButton(f'{titles[1]}',url='https://t.me/DarkhelperNews')],
        [InlineKeyboardButton('🛠🔔 تگ', callback_data='Pannel Tag')],
        [InlineKeyboardButton('🛠📢 اطلاع رسانی', callback_data='Pannel Notifications')],
        [InlineKeyboardButton('🛠📌 پین', callback_data='Pannel Pin')],
        [InlineKeyboardButton('🛠🔜 تنظیمات بازی', callback_data='Pannel Game')],
        [InlineKeyboardButton('🛠📛 استیت', callback_data='Pannel State')],
        [InlineKeyboardButton('🛠👻 سرگرمی', callback_data='Pannel Fun')],
        [InlineKeyboardButton(f'Werewolf {Bot_King_List[1]}', callback_data='Change bot_kind 1 werewolf'),InlineKeyboardButton(f'Onyx {Bot_King_List[0]}', callback_data='Change bot_kind 0 werewolf'),InlineKeyboardButton(f'Black {Bot_King_List[2]}', callback_data='Change bot_kind 2 werewolf')],
        [InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Main')]
    ])

def Pannel_Tag(Group):
    tags={'auto_tag':'📢 تگ خودکار ','auto_del':'🔇 پاکسازی تگ ','auto_tag_sup':'📣 تگ ساپورت','auto_del_sup':'🔕پاکسازی ساپورت'}
    inlines=[]
    for i in tags:
        inlines.append([InlineKeyboardButton(f'{tags[i]}', callback_data=f'Change {i} Rev Tag'),InlineKeyboardButton(f'{Get_Turn(int(Group.All_Atrebeutes[i]))}', callback_data=f'Change {i} Rev Tag')])
    inlines.append([InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Were')])
    return InlineKeyboardMarkup(inlines)

def Pannel_Pin(Group):
    pins={  'pin_shekar':'💂 پین شکارچی','pin_nazer':'👁‍🗨 پین ناظر','pin_list':'🧾 پین لیست '}
    inlines=[]
    for i in pins:
        inlines.append([InlineKeyboardButton(f'{pins[i]}', callback_data=f'Change {i} Rev Pin'),InlineKeyboardButton(f'{Get_Turn(int(Group.All_Atrebeutes[i]))}', callback_data=f'Change {i} Rev Pin')])
    inlines.append([InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Were')])
    return InlineKeyboardMarkup(inlines)

def Pannel_Notifications(Group):
    notifications={'alarm':'⚠️ هشدار ها ','admin_Alarm':'⚠️ هشدار ادمین ','jointime_sup':'🔔اطلاع جوین تایم','role_saver':'⚜️ رول سیور'}
    inlines=[]
    for i in notifications:
        inlines.append([InlineKeyboardButton(f'{notifications[i]}', callback_data=f'Change {i} Rev Notifications'),InlineKeyboardButton(f'{Get_Turn(int(Group.All_Atrebeutes[i]))}', callback_data=f'Change {i} Rev Notifications')])
    inlines.append([InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Were')])
    return InlineKeyboardMarkup(inlines)

def Pannel_Game(Group):
    Game={'auto_next_game':'🕛 نکست گیم خودکار','next_game_response':'💬 Next Response','dead_next':'☠️ نکست مردگان','auto_start':'♻️ استارت بازی','afk_warn':'🛃 وارن به افک ها'}
    inlines=[]
    for i in Game:
        inlines.append([InlineKeyboardButton(f'{Game[i]}', callback_data=f'Change {i} Rev Game'),InlineKeyboardButton(f'{Get_Turn(int(Group.All_Atrebeutes[i]))}', callback_data=f'Change {i} Rev Game')])
    inlines.append([InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Were')])
    return InlineKeyboardMarkup(inlines)
    

def Pannel_Fun(Group):
    Funs={'fun_mute':'📵 قدرت سکوت','sooti':'😝 ذخیره سوتی','questions':'🤔 سوالات','bors':'💲 بورس','bet':'💰 شرطبندی'}
    inlines=[]
    for i in Funs:
        inlines.append([InlineKeyboardButton(f'{Funs[i]}', callback_data=f'Change {i} Rev Fun'),InlineKeyboardButton(f'{Get_Turn(int(Group.All_Atrebeutes[i]))}', callback_data=f'Change {i} Rev Fun')])
    inlines.append([InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Were')])
    return InlineKeyboardMarkup(inlines)

a={'state':'',
'warn':'🚷 حداکثر اخطار',
'state_lock':''}




def Pannel_State(Group):
    st=Get_Turn_Bot_Emoji(Group.State_Lock)
    return InlineKeyboardMarkup([
        [InlineKeyboardButton('⛔️ استیت حداقل', callback_data='None')],
        [InlineKeyboardButton('🔆 مقدار فعلی', callback_data='None'),InlineKeyboardButton(f'{Group.Least_State}', callback_data='None')],
        [InlineKeyboardButton('〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️', callback_data='None')],
        [InlineKeyboardButton('🚸 غیرفعال', callback_data='Change state 0 State')],
        [InlineKeyboardButton('1', callback_data='Change state 1 State'),InlineKeyboardButton('3', callback_data='Change state 3 State'),InlineKeyboardButton('5', callback_data='Change state 5 State')],
        [InlineKeyboardButton('10', callback_data='Change state 10 State'),InlineKeyboardButton('15', callback_data='Change state 15 State'),InlineKeyboardButton('20', callback_data='Change state 20 State')],
        [InlineKeyboardButton('35', callback_data='Change state 35 State'),InlineKeyboardButton('50', callback_data='Change state 50 State'),InlineKeyboardButton('100', callback_data='Change state 100 State')],
        [InlineKeyboardButton('〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️', callback_data='None')],
        [InlineKeyboardButton('🌗 نوع قفل', callback_data='None')],
        [InlineKeyboardButton('🔎 پیام دادن فقط پلیر ها', callback_data='None'),InlineKeyboardButton(f'{Get_Turn(int(Group.Players_Lock_Only))}', callback_data=f'Turn anti_tabchi Rev Group')],
        [InlineKeyboardButton(f'☀️{st[0]} 24 ساعت ', callback_data='Change state_lock 0 State'),InlineKeyboardButton(f'🌑{st[1]} شبانه', callback_data='Change state_lock 1 State')],
        [InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Were')]
    ])

def Pannel_Warn(Group):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton('⚠️ حداکثر وارن ', callback_data='None')],
        [InlineKeyboardButton('🔆 مقدار فعلی', callback_data='None'),InlineKeyboardButton(f'{Group.Warn}', callback_data='None')],
        [InlineKeyboardButton('⚡️〰️〰️〰️〰️〰️〰️〰️🔆〰️〰️〰️〰️〰️〰️⚡️', callback_data='None')],
        [InlineKeyboardButton('🚸 غیرفعال', callback_data='Change warn 0 Warn')],
        [InlineKeyboardButton('1', callback_data='Change warn 1 Warn'),InlineKeyboardButton('3', callback_data='Change warn 3 Warn'),InlineKeyboardButton('5', callback_data='Change warn 5 Warn')],
        [InlineKeyboardButton('6', callback_data='Change warn 6 Warn'),InlineKeyboardButton('8', callback_data='Change warn 8 Warn'),InlineKeyboardButton('10', callback_data='Change warn 10 Warn')],
        [InlineKeyboardButton('12', callback_data='Change warn 12 Warn'),InlineKeyboardButton('15', callback_data='Change warn 15 Warn'),InlineKeyboardButton('20', callback_data='Change warn 20 Warn')],
        [InlineKeyboardButton('30', callback_data='Change warn 30 Warn'),InlineKeyboardButton('50', callback_data='Change warn 50 Warn'),InlineKeyboardButton('100', callback_data='Change warn 100 Warn')],
        [InlineKeyboardButton('⚡️〰️〰️〰️〰️〰️〰️〰️🔆〰️〰️〰️〰️〰️〰️⚡️', callback_data='None')],
        [InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Group')]
    ])
def Pannel_Spam(Group):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton('⚠️ حداکثر پیام در 10 ثانیه ', callback_data='None')],
        [InlineKeyboardButton('🔆 مقدار فعلی', callback_data='None'),InlineKeyboardButton(f'{Group.Spam_Count}', callback_data='None')],
        [InlineKeyboardButton('〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️', callback_data='None')],
        [InlineKeyboardButton('🚸 غیرفعال', callback_data='Turn spam_count 999999999999 Spam')],
        [InlineKeyboardButton('3', callback_data='Turn spam_count 3 Spam'),InlineKeyboardButton('5', callback_data='Turn spam_count 5 Spam'),InlineKeyboardButton('7', callback_data='Turn spam_count 7 Spam')],
        [InlineKeyboardButton('8', callback_data='Turn spam_count 8 Spam'),InlineKeyboardButton('10', callback_data='Turn spam_count 10 Spam'),InlineKeyboardButton('13', callback_data='Turn spam_count 13 Spam')],
        [InlineKeyboardButton('15', callback_data='Turn spam_count 15 Spam'),InlineKeyboardButton('20', callback_data='Turn spam_count 20 Spam'),InlineKeyboardButton('50', callback_data='Turn spam_count 50 Spam')],
        [InlineKeyboardButton('〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️', callback_data='None')],
        [InlineKeyboardButton('🧠 قفل اسپم هوشمند', callback_data='Turn anti_spam rev Spam'),InlineKeyboardButton(f'{Get_Turn(int(Group.Anti_Spam))}', callback_data=f'Turn anti_spam rev Spam')],
        [InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Group')]
    ])

#✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪⍟ |-Group--| ✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✮✪✮✪✮|
#✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪ |-Pannel-| ✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮✪✮|
def Group_Pannel(group):
    channel=group.Show_Channel
    if not channel :
        channel = 'https://t.me/DarkhelperNews'
    return InlineKeyboardMarkup([ 

        [InlineKeyboardButton(f' 🛠🔞 قفل پورن', callback_data=f'Pannel Porn')],

        [InlineKeyboardButton(f' 🛠🔒 قفل نوع پیام', callback_data=f'Pannel Filters')],

        [InlineKeyboardButton(f'🛠🛡 قفل اسپم', callback_data=f'Pannel Spam')],

        [InlineKeyboardButton('〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️', callback_data='None')],

        [InlineKeyboardButton(f'🛠🚓 تنظیمات وارن', callback_data=f'Pannel Warn')],

        [InlineKeyboardButton('〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️', callback_data='None')],

        [InlineKeyboardButton(f'🤖 انتی ربات', callback_data=f'Turn anti_robot Rev Group'),
        InlineKeyboardButton(f'{Get_Turn(int(group.Anti_Robot))}', callback_data=f'Turn anti_robot Rev Group')],

        [InlineKeyboardButton(f'📵 انتی تبچی', callback_data=f'Turn anti_tabchi Rev Group'),
        InlineKeyboardButton(f'{Get_Turn(int(group.Anti_Tabchi))}', callback_data=f'Turn anti_tabchi Rev Group')],

        [InlineKeyboardButton(f'⚠️ فیلتر فحش', callback_data=f'Turn fosh_filter Rev Group'),
        InlineKeyboardButton(f'{Get_Turn(int(group.Anti_NFSW))}', callback_data=f'Turn fosh_filter Rev Group')],

        [InlineKeyboardButton(f'🌟 کانال', callback_data=f'None'),
        InlineKeyboardButton(f'{group.Channel_Text}', url=f'{channel}')],

        [InlineKeyboardButton(f'🔇 قفل کانال', callback_data=f'Turn channellock Rev Group'),
        InlineKeyboardButton(f'{Get_Turn(int(group.Channel_Lock))}', callback_data=f'Turn channellock Rev Group')],

        [InlineKeyboardButton(f'🎉 خوشامد گو', callback_data=f'Turn welcometurn Rev Group'),
        InlineKeyboardButton(f'{Get_Turn(int(group.Welcome_Turn))}', callback_data=f'Turn welcometurn Rev Group')],

        [InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Main')]
    ])

def Porn_Pannel(Group):
    Porn={'dick':'الت تناسلی','pussy':'واژن','coveredpossy':'واژن پوشیده شده','fboobs':'سینه زن','mboobs':'سینه مرد','coveredboobs':'سینه پوشیده','stomack':'شکم برهنه','baghal':'زیر بغل','ass':'مقعد','feet':'پا','coveredass':'مقعد پوشیده'}
    inlines=[]
    inlines.append([InlineKeyboardButton(f'قفل پورن {Get_Turn_Emoji(int(Group.Porn))}', callback_data='Turn porn rev Porn')])
    for i in Porn:
        inlines.append([InlineKeyboardButton(f'{Porn[i]}', callback_data=f'Turn {i} Rev Porn'),InlineKeyboardButton(f'{Get_Turn(int(Group.Porn_All_Filters[i]))}', callback_data=f'Turn {i} Rev Porn')])
    inlines.append([InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Group')])
    return InlineKeyboardMarkup(inlines)

def Filters_pannel(Group):
    Filters={'voice_lock':'🔇 قفل وویس','sticker_lock':'🃏 قفل استیکر','photo_lock':'🖼 قفل عکس','link_lock':'📡 قفل لینک','forward_lock':'📧 قفل فروارد',
    'video_lock':'📽 قفل فیلم','service_lock':'💻 قفل سرویس'}
    inlines=[]
    for i in Filters:
        inlines.append([InlineKeyboardButton(f'{Filters[i]}', callback_data=f'Turn {i} Rev Filters'),InlineKeyboardButton(f'{Get_Turn(int(Group.All_Controls[i]))}', callback_data=f'Turn {i} Rev Filters')])
    inlines.append([InlineKeyboardButton('🔙 بازگشت 🔙', callback_data='Undo Group')])
    return InlineKeyboardMarkup(inlines)
    
async def Inline_Answer(inline_query,prof):
    await inline_query.answer(
        results=[            
            # InlineQueryResultArticle(
            #     title="🌐📊 Statics",
            #     input_message_content=InputTextMessageContent(
            #         f"{statics_in}"
            #     ),
            #     description="How to use Pyrogram",
            #     thumb_url="https://i.imgur.com/JyxrStE.png",
            #     reply_markup=InlineKeyboardMarkup(
            #         [
            #             [InlineKeyboardButton(
            #                 "Open website",
            #                 callback_data=""
            #             )]
            #         ]
            #     )
            # ),

            InlineQueryResultArticle(
                title="🗃👤 My Statics",
                input_message_content=InputTextMessageContent(
                    f"{prof}"
                ),
                description=f"{My_Statics}",
                reply_markup=Dark_Channel)
        ],
        cache_time=1
    )

