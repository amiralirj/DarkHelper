from asyncio import sleep
from random import choice
async def Tag(group , bot):
    Emojies = ['ðĶ', 'ðŊ', 'ðĶ', 'ðĶ', 'ð', 'ðš', 'ðĶ', 'ð', 'ðģ', 'ðŽ', 'ðž', 'ðĶ', 'ð', 'ðē', 'ð', 'ð', 'ð·', 'ðđ', 'ðš', 'ðļ', 'ðž', 'ð', 'ð', 'ðŠ', 'ðŦ', 'â­ïļ', 'âĻ', 'âĄïļ', 'ðĨ', 'ð', 'âïļ', 'âïļ', 'ð', 'ð', 'ð', 'ð', 'ð', 'ð§', 'ð°', 'ð­', 'ðŽ', 'ðŦ', 'ðŋ', 'ðĐ', 'ðŠ', 'ðĨ', 'ðļ', 'ðđ', 'ð§', 'ðū', 'â―ïļ', 'ð', 'ð', 'âūïļ', 'ðĨ', 'ðū', 'ð', 'ð', 'ðĨ', 'ðļ', 'ðš', 'ð·', 'ð', 'ð', 'âïļ', 'ð', 'ðļ', 'ð°', 'ðž', 'ðĄ', 'ðĐ', 'ðą', 'ðŧ', 'ðĨ', 'ð°', 'ð§Ļ', 'ðĢ', 'ðŠ', 'ð', 'âąïļ', 'ðŪ', 'ðĐļ', 'ðĶ ', 'ð', 'ð§ļ', 'ð', 'ð', 'ðŊ', 'âĪïļ', 'ð§Ą', 'ð', 'ð', 'ð', 'ð', 'ðĪ', 'ðĪ', 'ðĪ', 'âĢïļ', 'ð', 'ð', 'ð', 'âïļ', 'ðą', 'ðĢ', 'âĨïļ', 'ð', 'ðĨ°', 'ðĨģ', 'ðĪĐ', 'ðĪŠ', 'ðū', 'ðŧ', 'ð', 'ð', 'ð', 'ðĐ']
    User_Ids=[int(user[0]) for user in group.All_Players ]
    tgs=''
    symbls=['â', 'â', 'âĄ', 'âĶ', 'â§', 'âĐ', 'âŠ', 'âŦ', 'âŽ', 'â­', 'âŪ', 'âŊ', 'â°', 'â', 'â', 'â', 'âĒ', 'âĢ', 'âĪ', 'âĨ', 'âą', 'âē', 'âģ', 'âī', 'âĩ', 'âķ', 'â·', 'âļ', 'âđ', 'âš', 'âŧ', 'âž', 'â―', 'âū', 'âŋ', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'áŊ', 'âē', 'āŋ', 'ę°', 'Û', 'â­', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'âĪ', 'â ', 'â§', 'âĢ', 'âĄ', 'âĨ', 'âĒ', 'âĶ', 'âĐ', 'âŦ', 'âŽ', 'â­', 'âŊ', 'â―', 'âū', 'â', 'â', 'â', 'â', 'â', 'â', 'â', 'â ', 'âđ', 'âĄ', 'â', 'â', 'â', 'â', 'â ', 'âĄ', 'âĒ', 'å', 'å', 'ã·', 'â ', 'âĒ', 'âĢ', 'âĶ']
    x=0
    symbol1=choice(symbls)
    symbol2=choice(symbls)
    rand=choice(Emojies)
    group.Tag_Started()
    print(f'{group.Show_Istagging}-------------{group.Show_JoinTime}')
    if  bool(group.Show_Istagging) :
        async for i in bot.iter_chat_members(group.Main , limit=1500):
            if bool(group.Show_Istagging) :
                if bool(group.Show_JoinTime):
                    if int(i.user.id) in User_Ids and not i.user.is_bot  and not i.user.is_deleted :
                        tgs+=f'{symbol1}{rand}âļ{i.user.mention}â{rand}{symbol2}\n'
                        x+=1
                        if x>=5:
                            await bot.send_message(group.Main , tgs)
                            x=0
                            symbol1=choice(symbls)
                            symbol2=choice(symbls)
                            rand=choice(Emojies)
                            tgs=''
                            await sleep(3)
                else:
                    group.Tag_Stopped()
                    print('this an')
                    return
            else:
                group.Tag_Stopped()
                print('this kir')
                return
        group.Tag_Stopped()



async def Support_tag(bot,group):
    tg=''
    x=0
    async for i in bot.iter_chat_members(group.Support , limit=50):
        tg+=f'âïļ {i.user.mention}\n'
        x+=1
        if x>=8:
            await bot.send_message(group.Support , tg)
            await sleep(1)
            x=0
            tg=''
    if x!=0:await bot.send_message(group.Support , tg)
