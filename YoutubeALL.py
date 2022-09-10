from __future__ import unicode_literals
import requests
import shutil
import json
import yt_dlp
m3u = None

URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    print(json.dumps(ydl.sanitize_info(info)))
    

    
    write_to_playlist = json.dumps(ydl.sanitize_info(info)
    
    
def write_to_playlist(content):
    global m3u    
    m3u.write(content)


def create_playlist():
    global m3u
    m3u = open("YoutubeALL.m3u8", "w")
    m3u.write("#EXTM3U")
    m3u.write("\n")                                 

def close_playlist():
    global m3u
    m3u.close()
                                 
def generate_youtube_PlayList():
    create_playlist()
                                 
                                 
    close_playlist()                                 
                                 
if __name__ == '__main__':
    generate_youtube_PlayList()                                    
