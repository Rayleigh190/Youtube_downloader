from pytube import Playlist

p = Playlist("url")

print(f'Downloading: {p.title}')

cnt = 0
for video in p.videos:
    if cnt > 28:
        video.streams.get_by_itag(22).download('./video')
    cnt = cnt + 1

# pl.download_all() #파이썬 파일과 같은 위치
#pl.download_all('./video') #저장위치