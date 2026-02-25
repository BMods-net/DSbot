import discord
from discord.ext import commands

class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send(f"Nothing for now...\n"
                       f"tedt\n"
                       f"fafwdgryg\n",
                       delete_after=5)

async def setup(bot):
    await bot.add_cog(Common(bot))
