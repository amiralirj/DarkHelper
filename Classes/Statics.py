import datetime
class Statics:
    def __init__( self , List ) -> None:
        self.list=List
    

    def Filter_Newer(self,Date):
        Newer=[]
        for i in self.list :
            another_day = datetime.datetime.now().strptime(Date,"%Y-%m-%d")
            Day = datetime.datetime.now().strptime(i[4],"%Y-%m-%d")
            if Day > another_day:
                Newer.append(i)
        return Newer


    def Filter_Older(self , Date):
        Older=[]
        for i in self.list :
            another_day = datetime.datetime.now().strptime(Date,"%Y-%m-%d")
            Day = datetime.datetime.now().strptime(i[4],"%Y-%m-%d")
            if Day < another_day:
                Older.append(i)
        return Older

    def Filter_Date(self,Date,index=4):
        li=[]
        Dt=(datetime.datetime.now() + datetime.timedelta(days=Date))
        for i in self.list :
            print('------------------------------------')
            print(Dt)
            Day = datetime.datetime.now().strptime(i[index],"%Y-%m-%d")
            print(Day)
            if Day > Dt:
                li.append(i)
        return li
    
    @property
    def Point(self):
        # time,players,hour,afk,date
        Main_Point=0
        for i in self.list :
            join_time=self.Join_Time_All
            Join_Sec=int( join_time[0] + (join_time[1] * 60) )
            Join_Time_Point=Join_Sec ** (1/3)
            #---------------------------------------------------
            Players=int(i[1])
            Players_Point=Players ** (5/3)
            #---------------------------------------------------
            Afk=int(i[3])
            AFK_Point=((Afk)** 3 )
            #---------------------------------------------------
            Main_Point+=(
                (Players_Point / Join_Time_Point ) - AFK_Point
            )
        return Main_Point
        
    @property
    def AFK(self):
        AFKS=0
        for i in self.list:
            AFKS+=int(i[3])
        return AFKS

    @property
    def Players(self):
        PLAYERS=0
        for i in self.list:
            PLAYERS+=int(i[1])
        return PLAYERS

    @property
    def Join_Time(self):
        JOIN_TIME=0
        for i in self.list:
            join_time=str(i[0]).split(':')
            Join_Sec=int(int(join_time[-2] * 60) + int(join_time[-1]))
            if Join_Sec<10000:
                JOIN_TIME +=int(Join_Sec)
        return JOIN_TIME

    @property
    def Join_Time_All(self):
        JOIN_TIME=0
        JOINTIME_MIN=0
        for i in self.list:
            join_time=str(i[0]).split(':')
            Join_Sec=int(join_time[-1])
            join_min=int(join_time[-2])
            if join_min<30:
                JOIN_TIME +=int(Join_Sec)
                JOINTIME_MIN+=int(join_min)
        return [JOIN_TIME,JOINTIME_MIN]

    @property
    def Join_Time_List(self):
        JOIN_TIME=[]
        for i in self.list:
            join_time=str(i[0]).split(':')
            Join_Sec=int(join_time[-2]* 60) + int(join_time[-1])
            if Join_Sec<100000:
                JOIN_TIME.append(Join_Sec)
        return JOIN_TIME

    @property
    def Games_Num(self):
        return len(self.list)



#{1437765068: {'win': True, 'point': 35, 'alive': False, 'naghsh': '🌀', 'team': 'روستا👨🏻'}, 1593578569: {'win': True, 'point': 15, 'alive': False, 'naghsh': '??', 'team': '?'}, 1687856345: {'win': False, 'point': 25, 'alive': False, 'naghsh': '👤', 'team': 'فرقه👤'}, 1409846062: {'win': False, 'point': 70, 'alive': False, 'naghsh': '🐶', 'team': 'گرگ 🐺'}, 1636939130: {'win': True, 'point': 30, 'alive': False, 'naghsh': '🍵', 'team': 'گرگ 🐺'}, 1833028431: {'win': False, 'point': 55, 'alive': False, 'naghsh': '🐺', 'team': 'گرگ 🐺'}, 1400347694: {'win': False, 'point': 80, 'alive': False, 'naghsh': '🏹', 'team': 'قاتل 🔪'}, 387483042: {'win': False, 'point': 35, 'alive': False, 'naghsh': '💋', 'team': 'روستا👨🏻'}, 1255626997: {'win': False, 'point': 15, 'alive': False, 'naghsh': '??', 'team': '?'}, 708476833: {'win': False, 'point': 15, 'alive': False, 'naghsh': '??', 'team': '?'}, 1217847024: {'win': False, 'point': 25, 'alive': False, 'naghsh': '🧙🏻\u200d♂️', 'team': 'گرگ 🐺'}, 116291120: {'win': False, 'point': 25, 'alive': False, 'naghsh': '👶🏻', 'team': 'گرگ 🐺'}, 691943577: {'win': True, 'point': 10, 'alive': False, 'naghsh': '⚒', 'team': 'روستا👨🏻'}, 949703124: {'win': False, 'point': 70, 'alive': False, 'naghsh': '🐶', 'team': 'گرگ 🐺'}, 1703924675: {'win': True, 'point': 20, 'alive': True, 'naghsh': '📚', 'team': 'روستا👨🏻'}, 1765989432: {'win': True, 'point': 15, 'alive': True, 'naghsh': '??', 'team': '?'}, 1523061357: {'win': True, 'point': 40, 'alive': True, 'naghsh': '🔫', 'team': 'روستا👨🏻'}, 1419587011: {'win': True, 'point': 15, 'alive': True, 'naghsh': '??', 'team': '?'}}
