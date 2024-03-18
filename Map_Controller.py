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
