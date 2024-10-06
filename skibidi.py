import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("My name is Kira Yoshikage and i'm ready to start working")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, Dexter Morgan")

client.run('MTI5MjI3MjYyNTg1ODY0NjA3Ng.Ggi6-E.uIOx_BAskw9QMf19a-U7qE-mwGBdXVbdXUBOd8')