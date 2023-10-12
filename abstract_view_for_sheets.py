from abc import ABC, abstractmethod
import customtkinter
import TabView
import math


def calculate_bonus_modifier(score=0, other_bonuses=0):
    bonus_modifier = (int(score) + int(other_bonuses) - 10) / 2
    rounded_bonus_modifier = math.floor(bonus_modifier)
    return rounded_bonus_modifier


class AbstractViewForSheets(customtkinter.CTkFrame, ABC):
    def __init__(self, parent, controller, config):
        customtkinter.CTkFrame.__init__(self, parent)
        self.charisma_sum = None
        self.charisma_bonus_mod = None
        self.wisdom_bonus_mod = None
        self.wisdom_sum = None
        self.intelligence_bonus_mod = None
        self.intelligence_sum = None
        self.constitution_bonus_mod = None
        self.constitution_sum = None
        self.dexterity_bonus_mod = None
        self.dexterity_sum = None
        self.tab_view = None
        self.bonus_modifier_label = None
        self.ability_score_label = None
        self.charisma_label_2 = None
        self.charisma_label = None
        self.intelligence_label_2 = None
        self.wisdom_label_2 = None
        self.wisdom_label = None
        self.intelligence_label = None
        self.constitution_label_2 = None
        self.constitution_label = None
        self.dexterity_label_2 = None
        self.dexterity_label = None
        self.strength_bonus_mod = None
        self.strength_sum = None
        self.strength_label_2 = None
        self.strength_label = None
        self.alignment = None
        self.experience = None
        self.level = None
        self.experience_label = None
        self.label = None

        self.config = config
        self.controller = controller

        self.name = customtkinter.StringVar(self, value="Name", name="name")
        self.level_var = customtkinter.StringVar(self, value="Level", name="lvl")
        self.experience_var = customtkinter.StringVar(self, value="Exp gain", name="exp")
        self.alignment_var = customtkinter.StringVar(self, value="Alignment", name="alignment")

        self.str_sum_var = customtkinter.StringVar(self, value="0", name="strength sum")
        self.str_bonus_mod = customtkinter.StringVar(self, value="0", name="strength modifier")
        self.dex_sum_var = customtkinter.StringVar(self, value="0", name="dexterity sum")
        self.dex_bonus_mod = customtkinter.StringVar(self, value="0", name="dexterity modifier")
        self.con_sum_var = customtkinter.StringVar(self, value="0", name="constitution sum")
        self.con_bonus_mod = customtkinter.StringVar(self, value="0", name="constitution modifier")
        self.int_sum_var = customtkinter.StringVar(self, value="0", name="intelligence sum")
        self.int_bonus_mod = customtkinter.StringVar(self, value="0", name="intelligence modifier")
        self.wis_sum_var = customtkinter.StringVar(self, value="0", name="wisdom sum")
        self.wis_bonus_mod = customtkinter.StringVar(self, value="0", name="wisdom modifier")
        self.cha_sum_var = customtkinter.StringVar(self, value="0", name="charisma sum")
        self.cha_bonus_mod = customtkinter.StringVar(self, value="0", name="charisma modifier")

    @abstractmethod
    def setup_frame(self):
        self.label = customtkinter.CTkLabel(self, textvariable=self.name, text_color=self.config["COLORS"]["TEXT"])
        self.label.place(y=20, x=100)
        self.experience_label = customtkinter.CTkLabel(self, text="EXPERIENCE", text_color=self.config["COLORS"]["TEXT"])
        self.experience_label.place(y=50, x=20)
        self.level = customtkinter.CTkLabel(self, textvariable=self.level_var, text_color=self.config["COLORS"]["TEXT"])
        self.level.place(y=50, x=200)
        self.experience = customtkinter.CTkLabel(self, textvariable=f"{self.experience_var}", text_color=self.config["COLORS"]["TEXT"])
        self.experience.place(y=50, x=350)
        self.alignment = customtkinter.CTkLabel(self, textvariable=self.alignment_var, text_color=self.config["COLORS"]["TEXT"])
        self.alignment.place(y=20, x=300)

        # Abilities
        self.strength_label = customtkinter.CTkLabel(self, text="STR", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.strength_label.place(y=130, x=48)
        self.strength_label_2 = customtkinter.CTkLabel(self, text="STRENGTH", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.strength_label_2.place(y=151, x=30)
        self.strength_sum = customtkinter.CTkLabel(self, textvariable=self.str_sum_var, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.strength_sum.place(y=130, x=175)
        self.strength_bonus_mod = customtkinter.CTkLabel(self, textvariable=self.str_bonus_mod, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.strength_bonus_mod.place(y=130, x=305)

        self.dexterity_label = customtkinter.CTkLabel(self, text="DEX", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.dexterity_label.place(y=180, x=48)
        self.dexterity_label_2 = customtkinter.CTkLabel(self, text="DEXTERITY", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.dexterity_label_2.place(y=201, x=30)
        self.dexterity_sum = customtkinter.CTkLabel(self, textvariable=self.dex_sum_var, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.dexterity_sum.place(y=180, x=175)
        self.dexterity_bonus_mod = customtkinter.CTkLabel(self, textvariable=self.dex_bonus_mod, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.dexterity_bonus_mod.place(y=180, x=305)

        self.constitution_label = customtkinter.CTkLabel(self, text="CON", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.constitution_label.place(y=230, x=47)
        self.constitution_label_2 = customtkinter.CTkLabel(self, text="CONSTITUTION", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.constitution_label_2.place(y=251, x=10)
        self.constitution_sum = customtkinter.CTkLabel(self, textvariable=self.con_sum_var, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.constitution_sum.place(y=230, x=175)
        self.constitution_bonus_mod = customtkinter.CTkLabel(self, textvariable=self.con_bonus_mod, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.constitution_bonus_mod.place(y=230, x=305)

        self.intelligence_label = customtkinter.CTkLabel(self, text="INT", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.intelligence_label.place(y=280, x=60)
        self.intelligence_label_2 = customtkinter.CTkLabel(self, text="INTELLIGENCE", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.intelligence_label_2.place(y=301, x=14)
        self.intelligence_sum = customtkinter.CTkLabel(self, textvariable=self.int_sum_var, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.intelligence_sum.place(y=280, x=175)
        self.intelligence_bonus_mod = customtkinter.CTkLabel(self, textvariable=self.int_bonus_mod, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.intelligence_bonus_mod.place(y=280, x=305)

        self.wisdom_label = customtkinter.CTkLabel(self, text="WIS", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.wisdom_label.place(y=330, x=50)
        self.wisdom_label_2 = customtkinter.CTkLabel(self, text="WISDOM", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.wisdom_label_2.place(y=351, x=45)
        self.wisdom_sum = customtkinter.CTkLabel(self, textvariable=self.wis_sum_var, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.wisdom_sum.place(y=330, x=175)
        self.wisdom_bonus_mod = customtkinter.CTkLabel(self, textvariable=self.wis_bonus_mod, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.wisdom_bonus_mod.place(y=330, x=305)

        self.charisma_label = customtkinter.CTkLabel(self, text="CHA", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.charisma_label.place(y=380, x=50)
        self.charisma_label_2 = customtkinter.CTkLabel(self, text="CHARISMA", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.charisma_label_2.place(y=401, x=35)
        self.charisma_sum = customtkinter.CTkLabel(self, textvariable=self.cha_sum_var, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.charisma_sum.place(y=380, x=175)
        self.charisma_bonus_mod = customtkinter.CTkLabel(self, textvariable=self.cha_bonus_mod, font=("Helvetica", 25), text_color=self.config["COLORS"]["TEXT"])
        self.charisma_bonus_mod.place(y=380, x=305)
        
        self.ability_score_label = customtkinter.CTkLabel(self, text="Ability Score", text_color=self.config["COLORS"]["TEXT"])
        self.ability_score_label.place(y=100, x=150)
        self.bonus_modifier_label = customtkinter.CTkLabel(self, text="Bonus Mod.", text_color=self.config["COLORS"]["TEXT"])
        self.bonus_modifier_label.place(y=100, x=280)

        # Tabview
        self.tab_view = TabView.MyTabView(parent=self, width=450, height=410, corner_radius=20, text_color=self.config["COLORS"]["TEXT"])
        self.tab_view.place(y=10, x=450)
