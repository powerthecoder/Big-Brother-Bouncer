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
    async def on_message_delete(self, message):
        if (message.guild_id == 806000095866650655):
            embed=discord.Embed(title="Deleted Message", description=f"**Author**: {message.author.mention} \n**Message**: {message.content} \n**Channel:** <#{message.channel_id}>")
            await self.console_log.send(embed=embed)
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            log = open("/home/leo/ftp/Discord/Big-Brother-Bouncer/cogs/Events/deleted_messages_log.txt", "w")
            log.write(f"{current_time}  |  {message.author.mention}  |  {message.content}")
            log.close()
        else:
            pass

def setup(client):
    client.add_cog(Main(client))