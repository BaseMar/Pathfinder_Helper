import customtkinter
from abstract_view_for_sheets import AbstractViewForSheets

class Character_Sheet_Frame(AbstractViewForSheets):
    def __init__(self, parent, controller, config):
        super().__init__(parent, controller, config)
        self.setup_frame()

    def setup_frame(self):
        super().setup_frame()