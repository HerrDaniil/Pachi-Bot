import discord
from discord.ext import commands
from tokens import *
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("My name is Kira Yoshikage and I'm ready to start working")

@client.event
async def on_member_join(member):

    channel = client.get_channel(1292233022640361548)

    responses = [
        f"{member.display_name}, you amazing!",
        f"Это же {member.display_name}! Сколько же мы его ждали!",
        f"Это же наш любимый {member.display_name}!",
    ]

    response = random.choice(responses)
        
    await channel.send(response)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1292233022640361548)
    await channel.send("SKIBIDI SIGMA, {member.display_name}, LEFT THE SERVER NOOOOOOOOOOO")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'you amazing' in message.content.lower():
        responses = [
            f"Нет, {message.author.display_name}, you amazing!",
            f"Спасибо за комплимент, но хочу сказать, что you amazing!",
            f"{message.author.display_name}, я конечно amazing, но ты просто amazing",
        ]

        response = random.choice(responses)
        
        await message.channel.send(response)

@client.command()
async def hello(ctx):
    await ctx.send("Hello, Dexter Morgan")

client.run(ToshaToken)
