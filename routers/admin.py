import discord
from discord.ext import commands
import datetime

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    @commands.has_any_role("admin", "moderator")
    async def purge(self, ctx, amount:int):
        await ctx.channel.purge(limit=amount + 1)
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"{ctx.author.mention}, you're not an admin.", delete_after=6)

    @commands.command(name="mute")
    @commands.has_any_role("admin", "moderator")
    async def timeout(self, ctx, member: discord.Member, minutes: int, *, reason:str):
        duration = datetime.timedelta(minutes=minutes)
        try:
            await member.timeout(duration, reason=reason)

            embed = discord.Embed(
                title="Muted",
                description=f"{member.mention} can't write for {minutes} minutes. Reason: {reason}.",
                color=discord.Color.red()
            )
            embed.add_field(name="Duration", value=f"{minutes} minutes.")
            embed.add_field(name="Reason", value=reason)

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Can't mute: {e}")

    @commands.command(name="unmute")
    @commands.has_any_role("admin", "moderator")
    async def unmute(self, ctx, member: discord.Member):
        await member.timeout(None)
        await ctx.send(f"{member.mention} can has been unmuted.")
    @timeout.error
    async def timeout_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to write this command.")

    @commands.command(name="ban")
    @commands.has_role("admin")
    async def ban(self, ctx, member: discord.Member, *, reason):
        try:
            try:
                await member.send(f"You have been baned on {ctx.guild.name} server. Reason: {reason}")
            except:
                pass

            await member.ban(reason=reason)

            embed = discord.Embed(
                title="Ban",
                description=f"{member} has been banned.",
                color=discord.Color.dark_red()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.add_field(name="Admin", value=ctx.author.mention)
            embed.add_field(name="Reason", value=reason)

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"You can't ban: {e}")
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You can't ban someone.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("User not found.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
