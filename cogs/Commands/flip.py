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
    
    @command.commands(aliases=['coin'])
    async def flip(self, ctx):
        sides = ['heads', 'tails']
        msg = await ctx.send("Flipping Coin...")
        asyncio.sleep(1)
        await msg.delete()
        await ctx.send(random.choice(sides))


def setup(client):
    client.add_cog(Main(client))