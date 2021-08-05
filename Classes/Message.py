import sys , os
from deep_translator import GoogleTranslator
sys.path.insert(1, r'C:\Users\ASUS\Desktop\sources\Telegram\werewolf\Darkhelper\V2')
from Databases.Groups.Message import MessageBase
from Databases.Groups import GroupsBase
from Config.Texts.NFSW import NFSW
from Errors.Error import  error as Error
from Functions.Requests import NudeDet
from Functions.Pointing.Charts.Charts_AND_Draw import reqt
from Functions.Cv2.Video import Get_Frame

class Message:
    def __init__(self,message) -> None:
        self.message_id=int(message.message_id)
        self.text=str(message.text)
        self.link=str(message.text)
        self.m=message
        self.link=message

    def is_NFSW(self):
        for i in NFSW.NFSW_Texts :
            if i in self.text :
                return True
        return False

    def Add_To_24_Delete(self):
        MessageBase.Add_message(int(self.message_id))
        return True

    def __call__(self):
        msg_dict={}
        Gp_List= GroupsBase.Show_All_GroupIds()
        for Gap_ids in Gp_List: 
            msg_dict[int(Gap_ids[0])]=[]
            msg_dict[int(Gap_ids[1])]=[]
        Msg_List=MessageBase.Show_All_Messages()
        for i in Msg_List:
            msg_dict[int(i[1])].append(int(i[0]))

        return msg_dict
            #await bot.Client.delete_messages( chat_id = int(id) , message_ids = Msg_List[id] , revoke = True)

    async def is_nude(self,Path,group):
        #{'id': 'c8aef360-5cbf-4bf2-bd24-34a733c48ae0', 'output': {'detections': [{'confidence': '0.92', 'bounding_box': [84, 53, 52, 41], 'name': 'Female Breast - Exposed'},
        #  {'confidence': '0.88', 'bounding_box': [49, 90, 45, 52], 'name': 'Female Breast - Exposed'},
        #  {'confidence': '0.7', 'bounding_box': [220, 107, 61, 39], 'name': 'Male Genitalia - Exposed'}], 'nsfw_score': 0.9993282556533813}}
        Detections=(await NudeDet.Is_Nude(Path))
        if float(Detections['output']['nsfw_score']) > 0.70 :
            return Detections
        FILTERS=group.Porn_All_Filters
        for det in Detections['output']['detections']:
            for i in NFSW.Porn :
                if FILTERS[i] :
                    if NFSW.Porn[i] in det['name'] or NFSW.Porn[i] == det['name']:
                        return Detections
                
    async def Lock_Nude(self,group):
        PT=None
        Path=(await self.m.download())
        if self.m.sticker or  self.m.photo:
            Path=(await self.m.download())
        else:
            PT=(Get_Frame(Path))
            Path=PT[0]
        res=(await self.is_nude(Path,group))
        if res!=None and res!=False :
            await self.m.delete()
            Path=reqt(res, Path)
            text='{}\n'
            translated = GoogleTranslator(source='en', target='fa')#.translate(text='hi')
            for i in res['output']['detections']:
                text+=f"{translated.translate(i['name'])}\n"
            try:os.remove(PT[0])
            except:pass
            return [Path,text,res['id']]
        else:
            if PT:
                Path=PT[1]
                res2=(await self.is_nude(Path,group))
                if res2!=None and res2!=False :
                    await self.m.delete()
                    try:
                        Path=reqt(res2, Path)
                        text='{}\n'
                        translated = GoogleTranslator(source='en', target='fa')#.translate(text='hi')
                        for i in res2['output']['detections']:
                            text+=f"{translated.translate(i['name'])}\n"
                        os.remove(PT[1])
                        return [Path,text,res2['id']]
                    except:pass
                else:
                    try:os.remove(PT[1])
                    except:pass
                    return False
            else:return False

    async def Auto_Lock(self , Group , User , message):
        try:
            if Group.Anti_NFSW:
                try:
                    if self.is_NFSW():
                        return 'NFSW'
                except Exception as e:
                    Error(f'{e} Classes-Message-42')

            if Group.Channel_Lock:
                try:
                    if Group.Show_Channel :
                        if not User.Joined_Channel :
                            return True
                except Exception as e:
                    Error(f'{e} Classes-Message-51')

            if Group.Voice_Lock:
                try:
                    if self.m.voice :
        
                        return True
                except Exception as e:
                    Error(f'{e} Classes-Message-59')

            if Group.Sticker_Lock:
                try:
                    if self.m.sticker :
        
                        return True
                except Exception as e:
                    Error(f'{e} Classes-Message-67')

            if Group.Photo_Lock:
                try:
                    if self.m.photo :
        
                        return True
                except Exception as e:
                    Error(f'{e} Classes-Message-75')

            if Group.Link_Lock:
                try:
                    for i in self.m.entities:
                        if str(i.type) in ['url','text_link']:return True
                except Exception as e:
                    Error(f'{e} Classes-Message-83')

            if Group.Forward_Lock:
                try:
                    if self.m.forward_sender_name or self.m.forward_signature  or  self.m.forward_date   :return True
                except Exception as e:
                    Error(f'{e} Classes-Message-91')

            if Group.Video_Lock:
                try:
                    if self.m.video  or self.m.video_note  :return True
                except Exception as e:
                    Error(f'{e} Classes-Message-99')

            if Group.Service_Lock:
                try:
                    if self.m.service  :
                        return True
                except Exception as e:
                    Error(f'{e} Classes-Message-107')

            if User.is_Muted(Group.chat_id):
                try:
                    return True
                except Exception as e:
                    Error(f'{e} Classes-Message-115')

            if Group.Message_State :
                if not (await User.is_State_Enough(Group)):
                    try:
                        return True
                    except Exception as e:
                        Error(f'{e} Classes-Message-123')
            if Group.Players_Lock_Only:
                try:
                    if int(User) in Group.Show_Players :pass
                    else:return True
                except Exception as e:
                    Error(f'{e} Classes-Message-183')
            return False
        except Exception as e:
            Error(e)


                    