from asyncio import sleep
from random import choice
async def Tag(group , bot):
    Emojies = ['🦁', '🐯', '🦊', '🦄', '🐝', '🐺', '🦋', '🐞', '🐳', '🐬', '🐼', '🦚', '🎄', '🌲', '🍄', '🍁', '🌷', '🌹', '🌺', '🌸', '🌼', '🌗', '🌓', '🪐', '💫', '⭐️', '✨', '⚡️', '🔥', '🌈', '☃️', '❄️', '🍔', '🍕', '🍓', '🍉', '🍟', '🧁', '🍰', '🍭', '🍬', '🍫', '🍿', '🍩', '🍪', '🥂', '🍸', '🍹', '🧉', '🍾', '⚽️', '🏀', '🏈', '⚾️', '🥎', '🎾', '🎖', '🎗', '🥁', '🎸', '🎺', '🎷', '🏎', '🚀', '✈️', '🚁', '🛸', '🏰', '🗼', '🎡', '🛩', '📱', '💻', '🖥', '💰', '🧨', '💣', '🪓', '💎', '⚱️', '🔮', '🩸', '🦠', '🛎', '🧸', '🎉', '💌', '📯', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕', '💞', '💝', '⚜️', '🔱', '📣', '♥️', '😍', '🥰', '🥳', '🤩', '🤪', '👾', '😻', '💋', '👑', '💍', '🎩']
    User_Ids=[int(user[0]) for user in group.All_Players ]
    tgs=''
    symbls=['★', '☆', '✡', '✦', '✧', '✩', '✪', '✫', '✬', '✭', '✮', '✯', '✰', '⁂', '⁎', '⁑', '✢', '✣', '✤', '✥', '✱', '✲', '✳', '✴', '✵', '✶', '✷', '✸', '✹', '✺', '✻', '✼', '✽', '✾', '✿', '❀', '❁', '❂', '❃', '❇', '❈', '❉', '❊', '❋', '❄', '❆', '❅', '⋆', '≛', 'ᕯ', '✲', '࿏', '꙰', '۞', '⭒', '⍟', '♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟', '♤', '♠', '♧', '♣', '♡', '♥', '♢', '♦', '☩', '☫', '☬', '☭', '☯', '☽', '☾', '✙', '✚', '✛', '✜', '✝', '✞', '✟', '†', '⊹', '‡', '♁', '♆', '❖', '♅', '✠', '✡', '✢', '卍', '卐', '〷', '☠', '☢', '☣', '☦']
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
                        tgs+=f'{symbol1}{rand}▸{i.user.mention}◂{rand}{symbol2}\n'
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
        tg+=f'⚜️ {i.user.mention}\n'
        x+=1
        if x>=8:
            await bot.send_message(group.Support , tg)
            await sleep(1)
            x=0
            tg=''
    if x!=0:await bot.send_message(group.Support , tg)
