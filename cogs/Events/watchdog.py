import os
import sys
import time
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from discord.ext.commands import MissingPermissions
from discord.utils import find
from discord.utils import get
import asyncio
import json
import datetime
from datetime import datetime

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.console_log = client.get_channel(848439854483636254)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        x = 0

        suicidal_1 = ["kill", "suicide", "end", "hang", "help", "die", "kys"]
        suicidal_2 = ["me", "commit", "myself", "I want to", "I", "I should just", "I should", "my life", "my self"]
        for i in suicidal_1:
            for z in suicidal_2:
                if (i in message.content) and (z in message.content):
                    if (x != 1):
                        now = datetime.now()
                        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        log = open("/home/leo/ftp/Discord/Big-Brother-Bouncer/cogs/Events/watchdog.txt", "a")
                        log.write(f"{current_time}  |  {message.author.name}  |  {message.content}\n")
                        log.close()
                        embed=discord.Embed(title="LOOK FOR", description=f"**User:** <@{message.author.id}> \n**Message:** {message.content}\n**Channel:** {message.channel}\n\n**Reason For Warning:** \nSuicidal Thoughts", color=0xFF0000)
                        user = self.client.get_user(291360056002215937)
                        await user.send(embed=embed)
                        x += 1
                    else:
                        pass
                else:
                    pass



def setup(client):
    client.add_cog(Main(client))