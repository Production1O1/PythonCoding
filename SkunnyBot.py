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
