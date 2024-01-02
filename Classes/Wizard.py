class Wizard:
    def __init__(self, data):
        self.id = data.get('ID')
        self.lvl = data.get('LvL')
        self.bab = data.get('BaB')
        self.fort_save = data.get('Fort_Save')
        self.ref_save = data.get('Ref_Save')
        self.will_save = data.get('Will_Save')
        self.special = data.get('Special')
        self.spells_per_day_1 = data.get('1_spells_per_day')
        self.spells_per_day_2 = data.get('2_spells_per_day')
        self.spells_per_day_3 = data.get('3_spells_per_day')
        self.spells_per_day_4 = data.get('4_spells_per_day')
        self.spells_per_day_5 = data.get('5_spells_per_day')
        self.spells_per_day_6 = data.get('6_spells_per_day')
        self.spells_per_day_7 = data.get('7_spells_per_day')
        self.spells_per_day_8 = data.get('8_spells_per_day')
        self.spells_per_day_9 = data.get('9_spells_per_day')

    def __repr__(self):
        return (f"Wizard(id={self.id}, lvl={self.lvl}, bab={self.bab}, fort_save = {self.fort_save}, ref_save={self.ref_save}, will_save={self.will_save}, special={self.special}),"
                f"1lvl spells per day: {self.spells_per_day_1}, 2lvl spells per day: {self.spells_per_day_2},"
                f"3lvl spells per day: {self.spells_per_day_3}, 4lvl spells per day: {self.spells_per_day_4},"
                f"5lvl spells per day: {self.spells_per_day_5}, 6lvl spells per day: {self.spells_per_day_6},"
                f"7lvl spells per day: {self.spells_per_day_7}, 8lvl spells per day: {self.spells_per_day_8},"
                f"9lvl spells per day: {self.spells_per_day_9}")
