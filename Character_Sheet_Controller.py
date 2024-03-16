import math
import os
from Deity import Deity
from MySQL_Service import MySQLService
from Races import Races
from Classes import Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Wizard
from Skills import Skills
from Spells import Spells
from Items import Armor_Shield, Magic_Items

def check_trained_skills(setting, class_name):
    match class_name:
        case "Barbarian":
            if setting.barbarian == "1":
                return True
            else:
                return False
        case "Bard":
            if setting.bard == "1":
                return True
            else:
                return False
        case "Cleric":
            if setting.cleric == "1":
                return True
            else:
                return False
        case "Druid":
            if setting.druid == "1":
                return True
            else:
                return False
        case "Fighter":
            if setting.fighter == "1":
                return True
            else:
                return False
        case "Monk":
            if setting.monk == "1":
                return True
            else:
                return False
        case "Paladin":
            if setting.paladin == "1":
                return True
            else:
                return False
        case "Ranger":
            if setting.ranger == "1":
                return True
            else:
                return False
        case "Rogue":
            if setting.rogue == "1":
                return True
            else:
                return False
        case "Sorcerer":
            if setting.sorcerer == "1":
                return True
            else:
                return False
        case "Wizard":
            if setting.wizard == "1":
                return True
            else:
                return False


class CharacterSheetController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.data_container = MySQLService()
        self.disable_all_spell_buttons()

    def load_data_from_db(self):
        deity = self.data_container.load_data('Deity', Deity.Deity)
        self.model.character_deity_list = [deity.name for deity in deity]
        self.model.character_alignment_list = [deity.alignment for deity in deity]
        self.model.character_alignment_list = list(dict.fromkeys(self.model.character_alignment_list))

        races_name = self.data_container.load_data("Races", Races.Races)
        self.model.character_race_list = [races_name.name for races_name in races_name]

        classes_folder_path = 'Classes'
        if os.path.exists(classes_folder_path) and os.path.isdir(classes_folder_path):
            class_files = [f for f in os.listdir(classes_folder_path) if
                           os.path.isfile(os.path.join(classes_folder_path, f))]
            self.model.character_class_list.extend([os.path.splitext(f)[0] for f in class_files])
        self.model.character_filename = self.model.character_class_list[0]

        skill_folder_path = "Skills"
        if os.path.exists(skill_folder_path) and os.path.isdir(skill_folder_path):
            skills_object = self.data_container.load_data("Skill", Skills.Skills)
            self.model.skill_dictionary_settings = {skills_object.name: skills_object for skills_object in skills_object}

        spells_object = self.data_container.load_data("Spells", Spells.Spells)
        self.model.character_spell_list = [spells_object for spells_object in spells_object]

        item_object = self.data_container.load_data("armor_shield", Armor_Shield.Armor_Shield)
        item_object_2 = self.data_container.load_data("magic_items", Magic_Items.Magic_Items)
        self.model.gear_items = [item for sublist in [item_object, item_object_2] for item in sublist]
        self.model.head_list = [item.name for item in self.model.gear_items if item.slot == "Head"]
        self.model.headband_list = [item.name for item in self.model.gear_items if item.slot == "Headband"]
        self.model.eyes_list = [item.name for item in self.model.gear_items if item.slot == "Eye"]
        self.model.shoulders_list = [item.name for item in self.model.gear_items if item.slot == "Shoulders"]
        self.model.neck_list = [item.name for item in self.model.gear_items if item.slot == "Neck"]
        self.model.chest_list = [item.name for item in self.model.gear_items if item.slot == "Chest"]
        self.model.body_list = [item.name for item in self.model.gear_items if item.slot == "Body"]
        self.model.armor_list = [item.name for item in self.model.gear_items if item.slot == "Armor"]
        self.model.hand_list = [item.name for item in self.model.gear_items if item.slot in ["Shield", "Weapon"]]
        self.model.belt_list = [item.name for item in self.model.gear_items if item.slot == "Belt"]
        self.model.wrist_list = [item.name for item in self.model.gear_items if item.slot == "Wrist"]
        self.model.hands_list = [item.name for item in self.model.gear_items if item.slot == "Hands"]
        self.model.ring_list = [item.name for item in self.model.gear_items if item.slot == "Ring"]
        self.model.feet_list = [item.name for item in self.model.gear_items if item.slot == "Feet"]

        return self.model

    def calculate_mod(self, attr_type, score, increase):
        model_attr_score = score
        model_attr_increase = increase
        model_attr_other_bonuses = getattr(self.model, f"{attr_type}_race_bonus") + getattr(self.model, f"{attr_type}_item_bonus") + getattr(self.model, f"{attr_type}_spell_bonus")

        suma = sum([score, increase, model_attr_other_bonuses])
        mod = math.floor((suma - 10) / 2)

        setattr(self.model, f"{attr_type}_score", model_attr_score)
        setattr(self.model, f"{attr_type}_increase", model_attr_increase)
        setattr(self.model, f"{attr_type}_other_bonuses", model_attr_other_bonuses)
        setattr(self.model, f"{attr_type}_sum", suma)
        setattr(self.model, f"{attr_type}_mod", mod)

        return self.model

    def race_selection(self, race_name):
        races = self.data_container.load_data("Races", Races.Races)
        selected_race = [races for races in races if races.name == race_name][0]
        self.model.str_race_bonus = selected_race.str_bonus
        self.model.dex_race_bonus = selected_race.dex_bonus
        self.model.con_race_bonus = selected_race.con_bonus
        self.model.int_race_bonus = selected_race.int_bonus
        self.model.wis_race_bonus = selected_race.wis_bonus
        self.model.cha_race_bonus = selected_race.cha_bonus
        self.model.character_size = selected_race.size
        self.model.character_speed = selected_race.speed
        self.model.character_languages_list = selected_race.languages.split(',')
        self.model.character_racial_traits_list = selected_race.special.split(',')

        for attribute in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            score_attr = getattr(self.model, f"{attribute}_score")
            increase_attr = getattr(self.model, f"{attribute}_increase")
            self.calculate_mod(attribute, score_attr, increase_attr)
        self.size_mod()
        return self.model

    def class_selection(self, class_name):
        lvl = self.model.character_selected_lvl
        self.model.character_filename = class_name
        self.model.character_feats_list = []
        self.model.selected_character_class = None
        self.reset_all_misc_mod_skills()
        self.reset_all_spells()
        self.enable_all_spell_buttons()
        self.trained_skills(class_name)
        match class_name:
            case "Barbarian":
                self.model.selected_character_class = self.data_container.load_data(class_name, Barbarian.Barbarian)
                self.disable_all_spell_buttons()
            case "Bard":
                self.model.selected_character_class = self.data_container.load_data(class_name, Bard.Bard)
                self.pull_bard_spells(self.model.selected_character_class[lvl-1])
            case "Cleric":
                self.model.selected_character_class = self.data_container.load_data(class_name, Cleric.Cleric)
                self.pull_cleric_spells(self.model.selected_character_class[lvl-1])
            case "Druid":
                self.model.selected_character_class = self.data_container.load_data(class_name, Druid.Druid)
                self.pull_druid_spells(self.model.selected_character_class[lvl-1])
            case "Fighter":
                self.model.selected_character_class = self.data_container.load_data(class_name, Fighter.Fighter)
                self.disable_all_spell_buttons()
            case "Monk":
                self.model.selected_character_class = self.data_container.load_data(class_name, Monk.Monk)
                self.disable_all_spell_buttons()
            case "Paladin":
                self.model.selected_character_class = self.data_container.load_data(class_name, Paladin.Paladin)
                self.pull_paladin_spells(self.model.selected_character_class[lvl-1])
            case "Ranger":
                self.model.selected_character_class = self.data_container.load_data(class_name, Ranger.Ranger)
                self.pull_ranger_spells(self.model.selected_character_class[lvl-1])
            case "Rogue":
                self.model.selected_character_class = self.data_container.load_data(class_name, Rogue.Rogue)
                self.disable_all_spell_buttons()
            case "Sorcerer":
                self.model.selected_character_class = self.data_container.load_data(class_name, Sorcerer.Sorcerer)
                self.pull_sorcerer_spells(self.model.selected_character_class[lvl-1])
            case "Wizard":
                self.model.selected_character_class = self.data_container.load_data(class_name, Wizard.Wizard)
                self.pull_wizard_spells(self.model.selected_character_class[lvl-1])

        self.model.character_bab = self.model.selected_character_class[lvl-1].bab
        self.model.character_fort_base = self.model.selected_character_class[lvl-1].fort_save
        self.model.character_ref_base = self.model.selected_character_class[lvl-1].ref_save
        self.model.character_will_base = self.model.selected_character_class[lvl-1].will_save
        self.model.character_feats_list.extend([feat.strip() for char_class in self.model.selected_character_class if char_class.lvl <= lvl for feat in char_class.special.split(',') if feat.strip()])

        return self.model

    def change_lvl(self, lvl):
        self.model.character_selected_lvl = int(lvl)
        self.class_selection(self.model.character_filename)
        return self.model

    def pull_bard_spells(self, bard):
        ability_mod = self.model.cha_mod
        self.model.spells_known_0 = bard.spells_known_0
        self.model.spell_save_dc_0 = sum([10, 0, ability_mod])
        self.model.spells_known_1 = bard.spells_known_1
        self.model.spell_save_dc_1 = sum([10, 1, ability_mod])
        self.model.spells_per_day_1 = bard.spells_per_day_1
        self.model.spell_bonus_1 = 0
        self.model.spells_known_2 = bard.spells_known_2
        self.model.spell_save_dc_2 = sum([10, 2, ability_mod])
        self.model.spells_per_day_2 = bard.spells_per_day_2
        self.model.spell_bonus_2 = 0
        self.model.spells_known_3 = bard.spells_known_3
        self.model.spell_save_dc_3 = sum([10, 3, ability_mod])
        self.model.spells_per_day_3 = bard.spells_per_day_3
        self.model.spell_bonus_3 = 0
        self.model.spells_known_4 = bard.spells_known_4
        self.model.spell_save_dc_4 = sum([10, 4, ability_mod])
        self.model.spells_per_day_4 = bard.spells_per_day_4
        self.model.spell_bonus_4 = 0
        self.model.spells_known_5 = bard.spells_known_5
        self.model.spell_save_dc_5 = sum([10, 5, ability_mod])
        self.model.spells_per_day_5 = bard.spells_per_day_5
        self.model.spell_bonus_5 = 0
        self.model.spells_known_6 = bard.spells_known_6
        self.model.spell_save_dc_6 = sum([10, 6, ability_mod])
        self.model.spells_per_day_6 = bard.spells_per_day_6
        self.model.spell_bonus_6 = 0
        self.view.spell_7_button.configure(state="disabled")
        self.view.spell_8_button.configure(state="disabled")
        self.view.spell_9_button.configure(state="disabled")

    def pull_cleric_spells(self, cleric):
        ability_mod = self.model.wis_mod
        self.model.spell_save_dc_0 = sum([10, 0, ability_mod])
        self.model.spells_per_day_0 = cleric.spells_per_day_0
        self.model.spell_save_dc_1 = sum([10, 1, ability_mod])
        self.model.spells_per_day_1 = cleric.spells_per_day_1
        self.model.spell_bonus_1 = 0
        self.model.spell_save_dc_2 = sum([10, 2, ability_mod])
        self.model.spells_per_day_2 = cleric.spells_per_day_2
        self.model.spell_bonus_2 = 0
        self.model.spell_save_dc_3 = sum([10, 3, ability_mod])
        self.model.spells_per_day_3 = cleric.spells_per_day_3
        self.model.spell_bonus_3 = 0
        self.model.spell_save_dc_4 = sum([10, 4, ability_mod])
        self.model.spells_per_day_4 = cleric.spells_per_day_4
        self.model.spell_bonus_4 = 0
        self.model.spell_save_dc_5 = sum([10, 5, ability_mod])
        self.model.spells_per_day_5 = cleric.spells_per_day_5
        self.model.spell_bonus_5 = 0
        self.model.spell_save_dc_6 = sum([10, 6, ability_mod])
        self.model.spells_per_day_6 = cleric.spells_per_day_6
        self.model.spell_bonus_6 = 0
        self.model.spell_save_dc_7 = sum([10, 7, ability_mod])
        self.model.spells_per_day_7 = cleric.spells_per_day_7
        self.model.spell_save_dc_8 = sum([10, 8, ability_mod])
        self.model.spells_per_day_8 = cleric.spells_per_day_8
        self.model.spell_bonus_8 = 0
        self.model.spell_save_dc_9 = sum([10, 9, ability_mod])
        self.model.spells_per_day_9 = cleric.spells_per_day_9
        self.model.spell_bonus_9 = 0

    def pull_druid_spells(self, druid):
        ability_mod = self.model.wis_mod
        self.model.spell_save_dc_0 = sum([10, 0, ability_mod])
        self.model.spells_per_day_0 = druid.spells_per_day_0
        self.model.spell_save_dc_1 = sum([10, 1, ability_mod])
        self.model.spells_per_day_1 = druid.spells_per_day_1
        self.model.spell_bonus_1 = 0
        self.model.spell_save_dc_2 = sum([10, 2, ability_mod])
        self.model.spells_per_day_2 = druid.spells_per_day_2
        self.model.spell_bonus_2 = 0
        self.model.spell_save_dc_3 = sum([10, 3, ability_mod])
        self.model.spells_per_day_3 = druid.spells_per_day_3
        self.model.spell_bonus_3 = 0
        self.model.spell_save_dc_4 = sum([10, 4, ability_mod])
        self.model.spells_per_day_4 = druid.spells_per_day_4
        self.model.spell_bonus_4 = 0
        self.model.spell_save_dc_5 = sum([10, 5, ability_mod])
        self.model.spells_per_day_5 = druid.spells_per_day_5
        self.model.spell_bonus_5 = 0
        self.model.spell_save_dc_6 = sum([10, 6, ability_mod])
        self.model.spells_per_day_6 = druid.spells_per_day_6
        self.model.spell_bonus_6 = 0
        self.model.spell_save_dc_7 = sum([10, 7, ability_mod])
        self.model.spells_per_day_7 = druid.spells_per_day_7
        self.model.spell_save_dc_8 = sum([10, 8, ability_mod])
        self.model.spells_per_day_8 = druid.spells_per_day_8
        self.model.spell_bonus_8 = 0
        self.model.spell_save_dc_9 = sum([10, 9, ability_mod])
        self.model.spells_per_day_9 = druid.spells_per_day_9
        self.model.spell_bonus_9 = 0

    def pull_paladin_spells(self, paladin):
        ability_mod = self.model.cha_mod
        self.model.spell_save_dc_1 = sum([10, 1, ability_mod])
        self.model.spells_per_day_1 = paladin.spells_per_day_1
        self.model.spell_bonus_1 = 0
        self.model.spell_save_dc_2 = sum([10, 2, ability_mod])
        self.model.spells_per_day_2 = paladin.spells_per_day_2
        self.model.spell_bonus_2 = 0
        self.model.spell_save_dc_3 = sum([10, 3, ability_mod])
        self.model.spells_per_day_3 = paladin.spells_per_day_3
        self.model.spell_bonus_3 = 0
        self.model.spell_save_dc_4 = sum([10, 4, ability_mod])
        self.model.spells_per_day_4 = paladin.spells_per_day_4
        self.model.spell_bonus_4 = 0
        self.view.spell_0_button.configure(state="disabled")
        self.view.spell_5_button.configure(state="disabled")
        self.view.spell_6_button.configure(state="disabled")
        self.view.spell_7_button.configure(state="disabled")
        self.view.spell_8_button.configure(state="disabled")
        self.view.spell_9_button.configure(state="disabled")
        
    def pull_ranger_spells(self, ranger):
        ability_mod = self.model.wis_mod
        self.model.spell_save_dc_1 = sum([10, 1, ability_mod])
        self.model.spells_per_day_1 = ranger.spells_per_day_1
        self.model.spell_bonus_1 = 0
        self.model.spell_save_dc_2 = sum([10, 2, ability_mod])
        self.model.spells_per_day_2 = ranger.spells_per_day_2
        self.model.spell_bonus_2 = 0
        self.model.spell_save_dc_3 = sum([10, 3, ability_mod])
        self.model.spells_per_day_3 = ranger.spells_per_day_3
        self.model.spell_bonus_3 = 0
        self.model.spell_save_dc_4 = sum([10, 4, ability_mod])
        self.model.spells_per_day_4 = ranger.spells_per_day_4
        self.model.spell_bonus_4 = 0
        self.view.spell_0_button.configure(state="disabled")
        self.view.spell_5_button.configure(state="disabled")
        self.view.spell_6_button.configure(state="disabled")
        self.view.spell_7_button.configure(state="disabled")
        self.view.spell_8_button.configure(state="disabled")
        self.view.spell_9_button.configure(state="disabled")

    def pull_sorcerer_spells(self, sorcerer):
        ability_mod = self.model.cha_mod
        self.model.spells_known_0 = sorcerer.spells_known_0
        self.model.spell_save_dc_0 = sum([10, 0, ability_mod])
        self.model.spells_known_1 = sorcerer.spells_known_1
        self.model.spell_save_dc_1 = sum([10, 1, ability_mod])
        self.model.spells_per_day_1 = sorcerer.spells_per_day_1
        self.model.spell_bonus_1 = 0
        self.model.spells_known_2 = sorcerer.spells_known_2
        self.model.spell_save_dc_2 = sum([10, 2, ability_mod])
        self.model.spells_per_day_2 = sorcerer.spells_per_day_2
        self.model.spell_bonus_2 = 0
        self.model.spells_known_3 = sorcerer.spells_known_3
        self.model.spell_save_dc_3 = sum([10, 3, ability_mod])
        self.model.spells_per_day_3 = sorcerer.spells_per_day_3
        self.model.spell_bonus_3 = 0
        self.model.spells_known_4 = sorcerer.spells_known_4
        self.model.spell_save_dc_4 = sum([10, 4, ability_mod])
        self.model.spells_per_day_4 = sorcerer.spells_per_day_4
        self.model.spell_bonus_4 = 0
        self.model.spells_known_5 = sorcerer.spells_known_5
        self.model.spell_save_dc_5 = sum([10, 5, ability_mod])
        self.model.spells_per_day_5 = sorcerer.spells_per_day_5
        self.model.spell_bonus_5 = 0
        self.model.spells_known_6 = sorcerer.spells_known_6
        self.model.spell_save_dc_6 = sum([10, 6, ability_mod])
        self.model.spells_per_day_6 = sorcerer.spells_per_day_6
        self.model.spell_bonus_6 = 0
        self.model.spells_known_7 = sorcerer.spells_known_7
        self.model.spell_save_dc_7 = sum([10, 7, ability_mod])
        self.model.spells_per_day_7 = sorcerer.spells_per_day_7
        self.model.spell_bonus_7 = 0
        self.model.spells_known_8 = sorcerer.spells_known_8
        self.model.spell_save_dc_8 = sum([10, 8, ability_mod])
        self.model.spells_per_day_8 = sorcerer.spells_per_day_8
        self.model.spell_bonus_8 = 0
        self.model.spells_known_9 = sorcerer.spells_known_9
        self.model.spell_save_dc_9 = sum([10, 9, ability_mod])
        self.model.spells_per_day_9 = sorcerer.spells_per_day_9
        self.model.spell_bonus_9 = 0

    def pull_wizard_spells(self, wizard):
        ability_mod = self.model.int_mod
        self.model.spell_save_dc_0 = sum([10, 0, ability_mod])
        self.model.spells_per_day_0 = wizard.spells_per_day_0
        self.model.spell_save_dc_1 = sum([10, 1, ability_mod])
        self.model.spells_per_day_1 = wizard.spells_per_day_1
        self.model.spell_bonus_1 = 0
        self.model.spell_save_dc_2 = sum([10, 2, ability_mod])
        self.model.spells_per_day_2 = wizard.spells_per_day_2
        self.model.spell_bonus_2 = 0
        self.model.spell_save_dc_3 = sum([10, 3, ability_mod])
        self.model.spells_per_day_3 = wizard.spells_per_day_3
        self.model.spell_bonus_3 = 0
        self.model.spell_save_dc_4 = sum([10, 4, ability_mod])
        self.model.spells_per_day_4 = wizard.spells_per_day_4
        self.model.spell_bonus_4 = 0
        self.model.spell_save_dc_5 = sum([10, 5, ability_mod])
        self.model.spells_per_day_5 = wizard.spells_per_day_5
        self.model.spell_bonus_5 = 0
        self.model.spell_save_dc_6 = sum([10, 6, ability_mod])
        self.model.spells_per_day_6 = wizard.spells_per_day_6
        self.model.spell_bonus_6 = 0
        self.model.spell_save_dc_7 = sum([10, 7, ability_mod])
        self.model.spells_per_day_7 = wizard.spells_per_day_7
        self.model.spell_bonus_7 = 0
        self.model.spell_save_dc_8 = sum([10, 8, ability_mod])
        self.model.spells_per_day_8 = wizard.spells_per_day_8
        self.model.spell_bonus_8 = 0
        self.model.spell_save_dc_9 = sum([10, 9, ability_mod])
        self.model.spells_per_day_9 = wizard.spells_per_day_9
        self.model.spell_bonus_9 = 0

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
        self.calculate_cmb()
        self.calculate_cmd()
        self.calculate_ac()

    def calculate_ac(self):
        armor = self.model.character_ac_armor_bonus
        shield = self.model.character_ac_shield_bonus
        size = self.model.character_ac_size_modifier
        natural = self.model.character_ac_natural_armor
        deflect = self.model.character_ac_deflection_bonus
        misc = self.model.character_ac_misc_modifier

        suma = sum([10, armor, shield, self.model.dex_mod, size, natural, deflect, misc])
        self.model.character_ac_sum = suma
        suma = sum([10, self.model.dex_mod, size, deflect, misc])
        self.model.character_touch_ac = suma
        suma = sum([10, armor, shield, size, natural, deflect, misc])
        self.model.character_flat_ac = suma

    def calculate_initiative(self):
        misc = self.model.character_initiative_misc
        suma = sum([self.model.dex_mod, misc])
        self.model.character_initiative_total = suma

    def calculate_fortitude_save(self):
        base = self.model.character_fort_base
        magic = self.model.character_fort_magic_mod
        misc = self.model.character_fort_misc_mod
        suma = sum([base, self.model.con_mod, magic, misc])
        self.model.character_fort_save_sum = suma

    def calculate_reflex_save(self):
        base = self.model.character_ref_base
        magic = self.model.character_ref_magic_mod
        misc = self.model.character_ref_misc_mod
        suma = sum([base, self.model.dex_mod, magic, misc])
        self.model.character_ref_save_sum = suma

    def calculate_will_save(self):
        base = self.model.character_will_base
        magic = self.model.character_will_magic_mod
        misc = self.model.character_will_misc_mod
        suma = sum([base, self.model.wis_mod, magic, misc])
        self.model.character_will_save_sum = suma

    def calculate_cmb(self):
        bab = self.model.character_bab
        seize = self.model.character_cmb_size_mod
        suma = sum([bab, seize, self.model.str_mod])
        self.model.character_cmb_sum = suma

    def calculate_cmd(self):
        bab = self.model.character_bab
        seize = self.model.character_cmd_size_mod
        suma = sum([bab, self.model.str_mod, self.model.dex_mod, seize, 10])
        self.model.character_cmd_sum = suma

    def calculate_skill(self):
        self.model.acrobatics_sum = sum([self.model.acrobatics_rank, self.model.acrobatics_misc_mod, self.model.dex_mod])
        self.model.appraise_sum = sum([self.model.appraise_rank, self.model.appraise_misc_mod, self.model.int_mod])
        self.model.bluff_sum = sum([self.model.bluff_rank, self.model.bluff_misc_mod, self.model.cha_mod])
        self.model.climb_sum = sum([self.model.climb_rank, self.model.climb_misc_mod, self.model.str_mod])
        self.model.craft_sum = sum([self.model.craft_rank, self.model.craft_misc_mod, self.model.int_mod])
        self.model.diplomacy_sum = sum([self.model.diplomacy_rank, self.model.diplomacy_misc_mod, self.model.cha_mod])
        self.model.disable_device_sum = sum([self.model.disable_device_rank, self.model.disable_device_misc_mod, self.model.dex_mod])
        self.model.disguise_sum = sum([self.model.disguise_rank, self.model.disguise_misc_mod, self.model.cha_mod])
        self.model.escape_artist_sum = sum([self.model.escape_artist_rank, self.model.escape_artist_misc_mod, self.model.dex_mod])
        self.model.fly_sum = sum([self.model.fly_rank, self.model.fly_misc_mod, self.model.dex_mod])
        self.model.handle_animal_sum = sum([self.model.handle_animal_rank, self.model.handle_animal_misc_mod, self.model.cha_mod])
        self.model.heal_sum = sum([self.model.heal_rank, self.model.heal_misc_mod, self.model.wis_mod])
        self.model.intimidate_sum = sum([self.model.intimidate_rank, self.model.intimidate_misc_mod, self.model.cha_mod])
        self.model.knowledge_arcana_sum = sum([self.model.knowledge_arcana_rank, self.model.knowledge_arcana_misc_mod, self.model.int_mod])
        self.model.knowledge_dungeoneering_sum = sum([self.model.knowledge_dungeoneering_rank, self.model.knowledge_dungeoneering_misc_mod, self.model.int_mod])
        self.model.knowledge_engineering_sum = sum([self.model.knowledge_engineering_rank, self.model.knowledge_engineering_misc_mod, self.model.int_mod])
        self.model.knowledge_geography_sum = sum([self.model.knowledge_geography_rank, self.model.knowledge_geography_misc_mod, self.model.int_mod])
        self.model.knowledge_history_sum = sum([self.model.knowledge_history_rank, self.model.knowledge_history_misc_mod, self.model.int_mod])
        self.model.knowledge_local_sum = sum([self.model.knowledge_local_rank, self.model.knowledge_local_misc_mod, self.model.int_mod])
        self.model.knowledge_nature_sum = sum([self.model.knowledge_nature_rank, self.model.knowledge_nature_misc_mod, self.model.int_mod])
        self.model.knowledge_nobility_sum = sum([self.model.knowledge_nobility_rank, self.model.knowledge_nobility_misc_mod, self.model.int_mod])
        self.model.knowledge_planes_sum = sum([self.model.knowledge_planes_rank, self.model.knowledge_planes_misc_mod, self.model.int_mod])
        self.model.knowledge_religion_sum = sum([self.model.knowledge_religion_rank, self.model.knowledge_religion_misc_mod, self.model.int_mod])
        self.model.linguistics_sum = sum([self.model.linguistics_rank, self.model.linguistics_misc_mod, self.model.int_mod])
        self.model.perception_sum = sum([self.model.perception_rank, self.model.perception_misc_mod, self.model.wis_mod])
        self.model.perform_sum = sum([self.model.perform_rank, self.model.perform_misc_mod, self.model.cha_mod])
        self.model.profession_sum = sum([self.model.profession_rank, self.model.profession_misc_mod, self.model.wis_mod])
        self.model.ride_sum = sum([self.model.ride_rank, self.model.ride_misc_mod, self.model.dex_mod])
        self.model.sense_motive_sum = sum([self.model.sense_motive_rank, self.model.sense_motive_misc_mod, self.model.wis_mod])
        self.model.sleight_of_hand_sum = sum([self.model.sleight_of_hand_rank, self.model.sleight_of_hand_misc_mod, self.model.dex_mod])
        self.model.spellcraft_sum = sum([self.model.spellcraft_rank, self.model.spellcraft_misc_mod, self.model.int_mod])
        self.model.stealth_sum = sum([self.model.stealth_rank, self.model.stealth_misc_mod, self.model.dex_mod])
        self.model.survival_sum = sum([self.model.survival_rank, self.model.survival_misc_mod, self.model.wis_mod])
        self.model.swim_sum = sum([self.model.swim_rank, self.model.swim_misc_mod, self.model.str_mod])
        self.model.use_magic_device_sum = sum([self.model.use_magic_device_rank, self.model.use_magic_device_misc_mod, self.model.cha_mod])

        return self.model

    def trained_skills(self, class_name):
        if check_trained_skills(self.model.skill_dictionary_settings["Acrobatics"], class_name) and self.model.acrobatics_rank >= 1:
            self.model.acrobatics_misc_mod = 3
        else:
            self.model.acrobatics_misc_mod = 0
        if check_trained_skills(self.model.skill_dictionary_settings["Appraise"], class_name):
            if self.model.appraise_rank >= 1:
                self.model.appraise_misc_mod = 3
            else:
                self.model.appraise_misc_mod = 0
        if check_trained_skills(self.model.skill_dictionary_settings["Bluff"], class_name):
            if self.model.bluff_rank >= 1:
                self.model.bluff_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Climb"], class_name):
            if self.model.climb_rank >= 1:
                self.model.climb_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Craft"], class_name):
            if self.model.craft_rank >= 1:
                self.model.craft_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Diplomacy"], class_name):
            if self.model.diplomacy_rank >= 1:
                self.model.diplomacy_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Disable Device"], class_name):
            if self.model.disable_device_rank >= 1:
                self.model.disable_device_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Disguise"], class_name):
            if self.model.disguise_rank >= 1:
                self.model.disguise_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Escape Artist"], class_name):
            if self.model.escape_artist_rank >= 1:
                self.model.escape_artist_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Fly"], class_name):
            if self.model.fly_rank >= 1:
                self.model.fly_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Handle Animal"], class_name):
            if self.model.handle_animal_rank >= 1:
                self.model.handle_animal_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Heal"], class_name):
            if self.model.heal_rank >= 1:
                self.model.heal_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Intimidate"], class_name):
            if self.model.intimidate_rank >= 1:
                self.model.intimidate_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (arcana)"], class_name):
            if self.model.knowledge_arcana_rank >= 1:
                self.model.knowledge_arcana_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (dungeoneering)"], class_name):
            if self.model.knowledge_dungeoneering_rank >= 1:
                self.model.knowledge_dungeoneering_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (engineering)"], class_name):
            if self.model.knowledge_engineering_rank >= 1:
                self.model.knowledge_engineering_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (geography)"], class_name):
            if self.model.knowledge_geography_rank >= 1:
                self.model.knowledge_geography_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (history)"], class_name):
            if self.model.knowledge_history_rank >= 1:
                self.model.knowledge_history_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (local)"], class_name):
            if self.model.knowledge_local_rank >= 1:
                self.model.knowledge_local_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (nature)"], class_name):
            if self.model.knowledge_nature_rank >= 1:
                self.model.knowledge_nature_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (nobility)"], class_name):
            if self.model.knowledge_nobility_rank >= 1:
                self.model.knowledge_nobility_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (planes)"], class_name):
            if self.model.knowledge_planes_rank >= 1:
                self.model.knowledge_planes_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Knowledge (religion)"], class_name):
            if self.model.knowledge_religion_rank >= 1:
                self.model.knowledge_religion_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Linguistics"], class_name):
            if self.model.linguistics_rank >= 1:
                self.model.linguistics_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Perception"], class_name):
            if self.model.perception_rank >= 1:
                self.model.perception_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Perform"], class_name):
            if self.model.perform_rank >= 1:
                self.model.perform_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Profession"], class_name):
            if self.model.profession_rank >= 1:
                self.model.profession_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Ride"], class_name):
            if self.model.ride_rank >= 1:
                self.model.ride_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Sense Motive"], class_name):
            if self.model.sense_motive_rank >= 1:
                self.model.sense_motive_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Sleight of Hand"], class_name):
            if self.model.sleight_of_hand_rank >= 1:
                self.model.sleight_of_hand_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Spellcraft"], class_name):
            if self.model.spellcraft_rank >= 1:
                self.model.spellcraft_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Stealth"], class_name):
            if self.model.stealth_rank >= 1:
                self.model.stealth_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Survival"], class_name):
            if self.model.survival_rank >= 1:
                self.model.survival_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Swim"], class_name):
            if self.model.swim_rank >= 1:
                self.model.swim_misc_mod = 3
        if check_trained_skills(self.model.skill_dictionary_settings["Use Magic Device"], class_name):
            if self.model.use_magic_device_rank >= 1:
                self.model.use_magic_device_misc_mod = 3
        self.calculate_skill()
        return self.model

    def reset_all_misc_mod_skills(self):
        self.model.acrobatics_misc_mod = 0
        self.model.appraise_misc_mod = 0
        self.model.bluff_misc_mod = 0
        self.model.climb_misc_mod = 0
        self.model.craft_misc_mod = 0
        self.model.diplomacy_misc_mod = 0
        self.model.disable_device_misc_mod = 0
        self.model.disguise_misc_mod = 0
        self.model.escape_artist_misc_mod = 0
        self.model.fly_misc_mod = 0
        self.model.handle_animal_misc_mod = 0
        self.model.heal_misc_mod = 0
        self.model.intimidate_misc_mod = 0
        self.model.knowledge_arcana_misc_mod = 0
        self.model.knowledge_dungeoneering_misc_mod = 0
        self.model.knowledge_engineering_misc_mod = 0
        self.model.knowledge_geography_misc_mod = 0
        self.model.knowledge_history_misc_mod = 0
        self.model.knowledge_local_misc_mod = 0
        self.model.knowledge_nature_misc_mod = 0
        self.model.knowledge_nobility_misc_mod = 0
        self.model.knowledge_planes_misc_mod = 0
        self.model.knowledge_religion_misc_mod = 0
        self.model.linguistics_misc_mod = 0
        self.model.perception_misc_mod = 0
        self.model.perform_misc_mod = 0
        self.model.profession_misc_mod = 0
        self.model.ride_misc_mod = 0
        self.model.sense_motive_misc_mod = 0
        self.model.sleight_of_hand_misc_mod = 0
        self.model.spellcraft_misc_mod = 0
        self.model.stealth_misc_mod = 0
        self.model.survival_misc_mod = 0
        self.model.swim_misc_mod = 0
        self.model.use_magic_device_misc_mod = 0

    def reset_all_spells(self):
        self.model.spells_known_0 = 0
        self.model.spell_save_dc_0 = 0
        self.model.spells_per_day_0 = 0
        self.model.spells_known_1 = 0
        self.model.spell_save_dc_1 = 0
        self.model.spells_per_day_1 = 0
        self.model.spell_bonus_1 = 0
        self.model.spells_known_2 = 0
        self.model.spell_save_dc_2 = 0
        self.model.spells_per_day_2 = 0
        self.model.spell_bonus_2 = 0
        self.model.spells_known_3 = 0
        self.model.spell_save_dc_3 = 0
        self.model.spells_per_day_3 = 0
        self.model.spell_bonus_3 = 0
        self.model.spells_known_4 = 0
        self.model.spell_save_dc_4 = 0
        self.model.spells_per_day_4 = 0
        self.model.spell_bonus_4 = 0
        self.model.spells_known_5 = 0
        self.model.spell_save_dc_5 = 0
        self.model.spells_per_day_5 = 0
        self.model.spell_bonus_5 = 0
        self.model.spells_known_6 = 0
        self.model.spell_save_dc_6 = 0
        self.model.spells_per_day_6 = 0
        self.model.spell_bonus_6 = 0
        self.model.spells_known_7 = 0
        self.model.spell_save_dc_7 = 0
        self.model.spells_per_day_7 = 0
        self.model.spell_bonus_7 = 0
        self.model.spells_known_8 = 0
        self.model.spell_save_dc_8 = 0
        self.model.spells_per_day_8 = 0
        self.model.spell_bonus_8 = 0
        self.model.spells_known_9 = 0
        self.model.spell_save_dc_9 = 0
        self.model.spells_per_day_9 = 0
        self.model.spell_bonus_9 = 0

    def enable_all_spell_buttons(self):
        self.view.spell_0_button.configure(state="normal")
        self.view.spell_1_button.configure(state="normal")
        self.view.spell_2_button.configure(state="normal")
        self.view.spell_3_button.configure(state="normal")
        self.view.spell_4_button.configure(state="normal")
        self.view.spell_5_button.configure(state="normal")
        self.view.spell_6_button.configure(state="normal")
        self.view.spell_7_button.configure(state="normal")
        self.view.spell_8_button.configure(state="normal")
        self.view.spell_9_button.configure(state="normal")

    def disable_all_spell_buttons(self):
        self.view.spell_0_button.configure(state="disabled")
        self.view.spell_1_button.configure(state="disabled")
        self.view.spell_2_button.configure(state="disabled")
        self.view.spell_3_button.configure(state="disabled")
        self.view.spell_4_button.configure(state="disabled")
        self.view.spell_5_button.configure(state="disabled")
        self.view.spell_6_button.configure(state="disabled")
        self.view.spell_7_button.configure(state="disabled")
        self.view.spell_8_button.configure(state="disabled")
        self.view.spell_9_button.configure(state="disabled")
