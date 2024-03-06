class Monk:
    def __init__(self, data):
        self.id = data.get('ID')
        self.lvl = data.get('LvL')
        self.bab = data.get('BaB')
        self.fort_save = data.get('Fort_Save')
        self.ref_save = data.get('Ref_Save')
        self.will_save = data.get('Will_Save')
        self.special = data.get('Special')
        self.flurry_of_blow = data.get('Flurry_of_blow_AB')
        self.unarmed_damage = data.get('Unarmed_Damage')
        self.ac_bonus = data.get('AC_Bonus')
        self.fast_movement = data.get('Fast_Movement')
