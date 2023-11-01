import customtkinter
from Monster import Monster
import csv
from TabView import MyTabView
from CTkListbox import *


class Monster_Frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller, config):
        customtkinter.CTkFrame.__init__(self, parent)
        self.monster_list = {}
        self.monster_cr_list = []
        self.monster_environment_list = []

        # Configure geometry of a Frame 4x2
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.load_data()

        # Monster list box
        self.monster_list_box = CTkListbox(self, border_color=config["COLORS"]["BUTTON"],
                                           border_width=1,
                                           width=280,
                                           hover_color=config["COLORS"]["HOVER"],
                                           text_color=config["COLORS"]["TEXT"],
                                           multiple_selection=False,
                                           command=self.show_monster_data)

        # TabView
        self.tab_view = MyTabView(self, width=550)
        self.tab_view.tab("Summary").grid_columnconfigure((0, 1, 2), weight=1)
        self.tab_view.tab("Summary").grid_rowconfigure(2, weight=0)

        # Filters widgets
        self.monster_cr_combobox_var = customtkinter.StringVar(value=self.monster_cr_list[0])
        self.monster_cr_combobox = customtkinter.CTkComboBox(self, values=self.monster_cr_list, variable=self.monster_cr_combobox_var, width=20)

        self.update_listbox()

        self.monster_cr_combobox_var.trace_add("write", self.update_listbox)

        # Place widget to Monster Frame
        self.setup_frame()

        # Implement widgets to TabView - Summary
        # Information of a monster
        self.monster_name_var = customtkinter.StringVar(value="Monster Name: ")
        self.monster_name = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_name_var, font=("Arial", 20), text_color=config["COLORS"]["TEXT"])
        self.monster_cr_var = customtkinter.StringVar(value="CR: ")
        self.monster_cr = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_cr_var, font=("Arial", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_exp_var = customtkinter.StringVar(value="EXP: ")
        self.monster_exp = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_exp_var, font=("Arial", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_alignment_var = customtkinter.StringVar(value="Alignment: ")
        self.monster_alignment = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_alignment_var, font=("Arial", 15), text_color=config["COLORS"]["TEXT"])

        # Abilities of a monster
        self.monster_abilities_holder = customtkinter.CTkFrame(self.tab_view.tab("Summary"), width=70, height=300)
        self.monster_str_var = customtkinter.StringVar(value="Strength")
        self.monster_str = customtkinter.CTkLabel(self.monster_abilities_holder, textvariable=self.monster_str_var, text_color=config["COLORS"]["TEXT"])
        self.monster_dex_var = customtkinter.StringVar(value="Dexterity")
        self.monster_dex = customtkinter.CTkLabel(self.monster_abilities_holder, textvariable=self.monster_dex_var, text_color=config["COLORS"]["TEXT"])
        self.monster_con_var = customtkinter.StringVar(value="Condition")
        self.monster_con = customtkinter.CTkLabel(self.monster_abilities_holder, textvariable=self.monster_con_var, text_color=config["COLORS"]["TEXT"])
        self.monster_int_var = customtkinter.StringVar(value="Intelligence")
        self.monster_int = customtkinter.CTkLabel(self.monster_abilities_holder, textvariable=self.monster_int_var, text_color=config["COLORS"]["TEXT"])
        self.monster_wis_var = customtkinter.StringVar(value="Wisdom")
        self.monster_wis = customtkinter.CTkLabel(self.monster_abilities_holder, textvariable=self.monster_wis_var, text_color=config["COLORS"]["TEXT"])
        self.monster_cha_var = customtkinter.StringVar(value="Charisma")
        self.monster_cha = customtkinter.CTkLabel(self.monster_abilities_holder, textvariable=self.monster_cha_var, text_color=config["COLORS"]["TEXT"])

        # Monster Skills
        self.monster_skills_holder = customtkinter.CTkScrollableFrame(self.tab_view.tab("Summary"), width=70, height=300)

        self.setup_summary_view()

        # Place widgets to TabView - Abilities
        # Place widgets to TabView - Martial
        # Place widgets to TabView - Spells

    def load_data(self):
        # Loading CSV DataBase
        with open("DataBase/MonsterList.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            cr_set = set()

            for row in csv_reader:
                monster = Monster(row)

                # Add data to sets to eliminate duplicates
                cr_set.add(float(monster.cr))
                self.monster_list[monster.name] = monster

            # Convert sets back to lists
            self.monster_cr_list = sorted(cr_set)
            self.monster_cr_list = [str(int(cr) if cr.is_integer() else cr) for cr in self.monster_cr_list]

    def setup_frame(self):
        self.monster_list_box.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.tab_view.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)
        self.monster_cr_combobox.grid(row=0, column=0, sticky="ew", padx=10)

    def show_monster_data(self, selected_option):
        selected_monster = self.monster_list[selected_option]
        self.monster_name_var.set(f"{selected_monster.name} ({selected_monster.size} {selected_monster.type})")
        self.monster_exp_var.set(f"EXP: {selected_monster.xp}")
        self.monster_cr_var.set(f"CR: {selected_monster.cr}")
        self.monster_alignment_var.set(f"Alignment: {selected_monster.alignment}")

        self.monster_str_var.set(f"STR: {selected_monster.str}")
        self.monster_dex_var.set(f"DEX: {selected_monster.dex}")
        self.monster_con_var.set(f"CON: {selected_monster.con}")
        self.monster_int_var.set(f"INT: {selected_monster.int}")
        self.monster_wis_var.set(f"WIS: {selected_monster.wis}")
        self.monster_cha_var.set(f"CHA: {selected_monster.cha}")

        self.parse_and_print_skills(selected_monster)

    def setup_summary_view(self):
        self.monster_name.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.monster_cr.grid(row=1, column=2, padx=10, pady=10)
        self.monster_exp.grid(row=1, column=0, padx=10, pady=10)
        self.monster_alignment.grid(row=1, column=1, padx=10, pady=10)

        self.monster_abilities_holder.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.monster_str.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.monster_dex.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.monster_con.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.monster_int.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.monster_wis.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        self.monster_cha.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        self.monster_skills_holder.grid(row=2, column=1, padx=10, pady=10, sticky="nsew", columnspan=2)

    def update_listbox(self, *args):
        # Get the selected filter criteria
        selected_cr = self.monster_cr_combobox_var.get()

        # Clear the listbox
        try:
            self.monster_list_box.delete(0, "end")
        except IndexError:
            pass

        # Filter the monsters based on the selected criteria
        filtered_monsters = self.filter_monsters(selected_cr)

        # Populate the listbox with the filtered monsters
        for monster in filtered_monsters:
            self.monster_list_box.insert("end", monster.name)

    def filter_monsters(self, cr):
        filtered_monsters = []
        for monster in self.monster_list.values():
            if str(monster.cr) == cr:
                filtered_monsters.append(monster)
        return filtered_monsters

    def parse_and_print_skills(self, selected_monster):
        for widget in self.monster_skills_holder.winfo_children():
            widget.destroy()
        if selected_monster is not None:
            skills = selected_monster.skills.split(', ')
            skills_list = []
            for skill in skills:
                if "(" in skill and ")" in skill:
                    skills_list.append(skill)
                else:
                    skills_list.extend(skill.split(", "))
            skills_text = ', '.join(skills_list)
            skills_text = skills_text.replace(", ", "\n")

            skills_label = customtkinter.CTkLabel(self.monster_skills_holder, text=skills_text)
            skills_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)



