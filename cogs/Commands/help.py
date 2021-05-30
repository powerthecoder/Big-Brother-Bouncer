import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.utils import get
import asyncio

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help Menu",description="Prefix - \n<> Required \n[] Optional")
        embed.add_field(name=".help", value="This Menu", inline=False)
        embed.add_field(name=".choice <arg1,arg2,arg3,arg4>", value="Bot randomly chooses a choice. Up to 4 choices", inline=False)
        embed.add_field(name=".flip", value="Bot flips a coin", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))