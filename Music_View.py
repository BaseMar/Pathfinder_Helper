import customtkinter
from CTkListbox import *
from pygame import mixer

class MusicView(customtkinter.CTkFrame):
    def __init__(self, parent, config):
        self.config = config
        self.controller = None

        super().__init__(parent)
        mixer.init()
        self.lower_frame = customtkinter.CTkFrame(self, width=995, height=290)
        self.browse_button = customtkinter.CTkButton(self.lower_frame, text="Browse Folder", corner_radius=5, fg_color=config["COLORS"]["BUTTON"], text_color=config["COLORS"]["TEXT"], hover_color=config["COLORS"]["HOVER"], compound="left", command=self.add_music)
        self.music_listbox = CTkListbox(self.lower_frame, border_color=config["COLORS"]["BUTTON"], width=950, height=215, command=lambda index: self.play_music(index))
        self.pause_music_button = customtkinter.CTkButton(self.lower_frame, width=0, height=0, text="", fg_color="transparent", command=self.pause_music)
        self.previous_music_button = customtkinter.CTkButton(self.lower_frame, text="", width=0, height=0, fg_color="transparent", command=self.previous_music)
        self.next_music_button = customtkinter.CTkButton(self.lower_frame, text="", width=0, height=0, fg_color="transparent", command=self.next_music)
        self.grid_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def grid_widgets(self):
        self.lower_frame.place(x=10, y=400)
        self.browse_button.place(x=10, y=10)
        self.music_listbox.place(x=10, y=50)
        self.previous_music_button.place(x=420, y=10)
        self.pause_music_button.place(x=460, y=10)
        self.next_music_button.place(x=500, y=10)

    def init_data(self):
        self.pause_music_button.configure(image=self.controller.model.play_button)
        self.next_music_button.configure(image=self.controller.model.next_button)
        self.previous_music_button.configure(image=self.controller.model.previous_button)

    def add_music(self):
        self.controller.add_music()

    def play_music(self, music_name):
        self.controller.play_music(music_name)

    def pause_music(self):
        self.controller.pause_music()

    def next_music(self):
        self.controller.next_music()

    def previous_music(self):
        self.controller.previous_music()
