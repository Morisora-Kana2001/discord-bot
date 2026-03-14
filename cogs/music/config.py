FFMPEG_PATH = r"C:\Program Files\ffmpeg-7.1-full_build\bin\ffmpeg.exe"

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn"
}

YTDL_OPTIONS = {
    "noplaylist": True,
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "js": "node"
}