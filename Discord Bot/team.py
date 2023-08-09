import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
from connection import DataBaseConnection


class Team(commands.Cog, DataBaseConnection):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def team(self, ctx, *, team):
        team_dict = self.team_collection.find_one({"team": f"{team}"})

        self.embed = discord.Embed(
            title=f"{team_dict['team']}",  colour=discord.Colour.random())

        self.embed.set_image(
            url=f"{team_dict['image']}")

        self.rank_suffix = {"1": "st", "2": "nd", "3": "rd"}
        self.endings_suffix = self.rank_suffix.get(team_dict["rank"], "th")

        field_names = ["Rank", "Points", "GD",
                       "Wins", "Draws", "Losses", "Top Scorer"]

        field_values = [f"🏆 - {team_dict['rank']}{self.endings_suffix}",
                        f"💯 - {team_dict['points']}pts",
                        f"🥅  {team_dict['goal_differences']}",
                        f"✅ - {team_dict['wins']}W",
                        f"✍🏻 - {team_dict['draws']}D",
                        f"❌ - {team_dict['losses']}L",
                        f"⚽ - {team_dict['top_scorer']}"]

        for name, value in zip(field_names, field_values):
            self.embed.add_field(name=name, value=value,
                                 inline=(name != "Top Scorer"))

        await ctx.send(embed=self.embed)


async def setup(bot):
    await bot.add_cog(Team(bot))
