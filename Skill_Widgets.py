import customtkinter
import re

def validate(new_value):
    return re.match('^\d{0,3}$', new_value) is not None

class Skill_Widgets:
    def __init__(self, name, row, frame):
        self.name = name

        # String Var
        self.total = customtkinter.StringVar(value="0")
        self.ability_mod_var = customtkinter.StringVar(value="0")
        self.ranks = customtkinter.StringVar(value="0")
        self.misc_modifier = customtkinter.StringVar(value="0")

        # Widgets
        label = customtkinter.CTkLabel(frame, text=f"{name}: ")
        total = customtkinter.CTkLabel(frame, width=30, textvariable=self.total)
        ability_modifier = customtkinter.CTkLabel(frame, width=30, textvariable=self.ability_mod_var)
        ranks = customtkinter.CTkEntry(frame, width=35, textvariable=self.ranks)
        misc_modifier = customtkinter.CTkLabel(frame, width=30, textvariable=self.misc_modifier)

        # Grid
        label.grid(row=row, column=0, padx=2, pady=2)
        total.grid(row=row, column=1, padx=2, pady=2)
        ability_modifier.grid(row=row, column=2, padx=10, pady=2)
        ranks.grid(row=row, column=3, padx=2, pady=2)
        misc_modifier.grid(row=row, column=4, padx=2, pady=2)

        # Validations
        vcmd = (frame.register(validate), '%P')
        ranks.configure(validate="key", validatecommand=vcmd)

    def calculate_total_bonus(self, *args):
        try:
            ability_modifier = int(self.ability_mod_var.get())
            misc_modifier = int(self.misc_modifier.get())
            ranks = int(self.ranks.get())

            total = ranks + ability_modifier + misc_modifier

            self.total.set(str(total))
        except ValueError:
            pass
