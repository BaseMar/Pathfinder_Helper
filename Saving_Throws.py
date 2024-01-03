import customtkinter

class Saving_Throws:
    def __init__(self, name, row, frame, ability_modifier):
        self.name = name
        self.ability_modifier = ability_modifier

        # String Var
        self.total = customtkinter.StringVar(value="0")
        self.base_save = customtkinter.StringVar(value="0")
        self.ability_mod_var = customtkinter.StringVar(value=f"{self.ability_modifier}")
        self.magic_modifier = customtkinter.StringVar(value="0")
        self.misc_modifier = customtkinter.StringVar(value="0")
        self.temporary_modifier = customtkinter.StringVar(value="0")

        # Widgets
        label = customtkinter.CTkLabel(frame, text=f"{name}")
        total = customtkinter.CTkLabel(frame, width=30, textvariable=self.total)
        base_save = customtkinter.CTkLabel(frame, width=30, textvariable=self.base_save)
        ability_modifier_widget = customtkinter.CTkLabel(frame, width=30, textvariable=self.ability_mod_var)
        magic_modifier = customtkinter.CTkLabel(frame, width=30, textvariable=self.magic_modifier, state="disabled")
        misc_modifier = customtkinter.CTkLabel(frame, width=30, textvariable=self.misc_modifier)
        temporary_modifier = customtkinter.CTkLabel(frame, width=30, textvariable=self.temporary_modifier)

        # Grid
        label.grid(row=row, column=0, padx=2, pady=2)
        total.grid(row=row, column=1, padx=2, pady=2)
        base_save.grid(row=row, column=2, padx=2, pady=2)
        ability_modifier_widget.grid(row=row, column=3, padx=2, pady=2)
        magic_modifier.grid(row=row, column=4, padx=2, pady=2)
        misc_modifier.grid(row=row, column=5, padx=2, pady=2)
        temporary_modifier.grid(row=row, column=6, padx=2, pady=2)

    def calculate_total_bonus(self, *args):
        try:
            base_save = int(self.base_save.get())
            ability_modifier = int(self.ability_modifier)
            magic_modifier = int(self.magic_modifier.get())
            misc_modifier = int(self.misc_modifier.get())
            temporary_modifier = int(self.temporary_modifier.get())

            total = base_save + ability_modifier + magic_modifier + misc_modifier + temporary_modifier

            self.total.set(str(total))

        except ValueError:
            pass
