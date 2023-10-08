import customtkinter

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.add("Summary")
        self.add("Abilities")
        self.add("Martial")
        self.add("Class")
