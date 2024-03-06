import customtkinter
from CTkListbox import *
from pygame import mixer

class MusicView(customtkinter.CTkFrame):
    def __init__(self, parent, config):
        self.config = config
        self.controller = None

        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        mixer.init()
        self.upper_frame = customtkinter.CTkCanvas(self, background="#222831", borderwidth=1, confine=False, highlightthickness=0)
        self.lower_frame = customtkinter.CTkFrame(self)
        self.browse_button = customtkinter.CTkButton(self.lower_frame, corner_radius=5, fg_color=config["COLORS"]["BUTTON"], text_color=config["COLORS"]["TEXT"], hover_color=config["COLORS"]["HOVER"], command=self.add_music)
        self.music_listbox = CTkListbox(self.lower_frame, border_color=config["COLORS"]["BUTTON"], width=950, height=215, hover_color=config["COLORS"]["HOVER"], command=lambda index: self.play_music(index))
        self.pause_music_button = customtkinter.CTkButton(self.lower_frame, width=0, height=0, text="", fg_color="transparent", command=self.pause_music)
        self.previous_music_button = customtkinter.CTkButton(self.lower_frame, text="", width=0, height=0, fg_color="transparent", command=self.previous_music)
        self.next_music_button = customtkinter.CTkButton(self.lower_frame, text="", width=0, height=0, fg_color="transparent", command=self.next_music)
        self.grid_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def grid_widgets(self):
        self.upper_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.lower_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.browse_button.place(x=10, y=10)
        self.music_listbox.place(x=10, y=50)
        self.previous_music_button.place(x=420, y=10)
        self.pause_music_button.place(x=460, y=10)
        self.next_music_button.place(x=500, y=10)

    def init_data(self):
        self.browse_button.configure(image=self.controller.model.folder_image, text="Browse Folder", compound="left")
        self.pause_music_button.configure(image=self.controller.model.play_button, fg_color="transparent")
        self.next_music_button.configure(image=self.controller.model.next_button, fg_color="transparent")
        self.previous_music_button.configure(image=self.controller.model.previous_button, fg_color="transparent")

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
