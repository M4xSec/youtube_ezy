import pytube


def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos1(urls, resolution):
    download_video(urls, resolution)

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p", "1"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd", "2"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd", "3"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k", "4"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("\033[01m\033[95mNote: To Stop Enter- end \033[00m")
    print("\033[32m{+} Enter the link of Video's: \033[00m")

    links = []
    link = ""

    while link != "end" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links

def input_links_single():
    print("\033[32m{+} Enter the link of Video: \033[00m")

    links = input("")
    return links