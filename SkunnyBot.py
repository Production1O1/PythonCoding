#!/usr/bin/python3
print("SKUNNY:D")

# bot.py
import sys
from operator import truediv
import os
import discord
from discord import embeds
from discord_components import DiscordComponents, Button, Select, SelectOption
from discord import member
from discord import message
#from dotenv import load_dotenv
from discord.ext import commands
import discord
from io import BytesIO
from usefull.rickroll import *
import json
import random
#from utils.useful import Embed
import DiscordUtils
#from keep_alive import keep_alive
from discord.ext.commands import *
import json
import asyncio
from discord import Permissions
from datetime import *
#from prsaw import RandomStuff
#import prsaw


from discord import Color, Embed
import sys
import typing
import traceback

import requests
import math
import re
import aiosqlite
from PIL import Image
import asyncpraw
import tracemalloc
tracemalloc.start()
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import find
from discord.voice_client import VoiceClient
import youtube_dl
import aiohttp
import urllib.parse


#import disbotlist

#from disbotlist.py import *


#from discord_slash import SlashCommand, SlashContext

#my_secret = os.environ['TOKEN']
#TOKEN=''
def get_prefix(bot,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    try:
        return prefixes[str(message.guild.id)]
    except KeyError:
      return "+"
TOKEN='secret'


class MyBot(commands.Bot):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)



    async def on_ready(self):
        """Called upon the READY event"""
        print("Bot is ready.")
        DiscordComponents(bot)
        global detector
        detector = RickRollDetector()




intents=discord.Intents.default()
bot = MyBot(command_prefix=get_prefix,intents=intents,case_insensitive=True)
#slash = SlashCommand(bot)
bot.remove_command("help")

with open ("data.json", "r") as f:
    data = json.load(f)
    token = data["token"]
    db_pswd = data["db_pwd"]

@bot.command(description="Current version")
async def version(ctx):

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
   
    
    embed.set_author(name='**Update log**!')
    embed.add_field(name='1.81', value='Added +daily and +lbg minor bug fixes and patches.', inline=False)
    embed.add_field(name='1.8', value=' Added economy system, ticket system, Ai chatbot, 2 more commands and bug fixes since update 1.3!')
    embed.add_field(name='1.7', value=' Added 20 more commands and a new error handler for +kick. Cooldown on commands also added!')
    embed.add_field(name='1.6', value=' Reramped help command and added embeds to some commands')
    embed.add_field(name='1.5', value=' Made the bot run 24/7!')
    embed.add_field(name='1.4', value=' Just added 10 commands and specific command reactions')
    embed.add_field(name='1.3', value=' Fixed a major bug in most moderation commands and added some other stuff to the bot')
    embed.add_field(name='1.2', value=' Added Moderation commands')
    embed.add_field(name='1.1', value=' **nothing added idk why i even called it a update**')
    embed.add_field(name='1.0', value=' Bot got realeased into the public')
    embed.add_field(name='0.1', value=' Added one command. Just **one**')
    embed.add_field(name='0.5', value=' Added like 20 commands.')
    await ctx.send(embed = embed)


    print("context",ctx)
#dbl = disbotlist(bot,"secret")
@bot.command()
async def botserver(ctx):
  await ctx.send(f"I'm in {len(bot.guilds)} servers!")
#@bot.event
#async def on_command_error(ctx, error):
 # if isinstance(error, commands.CommandOnCooldown):
  #  msg = '**Command is still on cooldown**, try again in {:.2f} hours'.format(error.retry_after)


@bot.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    

    await ctx.send(f"The prefix was changed to {prefix}")




@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Error 404')
        embed.add_field(name='||The commands not even a command. +help exists for a reason||',value="...")
        embed.set_footer(text ='404')
        await ctx.send(embed=embed)

    elif isinstance(error, commands.TooManyArguments):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Too many letters/char')
        embed.add_field(name='The command you did had more then 256 letters/char discord limit is 256 thats why command did not work',value="...")
        embed.set_footer(text ='Too many arguements')
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        msg = '**Command is still on cooldown**, try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)

    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Permissions error')
        embed.add_field(name='Imagine thinking you can just get away with doing a perms needed command with no perms',value='...')
        embed.set_footer(text ='Why did you think you could do that.')
        await ctx.send(embed=embed)

        message = "You are missing the required permissions to run this command!"
    elif isinstance(error, commands.UserInputError):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Input error')
        embed.add_field(name='Something about your input was wrong.. just check your input and try again, You may have forgot to add a other arg, ex: +bet instead of +bet 59',value='...')
        embed.set_footer(text ='Imagine getting a error msg')
        await ctx.send(embed=embed)
    elif isinstance(error,commands.NotOwner):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Why just why...')
        embed.add_field(name='||You did a bot dev only command and thought it could work?||',value='...')
        embed.set_footer(text ='Why did you think you could do that.')
        await ctx.send(embed=embed)
    elif isinstance(error,commands.BotMissingPermissions):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Missing Bot perms')
        embed.add_field(name='StonkBot is missing the required permissions for the command to work, give it the proper perms or admin',value='...')
        embed.set_footer(text ='Did you forget to add the bot some perms?')
        await ctx.send(embed=embed)

    elif isinstance(error,commands.MissingRequiredArgument):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Missing arguement')
        embed.add_field(name='You forgot to add a arguement',value='...')
        embed.set_footer(text ='Hello fellow humans')
        await ctx.send(embed=embed)

    elif isinstance(error,commands.BadArgument):
        embed = discord.Embed(colour = discord.Colour.random())
        embed.set_author(name='Missing arguement')
        embed.add_field(name='You forgot to add a arguement',value='...')
        embed.set_footer(text ='Hello fellow humans')
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(colour = discord.Colour.random())
        embed.add_field(name='You managed to get a error I didnt even expect..',value='...')
        embed.set_footer(text ='how did you do it?')
        await ctx.send(embed=embed)
        raise error

@bot.command()
async def invite(ctx):
  embed = discord.Embed(
    colour = discord.Colour.red()
  )
  embed.set_author(name='Invite')
  embed.add_field(name='▼▼▼▼', value='[Bot invite](https://bit.ly/3tw374r)')
  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text ='Stop it, get some help.')
  await ctx.send(embed=embed)











#@slash.slash(name="test",
 #            description="This is just a test command, nothing more.")
#async def test(ctx):
 # await ctx.send(content="Hello World!")
async def ch_pr():
    await bot.wait_until_ready()
    statuses=[f'{len(bot.guilds)} servers','Stonks|+help','Doge coin', 'mass murders',]
    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(10)
bot.loop.create_task(ch_pr())


# @bot.command()
# async def stats(self, ctx):
#         embed = discord.Embed(title = f"{self.bot.user.name}'s botinfo.",  color = discord.Colour.dark_green())
#         ramUsage = self.process.memory_full_info().rss / 1024**2
#         embed.add_field(name="• Name:", value=f"`{self.bot.user}`",inline=True)
#         embed.add_field(name="• Id", value=f"`829836500970504213`")
#         embed.add_field(name="• Intents", value=f"`{self.bot.intents}`")
#         embed.add_field(name="• Python Version", value=f"`{platform.__version__}`")
#         embed.add_field(name="• Discord.py Version", value=f"`{discord.__version__}`")
#         embed.add_field(name="• Total Servers", value=f"`{len(self.bot.guilds)}`")
#         embed.add_field(name="• Total Members", value=f"`{len(self.bot.users)}`")
#         embed.add_field(name="• Total Commands", value=f"`{len(set(self.bot.commands))}`")
#         embed.add_field(name="• Total Cogs", value=f"`{len(set(self.bot.cogs))}`")
#         embed.add_field(name="• RAM", value=f"`{ramUsage:.2f} MB`")
#         embed.set_footer(text = f"Requested by {ctx.author})", icon_url = ctx.author.avatar_url)
#         await ctx.send(embed = embed)
