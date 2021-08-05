#--------------------------------------------------------------------------|Variebels For Api
api_id =5015063                                                          #-|
api_hash = '729213381bf743aec50971fa07a62264'                            #-|
bot_id= 1753769751                                                       #-|
#--------------------------------------------------------------------------| » Creating Client & Import Pyrogram
from pyrogram import Client                                              #-|                          
bot = Client('amirairj-partner', api_id, api_hash,                       #-|
workers=300,workdir =r'/root/helper/Dark_Helper/Config/Info/bot')        #-|
del  api_hash , api_id                                                   #-|
#--------------------------------------------------------------------------|