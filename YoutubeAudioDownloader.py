# Programmer - python_scripts (Abhijith Warrier)

# Importing necessary packages
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    linkLabel = Label(root, text="YOUTUBE LINK  :", bg="turquoise4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable=videoLink)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    destinationLabel = Label(root, text="DESTINATION    :", bg="turquoise4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=38, textvariable=downloadPath)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)

    browseButton = Button(root, text="BROWSE", command=Browse, width=15)
    browseButton.grid(row=2, column=2, pady=5, padx=5)

    dwldButton = Button(root, text="DOWNLOAD AUDIO", command=Download, width=30)
    dwldButton.grid(row=3, column=1, pady=5, padx=5)

# Defining Browse() to select a destination folder to save the audio file
def Browse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in downloadDirectory
    # Setting the initialdir argument is optional
    dwldDirectory = filedialog.askdirectory(initialdir="/Users/abhijithwarrier/Downloads/Music")

    # Displaying the directory in the directory textbox
    downloadPath.set(dwldDirectory)

# Defining Download() to download the video as audio file
def Download():
    # Fetching the user-input Youtube Link and storing it in yt_link variable
    yt_link = videoLink.get()
    # Fetching the Destination Directory and storing it in dwldFolder variable
    dwldFolder = downloadPath.get()

    # Specifying the configuration options for downloading the file
    audDWLDopt = {
        # Specifying to download audio in best format
        'format':'bestaudio/best',
        # Destination to save the audio file with the title as the name
        'outtmpl': dwldFolder+"/%(title)s.%(ext)s",
        # Converting video to audio
        'postprocessors':[{
            # Extracting audio from the video
            'key':'FFmpegExtractAudio',
            # Format for saving the audio (mp3, wav)
            'preferredcodec': 'mp3',
            # Quality of the audio (Audio BitRate)
            'preferredquality': '320'
        }],
    }

    # Downloading the audio file using the youtube_dl.YoutubeDL.download() which takes the link
    # as the argument. The youtube_dl.YoutubeDL() takes the configuration dictionary as argument
    with youtube_dl.YoutubeDL(audDWLDopt) as aud_dwld:
        aud_dwld.download([yt_link])

    # Displaying the message
    messagebox.showinfo("SUCCESS", "VIDEO CONVERTED AND DOWNLOADED AS AUDIO")

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and size of the tkinter window and disabling the
# resizing property
root.geometry("650x120")
root.resizable(False, False)
root.title("Py_Youtube_Audio_Downloader")
root.config(background="turquoise4")

# Creating the tkinter Variables
videoLink = StringVar()
downloadPath = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()

