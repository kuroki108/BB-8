import discord
from discord.ext import commands
import random
import asyncio
import os
import json
from discord.errors import LoginFailure
from dotenv import load_dotenv


load_dotenv() 

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


with open('film.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@bot.command()
async def watch(ctx):
    random_film = random.choice(data["titles"])  # Jedes Mal ein neuer Film!
    await ctx.send('Welchen Film wir wohl heute schauen werden?')
    await asyncio.sleep(1)
    await ctx.send('Die Antwort ist dum dum dum...')
    await asyncio.sleep(3)
    await ctx.send(f"---------{random_film['titel']}---------")



if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except LoginFailure:
        raise SystemExit(
            "Login failed: Your DISCORD_TOKEN appears to be invalid. "
            "Create a new bot token in the Discord Developer Portal and update your .env."
        )