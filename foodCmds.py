import discord
from discord.ext import commands
import asyncio
import vars as var

class Food(commands.Cog):
    @commands.command()
    async def doordash(self, ctx):
        msg = discord.Embed(title="DoorDash", color=0x00ff00)
        msg.add_field(name = "Instructions", value= var.doordashRefund, inline=False)
        await ctx.send(embed = msg)
    
    @commands.command()
    async def grubhub(self, ctx):
        msg = discord.Embed(title="GrubHub", color=0x1e90ff)
        msg.add_field(name = "Instructions", value= var.grubhubRefund, inline=False)
        await ctx.send(embed = msg)

    @commands.command()
    async def vouch(self, ctx):
        msg = discord.Embed(title = "How to Vouch", color = 0xF85FBE)
        msg.add_field(name = "Instructions", value = var.vouch, inline =False)
        await ctx.send(embed = msg)

    @commands.command()
    async def pizza(self, ctx):
        msg = discord.Embed(title="Dominos Pizza", color=0xff8c00)
        msg.add_field(name = "Instructions", value= var.pizza, inline=False)
        await ctx.send(embed = msg)






def setup(bot):
    bot.add_cog(Food(bot))