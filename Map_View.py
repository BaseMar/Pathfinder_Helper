import tkinter.messagebox

import customtkinter
from PIL import Image
from Player import Player
import re

def validate(new_value):
    return len(new_value) <= 30 and new_value.isalpha() or new_value == ""

def validate_2(new_value):
    return re.match("^\d{0,3}$", new_value) is not None

class MapView(customtkinter.CTkFrame):
    def __init__(self, parent, config):
        self.config = config
        self.controller = None

        super().__init__(parent)
        image_path = "load_map.png"
        self.load_map_button = customtkinter.CTkButton(self, corner_radius=10, text="Load Map", text_color=config["COLORS"]["TEXT"], fg_color=config["COLORS"]["BUTTON"], hover_color=config["COLORS"]["HOVER"], image=customtkinter.CTkImage(light_image=Image.open(f"Images/{image_path}"), dark_image=Image.open(f"Images/{image_path}"), size=(25, 25)), compound="left", command=self.load_map)
        self.initiative_list_frame = Player(master=self, width=300, corner_radius=0, command=self.remove_player_from_list)

        self.player_name_var = customtkinter.StringVar(value="Player name")
        self.player_name = customtkinter.CTkEntry(self, width=100, textvariable=self.player_name_var)
        self.player_init_var = customtkinter.StringVar(value="Init")
        self.player_init = customtkinter.CTkEntry(self, width=40, textvariable=self.player_init_var)
        self.player_hp_var = customtkinter.StringVar(value="HP")
        self.player_hp = customtkinter.CTkEntry(self, width=40, textvariable=self.player_hp_var)

        self.add_player_button = customtkinter.CTkButton(self, text="Add Object", text_color=config["COLORS"]["TEXT"], fg_color=config["COLORS"]["BUTTON"], hover_color=config["COLORS"]["HOVER"], command=self.add_player)

        self.roll_dice_combobox = customtkinter.CTkComboBox(self, command=self.roll_dice)
        self.bonus_entry_var = customtkinter.StringVar()
        self.bonus_entry = customtkinter.CTkEntry(self, textvariable=self.bonus_entry_var, width=50)
        self.result_label = customtkinter.CTkLabel(self, text="Result: 0", text_color=config["COLORS"]["TEXT"])
        self.multiply_dice_entry_var = customtkinter.StringVar()
        self.multiply_dice_entry = customtkinter.CTkEntry(self, textvariable=self.multiply_dice_entry_var, width=50)
        self.grid_widgets()

        # validations
        vcd = (self.register(validate), '%P')
        self.player_name.configure(validate="key", validatecommand=vcd)
        vcd_2 = (self.register(validate_2), '%P')
        self.multiply_dice_entry.configure(validate="key", validatecommand=vcd_2)
        self.player_init.configure(validate="key", validatecommand=vcd_2)
        self.bonus_entry.configure(validate="key", validatecommand=vcd_2)
        self.player_hp.configure(validate="key", validatecommand=vcd_2)

    def set_controller(self, controller):
        self.controller = controller

    def grid_widgets(self):
        self.load_map_button.grid(row=0, column=0, padx=10, pady=10)
        self.initiative_list_frame.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.player_name.grid(row=1, column=1, padx=5, pady=5)
        self.player_init.grid(row=1, column=2, padx=5, pady=5)
        self.player_hp.grid(row=1, column=3, padx=5, pady=5)
        self.add_player_button.grid(row=1, column=4, padx=5, pady=5)
        self.multiply_dice_entry.grid(row=2, column=0, padx=10, pady=10)
        self.roll_dice_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.bonus_entry.grid(row=2, column=2, padx=10, pady=10)
        self.result_label.grid(row=2, column=3, padx=10, pady=10)

    def init_data(self):
        self.roll_dice_combobox.configure(values=self.controller.model.dice_list)

    def pull_data(self, model):
        self.result_label.configure(text=f"Result: {model.result}")

    def load_map(self):
        self.controller.load_map()

    def remove_player_from_list(self, item):
        self.controller.remove_player(item)

    def add_player(self):
        name = self.player_name_var.get().strip()
        initiative = self.player_init_var.get().strip()
        hp = self.player_hp_var.get().strip()
        if not name or not initiative or not hp:
            tkinter.messagebox.showerror("Error", "Name, initiative, or HP cannot be empty.")
            return

        item = f"{initiative} {name} {hp}"
        self.controller.add_player(item)

    def roll_dice(self, choice):
        multiply = self.multiply_dice_entry_var.get() or 1
        bonus = self.bonus_entry_var.get() or 0
        self.pull_data(self.controller.roll_dice(choice, bonus, multiply))
