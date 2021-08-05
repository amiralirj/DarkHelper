from ...MainBase import Sql_Fun as Sql


def Start_Group_Bet(user_id,amount,team,zarib,main):
    row=Sql('insert into bet (user_id,amount,active,win,team,zarib,main) values (:user_id,:amount,:active,:win,:team,:zarib,:main)',
    {'user_id':int(user_id),'amount':int(amount),'active':1,'win':3,'team':int(team),'zarib':float(zarib),'main':int(main)})


def bet_active_cheak(user_id,main,amount):
    row=Sql(f'SELECT active FROM bet WHERE main=:main AND user_id=:user_id',{'main':int(main),'user_id':int(user_id)})
    q=row
    if q[0][0]==1:
        return True
    else:
        False

def End_Group_bet(main):
    Sql(f"update bet set active =:act where main =:id AND active=1 ",{'id':int(main),'act':0})  

def Get_User_History(user_id):
    row=Sql('SELECT amount,zarib FROM bet WHERE win=1 AND user_id=:user  ',{'user':int(user_id)})
    wins=row
    amount_win=0
    times=0
    for t in wins:
        amount_win+=int(float(t[0])*float(t[1]))-float(t[0])
        times+=1
    row=Sql('SELECT amount,zarib FROM bet WHERE win=0 AND user_id=:user  ',{'user':int(user_id)})
    lose=row
    amount_lose=0
    times_lose=0
    for i in lose:
        amount_lose+=int(float(i[0])*float(i[1]))-float(i[0])
        times_lose+=1
    sood=amount_win-amount_lose
    text=f"امار شرط های شما ⚜️ \n \n برد ها {times} 🟢 \n مقدار کل برد ها {amount_win}  🪙  \n \n تعداد باخت ها {times_lose} 🔴 \n مقدار کل باخت ها {amount_lose} 🪙 \n \n سود /ضرر : {sood} \n 👁‍🗨👁‍🗨"
    return text

def back_None():
    row=Sql('SELECT user_id,amount FROM bet WHERE win=3')
    q=row
    b=0
    for i in q:
        b+=int(i[1])
    row=Sql(f"update bet set win =1,active=0 where win=3 ")  
    return row

def win(team,main):
    row=Sql(f'SELECT user_id,amount,zarib FROM bet WHERE team=:team AND main=:main AND active=1',{'main':int(main),'team':int(team)})
    winners=row
    all_bets=[[],[]]
    for i in winners:
        try:
            row=Sql(f"update bet set win=1 where main =:id AND user_id=:user ",{'id':int(main),'user':int(i[0])})
        except:
            pass
        try:
            all_bets[0].append((i[0], i[1], i[2]))
        except:
            pass
    row=Sql(f'SELECT user_id,amount,zarib FROM bet WHERE NOT team=:team AND main=:main AND active=1',{'main':int(main),'team':int(team)})
    losers=row
    for i in losers:
        try:
            row=Sql(f"update bet set win =0 where main =:id AND user_id=:user ",{'id':int(main),'user':int(i[0])})
        except:
            pass
        try:
            all_bets[1].append((i[0], i[1], i[2]))
        except:
            pass
    row=Sql(f"update bet set active =:act where main =:id ",{'id':int(main),'act':0})  
    return all_bets
