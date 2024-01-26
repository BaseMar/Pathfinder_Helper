import customtkinter
from PIL import Image
from Character_Sheet_Controller import CharacterSheetController
from Character_Sheet_Model import CharacterSheetModel
from Character_Sheet_View import CharacterSheetView
from Map_Controller import MapController
from Map_Model import MapModel
from Map_View import MapView
from Monster_Controller import MonsterController
from Monster_Model import MonsterModel
from Monster_View import MonsterView
from Music_Controller import MusicController
from Music_Model import MusicModel
from Music_View import MusicView

# Configuration
config = {
    "WINDOW_TITLE": "Pathfinder Dungeon Master Helper",
    "WINDOW_WIDTH": 1200,
    "WINDOW_HEIGHT": 700,
    "COLORS": {
        "TEXT": "#EEEEEE",
        "BUTTON": "#00ADB5",
        "HOVER": "#007880"
    }
}

customtkinter.set_appearance_mode("Dark")


class App(customtkinter.CTk):
    def __init__(self):
        self.frames = []
        super().__init__()
        self.title(config["WINDOW_TITLE"])
        self.geometry(f"{config['WINDOW_WIDTH']}x{config['WINDOW_HEIGHT']}")
        self.after(201, lambda: self.iconbitmap('Images/Dungeon_Master.ico'))
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()

        self.container = customtkinter.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.init_modules()
        self.show_frame(0)  # Show Character Sheet Frame on start

    def init_modules(self):
        modules = [
            (CharacterSheetModel, CharacterSheetView, CharacterSheetController),
            (MapModel, MapView, MapController),
            (MonsterModel, MonsterView, MonsterController),
            (MusicModel, MusicView, MusicController),
        ]

        for model_class, view_class, controller_class in modules:
            model = model_class()
            view = view_class(self.container, config)
            controller = controller_class(model, view)
            view.set_controller(controller)

            self.frames.append(view)
            view.init_data()

    def create_sidebar(self):
        sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        sidebar_frame.grid_rowconfigure(5, weight=1)

        logo_label = customtkinter.CTkLabel(
            sidebar_frame,
            text="Menu",
            font=customtkinter.CTkFont(size=25, weight="bold"),
            text_color=config["COLORS"]["TEXT"]
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        buttons_data = [
            ("Character Sheet", "Character_Sheet.png"),
            ("Map", "Map.png"),
            ("Monster", "Monster.png"),
            ("Music", "Music.png"),
        ]

        for i, (text, image_path) in enumerate(buttons_data):
            button = customtkinter.CTkButton(
                sidebar_frame,
                corner_radius=10,
                text=text,
                text_color=config["COLORS"]["TEXT"],
                fg_color=config["COLORS"]["BUTTON"],
                hover_color=config["COLORS"]["HOVER"],
                image=customtkinter.CTkImage(
                    light_image=Image.open(f"Images/{image_path}"),
                    dark_image=Image.open(f"Images/{image_path}"),
                    size=(25, 25)
                ),
                compound="left",
                command=lambda i=i: self.show_frame(i)
            )
            button.grid(row=i + 1, column=0, padx=20, pady=10, sticky="nsew")

    def show_frame(self, index):
        for frame in self.frames:
            frame.grid_forget()
        self.frames[index].grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
