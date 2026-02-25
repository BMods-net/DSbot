import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def load_extensions():
    for filename in os.listdir('./handlers'):
        if filename.endswith('.py'):
            await bot.load_extension(f'handlers.{filename[:-3]}')
            print(f'Module {filename} completed')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

# Запускаем асинхронную функцию
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot turned off")