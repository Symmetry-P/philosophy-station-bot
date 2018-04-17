import discord
import asyncio
import math
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
check = 'I pledge to adhere to the regulations of this server: Philosophorum Disputationibusis. In addition to that, I will also engage in intellectually stimulating philosophical discussions during my time on this server.'

@client.event
async def on_message(message):
    if message.content == check:
        await client.add_roles(message.author, discord.utils.get(message.server.roles, name='Verified'))
    
@client.event
async def on_member_join(member):
    await client.send_message(discord.utils.get(member.server.channels, name='station'), 'Welcome to the *Philosophorum Disputationibusis* Server! ' + member.mention + '\n\nRead the ' + discord.utils.get(member.server.channels, name='regulations').mention + ' and ' + discord.utils.get(member.server.channels, name='information').mention + ' channels. Once you have done so, type (or copy) `' + check + '` \n\nIn doing so you will be verified and will be able to proceed to the main area of the server.')        

client.run(os.getenv('bot_token'))
