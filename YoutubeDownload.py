from pytube import YouTube
link = input("Enter link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
