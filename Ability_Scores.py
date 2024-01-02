import customtkinter
import re
import math


def validate(new_value):
    return re.match('^\d{0,3}$', new_value) is not None


class Ability_Scores:
    def __init__(self, name, row, frame):
        self.subject = None
        self.name = name

        self.ability_score = customtkinter.StringVar(value="0")
        self.ability_increase = customtkinter.StringVar(value="0")
        self.race_bonus = customtkinter.StringVar(value="0")
        self.spell_bonus = customtkinter.StringVar(value="0")
        self.item_bonus = customtkinter.StringVar(value="0")
        self.other_bonuses = customtkinter.StringVar(value="0")
        self.bonus_modifier = customtkinter.StringVar(value="-5")

        label = customtkinter.CTkLabel(frame, text=f"{name} = ")
        ability_score = customtkinter.CTkEntry(frame, width=35, textvariable=self.ability_score)
        ability_increase = customtkinter.CTkEntry(frame, width=35, textvariable=self.ability_increase)
        race_bonus = customtkinter.CTkLabel(frame, width=30, textvariable=self.race_bonus, state="disabled")
        spell_bonus = customtkinter.CTkLabel(frame, width=30, state="disabled", textvariable=self.spell_bonus)
        item_bonus = customtkinter.CTkLabel(frame, width=30, state="disabled", textvariable=self.item_bonus)
        other_bonuses = customtkinter.CTkLabel(frame, width=30, state="disabled", textvariable=self.other_bonuses)
        self.bonus_modifier_label = customtkinter.CTkLabel(frame, width=30, state="disabled", textvariable=self.bonus_modifier)

        # Validations
        vcmd = (frame.register(validate), '%P')
        ability_score.configure(validate="key", validatecommand=vcmd)
        ability_increase.configure(validate="key", validatecommand=vcmd)

        # Event handling
        ability_score.bind("<FocusOut>", self.fill_empty_with_zero)
        ability_increase.bind("<FocusOut>", self.fill_empty_with_zero)
        ability_score.bind("<KeyRelease>", self.calculate_bonus_modifier)
        ability_increase.bind("<KeyRelease>", self.calculate_bonus_modifier)

        label.grid(row=row, column=0, padx=2, pady=2)
        ability_score.grid(row=row, column=1, padx=2, pady=2)
        ability_increase.grid(row=row, column=2, padx=2, pady=2)
        race_bonus.grid(row=row, column=3, padx=2, pady=2)
        spell_bonus.grid(row=row, column=4, padx=2, pady=2)
        item_bonus.grid(row=row, column=5, padx=2, pady=2)
        other_bonuses.grid(row=row, column=6, padx=2, pady=2)
        self.bonus_modifier_label.grid(row=row, column=7, padx=20, pady=2)

    def calculate_bonus_modifier(self, *args):
        try:
            ability_score = self.ability_score.get()
            ability_increase = self.ability_increase.get()
            race_bonus = self.race_bonus.get()
            spell_bonus = self.spell_bonus.get()
            item_bonus = self.item_bonus.get()
            other_bonuses = self.other_bonuses.get()

            ability_score = int(ability_score)
            ability_increase = int(ability_increase)
            race_bonus = int(race_bonus)
            spell_bonus = int(spell_bonus)
            item_bonus = int(item_bonus)
            other_bonuses = int(other_bonuses)

            suma = ability_score + ability_increase + race_bonus + spell_bonus + item_bonus + other_bonuses
            bonus_modifier = str(math.floor((suma - 10) / 2))

            self.bonus_modifier.set(bonus_modifier)
            if self.subject is not None:
                self.subject.notify(bonus_modifier)

        except ValueError:
            pass

    def fill_empty_with_zero(self, event):
        if not event.widget.get().strip():
            event.widget.insert(0, "0")
            self.calculate_bonus_modifier()

    def add_subject(self, subject):
        self.subject = subject
