from pytube import YouTube
import time

label = \
'''**************************************

        [YOUTUBE DOWNLOADER]
 {MAKE SURE YOUR WIFI ISN'T UNSTABLE}
 
**************************************'''

print(label)
link = input('Please enter the link of the video: ')

video = YouTube(link)
resolution = input('Enter resolution (HIGH or LOW): ')


if resolution == 'HIGH' or 'low' or 'l':
    try:
            stream = video.streams.get_highest_resolution()
            stream.download()
            print('Success')
            time.sleep(2)
    except:
        print('An error occurred')
elif resolution == 'LOW' or 'low' or 'l':
    try:
            stream = video.streams.get_lowest_resolution()
            stream.download()
            print('Success')
            time.sleep(2)
    except:
        print('An error occurred')

