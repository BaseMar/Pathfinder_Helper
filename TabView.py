import customtkinter

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tabs = {}
        self.add("Summary")
        self.add("Abilities")
        self.add("Martial")
        self.add("Spells")
