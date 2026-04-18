import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
        self.role_id = int(os.getenv('WELCOME_ROLE_ID'))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.channel_id)

        role = member.guild.get_role(self.role_id)
        if role:
            await member.add_roles(role)
            print(f"{member.name} got {role.name} role.")

        if channel:
            embed = discord.Embed(
                title=f"Welcome,  {member.name}!",
                description=f"We're glad you are here!",
                color=discord.Color.green()
            )

async def setup(bot):
    await bot.add_cog(Welcome(bot))
