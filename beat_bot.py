# Libraries
import discord
from discord.ext import commands


token = "TOKEN HERE"
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")
    
client.run(token)
