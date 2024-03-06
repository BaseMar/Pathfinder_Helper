import customtkinter
from PIL import Image

class MusicModel:
    def __init__(self):
        self.play_button = customtkinter.CTkImage(light_image=Image.open("Images/Play_button.png"), dark_image=Image.open("Images/Play_button.png"), size=(30, 30))
        self.pause_button = customtkinter.CTkImage(light_image=Image.open("Images/Pause_button.png"), dark_image=Image.open("Images/Pause_button.png"), size=(30, 30))
        self.next_button = customtkinter.CTkImage(light_image=Image.open("Images/Next_button.png"), dark_image=Image.open("Images/Next_button.png"), size=(30, 30))
        self.previous_button = customtkinter.CTkImage(light_image=Image.open("Images/Previous_button.png"), dark_image=Image.open("Images/Previous_button.png"), size=(30, 30))
        self.folder_image = customtkinter.CTkImage(light_image=Image.open("Images/folder.png"), dark_image=Image.open("Images/folder.png"), size=(30, 30))
        self.is_playing = False
        self.audio_bars = []
