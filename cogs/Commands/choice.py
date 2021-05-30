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
    
    @commands.command(aliases=['choose'])
    async def choice(self, ctx, arg1=None, arg2=None, arg3=None, arg4=None):
        if (arg1 == None):
            msg = await ctx.send("Required 2 Arguments, but up to 4")
            asyncio.sleep(10)
            await msg.delete()
            await ctx.message.delete()
        elif (arg2 == None):
            msg = await ctx.send("Required 2 Arguments, but up to 4")
            asyncio.sleep(10)
            await msg.delete()
            await ctx.message.delete()
        else:
            if (arg3 == None):
                choices = [arg1, arg2]
                await ctx.send(f"I choose {random.choice(choices)}")
            elif (arg3 != None and arg4 == None):
                choices = [arg1, arg2, arg3]
                await ctx.send(f"I choose {random.choice(choices)}")
            elif (arg3 != None and arg4 != None):
                choices = [arg1, arg2, arg3, arg4]
                await ctx.send(f"I choose {random.choice(choices)}")


def setup(client):
    client.add_cog(Main(client))