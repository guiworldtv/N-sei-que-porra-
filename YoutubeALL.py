import json
import yt_dlp

URL = 'https://vimeo.com/748244075'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {
    'format_id': 'hls-akfire_interconnect_quic_sep-audio-medium-audio'
    }
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    print(json.dumps(ydl.sanitize_info(info)))
