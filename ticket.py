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
        
        *If you would like a custom bot like this for your server contact Skwiid#0001*
        """
        movie = """
        This is the Fandango Movie Ticket Service!
        If your theater can be found on fandango we can order you cheap tickets.
        $4 - 1 Movie Ticket
        $3 - 4 or more Movie Tickets

        Before pressing ready please fill out this template:
        Theater Name: 
        Movie:
        Time:
        Seats:

        **Once you have sent this information in the ticket react with 👍 to ping movie dealers**
        """

        print(channel, "had just been created")
        if channel.category_id == 609931723777507348:
            await asyncio.sleep(1)
            msg = discord.Embed(title="Deal Hub Assistant", color=0x00ff00)
            msg.add_field(name = "Menu", value = menu, inline = False)
            x = await channel.send(embed = msg)

            await x.add_reaction("🍟")
            await x.add_reaction("🍕")
            await x.add_reaction("🍔")
        
        if channel.category_id == 610284957184557066:
            await asyncio.sleep(1)
            msg = discord.Embed(title= "Deal Hub Assistant", color = 0x1F35F1)
            msg.add_field(name = "Movie Tickets", value = movie, inline = False)
            x = await channel.send(embed = msg)

            await x.add_reaction("👍")
            
    
    
    async def on_reaction_add(self, reaction, user):
        #INSTRUCTION VARS

        doordash = """
        Doordash Service
        --------------------------------
        :green_apple: - DoorDash Refund Service
        :apple: - DoorDash Buy 4 You Service

        **React to choose your preferred service!**
        """ 

        grubhub = """
        GrubHub Service
        --------------------------------
        :lemon: - GrubHub Refund Service
        :pear: - GrubHub Buy 4 You Service

        **React to choose your preferred service!**
        """ 

        doordashRefund = """
        For Doordash please make sure to make a new account before ordering (this is to ensure great history on your account and 100% success with me!)

        After you made a new account, these are the next steps:
        - Send your user name  & password
        - Send a picture of your receipt after placing the order
        - Send a refund fee payment of 60% off or 40% of the total order (via CashApp, BTC, ApplePay)
        - Once your food arrives, please wait 15 minutes after delivery, once 15 mins passed, ping me here and I'll refund you
        
        :smiley: We look forward to serving you!
        **ONCE YOU ARE READY TO ORDER PLEASE REACT WITH :thumbsup:**
        """
        doordashb4u = """
        Doordash Buy4u instructions RATE IS 60% OFF
        - You place your order with us in ticket. 
        - You send a payment fee first. 
        - Order will be placed. 
        - We will continue to update you as order comes. 
        - $50 minimum , $150 maximum 
        - In order to continue using our service we require you to take a picture of the food when it arrives clearly and post in vouches. 
          If not, you’ll be kicked. 

        :smiley: We look forward to serving you!
        **ONCE YOU ARE READY TO ORDER PLEASE REACT WITH :thumbsup:**


        """

        grubhubRefund = """
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
        **ONCE YOU ARE READY TO ORDER PLEASE REACT WITH :thumbsup:**
        """

        grubhubb4u = """
        GrubHub RATE IS 50% OFF
        - You make a ticket and place an order. 
        - Minimum must be $50 and maxmium can be $200
        - You pay fee first through Cashapp, Amazon Gift Card, Apple Pay or BTC
        - We process your order and update you 
        - In order to continue using our service we require you to take a picture of the food when it arrives clearly and post in vouches. 
          If not, you’ll be kicked

        We look forward to serving you! :smile:
        **ONCE YOU ARE READY TO ORDER PLEASE REACT WITH :thumbsup:**
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
        **ONCE YOU ARE READY TO ORDER PLEASE REACT WITH :thumbsup:**
        """

        blacklist = [609365980711354387, 608477963503140903, 608829750059991041, 608629202920669187, 608842648903483392, 608473616102981632, 609228196608737330, 608480316289712128, 609729795906863111, 608466353330061323, 608487863549427733, 609430100097630218, 609436856526045234, 609365925724160001, 609148676912316446, 609262611669975061, 608476484931420161, 608489313709326337, 608844703995002890, 608830017232961539, 608476361815752724, 608486819809460246, 608476296598650910, 608829329371037706, 609015582645288960, 608475769097945100, 608872074383196180, 608829846579314710, 608479896603328523, 608629264043999282, 608940595783663626, 609154707025428636, 608842738456068096, 608487570590007307, 609227559229587476, 608489314581741594, 608487923922501682, 609161544927936513, 608726287871115285, 608475820616450079, 608489313168130068, 608481643522555924, 608475810306850866, 608485222455050241, 609231020256002058, 608489315273670656, 608480656808476726, 608476373459140608, 609230752994820098, 609626372507435008]
        #categoryBL = [608829750059991041, 608489313168130068, 608487863549427733, 608466353330061323, 608476296598650910, 609230752994820098, 609931723777507348, 609365925724160001, 608475769097945100, 608726287871115285, 610284957184557066]
        if reaction.message.channel.id not in blacklist and reaction.message.channel.category_id == 609931723777507348: # and in Ticket Category
            if reaction.emoji == "🍟" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="DoorDash", color=0x00ff00)
                msg.add_field(name = "Instructions", value= doordash, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-DoorDash" 
                await reaction.message.channel.edit(name = newName)
                await asyncio.sleep(1)
                await x.add_reaction("🍏")
                await x.add_reaction("🍎")                
                
            elif reaction.emoji == "🍕" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="Dominos Pizza", color=0xff8c00)
                msg.add_field(name = "Instructions", value= pizza, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-Pizza" 
                await reaction.message.channel.edit(name = newName)
                await asyncio.sleep(1)
                await x.add_reaction("👍")   

            elif reaction.emoji == "🍔" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="GrubHub", color=0x1e90ff)
                msg.add_field(name = "Instructions", value= grubhub, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                newName = str(user.name) + "-GrubHub" 
                await reaction.message.channel.edit(name = newName)
                await asyncio.sleep(1)
                await x.add_reaction("🍋")
                await x.add_reaction("🍐")   

        #Refund or Buy4You
        if reaction.message.channel.category_id == 609931723777507348:
            #DOORDASH CHOICES
            if reaction.emoji == "🍏" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="DoorDash Refund Service", color=0xff8c00)
                msg.add_field(name = "Instructions", value= doordashRefund, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                await x.add_reaction("👍")

            elif reaction.emoji == "🍎" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="DoorDash Buy 4 You Service", color=0xff8c00)
                msg.add_field(name = "Instructions", value= doordashb4u, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                await x.add_reaction("👍")

            #GRUBHUB CHOICES
            if reaction.emoji == "🍋" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="GrubHub Refund Service", color=0xff8c00)
                msg.add_field(name = "Instructions", value= grubhubRefund, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                await x.add_reaction("👍")

            elif reaction.emoji == "🍐" and reaction.count == 2:
                await reaction.message.delete()
                msg = discord.Embed(title="GrubHub Buy 4 You Service", color=0xff8c00)
                msg.add_field(name = "Instructions", value= grubhubb4u, inline=False)
                x = await reaction.message.channel.send(embed = msg)
                await x.add_reaction("👍")





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

    async def on_message(self, message):
        #INSTRUCTION VARS
        doordash = """
        For Doordash please make sure to make a new account before ordering (this is to ensure great history on your account and 100% success with me!)

        After you made a new account, these are the next steps:
        - Send your user name  & password
        - Send a picture of your receipt after placing the order
        - Send a refund fee payment of 60% off or 40% of the total order (via CashApp, BTC, ApplePay)
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

        vouch = """
        Thank you for ordering from us! If you were satisfied with your order please go to the
        <#608473616102981632> channel!
        Please make vouches as descriptive as possible!

        Vouch Example:
        Vouch for **(Vendor Name)**, they provided me with **(Service Provided)**. (Description of experience and satisfaction level).

        Please do not leave short vouches as it does not help our server <3
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
            categoryList = []
            for guild in self.guilds:
                if guild.name == "Deal Hub":
                    for c in guild.categories:
                        categoryList.append(c.id)
            print(categoryList)
        
        if message.content.startswith('-vouch'):
            msg = discord.Embed(title = "How to Vouch", color = 0xF85FBE)
            msg.add_field(name = "Instructions", value = vouch, inline =False)
            await message.channel.send(embed = msg)
        

                        
    
#Run The Client!
client = MyClient()
client.run(TOKEN)

