from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    # take name of class, pass in the bot
    await bot.add_cog(Admin(bot))
