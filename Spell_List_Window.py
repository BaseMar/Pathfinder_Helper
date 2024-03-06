import customtkinter
from CTkListbox import *

class Spell_List_Window(customtkinter.CTkToplevel):
    def __init__(self, spell_lvl, config, selected_class, spell_list):
        self.config = config
        self.spell_lvl = spell_lvl
        self.selected_class = selected_class
        self.spell_list = spell_list
        super().__init__()
        self.grid_propagate(False)
        self.resizable(False, False)
        self.title(f"{selected_class} {spell_lvl} lvl spells")
        self.geometry("650x900")
        self.filtered_spells = []

        self.spell_name_var = customtkinter.StringVar()
        self.school_var = customtkinter.StringVar()
        self.casting_time_var = customtkinter.StringVar()
        self.components_var = customtkinter.StringVar()
        self.range_var = customtkinter.StringVar()
        self.effect_var = customtkinter.StringVar()
        self.target_var = customtkinter.StringVar()
        self.area_var = customtkinter.StringVar()
        self.duration_var = customtkinter.StringVar()
        self.saving_throw_var = customtkinter.StringVar()
        self.spell_resistance_var = customtkinter.StringVar()
        self.description_text_var = customtkinter.StringVar()

        self.spell_name = customtkinter.CTkLabel(self, textvariable=self.spell_name_var, font=("Impact", 25), text_color=config["COLORS"]["TEXT"], justify="center")
        self.school = customtkinter.CTkLabel(self, textvariable=self.school_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.casting_time = customtkinter.CTkLabel(self, textvariable=self.casting_time_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.components = customtkinter.CTkLabel(self, textvariable=self.components_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.range = customtkinter.CTkLabel(self, textvariable=self.range_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.effect = customtkinter.CTkLabel(self, textvariable=self.effect_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.target = customtkinter.CTkLabel(self, textvariable=self.target_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.area = customtkinter.CTkLabel(self, textvariable=self.area_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.duration = customtkinter.CTkLabel(self, textvariable=self.duration_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.saving_throw = customtkinter.CTkLabel(self, textvariable=self.saving_throw_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.spell_resistance = customtkinter.CTkLabel(self, textvariable=self.spell_resistance_var, font=("Courier", 15), text_color=config["COLORS"]["TEXT"], justify="left", wraplength=400)
        self.description = customtkinter.CTkScrollableFrame(self, width=600, height=250, border_width=1, border_color=config["COLORS"]["BUTTON"], label_text="Description", label_text_color=config["COLORS"]["TEXT"])
        self.description_text = customtkinter.CTkLabel(self.description, wraplength=590, font=("Courier", 13), justify="left", textvariable=self.description_text_var, text_color=config["COLORS"]["TEXT"])
        self.spell_listbox = CTkListbox(self, border_width=1, border_color=config["COLORS"]["BUTTON"], text_color=config["COLORS"]["TEXT"], hover_color=config["COLORS"]["HOVER"], command=self.show_spell_data, height=400)
        self.show_grid()
        self.show_spells(spell_lvl, selected_class, spell_list)

    def show_grid(self):
        self.spell_name.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.school.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.casting_time.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.components.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.range.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.effect.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.target.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.area.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.duration.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        self.saving_throw.grid(row=9, column=0, padx=10, pady=10, sticky='w')
        self.spell_resistance.grid(row=10, column=0, padx=10, pady=10, sticky='w')
        self.description.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky='w')
        self.description_text.grid(row=0, column=0, padx=10, pady=10)
        self.spell_listbox.grid(row=1, column=1, columnspan=2, rowspan=10, padx=10, pady=10, sticky='w')

    def show_spells(self, spell_lvl, selected_class, spell_list):
        try:
            self.spell_listbox.delete(0, "end")
        except:
            pass

        class_map = {
            "Bard": "bard",
            "Cleric": "cleric",
            "Druid": "druid",
            "Paladin": "paladin",
            "Ranger": "ranger",
            "Sorcerer/Wizard": "sorc_wiz"
        }

        class_attribute = class_map.get(selected_class, "sorc_wiz")

        for spell in spell_list:
            if getattr(spell, class_attribute) == spell_lvl:
                self.filtered_spells.append(spell)

        for spell in self.filtered_spells:
            self.spell_listbox.insert("end", spell.name)

    def show_spell_data(self, choice):
        for index, spell in enumerate(self.spell_list):
            if spell.name == choice:
                selected_spell_index = index
                break
        selected_spell = self.spell_list[selected_spell_index]

        self.spell_name_var.set(value=selected_spell.name)
        self.school_var.set(value=f"School: {selected_spell.school}")
        self.casting_time_var.set(value=f"Casting Time: {selected_spell.casting_time}")
        self.components_var.set(value=f"Components: {selected_spell.components}")
        self.range_var.set(value=f"Range: {selected_spell.range}")
        self.effect_var.set(value=f"Effect: {selected_spell.effect}")
        self.target_var.set(value=f"Target: {selected_spell.target}")
        self.area_var.set(value=f"Area: {selected_spell.area}")
        self.duration_var.set(value=f"Duration: {selected_spell.duration}")
        self.saving_throw_var.set(value=f"Saving Throw: {selected_spell.saving_throw}")
        self.spell_resistance_var.set(value=f"Spell Resistance: {selected_spell.spell_resistance}")
        self.description_text_var.set(value=selected_spell.description)
