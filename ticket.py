import random
import discord
import asyncio

TOKEN = "NjAyMDMxOTk4NTA0MDA5NzI4.XU5Gsg.fvtmqzwU0T-gZYg5lo3SFhIy2lE"


class MyClient(discord.Client):
    

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print(discord.__version__)

    
    async def on_guild_channel_create(self, channel):
        menu = """
        Choose a service by reacting to the correct emoji:
        :pizza: - Dominos Pizza
        :fries: - DoorDash
        :hamburger: - GrubHub
        :moneybag: - Other Services
        *If you would like a custom bot like this for your server contact Skwiid#0001*
        """

        print(channel, "had just been created")
        await asyncio.sleep(1)
        msg = discord.Embed(title="Deal Hub Assistant", color=0x00ff00)
        msg.add_field(name = "Menu", value = menu, inline = False)
        x = await channel.send(embed = msg)

        await x.add_reaction("🍟")
        await x.add_reaction("🍕")
        await x.add_reaction("🍔")
        #await x.add_reaction("💰")
    
    
    async def on_reaction_add(self, reaction, user):
         #INSTRUCTION VARS
        doordash = """
        For Doordash please make sure to make a new account before ordering (this is to ensure great history on your account and 100% success with me!)

        After you made a new account, these are the next steps:
        - Send your user name  & password
        - Send a picture of your receipt after placing the order
        - Send a refund fee payment of 70% off
        - Once your food arrives, please wait 15 minutes after delivery, once 15 mins passed, ping me here and I'll refund you
        
        :smiley: We look forward to serving you!
        """
        grubhub = """
        Hi! This is the Grubhub Refund Service

        You're allowed to order food from $1-150 as there is a 100% success rate! 

        Here are the steps:
        - Pick out the order you want from a restaurant
        - Send a picture of your receipt after placing order
        - Send a refund payment fee of 70% off to either my Cashapp, Apple Pay, as an Amazon Gift-Card or BTC
        - Once your food arrives, please wait 15 minutes after delivery to tell me

        Order Number:
        Store Number:

        & then the refund will be processed back to your credit card :)

        We look forward to serving you! :smile:
        """

        pizza = """
        Hi! This is the Pizza Service!

        First pick from the menu below:
        - $4 for 1 medium sized two topping pizza
        - $8 for 2 medium sized two topping pizza
        - $20 for 5 medium sized two topping pizza

        Now, choose your preferred payment method of either Cash App, Apple Pay, Amazon Gift Card or BTC and you'll receive your pizzas :)

        These are safe and you're allowed to do either pick-up or delivery. 
        Be aware of fees or tips that may pop up & ensure to change information to yours. 
        Lastly, these are organically grown pizza accounts made by collecting points from our friends :)

        We look forward to serving you! :smile:
        """

        blacklist = [609365980711354387, 608477963503140903, 608829750059991041, 608629202920669187, 608842648903483392, 608473616102981632, 609228196608737330, 608480316289712128, 609729795906863111, 608466353330061323, 608487863549427733, 609430100097630218, 609436856526045234, 609365925724160001, 609148676912316446, 609262611669975061, 608476484931420161, 608489313709326337, 608844703995002890, 608830017232961539, 608476361815752724, 608486819809460246, 608476296598650910, 608829329371037706, 609015582645288960, 608475769097945100, 608872074383196180, 608829846579314710, 608479896603328523, 608629264043999282, 608940595783663626, 609154707025428636, 608842738456068096, 608487570590007307, 609227559229587476, 608489314581741594, 608487923922501682, 609161544927936513, 608726287871115285, 608475820616450079, 608489313168130068, 608481643522555924, 608475810306850866, 608485222455050241, 609231020256002058, 608489315273670656, 608480656808476726, 608476373459140608, 609230752994820098, 609626372507435008]
        if reaction.message.channel.id not in blacklist:
            if reaction.emoji == "🍟" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="DoorDash", color=0x00ff00)
                msg.add_field(name = "Instructions", value= doordash, inline=False)
                await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-DoorDash" 
                await reaction.message.channel.edit(name = newName)                
                
            elif reaction.emoji == "🍕" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="Dominos Pizza", color=0xff8c00)
                msg.add_field(name = "Instructions", value= pizza, inline=False)
                await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-Pizza" 
                await reaction.message.channel.edit(name = newName)   

            elif reaction.emoji == "🍔" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="GrubHub", color=0x1e90ff)
                msg.add_field(name = "Instructions", value= grubhub, inline=False)
                await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-GrubHub" 
                await reaction.message.channel.edit(name = newName)   
            '''
            elif reaction.emoji == "💰" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="Other Services", color=0x1e90ff)
                msg.add_field(name = "Services Provided", value= other, inline=False)
                await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-Other" 
                await reaction.message.channel.edit(name = newName)   
            '''

    async def on_message(self, message):
        #INSTRUCTION VARS
        doordash = """
        For Doordash please make sure to make a new account before ordering (this is to ensure great history on your account and 100% success with me!)

        After you made a new account, these are the next steps:
        - Send your user name  & password
        - Send a picture of your receipt after placing the order
        - Send a refund fee payment of 70% off
        - Once your food arrives, please wait 15 minutes after delivery, once 15 mins passed, ping me here and I'll refund you
        
        :smiley: We look forward to serving you!
        """
        grubhub = """
        Hi! This is the Grubhub Refund Service

        You're allowed to order food from $1-150 as there is a 100% success rate! 

        Here are the steps:
        - Pick out the order you want from a restaurant
        - Send a picture of your receipt after placing order
        - Send a refund payment fee of 70% off to either my Cashapp, Apple Pay, as an Amazon Gift-Card or BTC
        - Once your food arrives, please wait 15 minutes after delivery to tell me

        Order Number:
        Store Number:

        & then the refund will be processed back to your credit card :)

        We look forward to serving you! :smile:
        """

        pizza = """
        Hi! This is the Pizza Service!

        First pick from the menu below:
        - $4 for 1 medium sized two topping pizza
        - $8 for 2 medium sized two topping pizza
        - $20 for 5 medium sized two topping pizza

        Now, choose your preferred payment method of either Cash App, Apple Pay, Amazon Gift Card or BTC and you'll receive your pizzas :)

        These are safe and you're allowed to do either pick-up or delivery. 
        Be aware of fees or tips that may pop up & ensure to change information to yours. 
        Lastly, these are organically grown pizza accounts made by collecting points from our friends :)

        We look forward to serving you! :smile:
        """

        #END INSTRUCTION VARS

        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        
        if message.content.startswith('-doordash'):
            msg = discord.Embed(title="DoorDash", color=0x00ff00)
            msg.add_field(name = "Instructions", value= doordash, inline=False)
            await message.channel.send(embed = msg)
            
        if message.content.startswith('-grubhub'):
            msg = discord.Embed(title="GrubHub", color=0x1e90ff)
            msg.add_field(name = "Instructions", value= grubhub, inline=False)
            await message.channel.send(embed = msg)
            
        if message.content.startswith('-pizza'):
            msg = discord.Embed(title="Dominos Pizza", color=0xff8c00)
            msg.add_field(name = "Instructions", value= pizza, inline=False)
            await message.channel.send(embed = msg)

        if message.content.startswith('$dev'):
            channelList = []
            for server in self.guilds:
                if server.name == 'Deal Hub':
                    for channel in server.channels:
                        channelList.append(channel.id)
            print(channelList)

                        
    
#Run The Client!
client = MyClient()
client.run(TOKEN)

