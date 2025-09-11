import discord
import film as film
import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):  
    async def play1(self):
        film.main_film()


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(TOKEN)
