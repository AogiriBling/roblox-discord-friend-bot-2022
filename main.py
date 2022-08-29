import os
from discord.ext import commands 
import discord, requests, random, threading, asyncio, keyboard, sys, socket, subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
from webserver import keep_alive

with open('cookies.txt', 'r') as cookies:
    cookies1 = cookies.read().splitlines()

bot = commands.Bot(command_prefix='.')

channel = 987525174968590336

my_secret = os.environ['token']
token = os.environ['token']

my_secret = os.environ['webhook']
log_webhook = os.environ['webhook']

@bot.event
async def on_ready():
 members = sum([guild.member_count for guild in bot.guilds])
 await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Aogiri Tree"))
 print("Members")

def add_user(cookie, userid):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
            session.post(f'https://friends.roblox.com/v1/users/{userid}/request-friendship')
    except:
        pass



@bot.command()
async def rfriend(ctx, userId):

    if ctx.channel.id == channel:

            embed = discord.Embed(color=0x0F0F0F, description=f"**__*<@{ctx.author.id}> Sent*__** `60` **__*Friend Requests*__**")
            await ctx.send(embed=embed)
            for x in cookies1:
                threading.Thread(target=add_user, args=(x, userId,)).start()

    else:
        embed=discord.Embed(title="Warning", description=f"ROBLOX command will be used only in <#{channel}>")
        await ctx.send(embed=embed)
        return

        webhook = DiscordWebhook(url=log_webhook)
        embed = DiscordEmbed(title='ROBLOX - Logs', description=(f'**{ctx.author} : {bot.command_prefix}rfriend : {userId}**'), color=16711936)
        webhook.add_embed(embed)
        response = webhook.execute()

keep_alive()
bot.run(token)
