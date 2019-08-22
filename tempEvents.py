import discord
from discord.ext import commands
import asyncio
import vars as var

class tempEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        print(channel, "had just been created")
        if channel.category_id == 609931723777507348:
            await asyncio.sleep(1)
            msg = discord.Embed(title="Deal Hub Assistant", color=0x00ff00)
            msg.add_field(name = "Menu", value = var.menu, inline = False)
            x = await channel.send(embed = msg)

            await x.add_reaction("🍟")
            await x.add_reaction("🍕")
            await x.add_reaction("🍔")
        
        if channel.category_id == 610284957184557066:
            await asyncio.sleep(1)
            msg = discord.Embed(title= "Deal Hub Assistant", color = 0x1F35F1)
            msg.add_field(name = "Movie Tickets", value = var.movie, inline = False)
            x = await channel.send(embed = msg)

            await x.add_reaction("👍")
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

        blacklist = [609365980711354387, 608477963503140903, 608829750059991041, 608629202920669187, 608842648903483392, 608473616102981632, 609228196608737330, 608480316289712128, 609729795906863111, 608466353330061323, 608487863549427733, 609430100097630218, 609436856526045234, 609365925724160001, 609148676912316446, 609262611669975061, 608476484931420161, 608489313709326337, 608844703995002890, 608830017232961539, 608476361815752724, 608486819809460246, 608476296598650910, 608829329371037706, 609015582645288960, 608475769097945100, 608872074383196180, 608829846579314710, 608479896603328523, 608629264043999282, 608940595783663626, 609154707025428636, 608842738456068096, 608487570590007307, 609227559229587476, 608489314581741594, 608487923922501682, 609161544927936513, 608726287871115285, 608475820616450079, 608489313168130068, 608481643522555924, 608475810306850866, 608485222455050241, 609231020256002058, 608489315273670656, 608480656808476726, 608476373459140608, 609230752994820098, 609626372507435008]
        if reaction.message.channel.id not in blacklist and reaction.message.channel.category_id == 609931723777507348: # and in Ticket Category
            if reaction.emoji == "🍟" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="DoorDash", color=0x00ff00)
                msg.add_field(name = "Instructions", value= var.doordashRefund, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-DoorDash" 
                await reaction.message.channel.edit(name = newName)              
                
            elif reaction.emoji == "🍕" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="Dominos Pizza", color=0xff8c00)
                msg.add_field(name = "Instructions", value= var.pizza, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-Pizza" 
                await reaction.message.channel.edit(name = newName)
                await asyncio.sleep(1)
                await x.add_reaction("👍")   

            elif reaction.emoji == "🍔" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="GrubHub", color=0x1e90ff)
                msg.add_field(name = "Instructions", value= var.grubhubRefund, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-GrubHub" 
                await reaction.message.channel.edit(name = newName)
 
        #FOOD 
        if reaction.message.channel.category_id == 609931723777507348: 
            if reaction.emoji == "👍" and reaction.count == 2:
                await reaction.message.channel.send('<@&608508009206775844> <@&608507934028333076> <@&608478222845345823> <@&608888673509048349>')
                await reaction.message.channel.send('Vendors have been notified, please wait for them to assist you!')
        #MOVIES
        elif reaction.message.channel.category_id == 610284957184557066:
             if reaction.emoji == "👍" and reaction.count == 2:
                await reaction.message.channel.send('<@501232992686047242> <@157690092863881216>')
                await reaction.message.channel.send('Movie Dealers have been notified!')
                newName = str(user.name) + "-Movie" 
                await reaction.message.channel.edit(name = newName)



def setup(bot):
    bot.add_cog(tempEvents(bot))