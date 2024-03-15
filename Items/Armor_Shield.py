class Armor_Shield:
    def __init__(self, data):
        self.id = data.get('ID')
        self.name = data.get('Name')
        self.ac_bonus = data.get('Armor_Shield_bonus')
        self.max_dex_bonus = data.get('Maximum_dex_bonus')
        self.check_penalty = data.get('Armor_Check_Penalty')
        self.speed_30 = data.get('Speed_30')
        self.speed_20 = data.get('Speed_20')
        self.slot = data.get('Slot')
