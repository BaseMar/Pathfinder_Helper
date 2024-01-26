import math
import os
from Deity import Deity
from MySQL_Service import MySQLService
from Races import Races

def calculate_sum(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

class CharacterSheetController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def load_data_from_db(self):
        data_container = MySQLService('Deity')
        deity = data_container.load_data(Deity.Deity)
        self.model.character_deity_list = [deity.name for deity in deity]
        self.model.character_alignment_list = [deity.alignment for deity in deity]
        self.model.character_alignment_list = list(dict.fromkeys(self.model.character_alignment_list))

        data_container = MySQLService('Races')
        races_name = data_container.load_data(Races.Races)
        self.model.character_race_list = [races_name.name for races_name in races_name]

        classes_folder_path = 'Classes'
        if os.path.exists(classes_folder_path) and os.path.isdir(classes_folder_path):
            class_files = [f for f in os.listdir(classes_folder_path) if
                           os.path.isfile(os.path.join(classes_folder_path, f))]
            self.model.character_class_list.extend([os.path.splitext(f)[0] for f in class_files])

        return self.model

    def calculate_mod(self, *args):
        suma = 0
        for arg in args[1:]:
            suma += arg
        mod = math.floor((suma - 10) / 2)

        match args[0]:
            case "str":
                self.model.str_score = args[1]
                self.model.str_increase = args[2]
                self.model.str_other_bonuses = args[3]
                self.model.str_sum = suma
                self.model.str_mod = mod
            case "dex":
                self.model.dex_score = args[1]
                self.model.dex_increase = args[2]
                self.model.dex_other_bonuses = args[3]
                self.model.dex_sum = suma
                self.model.dex_mod = mod
            case "con":
                self.model.con_score = args[1]
                self.model.con_increase = args[2]
                self.model.con_other_bonuses = args[3]
                self.model.con_sum = suma
                self.model.con_mod = mod
            case "int":
                self.model.int_score = args[1]
                self.model.int_increase = args[2]
                self.model.int_other_bonuses = args[3]
                self.model.int_sum = suma
                self.model.int_mod = mod
            case "wis":
                self.model.wis_score = args[1]
                self.model.wis_increase = args[2]
                self.model.wis_other_bonuses = args[3]
                self.model.wis_sum = suma
                self.model.wis_mod = mod
            case "cha":
                self.model.cha_score = args[1]
                self.model.cha_increase = args[2]
                self.model.cha_other_bonuses = args[3]
                self.model.cha_sum = suma
                self.model.cha_mod = mod
            case _:
                pass
        return self.model

    def size_mod(self):
        match self.model.character_size:
            case "Fine":
                self.model.character_cmb_size_mod = -8
                self.model.character_cmd_size_mod = -8
                self.model.character_ac_size_modifier = 8
            case "Diminutive":
                self.model.character_cmb_size_mod = -4
                self.model.character_cmd_size_mod = -4
                self.model.character_ac_size_modifier = 4
            case "Tiny":
                self.model.character_cmb_size_mod = -2
                self.model.character_cmd_size_mod = -2
                self.model.character_ac_size_modifier = 2
            case "Small":
                self.model.character_cmb_size_mod = -1
                self.model.character_cmd_size_mod = -1
                self.model.character_ac_size_modifier = 1
            case "Medium":
                self.model.character_cmb_size_mod = 0
                self.model.character_cmd_size_mod = 0
                self.model.character_ac_size_modifier = 0
            case "Large":
                self.model.character_cmb_size_mod = 1
                self.model.character_cmd_size_mod = 1
                self.model.character_ac_size_modifier = -1
            case "Huge":
                self.model.character_cmb_size_mod = 2
                self.model.character_cmd_size_mod = 2
                self.model.character_ac_size_modifier = -2
            case "Gargantuan":
                self.model.character_cmb_size_mod = 4
                self.model.character_cmd_size_mod = 4
                self.model.character_ac_size_modifier = -4
            case "Colossal":
                self.model.character_cmb_size_mod = 8
                self.model.character_cmd_size_mod = 8
                self.model.character_ac_size_modifier = -8

    def calculate_ac(self):
        armor = self.model.character_ac_armor_bonus
        shield = self.model.character_ac_shield_bonus
        size = self.model.character_ac_size_modifier
        natural = self.model.character_ac_natural_armor
        deflect = self.model.character_ac_deflection_bonus
        misc = self.model.character_ac_misc_modifier

        suma = calculate_sum(10, armor, shield, self.model.dex_mod, size, natural, deflect, misc)
        self.model.character_ac_sum = suma
        suma = calculate_sum(10, self.model.dex_mod, size, deflect, misc)
        self.model.character_touch_ac = suma
        suma = calculate_sum(10, armor, shield, size, natural, deflect, misc)
        self.model.character_flat_ac = suma

    def calculate_initiative(self):
        misc = self.model.character_initiative_misc
        suma = calculate_sum(self.model.dex_mod, misc)
        self.model.character_initiative_total = suma

    def calculate_fortitude_save(self):
        base = self.model.character_fort_base
        magic = self.model.character_fort_magic_mod
        misc = self.model.character_fort_misc_mod
        suma = calculate_sum(base, self.model.con_mod, magic, misc)
        self.model.character_fort_save_sum = suma

    def calculate_reflex_save(self):
        base = self.model.character_ref_base
        magic = self.model.character_ref_magic_mod
        misc = self.model.character_ref_misc_mod
        suma = calculate_sum(base, self.model.dex_mod, magic, misc)
        self.model.character_ref_save_sum = suma

    def calculate_will_save(self):
        base = self.model.character_will_base
        magic = self.model.character_will_magic_mod
        misc = self.model.character_will_misc_mod
        suma = calculate_sum(base, self.model.wis_mod, magic, misc)
        self.model.character_will_save_sum = suma

    def calculate_cmb(self):
        bab = self.model.character_bab
        seize = self.model.character_cmb_size_mod
        suma = calculate_sum(bab, seize, self.model.str_mod)
        self.model.character_cmb_sum = suma

    def calculate_cmd(self):
        bab = self.model.character_bab
        seize = self.model.character_cmd_size_mod
        suma = calculate_sum(bab, self.model.str_mod, self.model.dex_mod, seize, 10)
        self.model.character_cmd_sum = suma


