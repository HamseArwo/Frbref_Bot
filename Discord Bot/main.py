import discord
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


async def main():
    await client.load_extension("player")
    await client.load_extension("team")
    await client.load_extension("score")
    await client.load_extension("assist")
    await client.load_extension("cleansheet")

    await client.start("BOT TOKEN")

asyncio.run(main())
