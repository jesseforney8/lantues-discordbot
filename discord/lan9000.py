import os
import sys
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import random
from datetime import datetime
import pokebase as pd

#pokemon lookup function
def pokedex_lookup(name):

    try:
    
        pokemon_ = pd.pokemon(name)

        pokemon_type = ""
        p_type_list = []

        #iterates thru types and appends them to string withg comma
        for t in pokemon_.types:
            
            p_type_list.append(str(t.type))
            pokemon_type = ", ".join(p_type_list)
            pokemon_type += "."

        
        pokemon_height = pokemon_.height
        name = str(name).capitalize()

        return f"Name: {name}\nElement Type: {pokemon_type}\nHeight: {pokemon_height}"
    
    except:
        return "Could not find Pokemon. :("




#pull in token to start discord bot session
TOKEN = os.environ.get('TOKEN')
load_dotenv()
intents = discord.Intents.all()


bot = commands.Bot(command_prefix="!", case_insensitive=True, intents = intents)

#starts discord message event
@bot.event
async def on_message(message):
    dict1 = {"!hi": "Tells you what the fuck you did.", "!darth": "Tells a dark and ironic story.", "!shrek": "Tells a story about shrek.", "!lan900": "The story of LAN9000", "!brad": "This is brad", "!wack": "This shit is wack!"}

    #prevents bot from looping
    if message.author == bot.user:
        return
    if message.content.startswith('!help'):
        for item in dict1.items():
            for object in item:
                await message.channel.send(object)
    
    #random memes from !command
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
    if message.content.startswith('!myria'):
        msg = "Myria is gay. :wtf:"
        await message.channel.send(msg, tts=True)
    if message.content.startswith('!ass'):
        msg = "Wanna eat my ass? hehe"
        await message.channel.send(msg, tts=True)
    if message.content.startswith('!meow'):
        msg = "MEEEOWWW!"
        await message.channel.send(msg, tts=True)
    if message.content.startswith("!james"):
        james_list = ["Fuck you James!", "I love James!"]
        msg = random.choice(james_list)
        await message.channel.send(msg)

    #randomly picks poop fact from poop fact list    
    if message.content.startswith('!poop'):
        poop_facts = ["Wanna eat my ass? hehe", "Poop is mostly water.",
                       "Trillions of bacteria live in your poop :)"," Fiber is your friend.", "The perfect poop looks like a sausage.",
                       "Poop is mostly water", "Poop can look bloody from red food.", "You can’t digest corn.", "Babies have the strangest poop.",
                        "Squatting helps you poop.", "Stepstools help you poop.", "Poop transplants are real.", "Jesse poops green way too much."
                     ]

        msg = random.choice(poop_facts)
        await message.channel.send(msg)

    #tells current time
    if message.content.startswith("!time"):
        now = datetime.now()
        if now.hour < 12:
            hour = now.hour
            day_night = "AM"
        else:
            hour = now.hour - 12
            day_night = "PM"

        current_time = f"{hour}:{now.minute}{day_night}"
        await message.channel.send(current_time)

    #pulls pokemon info based off pokemon name after !pokemon command
    if message.content.startswith('!pokemon'):
        pokemon_name = message.content.split(" ")[-1]
        await message.channel.send(pokedex_lookup(pokemon_name))

    

    if message.content.startswith("!weather"):
        msg = "https://bit.ly/lan_weather"
        await message.channel.send(msg)

    if message.content.startswith("!cody"):
        cody_list = ["Cody is a cuck with a small pee pee!", "Cody is a black stallion with a big cock!"]
        msg = random.choice(cody_list)
        await message.channel.send(msg)
    if message.content.startswith("!johnny"):
        msg = "GSY GSY GSY"
        await message.channel.send(msg)

#bonk functionality
    if message.content.startswith('!bonk'):
        try:
            user_to_bonk = message.mentions[0]
            if user_to_bonk.voice is None:
                await message.channel.send("User is not in a voice channel, we can't bonk them!")
                return

            # Move user to bonk channel
            bonk_channel_id = 1279111855796654142
            #bonk_channel_id = 1279098714501415064
            original_channel = user_to_bonk.voice.channel
            voice_channel = bot.get_channel(bonk_channel_id)
            await user_to_bonk.move_to(voice_channel)

            # Play sound
            sound_path = "bonk.mp3"
            voice_client = await voice_channel.connect()
            source = discord.FFmpegPCMAudio(sound_path)
            voice_client.play(source)

            # Send a message after moving the user
            await message.channel.send(f"{user_to_bonk.mention} has been bonked!")

            # Wait for 5 seconds
            await asyncio.sleep(3)

            # Move user back to original channel
            #original_channel = user_to_bonk.voice.channel
            await user_to_bonk.move_to(original_channel)

            # Disconnect from voice channel
            await voice_client.disconnect()
        except Exception as e:
            print(f"Error: {e}")


    #roll dice function

bot.run(TOKEN)
