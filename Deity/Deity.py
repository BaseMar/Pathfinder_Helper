class Deity:
    def __init__(self, data):
        self.id = data.get('ID')
        self.name = data.get('Name')
        self.alignment = data.get('Alignment')
        self.domains = data.get('Domains')
        self.favored_weapon = data.get('Favored_Weapon')
        self.portfolio = data.get('Portfolio')
