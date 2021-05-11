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

cogs = [
    ''
]

class client(commands.AutoShardedBot):
    def __init__(self):
        with open("settings.json", "r") as f:
            data = json.load(f)
        prefix = data['prefix']

        super().__init__(command_prefix=prefix, case_insensitive=True)
    
    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server Cringe"))

        print()
        print("-------------------------------")
        print("Bot Online")
        print('Logged In As: ',client.user.name)
        print('ID: ',client.user.id)
        print('Discord Version: ',discord.__version__)
        print('-------------------------------')
        print()
        print()

        for cog in cogs:
            try:
                client.load_extension(cog)
                print(f"Loaded Cog {cog}")
            except Exception as e:
                print(f"Error on Loading {cog}. Error is {e}")

client = client()
client.remove_command('help')

@client.command(pass_context=True)
async def reload(ctx, cog=None):
    if not int(ctx.author.id) in client.devs:
        return
    if not cog:
        return
    try:
        client.reload_extension(cog)
        await ctx.message.add_reaction('✅')
        msg = await ctx.send(f"Reloading **{cog}**")
        await asyncio.sleep(20)
        await msg.delete()
    except Exception as e:
        await ctx.message.add_reaction('❌')
        msg = await ctx.send(f"<@291360056002215937> umm... **{cog}**!\n```{e}```")
        dev_logs = client.get_channel(665553350355582986)
        mod_logs = client.get_channel(477356858051526656)
        await asyncio.sleep(20)
        await msg.delete()
        await dev_logs.send(f"<@291360056002215937> umm... **{cog}**!\n```{e}```")
        await mod_logs.send(f"<@291360056002215937> umm... **{cog}**!\n```{e}```")



with open("settings.json", "r") as f:
    data = json.load(f)
token = data['token']

client.run(token)