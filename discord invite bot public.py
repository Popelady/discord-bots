import discord
from discord.ext import commands
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    for guild in client.guilds:
        print(guild.id)
        g=guild.id
        
@client.event
async def get_channel(ctx):
    channel = discord.utils.get(ctx.guild.channels, name='channel name')
    print(channel.id)   

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$singleUseInvite'):
        number_of_links = message.content[-1]
        await message.channel.send (number_of_links)
        f = 1
    while f < int(number_of_links):
        print('CREATING INVITES')
        for i in range(int(number_of_links)): # Create as many links as needed
            i = await message.channel.create_invite(max_uses=1, max_age=0, unique=True) # Create the invite link
            j="`" + str(i) + "`"
            await message.channel.send(j)
            
        break

#    print('Finished. Exiting soon...')
    
#    exit() #unhash this to have the program quit

client.run('put token here leaving in the little dashes')
