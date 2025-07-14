import os
import re
from yt_dlp import YoutubeDL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "music")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": os.path.join(DATA_DIR, "%(title)s.%(ext)s"),
    "noplaylist": True,
    "quiet": True,
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "256",
    }]
}

def is_yt_link(text):
    return re.match(r"https://(www\.)?(youtube\.com|youtu\.be)/", text)


with YoutubeDL(ydl_opts) as ydl:
    print("Input 'quit' or 'exit' to stop program from running!")
    while True:
        video_url = input("Enter music video: ").strip()

        if video_url in ("quit", "exit"):
            break

        if is_yt_link(video_url):
            ydl.download([video_url])

        else:
            print("Invalid Youtube link!\n")
                       

