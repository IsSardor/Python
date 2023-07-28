import os
from moviepy.editor import *
from pytube import YouTube
from pathlib import Path


pathado = Path('./audio')
pathvdo = Path('./video')

typedwnld = int(
    input("Select the type of download, audio = 1 or video = 2, enter 1 or 2: "))
url = input("Enter URL: ")
link = YouTube(url)

if typedwnld == 1:
    audio = link
    audio_file = audio.streams.get_audio_only().download(pathado)

    audio_clip = AudioFileClip(audio_file)
    audio_clip.write_audiofile(os.path.splitext(audio_file)[0] + ".mp3")

    os.remove(audio_file)
elif typedwnld == 2:
    video = link
    quality = int(
        input("Choose the quality (high = 1 / lowest = 2), enter 1 or 2: "))

    if quality == 1:
        output = video.streams.get_highest_resolution().download(pathvdo)
        
    elif quality == 2:
        output = video.streams.get_lowest_resolution().download(pathvdo)
