import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.report_channel_id = int(os.getenv('REPORTS_CHANNEL_ID'))
        report_channel_id:int = int(os.getenv('REPORTS_CHANNEL_ID'))
        if report_channel_id:
            self.report_channel_id = int(report_channel_id)
        else:
            print("Report channel id is not found")

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send(f"Nothing for now...\n"
                       f"tedt\n"
                       f"fafwdgryg\n",
                       delete_after=5)

    @commands.command(name="reportm")
    async def report(self, ctx, member: discord.Member, *, reason:str):
        report_channel = self.bot.get_channel(self.report_channel_id)

        if not report_channel:
            return await ctx.send("Error: can't find a report channel.", delete_after=5)

        embed = discord.Embed(
            title="NEW REPORT",
            description=f"Reported to {member.mention}",
            color=discord.Color.orange()
        )
        embed.add_field(name="Reason:", value=reason)
        embed.add_field(name="Sent by:", value=ctx.author.name)
        embed.add_field(name="Link for message:", value=f"[Go to message]({ctx.message.jump_url})", inline=False)

        await report_channel.send(embed=embed)
        await ctx.message.delete()
        await ctx.send("Report sent. Thanks!", delete_after=4)

async def setup(bot):
    await bot.add_cog(Common(bot))
