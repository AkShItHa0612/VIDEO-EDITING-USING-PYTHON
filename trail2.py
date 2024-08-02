import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from moviepy.editor import *
#from moviepy.video import concatenate_videoclips
#from moviepy.video import fx

# Variables
selected_files = []
output_filename = "Final splash.mp4"

# Functions
def select_files():
    global selected_files
    selected_files = filedialog.askopenfilenames(title="Select Video Files", filetypes=(("MP4 files", "*.mp4"),))
    print("Selected files:", selected_files)

def mix():
    if len(selected_files) < 2:
        print("Select at least 2 video files.")
        return

    clips = [VideoFileClip(file) for file in selected_files]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_filename)

def mirror():
    if not selected_files:
        print("Select a video file.")
        return

    clip = VideoFileClip(selected_files[0])
    clip_mirror = clip.fx(vfx.mirror_x)
    clip_mirror.write_videofile(output_filename)

def resize():
    if not selected_files:
        print("Select a video file.")
        return

    r = float(input("Enter your size: "))
    clip = VideoFileClip(selected_files[0])
    clip_resize = clip.resize(r)
    clip_resize.write_videofile(output_filename)

def effects_speed():
    if not selected_files:
        print("Select a video file.")
        return

    speed = float(input("Enter speed limit: "))
    clip = VideoFileClip(selected_files[0])
    clip_speed = clip.fx(vfx.speedx, speed)
    clip_speed.write_videofile(output_filename)

def effects_colour():
    if not selected_files:
        print("Select a video file.")
        return

    colour = float(input("Value of darkness: "))
    clip = VideoFileClip(selected_files[0])
    clip_color = clip.fx(vfx.colorx, colour)
    clip_color.write_videofile(output_filename)

def trim():
    if not selected_files:
        print("Select a video file.")
        return

    starting = int(input("Enter starting point: "))
    ending = int(input("Enter ending point: "))
    clip = VideoFileClip(selected_files[0])
    clip_trim = clip.cutout(starting, ending)
    clip_trim.write_videofile(output_filename)

def audio_file():
    if not selected_files:
        print("Select a video file.")
        return

    audio_file = filedialog.askopenfilename(title="Select Audio File", filetypes=(("MP3 files", "*.mp3"),))
    if not audio_file:
        print("No audio file selected.")
        return

    clip = VideoFileClip(selected_files[0])
    audioclip = AudioFileClip(audio_file)
    final_clip = clip.set_audio(audioclip)
    final_clip.write_videofile(output_filename)

# Main screen
root = tk.Tk()
root.title("Video Editing Platform")
root.geometry("800x600")

# Background Image
background_image = ImageTk.PhotoImage(Image.open("a1.jpg"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for video file selection
file_frame = tk.Frame(root, bg="white", padx=10, pady=10)
file_frame.pack(pady=20)

# Select Files button
select_button = tk.Button(file_frame, text="Select Files", bg="#A0BF37", fg="white", font=("Helvetica", 16, "bold"), relief=tk.FLAT, command=select_files)
select_button.pack(padx=10, pady=10)

# Selected Files label
selected_label = tk.Label(file_frame, text="Selected Files:", bg="white", fg="#A0BF37", font=("Helvetica", 14, "bold"))
selected_label.pack()

# Mix button
mix_button = tk.Button(root, text="Mix", relief=tk.GROOVE, bg="#A0BF37", fg="white", font=("Helvetica", 20, "bold"), command=mix)
mix_button.place(relx=0.2, rely=0.4, anchor="center")

# Mirror button
mirror_button = tk.Button(root, text="Mirror", relief=tk.GROOVE, bg="#A0BF37", fg="white", font=("Helvetica", 20, "bold"), command=mirror)
mirror_button.place(relx=0.5, rely=0.4, anchor="center")

# Resize button
resize_button = tk.Button(root, text="Resize", relief=tk.GROOVE, bg="#A0BF37", fg="white", font=("Helvetica", 20, "bold"), command=resize)
resize_button.place(relx=0.8, rely=0.4, anchor="center")

# Speed button
speed_button = tk.Button(root, text="Speed", relief=tk.GROOVE, bg="#A0BF37", fg="white", font=("Helvetica", 20, "bold"), command=effects_speed)
speed_button.place(relx=0.2, rely=0.6, anchor="center")

# Color button
color_button = tk.Button(root, text="Color", relief=tk.GROOVE, bg="#A0BF37", fg="white", font=("Helvetica", 20, "bold"), command=effects_colour)
color_button.place(relx=0.5, rely=0.6, anchor="center")

# Trim button
trim_button = tk.Button(root, text="Trim", relief=tk.GROOVE, bg="#A0BF37", fg="white", font=("Helvetica", 20, "bold"), command=trim)
trim_button.place(relx=0.8, rely=0.6, anchor="center")

# Audio button
audio_button = tk.Button(root, text="Audio", relief=tk.GROOVE, bg="#A0BF37", fg="white", font=("Helvetica", 20, "bold"), command=audio_file)
audio_button.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
