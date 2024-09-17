from discord.ext import commands
from tokenHandler import TOKEN
from pathlib import Path
import discord
import yt_dlp
import os

intents = discord.Intents.default()
intents.message_content = True
b = commands.Bot(intents=intents, help_command=None)

@b.event
async def on_ready():
    print(f"Youtube downloader bot online | {b.user}")
    botActivity = discord.Activity(type=discord.ActivityType.watching, name="YouTube")
    await b.change_presence(status=discord.Status.idle, activity=botActivity)

@b.slash_command(name="help", description="Show help message.")
async def help(ctx: discord.ApplicationContext):
    embed = discord.Embed(title="Youtube Downloader", description="Download video or audio from a YouTube URL.")
    embed.add_field(name="/download", value="Download video or audio from a YouTube URL. Use `format` argument for mp3.")
    await ctx.send(embed=embed)

@b.slash_command(name="download", description="Download video or audio from a YouTube URL.")
async def download(ctx: discord.ApplicationContext, url: str, format: str = "mp4"):
    await ctx.defer()
    try:
        if format == "mp3":
            ydl_opts = {
                'outtmpl': './youtube/%(title)s.%(ext)s',
                'format': 'bestaudio/best',
                'merge_output_format': 'mp3',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:
            ydl_opts = {
                'outtmpl': './youtube/%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
            }

        Path('./youtube').mkdir(parents=True, exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'downloaded_file')
            if format == 'mp3':
                file_path = Path('./youtube') / f"{title}.mp3"
            else:
                file_path = Path('./youtube') / f"{title}.mp4"

            if not file_path.exists():
                raise FileNotFoundError(f"No such file: {file_path}")

            if format == "mp3":
                await ctx.send_followup(f"Downloaded: {title} | mp3")
            else:
                await ctx.send_followup(f"Downloaded: {title} | mp4")

            await ctx.send_followup(file=discord.File(file_path))

    except Exception as e:
        await ctx.send_followup(f"Error: {str(e)}")

b.run(TOKEN)
