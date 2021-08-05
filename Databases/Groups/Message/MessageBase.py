from ...MainBase import Sql_Cheak as Sql # message ( message_id  INT , group INT)')

def Add_message(Message_id :int , Chat_id : int ):
    row=Sql('insert into message (message_id,Group_id) values (:message_id,:Group_id)',
        {'message_id':int(Message_id),'Group_id':int(Chat_id)})


def Show_All_Messages():
    row=Sql('SELECT message_id,Group_id FROM message')
    rows=row
    row=Sql('DELETE FROM message ')

    return rows