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
    
    @commands.command()
    async def hide(self, ctx):
        if (ctx.message.author.id == 291360056002215937):
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=False)
            embed=discord.Embed(title="HIDDEN", description=f"**Hidden By:** <@{ctx.author.id}>", color=0xff0000)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(1)
            await ctx.message.delete()
        else:
            msg = await ctx.send("mhm...")
            await asyncio.sleep(2)
            await msg.delete()
            await ctx.message.delete()
        
    @commands.command()
    async def show(self, ctx):
        if (ctx.message.author.id == 291360056002215937):
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
            embed=discord.Embed(title="Revealed", description=f"**Revealed By:** <@{ctx.author.id}>", color=0x00ff00)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(1)
            await ctx.message.delete()
        else:
            msg = await ctx.send("mhm...")
            await asyncio.sleep(2)
            await msg.delete()
            await ctx.message.delete()


def setup(client):
    client.add_cog(Main(client))