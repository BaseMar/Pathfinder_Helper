import customtkinter
from CTkListbox import CTkListbox


def validate_entry(text):
    return text.isalpha() or text == ""


class MonsterView(customtkinter.CTkFrame):
    def __init__(self, parent, config):
        self.controller = None
        self.config = config

        super().__init__(parent)
        self.monster_list_box = CTkListbox(self, border_color=config["COLORS"]["BUTTON"], border_width=1, width=300, height=615, hover_color=config["COLORS"]["HOVER"], text_color=config["COLORS"]["TEXT"], multiple_selection=False, command=self.show_monster_data)

        # TabView
        self.tabview = customtkinter.CTkTabview(self, width=650, height=670, border_width=1, border_color=config["COLORS"]["BUTTON"])
        self.tabview.grid_propagate(False)
        self.tabview.add("Summary")
        self.tabview.add("Abilities")
        self.tabview.add("Martial")
        self.tabview.add("Spells")
        self.tabview.tab("Summary").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Summary").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Summary").grid_columnconfigure(2, weight=1)
        self.tabview.tab("Summary").grid_rowconfigure(2, minsize=30)
        self.tabview.tab("Summary").grid_rowconfigure(6, minsize=30)
        self.tabview.tab("Summary").grid_rowconfigure(8, minsize=30)

        self.tabview.tab("Abilities").grid_rowconfigure(1, minsize=30)
        self.tabview.tab("Abilities").grid_rowconfigure(3, minsize=30)
        self.tabview.tab("Abilities").grid_rowconfigure(5, minsize=30)
        self.tabview.tab("Abilities").grid_rowconfigure(7, minsize=30)

        self.tabview.tab("Martial").grid_rowconfigure(4, minsize=30)
        self.tabview.tab("Martial").grid_rowconfigure(8, minsize=30)

        self.tabview.tab("Spells").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Spells").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Spells").grid_rowconfigure(1, minsize=50)

        # 1 - Summary
        self.monster_name_var = customtkinter.StringVar()
        self.monster_name = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_name_var, font=("Impact", 25), text_color=config["COLORS"]["TEXT"])
        self.monster_cr_var = customtkinter.StringVar()
        self.monster_cr = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_cr_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_xp_var = customtkinter.StringVar()
        self.monster_xp = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_xp_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_type_var = customtkinter.StringVar()
        self.monster_type = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_type_var, font=("Impact", 20), text_color=config["COLORS"]["TEXT"])
        self.monster_ability_scores_var = customtkinter.StringVar()
        self.monster_ability_scores = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_ability_scores_var, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_ability_scores_label = customtkinter.CTkLabel(self.tabview.tab("Summary"), text="Ability Score: ", font=("Courier", 13, "bold"), text_color=config["COLORS"]["TEXT"])
        self.monster_skills_var = customtkinter.StringVar()
        self.monster_skills = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_skills_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_feats_var = customtkinter.StringVar()
        self.monster_feats = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_feats_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_languages_var = customtkinter.StringVar()
        self.monster_languages = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_languages_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_environment_var = customtkinter.StringVar()
        self.monster_environment = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_environment_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_organization_var = customtkinter.StringVar()
        self.monster_organization = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_organization_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_treasure_var = customtkinter.StringVar()
        self.monster_treasure = customtkinter.CTkLabel(self.tabview.tab("Summary"), textvariable=self.monster_treasure_var, font=("Courier", 13), wraplength=630, text_color=config["COLORS"]["TEXT"], justify="left")

        # 2 - Abilities
        self.monster_senses_var = customtkinter.StringVar()
        self.monster_senses = customtkinter.CTkLabel(self.tabview.tab("Abilities"), font=("Courier", 13), wraplength=630, textvariable=self.monster_senses_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_aura_var = customtkinter.StringVar()
        self.monster_aura = customtkinter.CTkLabel(self.tabview.tab("Abilities"), textvariable=self.monster_aura_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_defensive_abilities_var = customtkinter.StringVar()
        self.monster_defensive_abilities = customtkinter.CTkLabel(self.tabview.tab("Abilities"), wraplength=630, textvariable=self.monster_defensive_abilities_var, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_sq_var = customtkinter.StringVar()
        self.monster_sq = customtkinter.CTkLabel(self.tabview.tab("Abilities"), textvariable=self.monster_sq_var, wraplength=630, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")
        self.tabview_scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("Abilities"), width=600, height=240, label_text="Special Abilities", label_anchor="center")
        self.monster_special_abilities_var = customtkinter.StringVar()
        self.monster_special_abilities = customtkinter.CTkLabel(self.tabview_scrollable_frame, textvariable=self.monster_special_abilities_var, wraplength=600, font=("Courier", 13), text_color=config["COLORS"]["TEXT"], justify="left")

        # 3 - Martial
        self.monster_init_var = customtkinter.StringVar()
        self.monster_init = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_init_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_ac_var = customtkinter.StringVar()
        self.monster_ac = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_ac_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_hp_var = customtkinter.StringVar()
        self.monster_hp = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_hp_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_saves_var = customtkinter.StringVar()
        self.monster_saves = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_saves_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_resistances_var = customtkinter.StringVar()
        self.monster_resistances = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_resistances_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_special_attacks_var = customtkinter.StringVar()
        self.monster_special_attacks = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_special_attacks_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_bab_var = customtkinter.StringVar()
        self.monster_bab = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_bab_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_space_reach_var = customtkinter.StringVar()
        self.monster_space_reach = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_space_reach_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_melee_var = customtkinter.StringVar()
        self.monster_melee = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_melee_var, text_color=config["COLORS"]["TEXT"], justify="left")
        self.monster_ranged_var = customtkinter.StringVar()
        self.monster_ranged = customtkinter.CTkLabel(self.tabview.tab("Martial"), font=("Courier", 13), wraplength=630, textvariable=self.monster_ranged_var, text_color=config["COLORS"]["TEXT"], justify="left")

        # 4 - Spells
        self.tabview_scrollable_frame3 = customtkinter.CTkScrollableFrame(self.tabview.tab("Spells"), height=250, label_text="Spell-Like Abilities", label_anchor="center")
        self.monster_spell_like_abilities_var = customtkinter.StringVar()
        self.monster_spell_like_abilities = customtkinter.CTkLabel(self.tabview_scrollable_frame3, wraplength=300, font=("Courier", 13), justify="left", textvariable=self.monster_spell_like_abilities_var, text_color=config["COLORS"]["TEXT"])
        self.tabview_scrollable_frame4 = customtkinter.CTkScrollableFrame(self.tabview.tab("Spells"), height=250, label_text="Spell Known", label_anchor="center")
        self.monster_spells_known_var = customtkinter.StringVar()
        self.monster_spells_known = customtkinter.CTkLabel(self.tabview_scrollable_frame4, wraplength=300, font=("Courier", 13), justify="left", textvariable=self.monster_spells_known_var, text_color=config["COLORS"]["TEXT"])
        self.tabview_scrollable_frame5 = customtkinter.CTkScrollableFrame(self.tabview.tab("Spells"), label_text="Spell Prepared", label_anchor="center")
        self.monster_spells_prepared_var = customtkinter.StringVar()
        self.monster_spells_prepared = customtkinter.CTkLabel(self.tabview_scrollable_frame5, wraplength=600, font=("Courier", 13), justify="left", textvariable=self.monster_spells_prepared_var, text_color=config["COLORS"]["TEXT"])

        self.monster_cr_combobox_var = customtkinter.StringVar()
        self.monster_cr_combobox = customtkinter.CTkComboBox(self, variable=self.monster_cr_combobox_var, width=100)
        self.monster_entry_filter = customtkinter.CTkEntry(self, width=200, placeholder_text="Filtering by name")

        self.grid_widgets()

        self.monster_cr_combobox_var.trace_add("write", self.update_listbox)
        self.monster_entry_filter.bind("<KeyRelease>", self.update_listbox)
        self.monster_entry_filter.configure(validate="key", validatecommand=(self.register(validate_entry), "%P"))

    def set_controller(self, controller):
        self.controller = controller

    def grid_widgets(self):
        self.monster_list_box.place(x=10, y=50)
        self.tabview.place(x=355, y=10)
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

    def init_data(self):
        model = self.controller.load_data()
        self.pull_data(model)

    def pull_data(self, model):
        self.monster_cr_combobox.configure(values=model.monster_cr_list)
        self.monster_cr_combobox_var.set(value=model.monster_cr_list[0])
        self.controller.update_listbox()

    def update_listbox(self, *args):
        self.controller.update_listbox()

    def show_monster_data(self, choice):
        self.controller.show_monster_data(choice)
