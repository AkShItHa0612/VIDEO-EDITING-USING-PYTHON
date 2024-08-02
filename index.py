import tkinter as tk
from moviepy.editor import *


# Variables
clip1 = VideoFileClip("song2.mp4")
clip2 = VideoFileClip("song3.mp4")
clip3 = VideoFileClip("song4.mp4")

# Functions
def mix():
    final_clip = concatenate_videoclips([clip1, clip2, clip3])
    final_clip.write_videofile("Final splash.mp4")

def mirror():
    clip_mirror = clip1.fx(vfx.mirror_x)
    clip_mirror.write_videofile("Final splash.mp4")

def resize():
    r = float(input("Enter your size: "))
    clip_resize = clip1.resize(r)
    clip_resize.write_videofile("Final splash.mp4")

def effects_speed():
    speed = float(input("Enter speed limit: "))
    clip_speed = clip1.fx(vfx.speedx, speed)
    clip_speed.write_videofile("Final splash.mp4")

def effects_colour():
    colour = float(input("Value of darkness: "))
    clip_color = clip1.fx(vfx.colorx, colour)
    clip_color.write_videofile("Final splash.mp4")

def trim():
    starting = int(input("Enter starting point: "))
    ending = int(input("Enter ending point: "))
    clip_trim = clip1.cutout(starting, ending)
    clip_trim.write_videofile("Final splash.mp4")

def audio_file():
    audioclip = AudioFileClip("audio.mp3")
    final_clip = clip1.set_audio(audioclip)
    final_clip.write_videofile("Final splash.mp4")

# Main screen
root = tk.Tk()
root.title("splash")
root.geometry("750x200")
root.minsize(750, 200)
root.maxsize(750, 200)
root.config(bg="#232323")

# Mix
b = tk.Button(root, text="Mix", relief=tk.GROOVE, bg="#232323", fg="white", command=mix)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Mirror
b = tk.Button(root, text="Mirror", relief=tk.GROOVE, bg="#232323", fg="white", command=mirror)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Resize
b = tk.Button(root, text="Resize", relief=tk.GROOVE, bg="#232323", fg="white", command=resize)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Speed
b = tk.Button(root, text="Speed", relief=tk.GROOVE, bg="#232323", fg="white", command=effects_speed)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Color
b = tk.Button(root, text="Color", relief=tk.GROOVE, bg="#232323", fg="white", command=effects_colour)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Trim
b = tk.Button(root, text="Trim", relief=tk.GROOVE, bg="#232323", fg="white", command=trim)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Audio
b = tk.Button(root, text="Audio", relief=tk.GROOVE, bg="#232323", fg="white", command=audio_file)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

root.mainloop()
