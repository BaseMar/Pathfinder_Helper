import customtkinter
from Monster import Monster
from abstract_view_for_sheets import AbstractViewForSheets, calculate_bonus_modifier
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
        self.label.setvar(name="name", value=f"Name: {selected_monster.name}")
        self.alignment.setvar(name="alignment", value=f"Alignment: {selected_monster.alignment}")
        self.level.setvar(name="lvl", value=f"LvL/CR: {selected_monster.cr}")
        self.experience.setvar(name="exp", value=f"EXP: {selected_monster.xp}")

        self.strength_sum.setvar(name="strength sum", value=selected_monster.str)
        str_calc = calculate_bonus_modifier(score=int(self.str_sum_var.get()))
        self.strength_bonus_mod.setvar(name="strength modifier", value=str_calc)

        self.dexterity_sum.setvar(name="dexterity sum", value=selected_monster.dex)
        dex_calc = calculate_bonus_modifier(score=int(self.dex_sum_var.get()))
        self.dexterity_bonus_mod.setvar(name="dexterity modifier", value=dex_calc)

        self.constitution_sum.setvar(name="constitution sum", value=selected_monster.con)
        con_calc = calculate_bonus_modifier(score=int(self.con_sum_var.get()))
        self.constitution_bonus_mod.setvar(name="constitution modifier", value=con_calc)

        self.intelligence_sum.setvar(name="intelligence sum", value=selected_monster.int)
        int_calc = calculate_bonus_modifier(score=int(self.int_sum_var.get()))
        self.intelligence_bonus_mod.setvar(name="intelligence modifier", value=int_calc)

        self.wisdom_sum.setvar(name="wisdom sum", value=selected_monster.wis)
        wis_calc = calculate_bonus_modifier(score=int(self.wis_sum_var.get()))
        self.wisdom_bonus_mod.setvar(name="wisdom modifier", value=wis_calc)

        self.charisma_sum.setvar(name="charisma sum", value=selected_monster.cha)
        cha_calc = calculate_bonus_modifier(score=int(self.cha_sum_var.get()))
        self.charisma_bonus_mod.setvar(name="charisma modifier", value=cha_calc)
