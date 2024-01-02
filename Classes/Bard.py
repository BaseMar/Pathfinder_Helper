class Bard:
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
        self.spells_known_0 = data.get('0_spells_known')
        self.spells_known_1 = data.get('1_spells_known')
        self.spells_known_2 = data.get('2_spells_known')
        self.spells_known_3 = data.get('3_spells_known')
        self.spells_known_4 = data.get('4_spells_known')
        self.spells_known_5 = data.get('5_spells_known')
        self.spells_known_6 = data.get('6_spells_known')

    def __repr__(self):
        return (f"Bard(id={self.id}, lvl={self.lvl}, bab={self.bab}, fort_save = {self.fort_save}, ref_save={self.ref_save}, will_save={self.will_save}, special={self.special}),"
                f"1lvl spells per day: {self.spells_per_day_1}, 2lvl spells per day: {self.spells_per_day_2},"
                f"3lvl spells per day: {self.spells_per_day_3}, 4lvl spells per day: {self.spells_per_day_4},"
                f"5lvl spells per day: {self.spells_per_day_5}, 6lvl spells per day: {self.spells_per_day_6},"
                f"0lvl spells known: {self.spells_known_0}, 1lvl spells known: {self.spells_known_1}, "
                f"2lvl spells known: {self.spells_known_2}, 3lvl spells known: {self.spells_known_3}, "
                f"4lvl spells known: {self.spells_known_4}, 5lvl spells known: {self.spells_known_5}, "
                f"6lvl spells known: {self.spells_known_6}")
