class Magic_Items:
    def __init__(self, data):
        self.id = data.get('ID')
        self.name = data.get('Name')
        self.str_bonus = data.get('str_bonus')
        self.dex_bonus = data.get('dex_bonus')
        self.con_bonus = data.get('con_bonus')
        self.int_bonus = data.get('int_bonus')
        self.wis_bonus = data.get('wis_bonus')
        self.cha_bonus = data.get('cha_bonus')
        self.fort_bonus = data.get('Fort_save')
        self.ref_bonus = data.get('Reflex_save')
        self.will_bonus = data.get('Will_save')
        self.ac_bonus = data.get('AC')
        self.slot = data.get('Slot')
        self.description = data.get('Description')
        