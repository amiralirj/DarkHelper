#--------------------------------------------------------------------------|Variebels For Api
api_id =5015063                                                          #-|
api_hash = '729213381bf743aec50971fa07a62264'                            #-|
bot_id= 1658760514                                                       #-|
bot_username='@Darkhelperrobot'#@darkhelperrobot'                        #-|
#--------------------------------------------------------------------------| » Creating Client & Import Pyrogram
from pyrogram import Client                                              #-|                          
bot = Client('amirairj-helper', api_id, api_hash                         #-|  
,workers=300,workdir =r'/root/helper/crused/V2/Config/Info/bot')         #-|
del  api_hash , api_id                                                   #-|
#--------------------------------------------------------------------------|