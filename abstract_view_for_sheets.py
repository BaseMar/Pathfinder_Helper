from abc import ABC, abstractmethod
import customtkinter
import TabView

class AbstractViewForSheets(customtkinter.CTkFrame, ABC):
    def __init__(self, parent, controller, config):
        customtkinter.CTkFrame.__init__(self, parent)
        self.config = config
        self.level_var = customtkinter.StringVar(self)
        self.experience_var = customtkinter.StringVar(self)
        self.alignment_var = customtkinter.StringVar(self)

    @abstractmethod
    def setup_frame(self):
        self.label = customtkinter.CTkLabel(self, text="Nazwa postaci/potwora", text_color=self.config["COLORS"]["TEXT"])
        self.label.place(y=20, x=100)
        self.experience_label = customtkinter.CTkLabel(self, text="EXPERIENCE", text_color=self.config["COLORS"]["TEXT"])
        self.experience_label.place(y=50, x=20)
        self.level = customtkinter.CTkLabel(self, textvariable=f"Level: {self.level_var}", text_color=self.config["COLORS"]["TEXT"])
        self.level.place(y=50, x=200)
        self.experience= customtkinter.CTkLabel(self, textvariable=f"{self.experience_var}", text_color=self.config["COLORS"]["TEXT"])
        self.experience.place(y=50, x=400)
        self.alignment = customtkinter.CTkLabel(self, textvariable=f"{self.alignment_var}", text_color=self.config["COLORS"]["TEXT"])
        self.alignment.place(y=20, x=300)
        self. progress_exp = customtkinter.CTkProgressBar(self, width=400, height=10)
        self.progress_exp.place(y=80, x=20)

        # Abilities
        self.strength_label=customtkinter.CTkLabel(self, text="STR", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.strength_label.place(y=130, x=48)
        self.strength_label_2 = customtkinter.CTkLabel(self, text="STRENGTH", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.strength_label_2.place(y=151, x=30)

        self.dexterity_label = customtkinter.CTkLabel(self, text="DEX", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.dexterity_label.place(y=180, x=48)
        self.dexterity_label_2 = customtkinter.CTkLabel(self, text="DEXTERITY", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.dexterity_label_2.place(y=201, x=30)

        self.constitution_label = customtkinter.CTkLabel(self, text="CON", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.constitution_label.place(y=230, x=47)
        self.constitution_label_2 = customtkinter.CTkLabel(self, text="CONSTITUTION", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.constitution_label_2.place(y=251, x=10)

        self.intelligence_label = customtkinter.CTkLabel(self, text="INT", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.intelligence_label.place(y=280, x=60)
        self.intelligence_label_2 = customtkinter.CTkLabel(self, text="INTELLIGENCE", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.intelligence_label_2.place(y=301, x=14)

        self.wisdom_label = customtkinter.CTkLabel(self, text="WIS", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.wisdom_label.place(y=330, x=50)
        self.wisdom_label_2 = customtkinter.CTkLabel(self, text="WISDOM", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.wisdom_label_2.place(y=351, x=45)

        self.charisma_label = customtkinter.CTkLabel(self, text="CHA", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 20))
        self.charisma_label.place(y=380, x=50)
        self.charisma_label_2 = customtkinter.CTkLabel(self, text="CHARISMA", text_color=self.config["COLORS"]["TEXT"], font=("Arial", 10))
        self.charisma_label_2.place(y=401, x=35)

        self.sum_label = customtkinter.CTkLabel(self, text="SUM", text_color=self.config["COLORS"]["TEXT"])
        self.sum_label.place(y=100, x=110)
        self.ability_score_label = customtkinter.CTkLabel(self, text="Ability Score", text_color=self.config["COLORS"]["TEXT"])
        self.ability_score_label.place(y=100, x=150)
        self.other_bonuses_label = customtkinter.CTkLabel(self, text="Other Bonuses", text_color=self.config["COLORS"]["TEXT"])
        self.other_bonuses_label.place(y=100, x=230)
        self.bonus_modifier_label = customtkinter.CTkLabel(self, text="Bonus Mod.", text_color=self.config["COLORS"]["TEXT"])
        self.bonus_modifier_label.place(y=100, x=350)

        # Tabview
        self.tab_view = TabView.MyTabView(parent=self, width=450, height=410, corner_radius=20, text_color=self.config["COLORS"]["TEXT"])
        self.tab_view.place(y=10, x=450)
