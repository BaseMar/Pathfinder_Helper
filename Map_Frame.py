import customtkinter

class Map_Frame(customtkinter.CTkFrame):
    def __init__(self, parent, controller, config):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Map Sheet")
        label.grid(row=0, column=4, padx=10, pady=10)
