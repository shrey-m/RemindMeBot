# RemindMeBot.py
import os
from dotenv import load_dotenv

from datetime import datetime
import threading

import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='!')#discord.Client()

def checkTime(time):
    # This function runs periodically every 1 second
    threading.Timer(1, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)

    if(current_time == time):  # check if matches with the desired time
        return "time"
    return current_time

def find_time(string, first, last):
    try:
        start = string.index(first) + len(first)
        end = string.index(last, start)
        return string[start:end]
    except ValueError:
        return ""

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "Generic Reminder"
    flag = False
    if message=="Generic Reminder":
        checkTime(find_time(message,"{","}"))
        while not flag:
            checkTime(find_time(message,"{","}"))
            if checkTime(find_time(message,"{","}"))=="time":
                flag = True
        
            
    await user.send(message)



#@client.command()
#async def send_anonymous_dm(ctx, member: discord.Member, *, content):
#    channel = await member.create_dm() # creates a DM channel for mentioned user
#    await channel.send(content) # send whatever in the content to the mentioned user.

load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))
