import datetime
def error(e):
    with open('errors.txt','a+') as f :
            f.write(f'{e} \n')

def Start_Error():
    Date=str((datetime.date.today()).strftime('%Y-%m-%d-%H:%M:%S'))
    with open('errors.txt','w') as f :
            f.write(f'Dark_helper Has Runned {Date} \n')