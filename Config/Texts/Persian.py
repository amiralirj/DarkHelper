Start_Text = lambda  mention: f'''☘️ سلام {mention} خوش اومدی به ربات دارک هلپر ☘️

این ربات دارای هزاران قابلیت سرگرمی و ... هست که برای دیدنشون کافیه رو دکمه زیر کلیک کنی 🤩🎆'''
pannel='پنل برای شما باز شد ! هم اکنون میتونید تغییراتی که میخواید رو انجام بدید !'

Question_text=lambda  qa: f''' #چالش_اطلاعات_عمومی
🤩🤩🤩🤩 واووو اینجاروو

هرکی سریع تر این سوالو جواب بده 500 دلارو 200 لایت کوین میگیره 
🧠🧠🧠🧠

سوال : {qa} «

🧠🧠🧠🧠'''
its_Correct='درست جواب دادی  🥳 🥳 🥳 🥳 🥳 \n برات 500 دلارو 200 لایت کوین واریز کردم !'

Membership='شما اشتراک ربات را ندارید ! برای خرید اشتراک به پیوی @amiralirj_pv مراجعه کنید !'

shekar_less_State=lambda  mes,state : f'''#اطلاعیه 🔆 
کاربری با استیت زیر ۳۰ شکارچی شده است 📛 لطفا جهت اموزش به پیوی ایشان اقدام کنید ! 
ɴᴀᴍᴇ : {mes.firstname}
ᴜꜱᴇʀɴᴀᴍᴇ : {mes.from_user.username}
ɪᴅ : {mes.from_user.id}
ꜱᴛᴀᴛꜱ »
    ᴡᴇʀᴇᴡᴏʟꜰ :{state[2]}
    ʙʟᴀᴄᴋ :{state[1]}
    ᴏɴʏx :{state[0]}
- @DarkHelperChannel'''

shekar=lambda  mention : f'''شکارچی بازی شناسایی شد {mention} 💂


🚨 برای اسپم رایتون از /ray استفاده کنید 🚨

💢 با دستور /ask نقش پلیر هارو بپرسید ! 💢'''

nazer='''👁‍🗨 ناظر بازی شناسایی شد 👤

» میتوانید با /ray رای خود را اسپم کنید 🔰'''


how_to_bet_correct='''• لطفا مقدار شرطی که میخواهید را جلوی دستور بنویسید مثلا : 
» /bet 85'''

not_Enough_Coin=lambda  Coin : f'''📇 لایت کوین های شما کافی نیست 
موجودی شما : {Coin} 🪙'''

not_Enough_dolar=lambda  dolar : f'''📇 دلار های شما کافی نیست 
موجودی شما : {dolar} 🪙'''

bet= '''<code> شرطتون روی کدام تیم ثبت شود ؟ </code>
💸 @DarkHelperChannel 💸
'''
bet_Details=lambda  group , zarib , amount , TM :f'''شرط شما با موفقیت بر روی {TM} بسته شد ✅
✘ گروه : {group}
✘ مقدار شرط : {amount} 💲
✘ ضریب : {zarib} 🔝
✘ سود شما در صورت برد  : {(amount * zarib) - amount  } 💰'''

bet_complited='<bold> شرط شما با موفقیت بسته شد ✅ </bold>'
cancel='🛑 لغو شد 🛑'

admin_setted=lambda  mention:f'👤 کاربر {mention} به لیست ادمین ها پیوست !'
admin_deleted=lambda  mention:f'👤 کاربر {mention} از لیست ادمین ها پاک شد !'

Muted_Fun=lambda  mention_Muter , mention_Victam:f'''👿شیطان خبیث {mention_Muter} من رو به سکوت کردن {mention_Victam} وادار کرده 👿
این قدرت اونقدر قوی بود که هیچ کاری از دستم بر نیمد😓 تنها راه شکستن این نفرین تسخیر کردن این شیطانه که باعث حبص شدنش تو زندان میشه 😱
'''

taskhir_bt=lambda  mention_Muter : f'😱 تسخیر {mention_Muter} ☠️'
own_Evil='نمیتونی خودتو که تسخیر کنی :('


on  = 'فعال ✅'
off = 'غیر فعال ❌'


reply='لطفا دستور را روی پیامی از فرد مورد نظر ریپلای کنید !'

grouppannel='وارد پنل گروه شدید , چه کاری میتونم برات انجام بدم ؟'
werepannel='وارد پنل ورولف شدید, چه کاری میتونم برات انجام بدم ؟'
saved='تنظیمات شما با موفقیت ذخیره شد ✅'
new_pannel="🔧 چه کاری براتون انجام بدم 🔧"

nfsw_detected=lambda  mention , NFSWs , id:f'''🚨 #فوری 
#{id}
یک پیام با محتوای فیلتر شده توسط {mention} فرستاده شد ! 🔞
محتوا پیام :
- - - - - - - - - - - - - - - - - - 
<code>{NFSWs}</code>
- - - - - - - - - - - - - - - - - - 
<bold>این پیام توسط ربات پاک شد✅ </bold>
'''


nfsw_alarm=lambda  mention :f'کاربر {mention} لطفا از فرستادن پیام با محتوای نامناسب خودداری کنید , درصورت تکرار بن خواهید شد !'

ban='Ban🚨'

ban_complited=lambda  mention,admin :f'#report 🛃 \n کاربر {mention} توسط ادمین {admin} بن شد !'
Error_Ocurred='مشکلی پیش امده :('

Owner_Setted=lambda  Fake_Hash :f'برای کاربر اختیارات کریتوری ازاد شد ✔️ \n هش استفاده شده : {Fake_Hash}'

Sooti_Saved=lambda  chnnl :f'😈😈 به به چه سوتی ای \n  سیوش کردم تو کانال 👻 {chnnl} 👻'


join_time_Filnished=lambda  time, date , players :f'''•|⛑| #ᴅᴀʀᴋ_ʜᴇʟᴘᴇʀ
ᴊᴏɪɴ ᴛɪᴍᴇ ғɪɴɪsʜᴇᴅ

-| ᴊᴏɪɴ ᴛɪᴍᴇ: | {time} |⏱

-| ᴘʟᴀʏᴇʀs: | {players} |👨🏻‍💻

-| ᴅᴀᴛᴇ: | {date} |⏳
'''

tag_stopped='تگ متوقف شد !'
tag_is_Also_Stopped='من که تگ نمیکنم :( '


Next_Dead=lambda next,men:f'{men}✨{next}'
Admin_Config=lambda Cor,Wor,hsh:f'⁑ تعداد {Cor} ادمین با موفقیت به لیست اضافه شدند ! و نعداد {Wor} نفر از قبل در لیست وجود داشتند \n هش استفاده شده » {hsh}'

statics_in='⭒ امار گپ ها با احتساب ( افک , جوین تایم . تعداد پلیر , تعداد بازی )\n  از دکمه های زیر میتونید مدت زمان امار را مشخص کنید !'

My_Statics='⭒ امار الماس ها و امتیازات جهانی و گروهی ⚡️'


User_ProFile=lambda mention , Group_Title , Coins , Points , Diamonds , Now_Global_Rank_point , Now_Local_Rank_point , Now_Global_Rank_coin , Now_Local_Rank_coin  , Ghost , Anti_Gost , Ghost_Killer , Point_Last_Rank , Coin_Last_Rank , Pointing_Ranks , laghab , birth   : f'''
👤نام: {mention}
╢گروه: {Group_Title}
╢لایت کوین🪙 : {Coins}
╢دلار💵 : {Points}
╢بیت کوین💎 : {Diamonds:.2f}
╢💵رتبه جهانی دلار : {Now_Global_Rank_point}
╢💵رتبه گروهی دلار : {Now_Local_Rank_point}
╢🪙رتبه جهانی لایت کوین : {Now_Global_Rank_coin}
╢🪙رتبه گروهی لایت کوین : {Now_Local_Rank_coin}
╢ارواح : {Ghost}
╢راهبه ها  : {Anti_Gost}
╝شیاطین: {Ghost_Killer}

🌐 رتبه های ماه قبل
╢⚡️🪙 : {Point_Last_Rank}
╢⚡️💵 : {Coin_Last_Rank}

🎈 تولد : {birth}
🔗 لقب : {laghab}
➖➖➖➖➖➖➖➖➖➖➖➖➖
{Pointing_Ranks[0]}
{Pointing_Ranks[1]}
{Pointing_Ranks[2]}
➖➖➖➖➖➖➖➖➖➖➖➖➖

#Id_Card 👁
'''
frame_help='''راهنمای ساخت فریم 🎆 
<code>میتوانید از لیبل های زیر برای جایگذاری امتیازات استفاده کنید !</code>
    🛑نام فرد -> {name}
    🛑امتیازات (دلار) -> {point}
    🛑لایت کوین -> {coin}
    🛑اسم گپ -> {title}
    🛑بیت کوین ها -> {bitcoin}
    🟢روح ها -> {ghost}
    🟢راهبه ها -> {antighost}
    🟢شیاطین -> {ghostkiller}
    🟢وارن ها -> {Warn}
    🛑لقب -> {laghab}
    🛑تولد -> {birth}
    🟢بت های درست -> {bets}
    🟢کارت ها -> {Pointing}
    🛑رتبه ماه قبل (دلار) -> {last_dolar_rank}
    🛑رتبه ماه قبل (لایت کوین) -> {last_litecoin_rank}
    🟢رتبه ی اکنونی لایت کوین (جهانی) -> {litecoin_rank_global}
    🟢رتبه ی اکنونی دلار (جهانی) -> {dolor_rank_global}
    🟢رتبه اکنونی لایت کوین (گروهی) -> {litecoin_rank_local}
    🟢رتبه اکنونی دلار (گروهی) -> {dolor_rank_local}
    
    
✗نکته : لطفا از لیبل هایی که کنارشان علامت قرمز دارند استفاده کنید و میتوانید از لیبل هایی تیک سبز دارند به صورت دلخواه استفاده کنید !'''

do_not_Talk='میشه انقدر دستو پا نزنی وقتی تسخیر شدی 🤨🤨'
self_mute='میدونم زندگیا سخت شده 😔 ولی خودکشی کار درستی نیست ☹️ بهترین کار اینه به روانشناس مراجعه کنی :('
message_id_sticker=23482
Bote_Muting='از ربات ها داش ارجی محافظت میکنه , بریم سمتشون کشته خواهیم شد :( بیا رو یه ادم امتحانش کن'
Suspended_Mute='بزار 10 دقیقه باز باشه گناه داره  :/'
message_id_devil_sticker=23489
NFSW_sticker=23491

not_Reg='ثبت نشده !'
set_second_birth=lambda b :f'تولد ادم که تغییر نمیکنه :( شما یکبار تولدتونو ثبت کردید( برای تغییر به پشتیبانی پیام بدهید !) '
birth_help='''راهنمای ثبت تولد 🎉🎉
لطفا تاریخ تولد خود را به میلادی به صورت زیر وارد کنید !
YYYY-MM-DD 
برای مثال : 
2004-2-24

@DarkHelperChannel'''

birth_reg='تاریخ تولد شما با موفقیت ثبت شد ✅'
have_NFSW='<code>لقب دارای الفاظ +18 است </code>'

laghab_setted='لقب شما با موفقیت ثبت شد ✅'
command='لطفا جلوی دستور مقدار را بنویسید \n مثال : \n  /setchannel https://t.me/DarkHelperChannel'
how_to_reg_channel='''راهنمای ثبت کانال 🚑 
برای ثبت کانال ایدی کانال مورد نظر را به صورت لینک در جلوی دستور بفرستید 
✉️ مثال : /setchannel https://t.me/DarkHelperChannel

🧧 نکته : دقت داشته باشید کانال های پرایویت پذیرفته نمیشوند !'''
channel_setted='کانال شما با موفقیت ثبت شد ✅'

tag_deleted =lambda tg :f'تعداد {tg} تگ با موفقیت پاک شد ✅'

GET_WARNED=lambda tg :''
Kicked_For_WARN=lambda tg,id :f'کاربر {tg} به علت پر شدن وارن ها از گروه کیک شد ! \n 🔸 علت : افک شدن \n 🔸 ایدی عددی : <code>{id}</code>'
Get_AFK=lambda tg :f'🔸 کاربر {tg} از شما به علت افک شدن تعداد 100 لایت کوین 🪙 و 200 دلار 💵  مصادره شد !'
Admin_Afked=lambda tg :f'''#اطلاعیه 📢 
ادمین {tg} در بازی افک شده است 

🔸 این پیام جهت اطلاع رسانی به کریتور ها و ناظر ها است !'''
dead='مرده'

join_time_Started='''جوین تایم شروع شد 🌗

    ⚜️همه ی ادمین ها ⚜️

    ☣️ به گپ مراجعه کنید  ☣️
    
    ⚠️    ⚠️     ⚠️     ⚠️'''

welcome='سلام {name} عزیز خوش اومدی به گروه {title} \n werewolf : {werewolf} \n onyx : {onyx} \n black : {black}'

welcome_help='''راهنمای ثبت قالب خوشامد 🎉 
<code>میتوانید از لیبل های زیر برای جایگذاری اطلاعات استفاده کنید !</code>

نام کاربر ➝ {name}🔴
اسم گروه ➝ {title}🟢
استیت های بازی (ورولف,اونیکس,بلک) ➝ {werewolf}  {onyx}  {black}🟢

    
✗نکته : لطفا از لیبل هایی که کنارشان علامت قرمز دارند استفاده کنید و میتوانید از لیبل هایی تیک سبز دارند به صورت دلخواه استفاده کنید !
'''

Closed='بسته شد ✔️'

statics_pannel='📈 وارد پنل امار شدید  , چه کاری میتونم براتون انجام بدم ؟ 📉'

Static_Dates_pannel=lambda  Date :f'📊 وارد بخش امار {Date} شدید ! امار مورد نظر خود را انتخاب کنید !'
week='هفتگی'
day='روزانه'
month='ماهانه'

Points_Title="Group's Pointing Charts"
Point_Xlabel='Group id'
Point_Ylabel='Points'

def Group_Pointing_help(Titles):
    txt='<bold>❉ ایدی گروه هایی که در تصویر مشاهده میکنید مربوط به گروه های زیر است !</bold>\n\n'
    for i in Titles:
        txt+=f'✡ {i[1]} ➺ {i[0]}\n'

    txt+='\n<code>در نمودار بالا پارامتر های زیر تاثیر گذار بوده اند :</code>\n'
    txt+='✘AFK\n✘JoinTime\n✘Players\n✘Number of Games\n✘Games Time'
    return txt

async def Analyz_Admin_P(Admin_Tag,Admin_Join,Admin_Afk,User,bot):
    text='☀️ᴛᴀɢ|ᴀꜰᴋ|ᴊᴏɪɴ☀️ :\n\n'
    for i in Admin_Tag:
        text+=f'🔥{Admin_Tag[i]}|{Admin_Afk[i]}|{Admin_Join[i]}🔥{(await User(i).mention(bot))}\n'

    return text

afk_players_labels=['Players','AFK']
AFK_title='AFK Statics'
AFK_Pie_Chart=lambda  afk,player :f'''نمودار بالا نشانگر تعداد افک ها را نسبت به کل پلیر ها نشان میدهد
✘ تعداد افک ها {afk} 
✘ تعداد پلیر ها {player} 
نفر در بازه زمانی انتخابی شما بوده اند !
درصد افک شدن :  {(afk / player) * 100 } %
'''
jointime_label='Join Time'
join_time_Statics=lambda  game_Times :f'<code>✤ این 3 نمودار نمایانگر جوین تایم به ترتیب بازی ها هست !</code> ✘ تعداد بازی های انجام شده : {game_Times} '
Hour_Afk_Detais='✤ نمودار بالا میزان افک ها نسبت به ساعات را به شما نشان میدهد  \n هدف نمودار : پیدا کردن ساعت های افت و بهترین ساعات برای برگذاری چالش 🌟'



bet_Title='💰 نتایج شرط ها 💰 \n \n'
bet_Loser=lambda men , Amount:f'🔴 {men} | {Amount}🪙'
bet_Winner=lambda men , Amount:f'🟢 {men} | {Amount}🪙'



Winner_private=lambda all  , amount :f'''☆ نتیجه بت شما مشخص شد 💰
✦ نتیجه : باخت 
✦ مقدار شرط💵: {amount}
✦ سود (ضیان) : {all} لایت کوین 🪙 
'''
Loser_private=lambda all  , amount :f'''☆ نتیجه بت شما مشخص شد 💰
✦ نتیجه : باخت 
✦ مقدار شرط💵: {amount}
✦ سود (ضیان) : {all} لایت کوین 🪙 
'''
banned=lambda id : f'#اطلاعیه \n--------------------\n کاربر {id} از گپ به علت فرستادن بیش از حد پیام بن شد !'

Average_Statics=lambda AFK,Games,Player,Join_Time:f'''#میانگین
⚜️        ⚜️        ⚜️        ⚜️        ⚜️ 
            🔆 امار متنی 🔆 
             -------------

میانگین ها 〽️ :

ᴘʟᴀʏᴇʀꜱ : {Player:.1f}
ᴊᴏɪɴ ᴛɪᴍᴇ : {Join_Time}
ᴀꜰᴋ : {AFK:.3f}
ɢᴀᴍᴇ ɴᴜᴍʙᴇʀꜱ : {Games}
⚜️        ⚜️        ⚜️        ⚜️        ⚜️    
'''
jointime_xlabel='JoinTime'
jointime_ylabel='Stats'

Game_Analised=lambda Players , teams :f'''بازی انالیز شد 📜🔎\n\n
{Players}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
قدرت تیم های درون بازی 👁‍🗨 \n\n
{teams}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
- @DarkHelperChannel
'''

Who='اسم کی رو اسپم کنم ؟ '

Im_hunter='⚡️شکارم اسکی برید 💥 '

elaction_Spam=lambda name:f'''💥⚜️رای شکارچی


                    🔰  ** {name} ** 🔰 💥 '''

next_List=lambda id :[f'دلبـــــــرمون {id} اومده قفلیـــــــــارو زخــــــ😎⚔ــــم کنه','به به ببین کی نکست زده🤤💦💜',f'امیدوارم دست بعد الفا شی ',f'چه نقشی دوس داری دست بعد داشته باشی👀📿',f'نوب الدیـــــــن {id} نکست زده 😂💦 جـــون جـــون',f'پرو پلـــــــــــیرمون {id} اومــده بــــ🤤ــاه بـــــ🤤ــــاه 💦💜',f'قفلیـــــــا برید خونتــــ😎⚔ــــون سلطان {id}👑اومده',f'اوفـــــــــــــ🤤 شکــــــــ💂🏻‍♂️ــــارچی بـــازی بعدیو !']

next_setted='متن نکست گیم برای شما ثبت شد !'
how_to_set_next_frame='راهنمای ثبت نکست گیم اختصاصی 🔰 \n - در متن نکست نباید هیچ لینکی وجود داشته باشد ! \n - متن نکست را در جلوی دستور بنویسید !'

Votting=lambda nm: f'رای بر روی {nm} قرار گرفت !'

usr_unbanned=lambda id : f'کاربر {id} از گروه ان بن شد !'
usr_banned=lambda id : f'کاربر {id} از گروه بن شد !'
muted=lambda id : f'کاربر {id} میوت شد'


temp_banned=lambda id,time : f'کاربر {id} برای {time} دقیقه بن شد !'
temp_muted=lambda id,time : f'کاربر {id} برای {time} دقیقه میوت شد !'

unlock='گروه باز شد !🔓'
lock='گروه قفل شد !🔐'

exchange=lambda amount ,coins:f'مقدار {coins} لایت کوین با مبادله ی {amount} دلار به کیف پول شما اضافه شد !'
wheather=lambda dic:f'''شهر : {dic['result']["شهر"]}
---------------
    امروز 🔆
سرعت باد : {dic["result"]["سرعت باد"]}
دما : {dic["result"]["دما"]} 
وضعیت هوا : {dic["result"]["وضعیت هوا"]}
----------------
    فردا 🔆 
دما : {dic["فردا"]["دما"]} 
وضعیت هوا : {dic["فردا"]["وضعیت هوا"]}
'''
report='گزارش برای ادمین ها ارسال شد !'