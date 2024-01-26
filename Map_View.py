import customtkinter


class MapView(customtkinter.CTkFrame):
    def __init__(self, parent, config):
        self.config = config
        self.controller = None

        super().__init__(parent)
        self.label = customtkinter.CTkLabel(self, text="Map Frame")

        self.grid_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def grid_widgets(self):
        self.label.grid(row=0, column=0)

    def init_data(self):
        pass
