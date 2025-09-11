import discord
from discord.ext import commands
import film as film 
from film import *
import random
import asyncio
import os
import json
from dotenv import load_dotenv
from discord.errors import LoginFailure

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


with open('film.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
random_film = random.choice(data["Films"])

@bot.command()
async def watch(ctx):
    await ctx.send('Welchen Film wir wohl heute schauen werden?')
    await asyncio.sleep(1)
    film.main_film()
    await ctx.send('Die Antwort ist dum dum dum...')
    await asyncio.sleep(3)
    await ctx.send(f"---------{random_film['titel']}---------")



@bot.command()
async def play(ctx):
    await ctx.send('Wanna play a number guessing game?')
    await asyncio.sleep(1)
    await ctx.send('Give me a Number from 1 to 10: ')
    
    number = random.randint(1, 10)
    #await ctx.send(f'Solution: {number}')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    while True:
        try:
            guess_msg = await bot.wait_for('message', check=check)
            guess = int(f'{guess_msg.content}')

            if guess < number:
                await ctx.send('Your Guess is too low. ')
                await ctx.send('Try again!')
            
            elif guess > number:
                await ctx.send('Your Guess is too high')
                await ctx.send('Try again!')
                
            elif guess == number:
                await ctx.send('Yaaay You won')
                
                break
        except ValueError:
            await ctx.send('Give me a valid Number from 1 to 10!')

    await asyncio.sleep(1)    
    await ctx.send('See you next time.')


@bot.command()
async def rpc(ctx):
    await ctx.send('Wanna play rock, paper or scissors?')

    #Rock Paper Scissors Game - Discord bot



if not TOKEN:
    raise RuntimeError(
        "Environment variable DISCORD_TOKEN is missing. Set it in .env or Docker Compose."
    )

try:
    bot.run(TOKEN)
except LoginFailure:
    # Invalid token -> provide a clear, actionable message
    raise SystemExit(
        "Login failed: Your DISCORD_TOKEN appears to be invalid. "
        "Create a new bot token in the Discord Developer Portal and update your .env."
    )