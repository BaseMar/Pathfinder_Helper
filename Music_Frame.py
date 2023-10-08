import os
import tkinter
from tkinter import END
import moviepy.editor as mp
from PIL import Image
import customtkinter
from pytube import YouTube
import threading
import pygame
from CTkListbox import *


def on_enter(e, button, hover_image):
    button.configure(image=hover_image)

def on_leave(e, button, normal_image):
    button.configure(image=normal_image)

def pause_music():
    pygame.mixer.music.stop()

class Music_Frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller, config):
        super().__init__(parent)
        self.song_list = []

        self.grid_rowconfigure(4, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.lbl_title = customtkinter.CTkLabel(
            self,
            text="Insert a YouTube link",
            text_color=config["COLORS"]["TEXT"]
        )
        self.lbl_title.grid(row=0, column=0, padx=10, pady=10)

        # Link input
        url_var = tkinter.StringVar()
        self.entry_link = customtkinter.CTkEntry(
            self,
            width=350,
            height=40,
            textvariable=url_var,
            text_color=config["COLORS"]["TEXT"]
        )
        self.entry_link.grid(row=1, column=0, padx=10, pady=10)

        # Download Button
        download_icon = customtkinter.CTkImage(
            dark_image=Image.open("Images/Download.png"),
            size=(25, 25)
        )
        self.btn_download = customtkinter.CTkButton(
            self,
            text="Download",
            text_color=config["COLORS"]["TEXT"],
            fg_color=config["COLORS"]["BUTTON"],
            hover_color=config["COLORS"]["HOVER"],
            image=download_icon,
            compound="left",
            command=self.startDownload
        )
        self.btn_download.grid(row=1, column=1, padx=10, pady=10)

        # Finished Downloading
        self.lbl_finish = customtkinter.CTkLabel(self, text="")
        self.lbl_finish.grid(row=3, column=0)

        # Progress percentage
        self.progress_bar = customtkinter.CTkProgressBar(self, width=350, height=20)
        self.progress_bar.set(0)
        self.progress_bar.grid(row=2, column=0)

        # Flag to track download state
        self.downloading = False

        # MP3 Player Controls
        pygame.mixer.init()
        self.song_box = CTkListbox(self, text_color=config["COLORS"]["TEXT"], height=300)
        self.song_box.grid(row=5, column=0, padx=100, pady=10, columnspan=2, sticky="nsew")
        self.load_music_from_directory()

        # Button images and coordinates
        button_images = {
            "Prev": ("Images/Hover_Previous_button.png", "Images/Previous_button.png"),
            "Play": ("Images/Hover_Play_button.png", "Images/Play_button.png"),
            "Pause": ("Images/Hover_Pause_button.png", "Images/Pause_button.png"),
            "Next": ("Images/Hover_Next_button.png", "Images/Next_button.png"),
        }

        self.buttons = {}
        x_coordinate = 400  # Initialize the X-coordinate

        for btn_name, (hover_image_path, normal_image_path) in button_images.items():
            hover_image = customtkinter.CTkImage(
                dark_image=Image.open(hover_image_path),
                size=(25, 25)
            )
            normal_image = customtkinter.CTkImage(
                dark_image=Image.open(normal_image_path),
                size=(25, 25)
            )

            button = customtkinter.CTkButton(
                self,
                image=normal_image,
                text="",
                width=0,
                height=0,
                fg_color="transparent",
                hover=False
            )
            button.place(x=x_coordinate, y=500)  # Adjust the Y-coordinate if needed

            # Bind different commands to different buttons
            if btn_name == "Play":
                button.configure(command=self.play_music)
            elif btn_name == "Pause":
                button.configure(command=pause_music)
            elif btn_name == "Prev":
                button.configure(command=self.previous_music)
            elif btn_name == "Next":
                button.configure(command=self.next_music)

            button.bind("<Enter>",
                        lambda e, button=button, hover_image=hover_image: on_enter(e, button, hover_image))
            button.bind("<Leave>",
                        lambda e, button=button, normal_image=normal_image: on_leave(e, button, normal_image))

            self.buttons[btn_name] = button
            x_coordinate += 30  # Increment X-coordinate by 30 pixels for the next button

    def startDownload(self):
        yt_link = self.entry_link.get()
        if yt_link:
            if not self.downloading:
                # Set downloading flag
                self.downloading = True

                # Disable the download button while downloading
                self.btn_download["state"] = "disabled"
                self.lbl_finish.configure(text="Downloading...", text_color="#00ADB5")

                # Create a new thread for downloading
                download_thread = threading.Thread(target=self.downloadVideo, args=(yt_link,))
                download_thread.start()
        else:
            self.lbl_finish.configure(text="Invalid URL", text_color="#BB2525")

    def downloadVideo(self, yt_link):
        try:
            ytObject = YouTube(yt_link, on_progress_callback=self.on_progress)
            video = ytObject.streams.get_lowest_resolution()
            self.lbl_title.configure(text=ytObject.title)
            video_path = video.download(output_path="Music/", filename="temp_video")
            # Use moviepy to convert the video to MP3
            clip = mp.VideoFileClip(video_path)
            audio = clip.audio
            audio_path = os.path.join("Music/", ytObject.title + ".mp3")
            audio.write_audiofile(audio_path)

            # Close and release resources associated with the clip and audio
            audio.close()
            clip.close()

            # Clean up temporary video file
            os.remove(video_path)

            self.lbl_finish.configure(text="Downloaded and converted to MP3!", text_color="#00ADB5")
            self.song_box.insert(END, ytObject.title + ".mp3")
            self.song_list.append(os.path.join("Music/", ytObject.title + ".mp3"))
        except Exception as e:
            print(str(e))
            self.lbl_finish.configure(text="Download and conversion error", text_color="#BB2525")
        finally:
            # Reset downloading flag and re-enable the download button
            self.downloading = False
            self.btn_download["state"] = "normal"

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = str(int(bytes_downloaded / total_size * 100))
        self.progress_bar.set(float(percentage_of_completion) / 100)
        self.lbl_finish.configure(text=f"{percentage_of_completion}%")

    def load_music_from_directory(self):
        music_dir = "Music/"
        if not os.path.exists(music_dir):
            os.makedirs(music_dir)

        for filename in os.listdir(music_dir):
            if filename.endswith(".mp3"):
                self.song_list.append(os.path.join(music_dir, filename))

        # Add songs to the song_box
        for song in self.song_list:
            self.song_box.insert(tkinter.END, os.path.basename(song))

    def play_music(self):
        song = self.song_box.get()
        pygame.mixer.music.load(f"Music/{song}")
        pygame.mixer.music.play()

    def previous_music(self):
        current_song = f"Music/{self.song_box.get()}"
        current_song_index = self.song_list.index(current_song) if current_song in self.song_list else -1
        if current_song_index >= 0:
            previous_song_index = current_song_index - 1
            self.song_box.selection_clear()
            self.song_box.activate(previous_song_index)
            self.play_music()
        else:
            # Obsłuż sytuację, gdy obecna piosenka nie istnieje na liście lub jest pierwszą piosenką.
            pass

    def next_music(self):
        current_song = f"Music/{self.song_box.get()}"
        current_song_index = self.song_list.index(current_song) if current_song in self.song_list else -1
        if current_song_index >= len(self.song_list) - 1:
            next_song_index = 0
        else:
            next_song_index = current_song_index + 1

        self.song_box.selection_clear()
        self.song_box.activate(next_song_index)
        self.song_box.activate(next_song_index)
        self.play_music()
