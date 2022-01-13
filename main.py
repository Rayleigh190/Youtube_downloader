from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import os
import string

print("1. 단일 영상 다운로드")
print("2. 플레이 리스트 다운로드")
sel_num = input("숫자를 입력하세요: ")

def download_video():  # 단일 영상 다운로드
    url = input("영상 주소를 입력하세요: ")
    yt = YouTube(url)
    itag = selec_quality(yt.streams)
    print(f'Downloading: {yt.title}')
    # 선택한 품질의 비디오 다운로드
    yt.streams.get_by_itag(itag).download('./video', 'video.mp4')
    # 최고 품질의 오디오 다운로드
    yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first().download('./video', 'audio.mp4')
    merge_files()
    os.remove('./video/video.mp4')
    os.remove('./video/audio.mp4')
    title = yt.title.replace('/','')
    os.rename('./video/title.mp4', "./video/"+title+".mp4")
    print("sucess!")

def download_playlist():  # 플레이리스트 다운로드
    url = input("플레이 리스트 주소를 입력하세요: ")
    p = Playlist(url)
    print(f'Downloading playlist: {p.title}')
    for video in p.videos:
        print(f'Downloading: {video.title}')
        video.streams.get_by_itag(22).download('./video')
    print("sucess!")

def selec_quality(yt_streams):  # 비도오 품질 선택 함수
    print("다운로드 가능한 화질: ")  # 고화질, mp4 포맷만 가져오기
    for i, stream in enumerate(yt_streams.filter(adaptive=True, file_extension='mp4')):
        # print(dir(stream))
        if stream.resolution != None:  # res 속성이 있는 stream만 출력
            print(i, " : ", stream.resolution)
    res_num = int(input("화질 번호를 선택하세요: "))
    return yt_streams.filter(adaptive=True, file_extension='mp4')[res_num].itag

def merge_files():  # 비디오, 오디오 합병 함수
    videoclip = VideoFileClip("./video/video.mp4")
    audioclip = AudioFileClip("./video/audio.mp4")
    videoclip.audio = audioclip  # 비디오 클립에 오디오를 넣어준다
    videoclip.write_videofile("./video/title.mp4")

if sel_num == '1':
    download_video()
elif sel_num == '2':
    download_playlist()
else:
    print("잘못 된 값을 입력 했습니다.")

# pl.download_all() #파이썬 파일과 같은 위치
#pl.download_all('./video') #저장위치