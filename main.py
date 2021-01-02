from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#Functions
Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        downloadLabel.config(text=Folder_Name, fg="green")
        DownloadVideo()
    else:
        downloadLabel.config(text="Pleasr Choose Folder", fg="red")


def DownloadVideo():
    try:
        choice = ytdChoices.get()
        url = urlEntry.get()

        if (len(url) > 1):
            urlError.config(text="")
            yt = YouTube(url)

            if (choice == choices[0]):
                select = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
            elif (choice == choices[1]):
                select = yt.streams.filter(progressive=True, file_extension="mp4").get_lowest_resolution()
            elif (choice == choices[2]):
                select = yt.streams.filter(only_audio=True).first()
        else:
            urlError.config(text="Past link again!", fg="red")

        select.download(Folder_Name)
        downloadLabel.config(text="Download Completed!!", fg="green")
    except Exception as err:
        print(err)


#UI
win = Tk()
win.title('YouTube video Downloader')
win.columnconfigure(0, weight=1)#set all content in center


title = Label(win, text='YouTube Video Downloader',
              fg='red',
              font=('jost', 20),
              ).grid(padx=100, row=0)

urlLabel = Label(win, text="Paste Video URL", font=('jost', 15),)
urlLabel.grid(row=1)

urlEntry = Entry(win, width=40, fg="blue", font=('jost', 15))
urlEntry.grid(row=2)

urlError = Label(win, text="", fg="red", font=('jost', 13))
urlError.grid(row=3)

choseLabel = Label(win, text="Chose type", font=('jost', 15))
choseLabel.grid(row=4)

choices = ["High quality", "Low quality", "Audio file"]
ytdChoices = ttk.Combobox(win, values=choices, font=('jost', 15))
ytdChoices.grid(row=5, pady=10)

DownloadBtn = Button(win, text="Download", width=20, bg="red",
                 fg="white",
                 command=openLocation,
                 font=('jost', 15))
DownloadBtn.grid(row=6, pady=10)

downloadLabel = Label(win, text="",fg="red", font=("jost", 10))
downloadLabel.grid(row=7, pady=10)

win.mainloop()