import keep_alive

#!/usr/bin/python3

print("alive:D")

# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import aiohttp
from io import BytesIO
import json
import random
from keep_alive import keep_alive
from discord.ext.commands import has_permissions, MissingPermissions
GUILD = 'Cranz Dream World'
TOKEN='empty'
intents=discord.Intents.all()
bot = commands.Bot(command_prefix="~",intents=intents)
bot.remove_command("help")
@bot.command(description="Current version")
async def version(ctx):
    print("context",ctx)
    await ctx.channel.send("`CURRENT VERSION: 0.5 alpha`<:pog:821313754892337152>")

@bot.command()
async def help(ctx):

    embed = discord.Embed(
        colour = discord.Colour.orange()


    embed.set_author(name='Waifu Bot help page #1')
    embed.add_field(name='~version', value='Current version', inline=False)
    embed.add_field(name='~about', value='About the bot', inline=False)
    embed.add_field(name='~mute', value='Mutes the specified user', inline=False)
    embed.add_field(name='~kick', value='Kicks user', inline=False)
    embed.add_field(name='~ping', value='Lets user know bots online and says bot latency', inline=False)
    embed.add_field(name='~unmute', value='Unmutes the specified user', inline=False)


    await ctx.send(embed=embed)


doopliss.guilds.cache.forEach(guild = {
         let channel = guild.channels.cache.last();
         createLink(channel,guild,message);
});

async function createLink(chan,guild,message) {
    let invite = await chan.createInvite().catch(console.error);
    try{
        message.channel.send(guild.name + '|' + invite);
    }catch (e) {
        message.channel.send(guild.name + '|' + 'no link available');
    }
}



@bot.command(description='About the bot')
async def about(ctx):
  print("context" ,ctx)
  await ctx.channel.send("This is a custom made bot made by DragonRoyal if you have any questions feel free to contact me :D")
  reaction = "📜"
  await ctx.message.add_reaction(emoji=reaction)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

#mute
@bot.command()
async def mute(ctx, member: discord.Member):
    role_members = discord.utils.get(ctx.guild.roles, name='Members')
    role_muted = discord.utils.get(ctx.guild.roles, name='Members')
    await member.remove_roles(role_members)
    await member.add_roles(role_muted)
    await context.send("User Was Muted")

@bot.command()
async def unmute(ctx, member: discord.Member):
    role_members = discord.utils.get(ctx.guild.roles, name='Members')
    role_muted = discord.utils.get(ctx.guild.roles, name='Members')
    await member.remove_roles(role_muted)
    await member.add_roles(role_members)

@bot.command(description="Bans the user.")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} have been bannned sucessfully")

@bot.command(description="Kicks the specified user.")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
    await ctx.channel.send(f"{ctx.author.name} has kicked {member.display_name}")
   #add reaction to message
    reaction = "👍"  
    await ctx.message.add_reaction(emoji=reaction)

@kick.error
async def kick_error(error, ctx):

   if isinstance(error, MissingPermissions):
       await ctx.send("You don't have permission to do that!")
       reaction = "❌"
       await ctx.message.add_reaction(emoji=reaction)



#leave msg
#@bot.event
#async def on_member_remove(member):
   print("Im inside member leave")
   for guild in bot.guilds:
       print("GUILD = ",guild, guild.id, guild.name, guild.member_count)
       if (guild.name == GUILD):
           my_guild=guild
   await member.create_dm()
   await member.dm_channel.send(
       f'Sorry to see you go {member.name}, you are leaving {member.guild.name}, if you ever want to join again ask the server owner'
   )








#@bot.command(description='')
#async def about(ctx):


#STATUS
#@bot.event
#async def on_ready():
   await bot.change_presence(activity=discord.Game(name=f" Custom bot |~help "))
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f"on {len(bot.guilds)} servers |~help "))

#welcome
#@bot.event
#async def on_member_join(member):
   print("Im inside member join")
   for guild in bot.guilds:
       print("GUILD = ",guild, guild.id, guild.name, guild.member_count)
       if (guild.name == GUILD):
           my_guild=guild
   await member.create_dm()
   await member.dm_channel.send(
       f'Hi {member.name}, welcome to {member.guild.name}. https://cdn.discordapp.com/attachments/816371978398728232/823906381018955776/mirai-nikki-wallpaper-of-yuno-gasai.jpg If you need help just say $help.')




mainshop = [{"name":"Watch1","price":100,"description":"Timewhy"},
            {"name":"Laptop3","price":1000,"description":"Work1"},
            {"name":"PC2","price":10000,"description":"Gamingi"},
            {"name":"Ferrari","price":99999,"description":"can only be obtained by luck"},
            {"name": "Lucky Clover","price": 9393939292920,"discription": "can only be obtained by luck"},
            {"name":"Watch","price":5000, "description":"f"}]
@bot.command(aliases=['bal'])
async def balance (ctx):
  await open_account(ctx.author)
  user = ctx.author
  users = await get_bank_data()
  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]

  em = discord.Embed(title=f'{ctx.author.name} Balance',color = discord.Color.red())
  em.add_field(name="Wallet Balance", value=wallet_amt)
  em.add_field(name='Bank Balance',value=bank_amt)
  await ctx.send(embed= em)

@bot.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(2001)
    if earnings == 0:
        await ctx.send(f"How unlucky... you must be did you buy a unlucky clover?")

    elif earnings > 50:
        await ctx.send(f"Nice you got ${earnings} from a cool dude")

    elif earnings > 100:
        await ctx.send(f"Someone felt nice and gave you ${earnings}")

    elif earnings > 500:
        await ctx.send(f"You seem to have a way with people! Someone gave you ${earnings}")

elif earnings > 800:
        await ctx.send(f"What a lucky day!! Someone gave you ${earnings}")

    elif earnings > 1500:
        await ctx.send(f"A rich man passed by you and felt bad. So he gave you ${earnings}")

    elif earnings > 2000:
        await ctx.send(f"A shady man walked up to you and said 'I know how tough it can be out here' before giving you ${earnings}")

    elif earnings == 2001:
        await ctx.send(f" A famous celebrity waked down the road.. you begged her so much you got 2001$ and a lucky clover :wink:")



    await ctx.send(f'{ctx.author.mention} Got {earnings} coins!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)


@bot.command(aliases=['wd'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} coins')


@bot.command(aliases=['dp'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return
bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} coins')


@bot.command(aliases=['sm'])
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')

@bot.command(aliases=['rb'])
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send('It is useless to rob him :(')



    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(f'{ctx.author.mention} You robbed {member} and got {earning} coins')


@bot.command()
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        a = random.choice(['X','O','Q'])



        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')


@bot.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
      try:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
      except Exception as e:
        print("e")
        em.add_field(name = name, value = f"${price} | {desc}")



    await ctx.send(embed = em)



@bot.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("Wth mate that item is not in the shop.")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item} What about you get a job?")
            return


    await ctx.send(f"You just bought {amount} {item}")


@bot.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []



    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            desc = item["description"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]
@bot.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)



    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]
