import discord
from discord.ext import commands
import asyncio

TOKEN = "your token"

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    print("Bot 已成功啟動")

async def main():

    async with bot:

        await bot.load_extension("cogs.basic")
        print("basic cog 已成功載入")

        await bot.load_extension("cogs.music.music")
        print("music cog 已成功載入")

        await bot.start(TOKEN)

asyncio.run(main())