class AttributePropertyMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name in attrs.get("__attributes__", []):
            # Create a property and setter for each attribute
            prop_name = f"_{attr_name}"
            attrs[attr_name] = property(lambda self, name=prop_name: getattr(self, name))
            attrs[f"set_{attr_name}"] = lambda self, value, name=prop_name: setattr(self, name, value)
        return super().__new__(cls, name, bases, attrs)

class Monster(metaclass=AttributePropertyMeta):
    # List of attributes you want to define properties for
    __attributes__ = [
        "name", "cr", "xp", "race", "class", "monster_source", "alignment", "size", "type", "subtype",
        "init", "senses", "aura", "ac", "ac_mods", "hp", "hd", "hp_mods", "saves", "fort", "ref", "will",
        "save_mods", "defensive_abilities", "dr", "immune", "resist", "sr", "weaknesses", "speed",
        "speed_mod", "melee", "ranged", "space", "reach", "special_attacks", "spell_like_abilities",
        "spells_known", "spells_prepared", "spell_domains", "ability_scores", "ability_score_mods",
        "base_atk", "cmb", "cmd", "feats", "skills", "racial_mods", "languages", "sq", "environment",
        "organization", "treasure", "description_visual", "group", "source", "is_template",
        "special_abilities", "description", "full_text", "gender", "bloodline", "prohibited_schools",
        "before_combat", "during_combat", "morale", "gear", "other_gear", "vulnerability", "note",
        "character_flag", "companion_flag", "fly", "climb", "burrow", "swim", "land", "templates_applied",
        "offense_note", "base_statistics", "extracts_prepared", "age_category", "dont_use_racial_hd",
        "variant_parent", "mystery", "class_archetypes", "patron", "companion_familiar_link",
        "focused_school", "traits", "alternate_name_form", "statistics_note", "link_text", "id",
        "unique_monster", "mr", "mythic", "mt"]

    def __init__(self, data):
        # Initialize all fields as private variables with None values
        self._name = data[0]
        self._cr = data[1]
        self._xp = data[2]
        self._race = data[3]
        self._class = data[4]
        self._monster_source = data[5]
        self._alignment = data[6]
        self._size = data[7]
        self._type = data[8]
        self._subtype = data[9]
        self._init = data[10]
        self._senses = data[11]
        self._aura = data[12]
        self._ac = data[13]
        self._ac_mods = data[14]
        self._hp = data[15]
        self._hd = data[16]
        self._hp_mods = data[17]
        self._saves = data[18]
        self._fort = data[19]
        self._ref = data[20]
        self._will = data[21]
        self._save_mods = data[22]
        self._defensive_abilities = data[23]
        self._dr = data[24]
        self._immune = data[25]
        self._resist = data[26]
        self._sr = data[27]
        self._weaknesses = data[28]
        self._speed = data[29]
        self._speed_mod = data[30]
        self._melee = data[31]
        self._ranged = data[32]
        self._space = data[33]
        self._reach = data[34]
        self._special_attacks = data[35]
        self._spell_like_abilities = data[36]
        self._spells_known = data[37]
        self._spells_prepared = data[38]
        self._spell_domains = data[39]
        self._ability_scores = data[40]
        self._ability_score_mods = data[41]
        self._base_atk = data[42]
        self._cmb = data[43]
        self._cmd = data[44]
        self._feats = data[45]
        self._skills = data[46]
        self._racial_mods = data[47]
        self._languages = data[48]
        self._sq = data[49]
        self._environment = data[50]
        self._organization = data[51]
        self._treasure = data[52]
        self._description_visual = data[53]
        self._group = data[54]
        self._source = data[55]
        self._is_template = data[56]
        self._special_abilities = data[57]
        self._description = data[58]
        self._full_text = data[59]
        self._gender = data[60]
        self._bloodline = data[61]
        self._prohibited_schools = data[62]
        self._before_combat = data[63]
        self._during_combat = data[64]
        self._morale = data[65]
        self._gear = data[66]
        self._other_gear = data[67]
        self._vulnerability = data[68]
        self._note = data[69]
        self._character_flag = data[70]
        self._companion_flag = data[71]
        self._fly = data[72]
        self._climb = data[73]
        self._burrow = data[74]
        self._swim = data[75]
        self._land = data[76]
        self._templates_applied = data[77]
        self._offense_note = data[78]
        self._base_statistics = data[79]
        self._extracts_prepared = data[80]
        self._age_category = data[81]
        self._dont_use_racial_hd = data[82]
        self._variant_parent = data[83]
        self._mystery = data[84]
        self._class_archetypes = data[85]
        self._patron = data[86]
        self._companion_familiar_link = data[87]
        self._focused_school = data[88]
        self._traits = data[89]
        self._alternate_name_form = data[90]
        self._statistics_note = data[91]
        self._link_text = data[92]
        self._id = data[93]
        self._unique_monster = data[94]
        self._mr = data[95]
        self._mythic = data[96]
        self._mt = data[97]
