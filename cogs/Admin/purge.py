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

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['nuke'])
    async def purge(self, ctx, arg=None):
        if (ctx.message.author.id == 291360056002215937):
            if (arg == None):
                msg = await ctx.send("Please enter how many messages you want to delete!")
            else:
                await ctx.channel.purge(limit=int(arg))
        else:
            msg = await ctx.send("mhm...")
            await asyncio.sleep(2)
            await msg.delete()
            await ctx.message.delete()
        


def setup(client):
    client.add_cog(Main(client))