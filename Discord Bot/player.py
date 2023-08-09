import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
from connection import DataBaseConnection


class Player(commands.Cog, DataBaseConnection):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is running!")

    @commands.command()
    async def player(self, ctx, *, player):
        # print(self.name)

        self.is_gk = False
        self.embed = discord.Embed(
            title=player, description="", colour=discord.Colour.random())

        self.player_dict = self.player_collection.find_one(
            {"name": f"{player}"})

        if self.player_dict == None:
            self.player_dict = self.gk_collection.find_one(
                {"name": f"{player}"})
            self.is_gk = True

        self.team_dict = self.team_collection.find_one(
            {'team': f"{self.player_dict['club']}"})

        # self.embed.set_thumbnail(url=self.player_dict['image'])

        self.embed.set_author(
            name=f"{self.player_dict['club']}", icon_url=self.team_dict['image'])
        self.embed.set_image(url=self.player_dict['image'])

        universal_field_name = ["Age", "Position",
                                "Club", "Appearances", "Mins Played"]
        universal_field_value = [f"📆 - {self.player_dict['age']}", f"📍 - {self.player_dict['position']}",
                                 f"🔰 - {self.player_dict['club']}", f"🎭 - {self.player_dict['apperances']}", f"⏳- {self.player_dict['mins_played']} mins"]

        if self.is_gk == False:
            universal_field_name = universal_field_name + ["Goals", "Assists", "G+A", "Xg",
                                                           "xAst", "PKG", "NPG"]

            universal_field_value = universal_field_value + [f"⚽- {self.player_dict['goals']}G", f"🤝🏻 - {self.player_dict['assist']}A", f"🎯- {self.player_dict['ga']}G/A",
                                                             f"🥅 - {self.player_dict['xg']}", f"🦾- {self.player_dict['xast']}", f"🛑- {self.player_dict['pkg']}",
                                                             f"🟢- {self.player_dict['npg']}"
                                                             ]
        else:

            universal_field_name = universal_field_name + ["Saves", "Shots Against", "Saves Percentage",
                                                           "Cleansheets", "Goals Against", "Goals Against/90"]

            universal_field_value = universal_field_value + [f"🧤- {self.player_dict['saves']}", f"🥅- {self.player_dict['SoTA']}", f"💯 - {self.player_dict['saves_percent']}%",
                                                             f"🧹- {self.player_dict['clean_sheets']}", f"⚽- {self.player_dict['ga']}G", f"💪 - {self.player_dict['ga_per_90']}G",

                                                             ]
        for name, value in zip(universal_field_name, universal_field_value):
            self.embed.add_field(
                name=name, value=value, inline=True)

        await ctx.send(embed=self.embed)


async def setup(bot):
    await bot.add_cog(Player(bot))
