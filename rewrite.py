import random
import discord
from discord.ext import commands
import asyncio
import vars as var
from discord.ext.commands import has_permissions, CheckFailure
import os

bot = commands.Bot(command_prefix = '$')
token = "NjAyMDMxOTk4NTA0MDA5NzI4.XU5Gsg.fvtmqzwU0T-gZYg5lo3SFhIy2lE"

currentDir = os.getcwd()
cogList = []
dirList = os.listdir(currentDir)


for f in dirList:
    if (f.endswith('.py') and f != 'rewrite.py' and f != 'ticket.py'):
        cogList.append(f) 



@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    print('Discord Py Version: {}'.format(discord.__version__))

@bot.command()
@has_permissions(administrator=True)
async def load(ctx, arg):
    bot.load_extension(arg)
    await ctx.send(arg + "has been loaded!")

@load.error
async def load_error(error, ctx):
    if isinstance(error, CheckFailure):
        await ctx.send("You don't have access to that command!")


@bot.command()
@has_permissions(administrator=True)
async def unload(ctx, arg):
    bot.unload_extension(arg)
    await ctx.send(arg + "has been unloaded!")

@unload.error
async def unload_error(error, ctx):
    if isinstance(error, CheckFailure):
        await ctx.send("You don't have access to that command!")



@bot.command()
@has_permissions(administrator=True)
async def cogs(ctx):
    x = ", ".join(cogList)
    await ctx.send(x)
        

bot.load_extension('foodCmds')
bot.load_extension('tempEvents')
bot.run(token)