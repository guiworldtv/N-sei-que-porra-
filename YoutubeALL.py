from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=1eWMMCCkwQk']
with YoutubeDL() as ydl:
    ydl.download(URLS)
