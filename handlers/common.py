import discord
from discord.ext import commands

class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send("Nothing for now...")

    @commands.command(name="repos")
    async def test(self, ctx):
        await ctx.send("Nothing for now...")

async def setup(bot):
    await bot.add_cog(Common(bot))
