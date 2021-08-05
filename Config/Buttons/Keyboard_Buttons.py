from pyrogram import Client,filters                          #-| Creating Client
api_id =2586462                                              #-|
api_hash = '68542129131999986899b84a10a6170c'                #-|
bot = Client('amirairj-helper', api_id, api_hash,workers=300)#-|
#--------------------------------------------------------------|Starting Database Tabales Creation
from Databases import MainBase                               #-|
MainBase.start()                                             #-|
#--------------------------------------------------------------|
