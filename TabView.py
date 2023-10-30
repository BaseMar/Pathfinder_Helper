import customtkinter

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tabs = {}  # Store tab objects
        self.add("Summary")
        self.add("Abilities")
        self.add("Martial")
        self.add("Spells")

