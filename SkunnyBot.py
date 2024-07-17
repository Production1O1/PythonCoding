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

