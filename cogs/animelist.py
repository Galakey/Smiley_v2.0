import discord
from discord.ext import commands
from data.data import Data


class Animelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, help="Returns the current anime list.")
    async def anime(self, ctx):
        animelist = Data.listAnime()
        desc = ""
        for entry in animelist["anime"]:
            desc += f"{entry['entryID']} | **[{entry['title']}]({entry['watch']})** | *ep. {entry['episode']}*\n"
        embed = discord.Embed(title=f"Anime List",
                              description=desc,
                              color=int(0xa0ebe4))

        await ctx.send(embed=embed)


async def setup(bot):
    # take name of class, pass in the bot
    await bot.add_cog(Animelist(bot))
