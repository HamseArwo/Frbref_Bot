import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
from connection import DataBaseConnection


class Assist(commands.Cog, DataBaseConnection):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def assist(self, ctx):
        self.embed = discord.Embed(
            title="Top Asissters", description="", colour=discord.Colour.blue())
        self.embed.set_author(
            name="Premier League", icon_url="https://www.pngkit.com/png/full/213-2133496_premier-league-and-fa-cup-premier-league-logo.png")

        players = self.player_collection.find().sort([(
            "assist", pymongo.DESCENDING), ("name", pymongo.DESCENDING)])

        self.field_name = [f"🥇{players[0]['name']}", f"🎯 {players[0]['assist']}A", f"{players[0]['club']} 🔵",
                           f"🥈{players[1]['name']}", f"🎯 {players[1]['assist']}A", f"{players[1]['club']} 🔴",
                           f"🥉{players[2]['name']}", f"🎯 {players[2]['assist']}A", f"{players[2]['club']} 🔵",
                           f"🎖️{players[3]['name']}", f"🎯 {players[3]['assist']}A", f"{players[3]['club']} 🟣",
                           f"🎖️{players[4]['name']}", f"🎯 {players[4]['assist']}A", f"{players[4]['club']} 🔴",]

        for name in self.field_name:
            self.embed.add_field(name=name, value="", inline=True)

        # self.embed.video(
        #     url="https://www.youtube.com/watch?v=pP8r4yDPnyE")

        self.embed.set_image(
            url="https://resources.premierleague.com/photos/2023/06/07/efe006e1-30d0-405b-be61-6b5c2cd1edd1/KDB.png?width=1400&height=800")
        await ctx.send(embed=self.embed)


async def setup(bot):
    await bot.add_cog(Assist(bot))
