import discord
import ssl
import json
import connectToSCPI

sslcontext = ssl.create_default_context()
sslcontext.check_hostname = False
sslcontext.verify_mode = ssl.CERT_NONE

intents = discord.Intents.all()

client = discord.Client(intents=intents, ssl=sslcontext)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # replace CHANNEL_ID with the ID of the channel you want to listen to
    if 'chatgpt' in message.content.lower():
        #debug
        print(message.content.lower()) 
        
        SCPIResponse = connectToSCPI.sendtoSCPI(message)
        
        #parse the SCPI response for actual result
        response_json = json.load(SCPIResponse)
        response = response_json['status']
        await message.channel.send(response)



#------- Read setting for discord ID's --------------

with open('setting.json', "r") as jsonfile:
        settings = json.load(jsonfile)

discord_setup = settings['discord_setup']        
        
#socket = discord.SocketConnector(ssl=sslcontext)        
client.run(discord_setup)
client.run(discord_setup, ssl=sslcontext)
