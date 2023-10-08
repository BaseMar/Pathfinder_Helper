import customtkinter
from Monster import Monster
from abstract_view_for_sheets import AbstractViewForSheets
import csv

class Monster_Frame(AbstractViewForSheets):
    def __init__(self, parent, controller, config):
        super().__init__(parent, controller, config)
        self.setup_frame()
        self.monster_list = {}

        # Load monster database
        self.load_data()

    def setup_frame(self):
        super().setup_frame()

    def load_data(self):
        with open("DataBase/MonsterList.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            for row in csv_reader:
                monster = Monster(row)
                self.monster_list[monster.name] = monster