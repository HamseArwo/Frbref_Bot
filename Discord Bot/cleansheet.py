import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
from connection import DataBaseConnection


class Cleansheets(commands.Cog, DataBaseConnection):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def save(self, ctx):
        self.embed = discord.Embed(
            title="Most Clean Sheets", description="", colour=discord.Colour.red())
        self.embed.set_author(
            name="Premier League", icon_url="https://www.pngkit.com/png/full/213-2133496_premier-league-and-fa-cup-premier-league-logo.png")

        players = self.gk_collection.find().sort([(
            "clean_sheets", pymongo.DESCENDING), ("name", pymongo.DESCENDING)])

        self.field_name = [f"🥇{players[0]['name']}", f"🧤 {players[0]['clean_sheets']}CLS", f"{players[0]['club']} 🔴",
                           f"🥈{players[1]['name']}", f"🧤 {players[1]['clean_sheets']}CLS", f"{players[1]['club']} ⚪⚫",
                           f"🥉{players[2]['name']}", f"🧤 {players[2]['clean_sheets']}CLS", f"{players[2]['club']} 🔴",
                           f"🎖️{players[3]['name']}", f"🧤 {players[3]['clean_sheets']}CLS", f"{players[3]['club']} 🔴",
                           f"🎖️{players[4]['name']}", f"🧤 {players[4]['clean_sheets']}CLS", f"{players[4]['club']} 🔴",]

        for name in self.field_name:
            self.embed.add_field(name=name, value="", inline=True)

        # self.embed.set_thumbnail(
        #     url="https://i.ytimg.com/vi/dhKZVbGi2lg/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBMOLLzaHP-2nRbnWYq-3vGuSZ1HA")

        # self.embed.add_field(
        #     name="Click here to see some of the BEST {players[0]['name']} SAVES 👇",
        #     value=f"https://www.youtube.com/watch?v=dhKZVbGi2lg&pp=ygUbZGF2aWQgZGUgZ2VhIGdvbGRlbiBnbG92ZSAg",
        #     inline=False)

        # self.embed.video(
        #     url="https://www.youtube.com/watch?v=pP8r4yDPnyE", height=100, width=100)

        self.embed.set_image(
            url="https://resources.premierleague.com/premierleague/photo/2023/06/01/c622c1b6-9525-4908-819b-2bc6e9106fdc/David-De-Gea-202223-Golden-Glove.JPG")
        await ctx.send(embed=self.embed)


async def setup(bot):
    await bot.add_cog(Cleansheets(bot))
