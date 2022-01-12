from pytube import YouTube
from pytube import Playlist

print("1. 단일 영상 다운로드")
print("2. 플레이 리스트 다운로드")
sel_num = input("숫자를 입력하세요: ")

def download_video():
    url = input("영상 주소를 입력하세요: ")
    yt = YouTube(url)
    print(f'Downloading: {yt.title}')
    yt.streams.get_by_itag(22).download('./video')
    print("sucess!")


def download_playlist():
    url = input("플레이 리스트 주소를 입력하세요: ")
    p = Playlist(url)
    print(f'Downloading: {p.title}')
    for video in p.videos:
        video.streams.get_by_itag(22).download('./video')
    print("sucess!")

if sel_num == '1':
    download_video()
else:
    download_playlist()

# pl.download_all() #파이썬 파일과 같은 위치
#pl.download_all('./video') #저장위치