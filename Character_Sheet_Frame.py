import customtkinter
from Deity import Deity
from MySQL_Service import MySQL_Service
from Races import Races
from Skills import Skills
import os
from Ability_Scores import Ability_Scores
from Saving_Throws import Saving_Throws
from Skill_Widgets import Skill_Widgets
from Observer import STRObserver, DEXObserver, CONObserver, INTObserver, WISObserver, CHAObserver, ConcreteSubject

class Character_Sheet_Frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller, config):
        customtkinter.CTkFrame.__init__(self, parent)
        self.config = config
        self.class_list = []
        self.race_list = []
        self.deity_list = []
        self.alignment_list = []
        self.skill_dict = {}
        self.lvl_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        abilities_list = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        str_based_list = []
        dex_based_list = []
        con_based_list = []
        int_based_list = []
        wis_based_list = []
        cha_based_list = []

        self.load_classes_from_folder()
        self.load_lists_from_db()

        # load and create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, width=720, height=680)
        self.ability_score_frame = customtkinter.CTkScrollableFrame(self.scrollable_frame, label_text="Ability Scores", label_anchor="center", width=320)
        self.saving_throw_frame = customtkinter.CTkFrame(self.scrollable_frame, width=320)
        self.skills_frame = customtkinter.CTkScrollableFrame(self.scrollable_frame, width=320, height=320, label_text="Skills", label_anchor="center")
        self.martial_frame = customtkinter.CTkFrame(self.scrollable_frame, width=720)
        self.scrollable_frame.grid_rowconfigure(3, minsize=30)

        # General widgets
        self.character_name = customtkinter.CTkEntry(self.scrollable_frame, width=150, placeholder_text="Character Name", text_color=config["COLORS"]["TEXT"])
        self.character_alignment = customtkinter.CTkComboBox(self.scrollable_frame, width=150, text_color=config["COLORS"]["TEXT"], values=self.alignment_list)
        self.character_player = customtkinter.CTkEntry(self.scrollable_frame, width=150, placeholder_text="Player Name", text_color=config["COLORS"]["TEXT"])
        self.character_gender = customtkinter.CTkComboBox(self.scrollable_frame, width=150, text_color=config["COLORS"]["TEXT"], values=["Male \u2642", "Female \u2640"])
        self.character_age = customtkinter.CTkEntry(self.scrollable_frame, width=40, placeholder_text="Age", text_color=config["COLORS"]["TEXT"])
        self.character_class = customtkinter.CTkComboBox(self.scrollable_frame, width=150, text_color=config["COLORS"]["TEXT"], values=self.class_list)
        self.character_lvl = customtkinter.CTkComboBox(self.scrollable_frame, width=70, text_color=config["COLORS"]["TEXT"], values=self.lvl_list)
        self.character_deity = customtkinter.CTkComboBox(self.scrollable_frame, width=150, text_color=config["COLORS"]["TEXT"], values=self.deity_list)
        self.character_homeland = customtkinter.CTkEntry(self.scrollable_frame, width=150, placeholder_text="Homeland", text_color=config["COLORS"]["TEXT"])
        self.character_size = customtkinter.CTkLabel(self.scrollable_frame, width=150, text="Size", text_color=config["COLORS"]["TEXT"], state="disabled")
        self.character_race = customtkinter.CTkComboBox(self.scrollable_frame, width=150, text_color=config["COLORS"]["TEXT"], values=self.race_list)

        # Abilities widgets
        abilities = {}
        for row, ability_name in enumerate(abilities_list):
            ability = Ability_Scores(ability_name, row, self.ability_score_frame)
            abilities[ability_name] = ability

        # Saving Throw widgets
        fortitude_save = Saving_Throws("Fortitude", 0, self.saving_throw_frame, int(abilities['CON'].bonus_modifier.get()))
        con_based_list.append(fortitude_save)

        reflex_save = Saving_Throws("Reflex", 1, self.saving_throw_frame, int(abilities['DEX'].bonus_modifier.get()))
        dex_based_list.append(reflex_save)

        will_save = Saving_Throws("Will", 2, self.saving_throw_frame, int(abilities['WIS'].bonus_modifier.get()))
        wis_based_list.append(will_save)

        # Skills widgets
        skills = {}
        for row, (skill_name, key_ability) in enumerate(self.skill_dict.items()):
            skill = Skill_Widgets(skill_name, row, self.skills_frame)
            skills[skill_name] = skill
            if key_ability == "str":
                str_based_list.append(skill)
            elif key_ability == "dex":
                dex_based_list.append(skill)
            elif key_ability == "con":
                con_based_list.append(skill)
            elif key_ability == "int":
                int_based_list.append(skill)
            elif key_ability == "wis":
                wis_based_list.append(skill)
            else:
                cha_based_list.append(skill)

        # Observers
        str_subject = ConcreteSubject()
        str_observer = STRObserver(str_based_list)
        str_subject.attach(str_observer)
        abilities['STR'].add_subject(str_subject)

        dex_subject = ConcreteSubject()
        dex_observer = DEXObserver(dex_based_list)
        dex_subject.attach(dex_observer)
        abilities['DEX'].add_subject(dex_subject)

        con_subject = ConcreteSubject()
        con_observer = CONObserver(con_based_list)
        con_subject.attach(con_observer)
        abilities['CON'].add_subject(con_subject)

        int_subject = ConcreteSubject()
        int_observer = INTObserver(int_based_list)
        int_subject.attach(int_observer)
        abilities['INT'].add_subject(int_subject)

        wis_subject = ConcreteSubject()
        wis_observer = WISObserver(wis_based_list)
        wis_subject.attach(wis_observer)
        abilities['WIS'].add_subject(wis_subject)

        cha_subject = ConcreteSubject()
        cha_observer = CHAObserver(cha_based_list)
        cha_subject.attach(cha_observer)
        abilities['CHA'].add_subject(cha_subject)

        # Martial Widgets
        self.character_hp = customtkinter.CTkEntry(self.martial_frame, width=40, text_color=config["COLORS"]["TEXT"], placeholder_text="HP")
        self.character_dr = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_bab = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_spell_resist = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])

        self.base_speed = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.speed_with_armor = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.fly_speed = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.swim_speed = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.climb_speed = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.burrow_speed = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])

        self.initiative_total = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.initiative_ab_mod = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.initiative_misc_mod = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])

        self.character_ac_total = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_ac_armor = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_ac_shield = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_ac_mod = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_ac_size = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_ac_natural = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_ac_deflect = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_ac_misc = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])

        self.character_touch_ac = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_flat_ac = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])

        self.character_cmb_total = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_cmb_bab = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_cmb_str = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_cmb_size = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])

        self.character_cmd_total = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_cmd_bab = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_cmd_str = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_cmd_dex = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])
        self.character_cmd_size = customtkinter.CTkLabel(self.martial_frame, width=30, text_color=config["COLORS"]["TEXT"])

        self.grid_widgets()

    def grid_widgets(self):
        self.scrollable_frame.place(x=5, y=5)
        self.character_name.grid(row=0, column=0, padx=5, pady=5)
        self.character_alignment.grid(row=0, column=1, padx=5, pady=5)
        self.character_player.grid(row=0, column=2, padx=5, pady=5)
        self.character_gender.grid(row=0, column=3, padx=5, pady=5)
        self.character_class.grid(row=1, column=0, padx=5, pady=5)
        self.character_lvl.grid(row=1, column=1, padx=5, pady=5)
        self.character_deity.grid(row=1, column=2, padx=5, pady=5)
        self.character_homeland.grid(row=1, column=3, padx=5, pady=5)
        self.character_race.grid(row=2, column=0, padx=5, pady=5)
        self.character_size.grid(row=2, column=1, padx=5, pady=5)
        self.character_age.grid(row=2, column=2, padx=5, pady=5)

        self.ability_score_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.skills_frame.grid(row=4, column=2, columnspan=2, rowspan=2, padx=10, pady=10, sticky="w")
        self.saving_throw_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.martial_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.character_hp.grid(row=0, column=0, padx=10, pady=10)

    def load_classes_from_folder(self):
        classes_folder_path = 'Classes'
        if os.path.exists(classes_folder_path) and os.path.isdir(classes_folder_path):
            class_files = [f for f in os.listdir(classes_folder_path) if
                           os.path.isfile(os.path.join(classes_folder_path, f))]
            self.class_list.extend([os.path.splitext(f)[0] for f in class_files])

    def load_lists_from_db(self):
        data_container = MySQL_Service('Deity')
        deity = data_container.load_data(Deity.Deity)
        self.deity_list = [deity.name for deity in deity]
        self.alignment_list = [deity.alignment for deity in deity]
        self.alignment_list = list(dict.fromkeys(self.alignment_list))

        data_container = MySQL_Service('Races')
        races_name = data_container.load_data(Races.Races)
        self.race_list = [races_name.name for races_name in races_name]

        data_container = MySQL_Service('Skill')
        skill = data_container.load_data(Skills.Skills)
        self.skill_dict = {skill.name: skill.key_ability for skill in skill}
