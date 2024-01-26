import customtkinter
class MonsterView(customtkinter.CTkFrame):
    def __init__(self, parent, config):
        self.controller = None
        self.config = config

        super().__init__(parent)
        self.label = customtkinter.CTkLabel(self, text="Monster Frame")

        self.grid_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def grid_widgets(self):
        self.label.grid(row=0, column=0)

    def init_data(self):
        pass
