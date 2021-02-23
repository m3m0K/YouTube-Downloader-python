from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('550x300')
root.resizable(0,0)
root.title("MEMO TTEN42")

Label(root,text = 'Youtube video indirme', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'buraya link yapıştır:', font = 'arial 15 bold').place(x= 220 , y = '60')
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 98)

def Downloader():
	url = YouTube(str(link.get()))
	video = url.streams.first()
	video.download()
	Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x = 180, y = 210)

Button(root,text = 'İNDİR', font = 'arial 15 bold', bg = 'pale violet red', padx = 2, command = Downloader).place(x = 225, y = 150)

root.mainloop()