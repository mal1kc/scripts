yt-dlp -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "./%(playlist_title)s/%(title)s.%(ext)s" $1
