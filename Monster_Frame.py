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
        self.monster_type_list = []
        self.monster_alignment_list = []

        # Configure geometry of a Frame 4x2
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.load_data()

        # Monster list box
        self.monster_list_box = CTkListbox(self, border_color=config["COLORS"]["BUTTON"],
                                           border_width=1,
                                           hover_color=config["COLORS"]["HOVER"],
                                           text_color=config["COLORS"]["TEXT"],
                                           multiple_selection=False,
                                           command=self.show_monster_data)

        # TabView
        self.tab_view = MyTabView(self)
        self.tab_view.tab("Summary").grid_columnconfigure((0, 1, 2), weight=1)

        # Filters widgets
        self.monster_cr_combobox_var = customtkinter.StringVar(value=self.monster_cr_list[0])
        self.monster_cr_combobox = customtkinter.CTkComboBox(self, values=self.monster_cr_list, variable=self.monster_cr_combobox_var, width=20)
        self.monster_type_combobox_var = customtkinter.StringVar(value=self.monster_type_list[0])
        self.monster_type_combobox = customtkinter.CTkComboBox(self, values=self.monster_type_list, variable=self.monster_type_combobox_var, width=40)
        self.monster_alignment_combobox_var = customtkinter.StringVar(value=self.monster_alignment_list[0])
        self.monster_alignment_combobox = customtkinter.CTkComboBox(self, values=self.monster_alignment_list, variable=self.monster_alignment_combobox_var, width=20)

        self.update_listbox()

        self.monster_cr_combobox_var.trace_add("write", self.update_listbox)
        self.monster_type_combobox_var.trace_add("write", self.update_listbox)
        self.monster_alignment_combobox_var.trace_add("write", self.update_listbox)

        # Place widget to Monster Frame
        self.setup_frame()

        # Place widgets to TabView - Summary
        self.monster_name_var = customtkinter.StringVar(value="Monster Name: ", name="name")
        self.monster_name = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_name_var, font=("Arial", 25), text_color=config["COLORS"]["TEXT"])
        self.monster_cr_var = customtkinter.StringVar(value="CR: ", name="cr")
        self.monster_cr = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_cr_var, font=("Arial", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_exp_var = customtkinter.StringVar(value="EXP: ", name="exp")
        self.monster_exp = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_exp_var, font=("Arial", 15), text_color=config["COLORS"]["TEXT"])
        self.monster_alignment_var = customtkinter.StringVar(value="Alignment: ", name="alignment")
        self.monster_alignment = customtkinter.CTkLabel(self.tab_view.tab("Summary"), textvariable=self.monster_alignment_var, font=("Arial", 15), text_color=config["COLORS"]["TEXT"])
        self.setup_summary_view()

        # Place widgets to TabView - Abilities
        # Place widgets to TabView - Martial
        # Place widgets to TabView - Spells

    def load_data(self):
        monsters = []
        with open("DataBase/MonsterList.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            cr_set = set()
            type_set = set()
            alignment_set = set()
            for row in csv_reader:
                monster = Monster(row)

                # Add data to sets to eliminate duplicates
                cr_set.add(float(monster.cr))
                type_set.add(monster.type)
                alignment_set.add(monster.alignment)

                self.monster_list[monster.name] = monster

            # Convert sets back to lists
            self.monster_cr_list = sorted(cr_set)
            self.monster_cr_list = [f"{cr:.2f}" for cr in self.monster_cr_list]
            self.monster_type_list = list(type_set) + ["Any"]
            unwanted_alignments = ["NG or NE", "Any alignment (same as creator)"]
            self.monster_alignment_list = [alignment for alignment in alignment_set if alignment not in unwanted_alignments]

    def setup_frame(self):
        self.monster_list_box.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
        self.tab_view.grid(row=0, column=3, rowspan=2, sticky="nsew", padx=10, pady=10)
        self.monster_cr_combobox.grid(row=0, column=0, sticky="ew", padx=10)
        self.monster_type_combobox.grid(row=0, column=1, sticky="ew", padx=10)
        self.monster_alignment_combobox.grid(row=0, column=2, sticky="ew", padx=10)

    def show_monster_data(self, selected_option):
        selected_monster = self.monster_list[selected_option]
        self.monster_name_var.set(f"{selected_monster.name}")
        self.monster_exp_var.set(f"EXP: {selected_monster.xp}")
        self.monster_cr_var.set(f"CR: {selected_monster.cr}")
        self.monster_alignment_var.set(f"Alignment: {selected_monster.alignment}")

    def setup_summary_view(self):
        self.monster_name.grid(row=0, column=1, padx=10, pady=10)
        self.monster_cr.grid(row=1, column=2, padx=10, pady=10)
        self.monster_exp.grid(row=1, column=0, padx=10, pady=10)
        self.monster_alignment.grid(row=1, column=1, padx=10, pady=10)

    def update_listbox(self, *args):
        # Get the selected filter criteria
        selected_cr = self.monster_cr_combobox_var.get()
        selected_type = self.monster_type_combobox_var.get()
        selected_alignment = self.monster_alignment_combobox_var.get()

        # Filter the monsters based on the selected criteria
        filtered_monsters = self.filter_monsters(selected_cr, selected_type, selected_alignment)

        # Populate the listbox with the filtered monsters
        for monster in filtered_monsters:
            self.monster_list_box.insert("end", monster.name)

    def filter_monsters(self, cr, monster_type, alignment):
        filtered_monsters = []

        for monster in self.monster_list.values():
            if (
                    (cr == "Filter" or monster.cr == cr) and
                    (monster_type == "Filter" or monster.type == monster_type) and
                    (alignment == "Filter" or monster.alignment == alignment)
            ):
                filtered_monsters.append(monster)

        return filtered_monsters
