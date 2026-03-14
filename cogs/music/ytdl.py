import discord
import yt_dlp
import asyncio

from .config import YTDL_OPTIONS, FFMPEG_OPTIONS, FFMPEG_PATH

ytdl = yt_dlp.YoutubeDL(YTDL_OPTIONS)

class YTDLSource:
    def __init__(self, source, *, data):
        self.source = source  # FFmpegOpusAudio
        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url):
        loop = asyncio.get_running_loop()
        data = await loop.run_in_executor(
            None,
            lambda: ytdl.extract_info(url, download=False)
        )

        if "entries" in data:
            data = data["entries"][0]

        stream_url = data["url"]

        audio = discord.FFmpegOpusAudio(
            stream_url,
            executable=FFMPEG_PATH,
            **FFMPEG_OPTIONS
        )

        return cls(audio, data=data)