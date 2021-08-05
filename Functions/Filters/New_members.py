from datetime import datetime
from Config.Buttons import Inline_Buttons 

async def New_Member_State(Group,user):
    permission=False
    now=datetime.now()
    if Group.State_Lock:
        if now.hour < 10 :
            permission=True
    else:
        permission=True

    if permission:
        if not (await user.is_State_Enough(Group)):
            return True
    return False
            
async def Welcome(group,user,usr,Chat_title,ment):
    if group.Show_Welcome  :
        state=(await user.State)
        WLC=str(str(group.Welcome).replace('{name}',ment).replace('{werewolf}',str(state[2])).replace('{onyx}',str(state[0])).replace('{black}',str(state[1])).replace('{title}',str(Chat_title)))
        group.Show_Channel
        if group.Show_Channel:
            reply=Inline_Buttons.Channel_Text(group.Channel_Text , group.Channel )
        else:
            reply= None
        return [WLC , reply]
    else: return [None,None]

def Locks(group , usr , Full_Name ,is_bot):
    li=[]
    if group.Anti_Tabchi:
        if usr.is_tabchi(Full_Name):
            li.append(True)
        else:
            li.append(False)
    else:
        li.append(False)

    if group.Anti_Robot:
        if is_bot :
            li.append(True)
        else:
            li.append(False)
    else:
        li.append(False)
        
    return li
