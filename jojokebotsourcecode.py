##Imports
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

#Defines client and prefix
Client = discord.Client()
client = commands.Bot(command_prefix="Jo!")


@client.event
#The following happens when the bot starts up:
async def on_ready():
    #Sets the bot's game
    await client.change_presence(game=discord.Game(name='Use Jo!Help for Command List!'))
    #Makes the bot print a phrase in the console
    print("OH MY GOD!")
    
@client.event
async def on_message(message):
###Misc
    #Checks what command is being used:
    if message.content.startswith('Jo!Help'):
        #Defines the name of your embed:
        emb = (discord.Embed(
            #Shows the text that the embed will display
            description="A bot for only the highest quality of JoJo memes! Currently running 35 JoJokes across 4 Parts!",
            #Chooses the color of the embed as hexcode
            colour=0x00FF00)
        )
        #shows the footer text of the embed
        emb.set_footer(text='Message @Skull#0666 if you need more help!')
        #shows thethumbnail of the embed in the topright corner
        emb.set_thumbnail(url='https://cdn.discordapp.com/attachments/386705873449254912/480552446662279168/horryshit.png')
        #shows who created the bot
        emb.set_author(name='@Skull#0666', icon_url='https://cdn.discordapp.com/attachments/386705873449254912/480552836493475840/bongiorno.png')
        #Text that appears below the description; `inline` tells whether the phrase are stacked or placed adjacent to each other
        emb.add_field(name='Part 1', value='For Part 1 JoJokes, Type **"Jo!List1"!**', inline=False)
        emb.add_field(name='Part 2', value='For Part 2 JoJokes, Type **"Jo!List2"!**', inline=False)
        emb.add_field(name='Part 3', value='For Part 3 JoJokes, Type **"Jo!List3"!**', inline=False)
        emb.add_field(name='Part 4', value='For Part 4 JoJokes, Type **"Jo!List4"!**', inline=False)
        #tells the bot to send the message. message.author tells it to dm the person who uses the command, and embed=emb tells it what embed to send
        await client.send_message(message.author, embed=emb)
    if message.content.startswith('Jo!List1'):
        emb = (discord.Embed(
            description="Part 1 JoJoke list (6 total):",
            colour=0x00FF00)
        )
        emb.add_field(name='Jo!Dio [text/@user]', value='If someone\'s expecting your text, reveal that it was I, Dio!', inline=False)
        emb.add_field(name='Jo!Dog [@user, text]', value='*Minor Spoiler.* Throw a user\'s item/pet/thing of your choice into a furnace.', inline=False)
        emb.add_field(name='Jo!Speedwagon', value='Send a random image of Speedwagon in chat.', inline=False)
        emb.add_field(name='Jo!RMH [@user]', value='*Minor Spoiler.* Tell a user that you reject your humanity!.', inline=False)
        emb.add_field(name='Jo!SYO', value='Charge up your hamon and activate Jonathan\'s iconic attack.', inline=False)
        emb.add_field(name='Jo!OP1', value='JOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOJO!.', inline=False)
        await client.send_message(message.author, embed=emb)
    if message.content.startswith('Jo!List2'):
        emb = (discord.Embed(
            description="Part 2 JoJoke list(8 total):",
            colour=0x00FF00)
        )
        emb.add_field(name='Jo!Nani <text>', value='Predict that someone\'s next line will be the text value you input.', inline=False)
        emb.add_field(name='Jo!Run', value='Utilize the Joestar final technique.', inline=False)
        emb.add_field(name='Jo!Awaken [@user]', value='Awaken your friends as Wamuu did.', inline=False)
        emb.add_field(name='Jo!Caeser [@user]', value='**SPOILER!** Give someone the last of your hamon.', inline=False)
        emb.add_field(name='Jo!Nice [text/@user]', value='Tell everyone what you think is niiiiice.', inline=False)
        emb.add_field(name='Jo!Nazi', value='Your Science is the best in the world!.', inline=False)
        emb.add_field(name='Jo!TJ', value='Bring some Tequila!', inline=False)
        emb.add_field(name='Jo!Naisu [@user]', value='Congradulate someone on a job well done.', inline=False)
        await client.send_message(message.author, embed=emb)
    if message.content.startswith('Jo!List3'):
        emb = (discord.Embed(
            description="Part 3 JoJoke list(13 total):",
            colour=0x00FF00)
        )
        emb.add_field(name='Jo!Menacing [@user]', value='When someone\'s giving you a bad feeling.', inline=False)
        emb.add_field(name='Jo!ORA [@user]', value='When what someone owes you could never be paid back with money.', inline=False)
        emb.add_field(name='Jo!Rero [@user]', value='Ask a user if they\'re gonna eat that cherry.', inline=False)
        emb.add_field(name='Jo!OJ', value='Send a random Old Joseph quote. OH MY GOD!', inline=False)
        emb.add_field(name='Jo!HAHA [@user/@text]', value='Laugh at another.', inline=False)
        emb.add_field(name='Jo!Iam [@user]', value='*Possible Spoiler.* MOHOMMED AVDOL!??!', inline=False)
        emb.add_field(name='Jo!H2U [@user]', value='Give another user hell...', inline=False)
        emb.add_field(name='Jo!Iggy [@user]', value='Launch Iggy at another user.', inline=False)
        emb.add_field(name='Jo!Good', value='Gooduh!', inline=False)
        emb.add_field(name='Jo!Scream', value='When something\'s so terrifying you just have to scream.', inline=False)
        emb.add_field(name='Jo!World', value='**Spoiler!** Activate the true power of THE WORLD!', inline=False)
        emb.add_field(name='Jo!Muda [@user]', value='**Spoiler!** Call someone useless, useless, USELESS!', inline=False)
        emb.add_field(name='Jo!RRD [@user]', value='**Spoiler!** Crush a user with a Road Roller!', inline=False)        
        await client.send_message(message.author, embed=emb)        
    if message.content.startswith('Jo!List4'):
        emb = (discord.Embed(
            description="Part 4 JoJoke list(8 total):",
            colour=0x00FF00)
        )
        emb.add_field(name='Jo!Great [@user]', value='For someone who you think is just great!', inline=False) 
        emb.add_field(name='Jo!Delet [@user]', value='When someone needs to delete a message they sent.', inline=False) 
        emb.add_field(name='Jo!Spider', value='When you need to taste something to get it just right.', inline=False)  
        emb.add_field(name='Jo!Quiet', value='Use when someone won\'t let you live a quiet life.', inline=False)    
        emb.add_field(name='Jo!Cry', value='When you just have to let the tears flow...', inline=False)
        emb.add_field(name='Jo!Yum [text]', value='When you just love the taste of something...', inline=False)        
        emb.add_field(name='Jo!BTD [@user]', value='**SPOILER!** Activate Killer Queen\'s third bomb on your victim.', inline=False)
        emb.add_field(name='Jo!Stop [@user]', value='**SPOILER!** Run over your victim with an amublance.', inline=False)
        await client.send_message(message.author, embed=emb)
###Part 1 
    #DIO!
    if message.content.startswith('Jo!Dio'):
        #Checks for who sent the command
        userID = message.author.id
        #Checks for the content of the message, removing the command
        args = message.content[len('Jo!Dio'):].strip()
        #This is what the bot will do if the user only sends the command
        if args == '':
            emb = (discord.Embed(
                description="You thought it was <@%s>, but it was I, DIO!" % (userID),
                
                colour=0x00FF00)
            )
            #shows the image of the embed
            emb.set_image(url="https://thumbs.gfycat.com/OblongFavoriteIndianpalmsquirrel-size_restricted.gif")
            #tells the bot to send the message. message.channel tells it to send it to the same channel as where the command was used.
            await client.send_message(message.channel, embed=emb)
        #This is what the bot will do if the user sends a string after the command
        else:    
            emb = (discord.Embed(
                #% `("".join(args[0:]))`=simply tells the bot to replace `%s` with whatever content comes after the command 
                description="You thought it was **%s**, but it was I, DIO!" % ("".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://thumbs.gfycat.com/OblongFavoriteIndianpalmsquirrel-size_restricted.gif")
            await client.send_message(message.channel, embed=emb)
    #Danny
    if message.content.startswith('Jo!Dog'):
        #userID checks the person who sent the message
        userID = message.author.id
        args = message.content[len('Jo!Dog'):].strip()
        if args == '':
            emb =(discord.Embed(
            #userID tells the bot to replace the %s with whoever sent the message; the <@> makes it so the tag will be complete
                description="<@%s> has thrown themselves into a furnace...?" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/ZV1RXE.gif")
            await client.send_message(message.channel, embed=emb)         
        else:
            emb =(discord.Embed(
                description="<@%s> has thrown **%s** into a furnace!" % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/ZV1RXE.gif")
            await client.send_message(message.channel, embed=emb)    
    #SpeedWagon
    if message.content.startswith('Jo!Speedwagon'):
        emb =(discord.Embed(
            description="A picture of the lord our god, Robert E. O. Speedwagon.",
            colour=0x00FF00)
        )
        #gives a list of items for the bot to choose from
        items = ["https://vignette.wikia.nocookie.net/jjba/images/f/f9/SpeedwagonIntroEoH.jpg/revision/latest/zoom-crop/width/240/height/240?cb=20170223081303",
        "https://i.ytimg.com/vi/JitZzYW1ZUY/maxresdefault.jpg",
        "https://carboncostume.com/wordpress/wp-content/uploads/2016/10/e4c7e7710174a852935fd1878d2665f0.jpg",
        "https://vignette.wikia.nocookie.net/jjba/images/7/75/Speedwagon_hat.png/revision/latest/scale-to-width-down/270?cb=20150621045246",
        "http://koi-nya.net/img/subidos_posts/2015/01/Robert-Speedwagon-ser%C3%A1-jugable-en-JoJos-Bizarre-Adventure-Eyes-of-Heaven.png"]
        #random.choice(items) tells the bot to choose randomly among the list
        emb.set_image(url=random.choice(items)
        )
        await client.send_message(message.channel, embed=emb)
    #I Reject My Humanity!
    if message.content.startswith('Jo!RMH'):
        userID = message.author.id
        args = message.content[len('Jo!RMH'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s> rejects their humanity!" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/jq1PJz.gif")
            await client.send_message(message.channel, embed=emb)         
        else:
            emb =(discord.Embed(
                description="<@%s> rejects their humanity, %s!" % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/jq1PJz.gif")
            await client.send_message(message.channel, embed=emb)
    #Overdrive
    if message.content.startswith('Jo!SYO'):
        userID = message.author.id
        emb =(discord.Embed(
            description="<@%s> is prepping their hamon!" % (userID),
            colour=0x00FF00)
        )
        emb.set_image(url="https://78.media.tumblr.com/9ef7919dee0947d3a60e3fc845aab8ef/tumblr_mifu9kDARX1r6mrcio1_500.gif")
        await client.send_message(message.channel, embed=emb)
        await client.send_message(message.channel, "SUNLIGHT YELLOW... OVERDRIIIIIIIVE!")
    #OP
    if message.content.startswith('Jo!OP1'):
        userID = message.author.id
        emb =(discord.Embed(
            description="SONO CHI NO SADAME!",
            colour=0x00FF00)
        )
        emb.set_image(url="https://i.kym-cdn.com/photos/images/original/001/244/607/a5f.gif")
        await client.send_message(message.channel, embed=emb)
        #you can send a string instead of an embed to make the bot send normal text
        await client.send_message(message.channel, "***JOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOJO!***")
###Part 2
    #NextYou'llSay
    if message.content.startswith('Jo!Nani'):
        userID = message.author.id
        args = message.content[len('Jo!Nani'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="And next you'll say, **'<@%s> doesn\'t know how to use this command'**! Am I right?" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.imgur.com/8jtcLZa.gif")
            await client.send_message(message.channel, embed=emb)         
        else:
          
            emb =(discord.Embed(
                description="And next you'll say, **'%s'**! Am I right?" % ("".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.imgur.com/8jtcLZa.gif")
            await client.send_message(message.channel, embed=emb)
    #RUN
    if message.content.startswith('Jo!Run'):
        userID = message.author.id
        emb =(discord.Embed(
            description="<@%s> Is using the Joestar final technique: RUN AWAY!" % (userID),
            colour=0x00FF00)
        )
        emb.set_image(url="https://media.giphy.com/media/3og0IBXaw5Nz9VQcnK/giphy.gif")
        await client.send_message(message.channel, embed=emb)
    #Awaken
    if message.content.startswith('Jo!Awaken'):
        userID = message.author.id
        args = message.content[len('Jo!Awaken'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s>! The time has come! Awaken, my Masters!" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="http://pa1.narvii.com/6735/09fbc01e8792075656c4aecf7e120d37812da360_00.gif")
            await client.send_message(message.channel, embed=emb)         
        else:
            emb =(discord.Embed(
                description="<@%s>! The time has come! Awaken, my %s!" % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="http://pa1.narvii.com/6735/09fbc01e8792075656c4aecf7e120d37812da360_00.gif")
            await client.send_message(message.channel, embed=emb)
    #SHIIIZA
    if message.content.startswith('Jo!Caeser'):
        userID = message.author.id
        args = message.content[len('Jo!Caeser'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s>! This is the last of my Hamon! TAKE IT FROM ME!" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://pa1.narvii.com/6462/a9f272f1f526f422f2fb6254cfa50eec263a3fc1_hq.gif")
            await client.send_message(message.channel, embed=emb)         
        else:
            emb =(discord.Embed(
                description="%s! This is the last of <@%s>'s Hamon! TAKE IT FROM THEM!" % ("".join(args[0:]), userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://pa1.narvii.com/6462/a9f272f1f526f422f2fb6254cfa50eec263a3fc1_hq.gif")
            await client.send_message(message.channel, embed=emb)
    #Nice
    if message.content.startswith('Jo!Nice'):
        userID = message.author.id
        args = message.content[len('Jo!Nice'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="Niiiiiiiiiiiiiiice!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://media1.tenor.com/images/392da4650dfa83b3055069e39ad74b45/tenor.gif?itemid=7319727")
            await client.send_message(message.channel, embed=emb)         
        else:
            emb =(discord.Embed(
                description="<@%s> thinks %s is Niiiiiiiiice!" % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://media1.tenor.com/images/392da4650dfa83b3055069e39ad74b45/tenor.gif?itemid=7319727")
            await client.send_message(message.channel, embed=emb)
    #German Science
    if message.content.startswith('Jo!Nazi'):
        userID = message.author.id
        emb =(discord.Embed(
            description="FOOOOOL! <@%s>'s SCIENCE IS THE BEST IN THE WORLD!" % (userID),
            colour=0x00FF00)
        )
        emb.set_image(url="https://i.imgur.com/cru1jFG.gif")
        await client.send_message(message.channel, embed=emb)
    #Tequila Josephine
    if message.content.startswith('Jo!TJ'):
        userID = message.author.id
        emb =(discord.Embed(
            description="<@%s> brought you some tequila! Will you let them by?" % (userID),
            colour=0x00FF00)
        )
        emb.set_image(url="https://img.gifmagazine.net/gifmagazine/images/150162/original.gif")
        await client.send_message(message.channel, embed=emb)
    #Naisu
    if message.content.startswith('Jo!Naisu'):
        userID = message.author.id
        args = message.content[len('Jo!Naisu'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="Naisu, Naisu! Very Naisu, <@%s>-chan!" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/Q0MRXM.gif")
            await client.send_message(message.channel, embed=emb)         
        else:
            emb = (discord.Embed(
                description="Naisu, Naisu! Very Naiiisu, %s-chan!" % ("".join(args[0:])), 
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/Q0MRXM.gif")
            await client.send_message(message.channel, embed=emb)    
###Part 3
    #Menacing
    if message.content.startswith('Jo!Menacing'):
        userID = message.author.id
        args = message.content[len('Jo!Menacing'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s> is giving off a feeling of doom and gloom..." % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/original/000/525/409/efc.gif")
            await client.send_message(message.channel, embed=emb)         
        else:
            emb =(discord.Embed(
                description="%s is giving off a feeling of doom and gloom..." % ("".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/original/000/525/409/efc.gif")
            await client.send_message(message.channel, embed=emb)
    #ORAORAORA
    if message.content.startswith('Jo!ORA'):
        userID = message.author.id
        args = message.content[len('Jo!ORA'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="**ORAORAORAORAORAORAORAORAORAORAORAORA!**",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.imgur.com/1wb4XCj.gif")
            await client.send_message(message.channel, "<@%s> is ready to themselves a beatdown...?" % (userID))
            await client.send_message(message.channel, embed=emb)         
        else:
            emb =(discord.Embed(
                description="**ORAORAORAORAORAORAORAORAORAORAORAORA!**",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.imgur.com/1wb4XCj.gif")
            await client.send_message(message.channel, "<@%s> is ready to give %s a beatdown...!" % (userID, "".join(args[0:])))
            await client.send_message(message.channel, embed=emb)
    #RERORERORERORERO
    if message.content.startswith('Jo!Rero'):
        userID = message.author.id
        args = message.content[len('Jo!Rero'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="**LickLickLickLickLickLickLickLick...**",
                colour=0x00FF00)
            )
            emb.set_image(url="http://blog-imgs-64.fc2.com/y/a/r/yaraon/fa11703.gif")
            await client.send_message(message.channel, "Isn't that right, old pal <@%s>?" % (userID))
            await client.send_message(message.channel, embed=emb)        
        else:
            emb =(discord.Embed(
                description="**LickLickLickLickLickLickLickLick...**",
                colour=0x00FF00)
            )
            emb.set_image(url="https://thumbs.gfycat.com/SilkyHastyBlackbear-size_restricted.gif")
            await client.send_message(message.channel, "%s, are you gonna eat that cherry :cherries: ? They're <@%s>'s favorite..." % ("".join(args[0:]), userID))
            await client.send_message(message.channel, embed=emb)   
    #Old Joseph
    if message.content.startswith('Jo!OJ'):
        args = message.content.split(" ")
        userID = message.author.id
        #OH MY GOD!
        emb =(discord.Embed(
            colour=0x00FF00)
        )
        emb.set_image(url="https://thumbs.gfycat.com/SpeedyFewBlackcrappie-small.gif")    
        #OH GOD!
        emb3 =(discord.Embed(
            colour=0x00FF00)
        )
        emb3.set_image(url="https://j.gifs.com/W7VRXo.gif") 
        
        #SON OF A BITCH!
        emb4 =(discord.Embed(
            colour=0x00FF00)
        )
        emb4.set_image(url="https://j.gifs.com/86VlxW.gif")         
        #OOOOOH NOOOOO!
        emb5 =(discord.Embed(
            colour=0x00FF00)
        )
        emb5.set_image(url="https://j.gifs.com/KZDRkJ.gif") 
        #HOOOLY SHIIIIIT!
        emb6 =(discord.Embed( 
            colour=0x00FF00)
        )
        emb6.set_image(url="https://j.gifs.com/l51PPV.gif") 
        itemlist2 = [emb, emb3, emb4, emb5, emb6]
        await client.send_message(message.channel, embed=random.choice(itemlist2)  
        )
    #HAHAHAHHA
    if message.content.startswith('Jo!HAHA'):
        userID = message.author.id
        args = message.content[len('Jo!HAHA'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s> is laughing their head off!" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.imgur.com/41IGwZE.gif")
            await client.send_message(message.channel, embed=emb)  
    
        else:
            emb =(discord.Embed(
                description="<@%s> is laughing their head off at %s!" % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.imgur.com/41IGwZE.gif")
            await client.send_message(message.channel, embed=emb)  
    #YESIAM
    if message.content.startswith('Jo!Iam'):
        userID = message.author.id
        args = message.content[len('Jo!Iam'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="**YES! I AM!**",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/000/820/446/17f.gif")
            await client.send_message(message.channel, "You're <@%s>!??!" % (userID))
            await client.send_message(message.channel, embed=emb)
        else:
            emb =(discord.Embed(
                description="**YES! I AM!**",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/000/820/446/17f.gif")
            await client.send_message(message.channel, "You're %s!??!" % ("".join(args[0:])))
            await client.send_message(message.channel, embed=emb)
    #HELL2U
    if message.content.startswith('Jo!H2U'):
        userID = message.author.id
        args = message.content[len('Jo!H2U'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s>! HELL 2 U!" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/W7VR0o.gif")
            await client.send_message(message.channel, embed=emb)
        else:
            emb =(discord.Embed(
                description="%s! HELL 2 U!" % ("".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/W7VR0o.gif")
            await client.send_message(message.channel, embed=emb)
    #Iggy
    if message.content.startswith('Jo!Iggy'):
        userID = message.author.id
        args = message.content[len('Jo!Iggy'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s> has thrown Iggy at themselves...?" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="http://pa1.narvii.com/6580/e11ee49665993ef4d418af0ffb6e0adbd2925c9f_00.gif")
            await client.send_message(message.channel, embed=emb)   
        else:
            emb =(discord.Embed(
                description="<@%s> has thrown Iggy at %s!" % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="http://pa1.narvii.com/6580/e11ee49665993ef4d418af0ffb6e0adbd2925c9f_00.gif")
            await client.send_message(message.channel, embed=emb)   
    #GOODUH
    if message.content.startswith('Jo!Good'):
        emb =(discord.Embed(
            description="GOOD!",
            colour=0x00FF00)
        )
        emb.set_image(url="https://j.gifs.com/mQ5P9R.gif")
        await client.send_message(message.channel, embed=emb)
    #SCREAM
    if message.content.startswith('Jo!Scream'):
        emb =(discord.Embed(
            description="AAAAAAAAAAAAAAAAAAAH!",
            colour=0x00FF00)
        )
        emb.set_image(url="https://j.gifs.com/yrjnv6.gif")
        await client.send_message(message.channel, embed=emb)
    #THEWORLD(Maybe make it so that if an admin uses it, it freezes chat)
    if message.content.startswith('Jo!World'):
        emb =(discord.Embed(
            description=random.choice(["THE WORLD! OH TIME, STAND STILL!", "THE WORLD! THIS TIME IS MINE ALONE!", "THE WORLD! TIME GRINDS TO A HALT!", "THE WORLD! TIME STANDS STILL!", "THE WORLD! TIME BENDS TO MY WILL!"]),
            colour=0x00FF00)
        )
        await client.send_message(message.channel, embed=emb)
        await client.send_message(message.channel, "https://files.kapwing.com/final_5b7a18a1adea410014f58d33.mp4")
    #MUDA
    if message.content.startswith('Jo!Muda'):
        userID = message.author.id
        args = message.content[len('Jo!Muda'):].strip()
        if args == '':
            emb = (discord.Embed(
                description="<@%s> is Useless, Useless, USELESS, USELESS, USELESSUSELESSUSELESS!" % (userID), 
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/000/974/391/ece.gif")
            await client.send_message(message.channel, embed=emb)  
        else:
            emb = (discord.Embed(
                description="%s is Useless, Useless, USELESS, USELESS, USELESSUSELESSUSELESS!" % ("".join(args[0:])), 
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/000/974/391/ece.gif")
            await client.send_message(message.channel, embed=emb) 
    #ROADO ROLLA DA
    if message.content.startswith('Jo!RRD'):
        userID = message.author.id
        args = message.content[len('Jo!RRD'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="IT'S A ROAD ROLLER!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://lh3.googleusercontent.com/-wwlWz0TgKkA/Vqop31NfCmI/AAAAAAAAANw/uC_p2kj7sXE/w500-h286-n/ROAD%2BROLLER%2BDA.gif")
            await client.send_message(message.channel, "<@%s> has a suprise for themselves...?" % (userID))
            await client.send_message(message.channel, embed=emb)
  
        else:
            emb =(discord.Embed(
                description="IT'S A ROAD ROLLER!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://lh3.googleusercontent.com/-wwlWz0TgKkA/Vqop31NfCmI/AAAAAAAAANw/uC_p2kj7sXE/w500-h286-n/ROAD%2BROLLER%2BDA.gif")
            await client.send_message(message.channel, "<@%s> has a suprise for %s..." % (userID, "".join(args[0:])))
            await client.send_message(message.channel, embed=emb)
###Part 4
    #GreatoDaze
    if message.content.startswith('Jo!Great'):
        userID = message.author.id
        args = message.content[len('Jo!Great'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="That's just great!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/ZV1RK5.gif")
            await client.send_message(message.channel, embed=emb) 
        else:
            emb =(discord.Embed(
                description="%s is just great!" % ("".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/ZV1RK5.gif")
            await client.send_message(message.channel, embed=emb)
    #Gun
    if message.content.startswith('Jo!Delet'):
        userID = message.author.id
        args = message.content[len('Jo!Delet'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s> has a secret message for themselves...?" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/190/025/848.gif")
            await client.send_message(message.channel, embed=emb) 
        else:
            emb =(discord.Embed(
                description="<@%s> has a secret message for %s..." % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/190/025/848.gif")
            await client.send_message(message.channel, embed=emb) 
    #RohanSpider
    if message.content.startswith('Jo!Spider'):
        userID = message.author.id
        emb =(discord.Embed(
            description="<@%s> Needs to get the taste of a spider..." % (userID),
            colour=0x00FF00)
        )
        emb.set_image(url="https://i.imgur.com/6MVIh19.gif")
        await client.send_message(message.channel, embed=emb)   
    #QuietLife
    if message.content.startswith('Jo!Quiet'):
        userID = message.author.id
        emb =(discord.Embed(
            description="<@%s> just wants to live a quiet life..." % (userID),
            colour=0x00FF00)
        )
        emb.set_image(url="https://78.media.tumblr.com/10b5b5cc1d2167c7553345b022e95cde/tumblr_oh9ais5Grf1sfay15o3_500.gif")
        await client.send_message(message.channel, embed=emb)     
    #Crying
    if message.content.startswith('Jo!Cry'):
        userID = message.author.id
        emb =(discord.Embed(
            description="<@%s> can't stop crying their eyes out..." % (userID),
            colour=0x00FF00)
        )
        emb.set_image(url="https://i.imgur.com/yGT41Vn.gif")
        await client.send_message(message.channel, embed=emb)  
    #FUCKIN A
    if message.content.startswith('Jo!Yum'):
        userID = message.author.id
        args = message.content[len('Jo!Yum'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="<@%s> loves the taste of Tonio's cooking!" % (userID),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/E9wBMY.gif")
            await client.send_message(message.channel, embed=emb)  
        else:
            emb =(discord.Embed(
                description="<@%s> loves the taste of %s!" % (userID, "".join(args[0:])),
                colour=0x00FF00)
            )
            emb.set_image(url="https://j.gifs.com/E9wBMY.gif")
            await client.send_message(message.channel, embed=emb)  
    #BITES THE DUST!
    if message.content.startswith('Jo!BTD'):
        userID = message.author.id
        args = message.content[len('Jo!BTD'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="KILLER QUEEN! ACTIVATE THIRD BOMB! BITES THE DUST!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/original/001/204/707/54b.gif")
            await client.send_message(message.channel, embed=emb)
            await client.send_message(message.channel, "<@%s>! Killer Queen's third bomb, Bites The Dust, has already entered your eye! That is what you are seeing." % (userID))
            await client.send_message(message.channel, "***Click!***")  
        else:
            emb =(discord.Embed(
                description="KILLER QUEEN! ACTIVATE THIRD BOMB! BITES THE DUST!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/original/001/204/707/54b.gif")
            await client.send_message(message.channel, embed=emb)
            await client.send_message(message.channel, "**%s!** Killer Queen's third bomb, Bites The Dust, has already entered your eye! That is what you are seeing." % ("".join(args[0:])))
            await client.send_message(message.channel, "***Click!***")  
    #Ambulance
    if message.content.startswith('Jo!Stop'):
        userID = message.author.id
        args = message.content[len('Jo!Stop'):].strip()
        if args == '':
            emb =(discord.Embed(
                description="STOP! STOOOP!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/202/920/84f.gif")
            await client.send_message(message.channel, "<@%s>'s ON THE GROUND DOWN THERE!" % (userID))  
            await client.send_message(message.channel, embed=emb)
        else:
            emb =(discord.Embed(
                description="STOP! STOOOP!",
                colour=0x00FF00)
            )
            emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/202/920/84f.gif")
            await client.send_message(message.channel, "%s's ON THE GROUND DOWN THERE!" % ("".join(args[0:])))  
            await client.send_message(message.channel, embed=emb)


#Runs the bot    
client.run("<insert your token here>")


