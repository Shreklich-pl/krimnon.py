# bot.py
import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands
from datetime import date

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')
today = date.today()
autorole = [] 
autorolerole = [] 

@bot.event
async def on_member_join(member):
    await member.edit(nick = member.display_name + ' ' + today.strftime("%d/%m"))

@bot.command(name='hejo')
async def hejo(message):
    response = 'Witam'
    await message.send(response)
    await bot.process_commands(message)

@bot.command(name='r')
async def roll(ctx, number_of_dices: int, sides: int):
    dice = [] * number_of_dices
    for i in range(number_of_dices):
        result = random.choice(range(1, sides + 1))
        dice.append(result) 
    await ctx.send(dice)     

@bot.event
async def on_message(message):
    if message.content == 'Dobry konik':
      await  message.channel.send('Ihahahahahaha')
    await bot.process_commands(message)

@bot.command(name='autorole')
async def sdsdsd(something, emoji, role: int, back: int):
    global autorole
    global autorolerole
    
    if back == 0:
        await  something.message.add_reaction(emoji)
        autorole.append(something.id)
        autorolerole.append(role)
    else:
        channel = something.channel
        messages = []
        await something.message.delete()
        messages = await channel.history(limit=back).flatten()
        await  messages[back-1].add_reaction(emoji)
        autorole.append(messages[back-1].id)
        autorolerole.append(role)
        

        
        
@bot.event
async def on_raw_reaction_add(payload):
    count = 0
    
    for guildserver in bot.guilds:
        if guildserver.name == GUILD:
            break
            
    for member in guildserver.members:
        if member.id == payload.user_id:
            break
        
    for dddd in autorole:
        if dddd == payload.message_id:
            role = guildserver.get_role(autorolerole[count])
            await member.add_roles(role, reason='None', atomic=True)
            break
        else:
            count = count+1


bot.run(TOKEN)

