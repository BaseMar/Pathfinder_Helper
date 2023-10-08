import customtkinter
from Monster import Monster
from abstract_view_for_sheets import AbstractViewForSheets
import csv
from CTkListbox import *

class Monster_Frame(AbstractViewForSheets):
    def __init__(self, parent, controller, config):
        super().__init__(parent, controller, config)
        self.setup_frame()
        self.monster_list = {}

        # Load monster database
        self.load_data()

        # Monster list box
        self.monster_var = customtkinter.StringVar()
        self.monster_combo_box = customtkinter.CTkComboBox(self, values=list(self.monster_list.keys()), text_color=config["COLORS"]["TEXT"], variable=self.monster_var, command=self.display_monster_info)
        self.monster_combo_box.place(y=430, x=450)

    def setup_frame(self):
        super().setup_frame()

    def load_data(self):
        with open("DataBase/MonsterList.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            for row in csv_reader:
                monster = Monster(row)
                self.monster_list[monster.name] = monster

    def display_monster_info(self, event):
        selected_monster_name = self.monster_var.get()
        selected_monster = self.monster_list[selected_monster_name]
        self.name.set(selected_monster.name)
        self.alignment_var.set(selected_monster.alignment)
        self.level_var.set(selected_monster.cr)
        self.experience_var.set(selected_monster.xp)
