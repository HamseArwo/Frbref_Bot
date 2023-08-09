import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
from connection import DataBaseConnection


class Score(commands.Cog, DataBaseConnection):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def score(self, ctx):
        self.embed = discord.Embed(
            title="Top Scorers", description="", colour=discord.Colour.blue())
        self.embed.set_author(
            name="Premier League", icon_url="https://www.pngkit.com/png/full/213-2133496_premier-league-and-fa-cup-premier-league-logo.png")

        players = self.player_collection.find().sort("goals", pymongo.DESCENDING)

        self.field_name = [f"🥇{players[0]['name']}", f"⚽ {players[0]['goals']}G", f"{players[0]['club']} 🔵",
                           f"🥈{players[1]['name']}", f"⚽ {players[1]['goals']}G", f"{players[1]['club']} ⚪",
                           f"🥉{players[2]['name']}", f"⚽ {players[2]['goals']}G", f"{players[2]['club']} 🔴",
                           f"🎖️{players[3]['name']}", f"⚽ {players[3]['goals']}G", f"{players[3]['club']} 🔴",
                           f"🎖️{players[4]['name']}", f"⚽ {players[4]['goals']}G", f"{players[4]['club']} ⚪⚫",]

        for name in self.field_name:
            self.embed.add_field(name=name, value="", inline=True)

        # self.embed.video()

        self.embed.set_image(
            url="https://resources.premierleague.com/premierleague/photo/2023/05/28/27c4eec7-49c2-4abe-a081-ec1d27a2311e/2023-05-28T173847Z_1871495450_UP1EJ5S1D0K97_RTRMADP_3_SOCCER-ENGLAND-BRE-MCI-REPORT.JPG")
        await ctx.send(embed=self.embed)


async def setup(bot):
    await bot.add_cog(Score(bot))
