# YouTube Downloader Bot

A simple discord bot that lets you download YouTube video's over discord.

## Features

- Download videos in `mp4` format.
- Download audio in `mp3` format.
- Slash commands for easy interaction.

## Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `yt-dlp` library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/lhwe/ytdl-pycord.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ytdl-pycord
   ```
3. Install the required Python packages:
   ```bash
   pip install discord.py yt-dlp
   ```
5. Change the contents of `tokenHandler.py` to have your bot token:
   ```python
   TOKEN = 'Your token goes here'
   ```
# Usage
1. Run the bot:
   ```bash
   python3 ytdl-bot.py
   ```
2. In Discord, use the following commands:
  - `/help` - Displays a help message.
  - `/download <url> [format]` - Downloads the video or audio from the specified YouTube URL. Format can be mp3 or mp4 (default is mp4).

# Example
  - To download a video:
   ```
   /download https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```
  - To download audio:
   ```
   /download https://www.youtube.com/watch?v=dQw4w9WgXcQ format:mp3
   ```
