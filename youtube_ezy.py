import sys
import threading
import os
from time import sleep
import pytube
import youtube_downloader
import file_converter

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(3. / 100)
        threading.Thread()

def slowprint1(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.6 / 100)
        threading.Thread()

def banner():
    print('''\033[31m  ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗        ███████╗███████╗██╗   ██╗
  ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝        ██╔════╝╚══███╔╝╚██╗ ██╔╝
   ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗          █████╗    ███╔╝  ╚████╔╝ 
    ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝          ██╔══╝   ███╔╝    ╚██╔╝  
     ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗███████╗███████╗███████╗   ██║   
     ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝   \033[00m''')
    slowprint1("                      \033[01m\033[33m       >>>- cOdEd By: Predator0x300 -<<<\033[00m\033[00m")
    slowprint1("              \033[04m\033[33m             >>>--- predator0x300@gmail.com --->>>               \033[00m\033[00m")
    slowprint1("             \033[01m\033[33m     >>>--- GitHub:\033[31m  https://github.com/Predator0x300 \033[00m\033[33m ---<<<\033[00m\033[00m")
    print("\n")



os.system("clear")
banner()
print("\033[93m[1]\033[00m \033[01m\033[31mYouTube Video Downloader\033[00m\033[00m")
print("\033[93m[2]\033[00m\033[01m \033[31mPlaylist Downloader\033[00m\033[00m")
print("\033[93m[3]\033[00m \033[01m\033[31mVideo To MP3\033[00m\033[00m")
print("\033[93m[4]\033[00m\033[01m \033[31mMulti Video Downloader\033[00m\033[00m")
print("\033[04m\033[33m------\033[00m\033[00m")
usr = input("\033[01m\033[95mYouTube:~/ \033[00m")

if usr== "1" or usr == "2" or usr =="4":
    print("\033[93m[1]\033[00m \033[01m\033[31mLow 360p\033[00m\033[00m")
    print("\033[93m[2]\033[00m\033[01m \033[31mHD 720p\033[00m\033[00m")
    print("\033[93m[3]\033[00m \033[01m\033[31mFull HD 1080p\033[00m\033[00m")
    print("\033[93m[3]\033[00m \033[01m\033[31mUltra 4k\033[00m\033[00m")
    if usr == "2":
        quality = input("\033[01m\033[95mYouTube/quality:~/ \033[00m")
        link = input("{+} Enter the link to the playlist: ")
        slowprint("\033[32m{+} Downloading playlist.....\033[00m")
        sleep(0.8)
        youtube_downloader.download_playlist(link, quality)
        print("\033[93m{+} Done@!! :))\033[00m")
    if usr == "1":
        quality = input("\033[01m\033[95mYouTube/quality:~/ \033[00m")

        links = youtube_downloader.input_links_single()
        slowprint("\033[32m{+} Downloading Video.....\033[00m")
        sleep(0.8)
        youtube_downloader.download_videos1(links, quality)
        print("\033[93m{+} Done@!! :))\033[00m")
    if usr == "4":
        quality = input("\033[01m\033[95mYouTube/quality:~/ \033[00m")
        links = youtube_downloader.input_links()
        slowprint("\033[32m{+} Downloading Video.....\033[00m")
        sleep(0.8)
        for link in links:
            youtube_downloader.download_video(link, quality)
        print("\033[93m{+} Done@!! :))\033[00m")

elif usr == "3":
    links = youtube_downloader.input_links()
    for link in links:
        slowprint("\033[32m{+} Retrieving Video.....\033[00m")
        slowprint("\033[32m{+} Converting Video To MP3.....\033[00m")
        filename = youtube_downloader.download_video(link, 'low')
        file_converter.convert_to_mp3(filename)
        #print("{+} Done@!! :))")


else:
    print("\033[01m\033[95m{-} Invalid Command!~ U F00L ;0\033[00m")
