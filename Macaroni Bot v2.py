import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")



@client.event
async def on_ready():
    print ("Bot is ready!")

@client.event
async def on_message(message):
           if message.content.upper().startswith ('!PING')
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Pong!" % (userID))











client.run ("NDE5NDU2NTE1OTEzNTQ3Nzc2.DXwbRQ.LLkNwaNrBCf2sXgjDPKFhsSzPJE")
