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







@bot.command(pass_context=True)
async def afg(ctx,role: discord.Role, user: discord.Member):
  await user.add_roles(role)
  await ctx.send("f")















#@bot.command()
#async def meme(ctx):
 #   async with aiohttp.BotSession() as cs:
  #    async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=top') or cs.get('https://www.reddit.com/r/memes/new.json?sort=top') or cs.get('https://www.reddit.com/r/programmingmemes/new.json?sort=top') or cs.get('https://www.reddit.com/r/cleanmemes/new.json?sort=top') as r:
   #     res = await r.json()

    #num = random.randint(0, len(res['data']['children'])-1)

    #m = res['data']['children'] [num]['data']['url']
    #e = Embed(description = f"**[{res['data']['children'] [num]['data']['title']}]({m})**", color=amberz)
   # e.set_footer(text= res['data']['children'] [num]['data']['author'], icon_url=ctx.guild.icon_url)
    #e.set_image(url = res['data']['children'] [num]['data']['url'])
   # await ctx.send(embed=e)









#--------------REDDIT MEME GENERATION!----------------
# wont work



#reddit = asyncpraw.Reddit(client_id ='OK4gxau76j-sPw',
#client_secret ='QqSS9K4UN9KFItLXFxJWRxBZ1GRsMQ', user_agent = 'praw', username ='Dragonroyal', password = 'savecup11',)

#subreddit = reddit.subreddit('memes')
#top = subreddit.top(Limit = 5)
#for submisson  in top:
#  print(submission.title)

#print("F")
#@bot.command()
#async def memeswork(ctx):
 # print("Ff")
  #subreddit = reddit.subreddit('memes')
  #top = subreddit.top(Limit = 50)
  #all_subs =[]
  #for submission in top:
   # all_subs.append(submission)
    #print("FFf")

  #random_sub = random.choice(all_subs)
  #print("fffds")
  #name = random_sub.title
  #url = random_sub.url
  #em = discord.Embed(title=name)
  #em.set_image(url=url)
  #print("ejksjs")
  #await ctx.send(embed = em)


#@bot.command()
#async def memef(ctx):
 #   memes_submissions = reddit.subreddit('memes').hot()
  #  post_to_pick = random.randint(1, 10)
  #  for i in range(0, post_to_pick):
  #      submission = next(x for x in memes_submissions if not x.stickied)

   # await bot.say(submission.url)



#who is command
@bot.command(aliases=["user","info"])
async def whois(ctx, member:discord.Member=None):

    if member is None:
        member = ctx.author
    user = member
    roles = [role for role in member.roles]
    allroles = [role.mention for role in roles[1:]]
    embed = discord.Embed(title = member.name , describtion = member.mention ,color = discord.Color(0x7289DA))
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name = "ID", value = member.id , inline = True)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=f"Roles (amount: {len(roles)}):", value="\n".join(allroles))
    embed.add_field(name="Highest Role:", value=f"{member.top_role.mention if member.top_role else 'N/A'}")
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text =   f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)




@bot.command()
async def botservers(ctx):
    await ctx.send("I'm in " + str(len(bot.guilds)) + " servers!")





@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def stonkrules(ctx):
  embed = discord.Embed(color = discord.Color(0x36393E))
  embed.set_author(name='Rules📓')
  embed.add_field(name='1.', value=' Please dont talk about religion or politics. People can be really sensitive about this stuff, so dont do it here, thanks!')
  embed.add_field(name='2.', value='No NSFW, sexist, racist, homophobic, transphobic, misogynistic or inappropriate content or anything remotely similar. Respect people, its the 21st century. This includes any slurs.')
  embed.add_field(name='3.', value='Causing drama is an instant punishment. Its simple, please dont.',)
  embed.add_field(name='6', value='Attempting to override a punishment or using alternate accounts will lead to all your accounts being banned. This includes leaving to bypass a mute.',)
  embed.add_field(name='7', value='Please keep discussion in English only. This includes voice chats.',)
  embed.add_field(name='8', value='Dont spam or use copy pastes here. Theyre not nice and make chat hard to manage.')
  embed.add_field(name='9', value='Dont Adv in wrong channels. Anything considered Adv is links that are unrelated to the convo topic and are meant to promote the users content, in short just try not to post any links',)
  embed.add_field(name='10', value='Common sense. Use common sense')
  embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1149577551708184576/6KG41LLu_400x400.jpg")
  embed.set_footer(text="Imagine not voting for this bot in top.gg")
  await ctx.send(embed=embed)

# async def on_message(message):
#   if bot.user == message.author:
#     return
#   if message.channel.id == 842336034431827988:
#     msg = message.content
#     key = os.getenv('key')
#     header = {"x-api-key": key}
#     dev_name = "ChaoticNebula"
#     type = "stable"
#     params = {'type':type , 'message':msg, 'dev_name': "ChaoticNebula", 'bot_name': "Ai Chat"}
#     async with aiohttp.ClientSession(headers=header) as session:
#       async with session.get(f'https://api.pgamerx.com/v3/ai/response', params=params) as resp:
#         text = await resp.json()
#         await message.channel.send(text[0]["message"])
#   else:
#     pass


#test
#if this works then WOW



@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}! My prefix is + Do +help to learn more about my commands. To setup my chatbot name a channel chatbot for chatbot to work'.format(guild.name))




# #supergoodchatbotbutnoembed
@bot.event
async def on_message(message):
    mention = f'<@!{bot.user.id}>'
    if mention in message.content:
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        try:
            a=prefixes[str(message.guild.id)]
        except KeyError:
            a="+"    
            em = discord.Embed(title=a,color=discord.Color.random())
            em.set_author(name='Incase you dont know my prefix its')
            await message.channel.send(embed=em)
        await bot.process_commands(message)
    if bot.user == message.author:
      return



    else:
        if message.channel.name == 'chatbot' or message.channel.name =='⭐・chat・bot' or message.channel.name =='ai':
            msg = message.content
            key = 'hNU9gUhSU5t8'
            header = {"x-api-key": key}
            type = "stable"

            params = {'type':type , 'message':msg, 'dev_name': "DragonRoyal", 'bot_name': "Stonk Bot"}
            async with aiohttp.ClientSession(headers=header) as session:
                async with session.get(f'https://api.pgamerx.com/v3/ai/response', params=params) as resp:

                    text = await resp.json()
                em = discord.Embed(title = text[0]["message"], color= discord.Color.random())
                em.set_footer(icon_url = message.author.avatar_url,text = f"Said to: {message.author.name}. Consider doing +vote")
                await bot.process_commands(message)
                await message.reply(embed = em)
        else:
            for i in message.content.split(" "):
                i = i.replace("<","").replace(">", "") #Removes <> that could be used to hide embeds
                if "https://" in i and await detector.find(i):
                    await message.add_reaction("<a:rickroll:866402530858631179>")
                    break



    await bot.process_commands(message)



# @bot.event
# async def on_message(message):
#     if bot.user == message.author:
#         return
#     if message.channel.name == 'chatbot' or message.channel.name =='⭐・chat・bot' or message.channel.name =='ai':
#         rs= randomstuff.Client(api_key='hNU9gUhSU5t8',)
#         response = rs.get_ai_response(message)
#         em = discord.Embed(title = response.message,color=discord.Color.random())
#         em.set_footer(icon_url = message.author.avatar_url,text = f"Said to: {message.author.name}. Consider voting for this bot in top.gg")
#         await message.reply(embed=em)

    #await bot.process_commands(message)
@bot.command() # Normal message wait_for
async def chatbot(ctx):

    await ctx.send("Do you want me to automatically setup chatbot?`(y/n)`")
    msg = await bot.wait_for('message', timeout=600)
    if msg.content == 'y':
        await ctx.send("In what catagory do you want me to set it up? say NONE if you dont care")
        msg = await bot.wait_for('message',timeout=600)
        if msg.content == 'NONE':
            guild = ctx.message.guild
            await guild.create_text_channel('chatbot')
            await ctx.send("Made the channel! #chatbot")
        else:
            await ctx.send('ok')


    else:
        await ctx.send("Ok I wont")

#            





@bot.command()
async def hi(ctx):
    await ctx.send("it worked")



    # @commands.command()
    # async def play(self, ctx, *, song=None):
    #     if song is None:
    #         return await ctx.send("You must include a song to play.")

    #     if ctx.voice_client is None:
    #         return await ctx.send("I must be in a voice channel to play a song.")

    #     # handle song where song isn't url
    #     if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
    #         await ctx.send("Searching for song, this may take a few seconds.")

    #         result = await self.search_song(1, song, get_url=True)

    #         if result is None:
    #             return await ctx.send("Sorry, I could not find the given song, try using my search command.")

    #         song = result[0]

    #     if ctx.voice_client.source is not None:
    #         queue_len = len(self.song_queue[ctx.guild.id])

    #         if queue_len < 10:
    #             self.song_queue[ctx.guild.id].append(song)
    #             return await ctx.send(f"I am currently playing a song, this song has been added to the queue at position: {queue_len+1}.")

    #         else:
    #             return await ctx.send("Sorry, I can only queue up to 10 songs, please wait for the current song to finish.")

    #     await self.play_song(ctx, song)
    #     await ctx.send(f"Now playing: {song}")




#os.system('python website.py')

# @bot.event
# async def on_ready():
#    await dbl.serverCountPost()
#   print(x)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        em = discord.Embed(title='A game is already in progress! Finish it or end the current game using +end before starting a new one',color=discord.Color.random())
        em.set_footer(text="a game was already running")
        await ctx.send(embed=em)



@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)

                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")

@bot.command()
async def end(ctx):
  global gameOver
  if not gameOver:
    gameOver = True
    em = discord.Embed(title='Stopping game..',color=discord.Color.random())
    em.set_footer(text="How about you do +vote 😏")
    await ctx.send(embed=em)
  else:
    em = discord.Embed(title='No games running...',color=discord.Color.random())
    em.set_footer(text="A game was not even running lol")
    await ctx.send(embed=em)




def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

#host = GameHost('*')
#host.add_game(Snake)
#bot ping work\


# @bot.event
# async def on_message(message):
#     await bot.process_commands(message)
#     mention = f'<@!{bot.user.id}>'
#     with open("prefixes.json", "r") as f:
#         prefixes = json.load(f)
#     try:
#        a=prefixes[str(message.guild.id)]
#     except KeyError:
#       a="+"

#     if mention in message.content:
#         em = discord.Embed(title=a,color=discord.Color.random())
#         em.set_author(name='Incase you dont know my prefix its')
#         await message.channel.send(embed=em)
#     await bot.process_commands(message)
#     pass
@bot.command(aliases=['lyrc']) # adding a aliase to the command so we can use !lyrc or !lyrics
async def lyrics(ctx, *, search=None):
    """A command to find lyrics easily!"""

    if not search: # if user hasnt typed anything, throw a error
        embed = discord.Embed(title="No search argument!", description="You havent entered anything, so i couldnt find lyrics!")
        await ctx.reply(embed=embed)

        # ctx.reply is available only on discord.py 1.6.0!

    song = search.replace(' ', '%20') # replace spaces with "%20"

    async with aiohttp.ClientSession() as lyricsSession: # define session
        async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: # define json data
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                lyricsData = await jsondata.json() # load json data
        songLyrics = lyricsData['lyrics'] # the lyrics
        songArtist = lyricsData['author'] # the authors name
        songTitle = lyricsData['title'] # the songs title

        try:
            for chunk in [songLyrics[i:i+2000] for i in range(0, len(songLyrics), 2000)]: # if the lyrics extend the discord character limit (2000): split the embed
                embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=discord.Color.blurple())
                embed.timestamp = datetime.utcnow()

                await lyricsSession.close() # closing the session

                await ctx.reply(embed=embed)

        except discord.HTTPException:
            embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=discord.Color.blurple())
            embed.timestamp = datetime.utcnow()

            await lyricsSession.close() # closing the session

            await ctx.reply(embed=embed)

extensions=['cogs.modcogs','cogs.funcogs','cogs.economycogs','cogs.musiccog','cogs.botdev','cogs.utilitycog','cogs.games','cogs.imagecog','cogs.helpcog']#'cogs.levelcogs']#'musiccog']
if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)
#bot.load_extension('cogs.modcogs')


#keep_alive()
#bot.ipc.start()
bot.run(TOKEN)
#host.run(TOKEN)

#bot.run(os.environ[TOKEN])
