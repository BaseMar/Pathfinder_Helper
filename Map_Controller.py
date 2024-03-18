import random
from tkinter import filedialog
import os
from Load_Map import Load_Map

class MapController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.toplevel_window = None

    def load_map(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if path:
            os.path.dirname(path)
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Load_Map(path)

    def remove_player(self, item):
        self.view.initiative_list_frame.remove_item(item)

    def add_player(self, item):
        self.view.initiative_list_frame.add_item(item)

    def roll_dice(self, choice, bonus, multiply):
        dice_range = {
            "d4": (1, 4),
            "d6": (1, 6),
            "d8": (1, 8),
            "d12": (1, 12),
            "d20": (1, 20)
        }

        min_value, max_value = dice_range.get(choice, (1, 1))

        total_sum = sum(random.randint(min_value, max_value) for _ in range(int(multiply))) + int(bonus)
        self.model.result = total_sum
        return self.model
