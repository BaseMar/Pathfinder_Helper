import customtkinter
from Monster import Monster
import csv
from TabView import MyTabView
from CTkListbox import *
import re

class Monster_Frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller, config):
        customtkinter.CTkFrame.__init__(self, parent)
        self.monster_list = {}
        self.monster_cr_list = []

        self.load_data()

        # Monster list box
        self.monster_list_box = CTkListbox(self, border_color=config["COLORS"]["BUTTON"],
                                           border_width=1,
                                           width=300,
                                           height=615,
                                           hover_color=config["COLORS"]["HOVER"],
                                           text_color=config["COLORS"]["TEXT"],
                                           multiple_selection=False,
                                           command=self.show_monster_data)

        # TabView
        self.tab_view = MyTabView(self, width=650, height=670, border_width=1, border_color=config["COLORS"]["BUTTON"])
        self.tab_view.tab("Summary").grid_columnconfigure(0, weight=1)
        self.tab_view.tab("Summary").grid_columnconfigure(1, weight=1)
        self.tab_view.tab("Summary").grid_columnconfigure(2, weight=1)
        self.tab_view.tab("Summary").grid_rowconfigure(2, minsize=30)
        self.tab_view.tab("Summary").grid_rowconfigure(6, minsize=30)
        self.tab_view.tab("Summary").grid_rowconfigure(8, minsize=30)

        self.tab_view.tab("Abilities").grid_rowconfigure(1, minsize=30)
        self.tab_view.tab("Abilities").grid_rowconfigure(3, minsize=30)
        self.tab_view.tab("Abilities").grid_rowconfigure(5, minsize=30)
        self.tab_view.tab("Abilities").grid_rowconfigure(7, minsize=30)

        self.tab_view.tab("Martial").grid_rowconfigure(4, minsize=30)
        self.tab_view.tab("Martial").grid_rowconfigure(8, minsize=30)

        self.tab_view.tab("Spells").grid_columnconfigure(0, weight=1)
        self.tab_view.tab("Spells").grid_columnconfigure(1, weight=1)
        self.tab_view.tab("Spells").grid_rowconfigure(1, minsize=50)

        # 1 - Summary
        self.monster_name_var = customtkinter.StringVar()
        self.monster_name = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_name_var, font=("Impact", 25), text_color=config["COLORS"]["TEXT"])
        self.monster_cr_var = customtkinter.StringVar()
        self.monster_cr = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_cr_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_xp_var = customtkinter.StringVar()
        self.monster_xp = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_xp_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_type_var = customtkinter.StringVar()
        self.monster_type = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_type_var, font=("Impact", 20), text_color=config["COLORS"]["TEXT"])
        self.monster_ability_scores_var = customtkinter.StringVar()
        self.monster_ability_scores = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_ability_scores_var, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_ability_scores_label = customtkinter.CTkLabel(self.tab_view.tab("Summary"), text="Ability Score: ", font=("Courier", 13, "bold"), text_color=config["COLORS"]["TEXT"])
        self.monster_skills_var = customtkinter.StringVar()
        self.monster_skills = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_skills_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_feats_var = customtkinter.StringVar()
        self.monster_feats = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_feats_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_languages_var = customtkinter.StringVar()
        self.monster_languages = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_languages_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_environment_var = customtkinter.StringVar()
        self.monster_environment = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_environment_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_organization_var = customtkinter.StringVar()
        self.monster_organization = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_organization_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_treasure_var = customtkinter.StringVar()
        self.monster_treasure = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_treasure_var, font=("Courier", 13), wraplength=630, text_color=config["COLORS"]["TEXT"], justify="left")

        # 2 - Abilities
        self.monster_senses_var = customtkinter.StringVar()
        self.monster_senses = customtkinter.CTkLabel(self.tab_view.tab("Abilities"), font=("Courier", 13), wraplength=630, textvariable=self.monster_senses_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_aura_var = customtkinter.StringVar()
        self.monster_aura = customtkinter.CTkLabel(self.tab_view.tab("Abilities"), textvariable=self.monster_aura_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_defensive_abilities_var = customtkinter.StringVar()
        self.monster_defensive_abilities = customtkinter.CTkLabel(self.tab_view.tab("Abilities"), wraplength=630, textvariable=self.monster_defensive_abilities_var, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_sq_var = customtkinter.StringVar()
        self.monster_sq = customtkinter.CTkLabel(self.tab_view.tab("Abilities"), textvariable=self.monster_sq_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.tabview_scrollable_frame = customtkinter.CTkScrollableFrame(self.tab_view.tab("Abilities"), width=600, height=240, label_text="Special Abilities", label_anchor="center")
        self.monster_special_abilities_var = customtkinter.StringVar()
        self.monster_special_abilities = customtkinter.CTkLabel(self.tabview_scrollable_frame, textvariable=self.monster_special_abilities_var, wraplength=600, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")

        # 3 - Martial
        self.monster_init_var = customtkinter.StringVar()
        self.monster_init = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_init_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_ac_var = customtkinter.StringVar()
        self.monster_ac = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_ac_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_hp_var = customtkinter.StringVar()
        self.monster_hp = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_hp_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_saves_var = customtkinter.StringVar()
        self.monster_saves = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_saves_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_resistances_var = customtkinter.StringVar()
        self.monster_resistances = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_resistances_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_special_attacks_var = customtkinter.StringVar()
        self.monster_special_attacks = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_special_attacks_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_bab_var = customtkinter.StringVar()
        self.monster_bab = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_bab_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_space_reach_var = customtkinter.StringVar()
        self.monster_space_reach = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_space_reach_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_melee_var = customtkinter.StringVar()
        self.monster_melee = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_melee_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_ranged_var = customtkinter.StringVar()
        self.monster_ranged = customtkinter.CTkLabel(self.tab_view.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_ranged_var, text_color=config["COLORS"]["TEXT"], justify="left")

        # 4 - Spells
        self.tabview_scrollable_frame3 = customtkinter.CTkScrollableFrame(self.tab_view.tab("Spells"), height=250, label_text="Spell-Like Abilities", label_anchor="center")
        self.monster_spell_like_abilities_var = customtkinter.StringVar()
        self.monster_spell_like_abilities = customtkinter.CTkLabel(self.tabview_scrollable_frame3, wraplength=300, font=("Courier", 13), justify="left", textvariable=self.monster_spell_like_abilities_var, text_color=config["COLORS"]["TEXT"])
        self.tabview_scrollable_frame4 = customtkinter.CTkScrollableFrame(self.tab_view.tab("Spells"), height=250, label_text="Spell Known", label_anchor="center")
        self.monster_spells_known_var = customtkinter.StringVar()
        self.monster_spells_known = customtkinter.CTkLabel(self.tabview_scrollable_frame4, wraplength=300, font=("Courier", 13), justify="left", textvariable=self.monster_spells_known_var, text_color=config["COLORS"]["TEXT"])
        self.tabview_scrollable_frame5 = customtkinter.CTkScrollableFrame(self.tab_view.tab("Spells"), label_text="Spell Prepared", label_anchor="center")
        self.monster_spells_prepared_var = customtkinter.StringVar()
        self.monster_spells_prepared = customtkinter.CTkLabel(self.tabview_scrollable_frame5, wraplength=600, font=("Courier", 13), justify="left", textvariable=self.monster_spells_prepared_var, text_color=config["COLORS"]["TEXT"])

        # Filters widgets
        self.monster_cr_combobox_var = customtkinter.StringVar(value=self.monster_cr_list[0])
        self.monster_cr_combobox = customtkinter.CTkComboBox(self, values=self.monster_cr_list, variable=self.monster_cr_combobox_var, width=100)
        self.monster_entry_filter = customtkinter.CTkEntry(self, width=200, placeholder_text="Filtering by name")

        self.monster_entry_filter.bind("<KeyRelease>", self.update_listbox)
        self.monster_entry_filter.configure(validate="key", validatecommand=(self.register(self.validate_entry), "%P"))

        self.update_listbox()

        self.monster_cr_combobox_var.trace_add("write", self.update_listbox)

        # Place widget to Monster Frame
        self.setup_frame()

    def load_data(self):
        # Loading CSV DataBase
        with open("DataBase/monster_bestiary_full - Updated 27Jul2015.csv", 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            cr_set = set()
            for row in csv_reader:
                monster = Monster(row)
                try:
                    cr_float = float(monster.cr)
                    cr_set.add(cr_float)
                    self.monster_list[monster.name] = monster
                except ValueError:
                    pass
            self.monster_cr_list = sorted(cr_set)
            self.monster_cr_list = [str(int(cr) if cr.is_integer() else cr) for cr in self.monster_cr_list]

    def setup_frame(self):
        self.monster_list_box.place(x=10, y=50)
        self.tab_view.place(x=355, y=10)
        self.monster_cr_combobox.place(x=10, y=10)
        self.monster_entry_filter.place(x=130, y=10)

        self.monster_name.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.monster_type.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.monster_cr.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.monster_xp.grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.monster_ability_scores.grid(row=3, column=0, padx=10, pady=10, sticky="w", columnspan=3)
        self.monster_skills.grid(row=4, column=0, padx=10, pady=10, sticky="w", columnspan=3)
        self.monster_feats.grid(row=5, column=0, padx=10, pady=10, sticky="w", columnspan=3)
        self.monster_languages.grid(row=7, column=0, padx=10, pady=10, sticky="w", columnspan=3)
        self.monster_environment.grid(row=9, column=0, padx=10, pady=10, sticky="w", columnspan=3)
        self.monster_organization.grid(row=10, column=0, padx=10, pady=10, sticky="w", columnspan=3)
        self.monster_treasure.grid(row=11, column=0, padx=10, pady=10, sticky="w", columnspan=3)

        self.monster_senses.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.monster_aura.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.monster_defensive_abilities.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.monster_sq.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.tabview_scrollable_frame.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")
        self.monster_special_abilities.grid(row=0, column=0)

        self.monster_hp.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.monster_ac.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.monster_saves.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.monster_resistances.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.monster_init.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.monster_bab.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.monster_space_reach.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.monster_melee.grid(row=9, column=0, padx=10, pady=10, sticky="w")
        self.monster_ranged.grid(row=10, column=0, padx=10, pady=10, sticky="w")
        self.monster_special_attacks.grid(row=11, column=0, padx=10, pady=10, sticky="w")

        self.monster_spell_like_abilities.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.monster_spells_known.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.monster_spells_prepared.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.tabview_scrollable_frame3.grid(row=0, column=0, sticky="nsew")
        self.tabview_scrollable_frame4.grid(row=0, column=1, sticky="nsew")
        self.tabview_scrollable_frame5.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def show_monster_data(self, selected_option):
        selected_monster = self.monster_list[selected_option]
        self.monster_name_var.set(value=selected_monster.name)
        self.monster_type_var.set(value=f"{selected_monster.alignment} {selected_monster.size} {selected_monster.type} {selected_monster.subtype}")
        self.monster_cr_var.set(value=f"CR: {selected_monster.cr}")
        self.monster_xp_var.set(value=f"XP: {selected_monster.xp}")
        self.monster_ability_scores_var.set(value=f"Ability Scores: {selected_monster.ability_scores}")
        self.monster_skills_var.set(value=f"Skills: {selected_monster.skills}")
        self.monster_feats_var.set(value=f"Feats: {selected_monster.feats}")
        self.monster_languages_var.set(value=f"Languages: {selected_monster.languages}")
        self.monster_environment_var.set(value=f"Environment: {selected_monster.environment}")
        self.monster_organization_var.set(value=f"Organization: {selected_monster.organization}")
        self.monster_treasure_var.set(value=f"Treasure: {selected_monster.treasure}")

        self.monster_senses_var.set(value=f"Senses: {selected_monster.senses}")
        self.monster_aura_var.set(value=f"Aura: {selected_monster.aura}")
        self.monster_defensive_abilities_var.set(value=f"Defensive Abilities: {selected_monster.defensive_abilities}")
        self.monster_sq_var.set(value=f"Special Qualities: {selected_monster.sq}")
        self.monster_special_abilities_var.set(value=self.add_double_newline(selected_monster.special_abilities))

        self.monster_init_var.set(value=f"Initiative: {self.analyze_number(selected_monster.init)}, Speed: {selected_monster.speed}")
        self.monster_ac_var.set(value=f"AC: {selected_monster.ac} {selected_monster.ac_mods}")
        self.monster_hp_var.set(value=f"HP: {selected_monster.hp} {selected_monster.hd} {selected_monster.hp_mods}")
        self.monster_saves_var.set(value=f"Saves: {selected_monster.saves} {selected_monster.save_mods}")
        self.monster_resistances_var.set(value=f"DR:{selected_monster.dr}, Immune:{selected_monster.immune}, Resist:{selected_monster.resist}, SR:{selected_monster.sr}, Weakness:{selected_monster.weaknesses}")
        self.monster_bab_var.set(value=f"BaB: {self.analyze_number(selected_monster.base_atk)}, CMB: {selected_monster.cmb}, CMD: {selected_monster.cmd}")
        self.monster_space_reach_var.set(value=f"Space/Reach: {selected_monster.space}/{selected_monster.reach}")
        self.monster_melee_var.set(value=f"Melee: {selected_monster.melee}")
        self.monster_ranged_var.set(value=f"Ranged: {selected_monster.ranged}")
        self.monster_special_attacks_var.set(value=f"Special Attacks: {selected_monster.special_attacks}")

        self.monster_spell_like_abilities_var.set(value=selected_monster.spell_like_abilities)
        self.monster_spells_known_var.set(value=selected_monster.spells_known)
        self.monster_spells_prepared_var.set(value=selected_monster.spells_prepared)

    def update_listbox(self, *args):
        selected_cr = self.monster_cr_combobox_var.get()
        filter_text = self.monster_entry_filter.get().lower()

        try:
            self.monster_list_box.delete(0, "end")
        except IndexError:
            pass

        # Filter the monsters based on the selected criteria and filter text
        filtered_monsters = self.filter_monsters(selected_cr)
        filtered_monsters = [monster for monster in filtered_monsters if filter_text in monster.name.lower()]

        # Populate the listbox with the filtered monsters
        for monster in filtered_monsters:
            self.monster_list_box.insert("end", monster.name)

    def filter_monsters(self, cr):
        filtered_monsters = []
        for monster in self.monster_list.values():
            if str(monster.cr) == cr:
                filtered_monsters.append(monster)
        return filtered_monsters

    def add_double_newline(self, input_str):
        pattern = re.compile(r'([A-Z][a-zA-Z\s]+)\s+(\(Ex\)|\(Su\)|\(Sp\))')
        result = pattern.sub(r'\n\n\1\2\n\n', input_str)
        return result

    def analyze_number(self, input_value):
        try:
            number = int(input_value)
            if number > 0:
                result = f'+{number}'
                return result
            elif number < 0:
                result = f'-{abs(number)}'
                return result
            else:
                return '0'
        except ValueError:
            return None

    def validate_entry(self, text):
        return text.isalpha() or text == ""
