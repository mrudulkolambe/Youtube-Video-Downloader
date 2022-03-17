import tkinter as tk
from pytube import YouTube

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Youtube Video Downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter Youtube Link : ')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
menu= tk.StringVar()
menu.set("Select The Option")

drop = tk.OptionMenu(root, menu,"360p", "720p","1080p")
canvas1.create_window(200, 180, window=drop)

def getSquareRoot ():
	link = entry1.get()
	yt = YouTube(link)
	yt.streams.filter(file_extension='mp4')
	option = menu.get()
	if option == "360p":
		stream = yt.streams.get_by_itag(18)
		stream.download()
	elif option == "720p":
		stream = yt.streams.get_by_itag(22)
		stream.download()
	elif option == "1080p":
		stream = yt.streams.get_by_itag(137)
		stream.download()
	else:
		print("Invalid")


    
button1 = tk.Button(text='Download', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 270, window=button1)
	
	



root.mainloop()