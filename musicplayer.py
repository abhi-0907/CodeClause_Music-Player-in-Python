from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("500x360")
root.resizable(False, False)



mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    #music.config(text=music_name[0:-4])

# icon
image_icon = PhotoImage(file=r"C:\Users\abhir\Downloads\music-player.png")
root.iconphoto(False, image_icon)

# button
play_button = PhotoImage(file=r"C:\Users\abhir\Downloads\icons8-play-100.png")
Button(root, image=play_button, bd=0, command=play_song).place(x=0, y=260)

stop_button = PhotoImage(file=r"C:\Users\abhir\Downloads\icons8-stop-100.png")
Button(root, image=stop_button, bd=0, command=mixer.music.stop).place(x=110, y=260)

resume_button = PhotoImage(file=r"C:\Users\abhir\Downloads\icons8-resume-button-100.png")
Button(root, image=resume_button, bd=0, command=lambda: mixer.music.unpause()).place(x=240, y=260)

pause_button = PhotoImage(file=r"C:\Users\abhir\Downloads\icons8-pause-100.png")
Button(root, image=pause_button, bd=0, command=lambda: mixer.music.pause()).place(x=350, y=260)

# label
#music = Label(root, text="", font=("arial, 15"), fg="white", bg="#6985e0")
#music.place(x=100, y=40, anchor="center")

music_frame = Frame(root, bd=2, relief=RIDGE, bg="#6985e0")
music_frame.place(x=0, y=10, width=500, height=250)

Button(root, text="Open Folder", width=10, height=2, font=("arial", 5, "bold"), fg="white", bg="#21b3de",
       command=open_folder).place(x=0, y=0)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey", selectbackground="lightblue",
                   cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
