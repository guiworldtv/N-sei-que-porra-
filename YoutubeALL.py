from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=DTXDxJVhunw']
with YoutubeDL() as ydl:
    ydl.download(URLS)
