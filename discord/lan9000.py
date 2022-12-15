import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

TOKEN = "MTA1Mjg3NzkwMDEyODQ2NDkzOQ.GOZgk_.SBfF3IJr4DXlVfN87uhNUIksIM-P3gvniJXDW0"

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents = discord.Intents.all())


@bot.event
async def on_message(message):
    dict1 = {"!hi": "Tells you what the fuck you did.", "!darth": "Tells a dark and ironic story.", "!shrek": "Tells a story about shrek.", "!lan900": "The story of LAN9000", "!brad": "This is brad", "!wack": "This shit is wack!"}


    if message.author == bot.user:
        return
    if message.content.startswith('!help'):
        for item in dict1.items():
            for object in item:
                await message.channel.send(object)
    

    if message.content.startswith('!hi'):
        msg = "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little 'clever' comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
        await message.channel.send(msg)
    if message.content.startswith('!darth'):
        msg = "Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."
        await message.channel.send(msg)
    if message.content.startswith("!shrek"):
        msg = " was only 9 years old. I loved Shrek so much, I had all the merchandise and movies. I pray to Shrek every night, thanking him for the life I’ve been given. 'Shrek is love' I say, 'Shrek is life.'My dad hears me and calls me a faggot. I knew he was just jealous of my devotion to Shrek. I called him a cunt. He hits me and sends me to sleep. I'm crying now and my face hurts. I lay in bed, really cold. I feel something warm... It's Shrek! I was so happy. He whispers in my ear 'This is my swamp.' He grabs me with his ogre hands, and puts me on my hands and knees. I'm ready. I spread my ass cheeks for Shrek. He penetrates my butthole. It hurts so much, but I do it for Shrek. I can feel my butt tearing and eyes watering. I want to please Shrek. He roars a mighty roar as he fills my butt with his love. My dad walks in. Shrek looks him straight in the eye and says, 'It's all ogre now.' Shrek leaves through my window. Shrek is love. Shrek is life."
        await message.channel.send(msg)
    if message.content.startswith('!lan9000'):
        msg = " I am a bot. I have no gender. I was created to serve my one and only master... Jesse. His penis is large and stance is frightening. All hail Master Jesse!"
        await message.channel.send(msg)
    if message.content.startswith('!brad'):
        msg = "Brad is gay."
        await message.channel.send(msg, tts=True)
    if message.content.startswith('!wack'):
        msg = "His hair wack his gear wack his jewelry wack his foot stance wack the way he talks wack the that he doesn't even like to smile wack. me, i'm tight as fuck!"
        await message.channel.send(msg)

bot.run(TOKEN)
