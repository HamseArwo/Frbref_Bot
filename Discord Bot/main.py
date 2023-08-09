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

    await client.start("MTEzNTYxOTY0MzQ5OTg4NDYyNg.G-PdbQ.rewcunI_E-K9q5UBiUgzUAOd2ley85sNdRbwKA")

asyncio.run(main())
