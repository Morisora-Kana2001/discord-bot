from discord.ext import commands
from .player import MusicPlayer


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player = MusicPlayer(bot)


    @commands.command()
    async def play(self, ctx, url):
        await self.player.play(ctx, url)

    @commands.command()
    async def skip(self, ctx):
        await self.player.skip(ctx)

    @commands.command()
    async def stop(self, ctx):
        await self.player.stop(ctx)

async def setup(bot):
    await bot.add_cog(Music(bot))