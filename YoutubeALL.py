from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import requests

URLS = with open('YoutubeALL.txt')
with YoutubeDL() as ydl:
    ydl.download(URLS)
