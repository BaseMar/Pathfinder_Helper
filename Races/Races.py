class Races:
    def __init__(self, data):
        self.id = data.get('ID')
        self.name = data.get('Name')
        self.str_bonus = data.get('str_bonus')
        self.dex_bonus = data.get('dex_bonus')
        self.con_bonus = data.get('con_bonus')
        self.int_bonus = data.get('int_bonus')
        self.wis_bonus = data.get('wis_bonus')
        self.cha_bonus = data.get('cha_bonus')
        self.size = data.get('size')
        self.speed = data.get('speed')
        self.languages = data.get('languages')
        self.languages_bonus = data.get('languages_bonus')
        self.special = data.get('special')
