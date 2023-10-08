import customtkinter
from PIL import Image
from Character_Sheet_Frame import Character_Sheet_Frame
from Map_Frame import Map_Frame
from Monster_Frame import Monster_Frame
from Music_Frame import Music_Frame

# Configuration
config = {
    "WINDOW_TITLE": "Pathfinder Dungeon Master Helper",
    "WINDOW_WIDTH": 1100,
    "WINDOW_HEIGHT": 800,
    "COLORS": {
        "TEXT": "#EEEEEE",
        "BUTTON": "#00ADB5",
        "HOVER": "#007880"
    }
}

customtkinter.set_appearance_mode("Dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(config["WINDOW_TITLE"])
        self.geometry(f"{config['WINDOW_WIDTH']}x{config['WINDOW_HEIGHT']}")
        self.after(201, lambda: self.iconbitmap('Images/Dungeon_Master.ico'))
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()

        self.frames = {}
        container = customtkinter.CTkFrame(self)
        container.grid(row=0, column=1, sticky="nsew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frame_classes = [Character_Sheet_Frame, Map_Frame, Monster_Frame, Music_Frame]
        for F in frame_classes:
            frame = F(container, self, config)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Character_Sheet_Frame)

    def create_sidebar(self):
        sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        sidebar_frame.grid_rowconfigure(5, weight=1)

        logo_label = customtkinter.CTkLabel(sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=25, weight="bold"), text_color=config["COLORS"]["TEXT"])
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        button_data = [
            {"name": "Character_Sheet", "text": "Character", "frame_class": Character_Sheet_Frame},
            {"name": "Map", "text": "Map", "frame_class": Map_Frame},
            {"name": "Monster", "text": "Monster", "frame_class": Monster_Frame},
            {"name": "Music", "text": "Music", "frame_class": Music_Frame}
        ]

        for i, button_info in enumerate(button_data):
            image = customtkinter.CTkImage(light_image=Image.open(f"Images/{button_info['name']}.png"), dark_image=Image.open(f"Images/{button_info['name']}.png"), size=(25, 25))
            button = customtkinter.CTkButton(
                sidebar_frame,
                corner_radius=10,
                text=button_info["text"],
                text_color=config["COLORS"]["TEXT"],
                fg_color=config["COLORS"]["BUTTON"],
                hover_color=config["COLORS"]["HOVER"],
                image=image,
                compound="left",
                command=lambda class_name=button_info["frame_class"]: self.show_frame(class_name)
            )
            button.grid(row=i + 1, column=0, padx=20, pady=10)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
