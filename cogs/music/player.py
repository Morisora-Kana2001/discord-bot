import discord
from .ytdl import YTDLSource

class MusicPlayer:
    def __init__(self, bot):
        self.bot = bot

    async def play(self, ctx, url):

        if not ctx.author.voice:
            await ctx.send("你需要先加入語音頻道!")
            return

        channel = ctx.author.voice.channel
        vc = ctx.voice_client

        if vc is None:
            vc = await channel.connect()

        elif vc.channel != channel:
            await vc.move_to(channel)

        if vc.is_playing():
            vc.stop()

        player = await YTDLSource.from_url(url)

        vc.play(
             player.source,  # 注意這裡用 player.source
             after=lambda e: print(f"播放錯誤: {e}") if e else None
        )
        await ctx.send(f"🎵 正在播放: {player.title}")

    async def skip(self, ctx):
        vc = ctx.voice_client

        if vc and vc.is_playing():
            vc.stop()
            await ctx.send("⏭ 已跳過歌曲")

        else:
            await ctx.send("沒有正在播放的音樂")

    async def stop(self, ctx):
        vc = ctx.voice_client

        if vc:
            await vc.disconnect()
            await ctx.send("⏹ 已離開語音頻道")

        else:
            await ctx.send("我不在任何語音頻道")