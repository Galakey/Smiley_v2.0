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

    @commands.command(hidden=True, help="Returns an anime matching the given ID.")
    async def searchID(self, ctx, entryID: int):
        anime = Data.getAnimeWithID(entryID)
        if anime is None:
            await ctx.send(f"No anime found matching the entryID: {entryID}.")
        else:
            embed = self.animeEmbed(anime)
            await ctx.send(embed=embed)

    @commands.command(hidden=True, help="Returns an anime matching the given ID.")
    async def searchTitle(self, ctx, title: str):
        anime = Data.getAnimeWithTitle(title)
        if anime is None:
            await ctx.send(f"No anime found matching the title: {title}.")
        else:
            await ctx.send(embed=self.animeEmbed(anime))

    @commands.command(hidden=True, help="Add an anime to the list. Use '$' to split values.\n"
                                        "**IF YOU SKIP A VALUE, ADD THE APPROPRIATE NUMBER OF '$'.\n"
                                        "eg. 's.addanime Beastars$$$myanimelist.com/Beastars' would skip the episode number and watch link."
                                        "Takes in a title, episode number, watch link and MAL link. "
                                        "Only a title is required.")
    async def addAnime(self, ctx, *, entry: str):
        # Dogshit implementation, bad inputs will make really shit entries.
        entry = entry.split("$")
        if len(entry) == 1:
            anime = Data.addAnime(entry[0], 1, "", "")
            print(anime)
            await ctx.send(embed=self.animeEmbed(anime))
        elif len(entry) == 2:
            anime = Data.addAnime(entry[0], int(entry[1]), "", "")
            print(anime)
            await ctx.send(embed=self.animeEmbed(anime))
        elif len(entry) == 3:
            anime = Data.addAnime(entry[0], int(entry[1]), entry[2], "")
            print(anime)
            await ctx.send(embed=self.animeEmbed(anime))
        elif len(entry) == 4:
            anime = Data.addAnime(entry[0], int(entry[1]), entry[2], entry[3])
            print(anime)
            await ctx.send(embed=self.animeEmbed(anime))

    def animeEmbed(self, anime):
        """The default embed design for an instance of a single anime."""
        embed = discord.Embed(title=f"{anime.getTitle()}",
                              description=f"entryID: **{anime.getEntryID()}**\n"
                                          f"Episode: **{anime.getEpisode()}**\n"
                                          f"Watch Link: [here]({anime.getWatch()})\n"
                                          f"MyAnimeList: {anime.getMal()}",
                              color=int(0xa0ebe4))
        return embed


async def setup(bot):
    # take name of class, pass in the bot
    await bot.add_cog(Animelist(bot))
