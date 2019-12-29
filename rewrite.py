import random
import discord
from discord.ext import commands
import asyncio
import vars as var
from discord.ext.commands import has_permissions, CheckFailure
import os

bot = commands.Bot(command_prefix = '$')
token = "" #Insert Bot token here

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
    bot.remove_command('help')

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

@bot.command()
async def help(ctx):
    msg = discord.Embed(title = "Help",color=0x1e90ff)
    msg.add_field(name = "Available Commands", value = "/n".join(var.commands), inline=False)
    await ctx.send(embed = msg)
        

bot.load_extension('foodCmds')
bot.load_extension('tempEvents')
bot.run(token)
