class CharacterSheetModel:
    def __init__(self):
        self.character_name = ""
        self.character_player = ""
        self.character_alignment_list = []
        self.character_deity_list = []
        self.character_class_list = []
        self.character_lvl_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        self.character_selected_lvl = 1
        self.character_filename = ""
        self.selected_character_class = None
        self.character_homeland = ""
        self.character_race_list = []
        self.character_gender_list = ["Male \u2642", "Female \u2640"]
        self.character_size = "Medium"
        self.character_racial_traits_list = []
        self.character_feats_list = []
        self.character_languages_list = ["Common"]
        self.skill_dictionary_settings = {}
        self.character_spell_list = {}

        self.character_hp = 1

        self.character_initiative_misc = 0
        self.character_initiative_total = 0

        self.character_ac_sum = 10
        self.character_ac_armor_bonus = 0
        self.character_ac_shield_bonus = 0
        self.character_ac_size_modifier = 0
        self.character_ac_natural_armor = 0
        self.character_ac_deflection_bonus = 0
        self.character_ac_misc_modifier = 0
        self.character_touch_ac = 10
        self.character_flat_ac = 10

        self.character_fort_save_sum = 0
        self.character_fort_base = 0
        self.character_fort_magic_mod = 0
        self.character_fort_misc_mod = 0
        self.character_ref_save_sum = 0
        self.character_ref_base = 0
        self.character_ref_magic_mod = 0
        self.character_ref_misc_mod = 0
        self.character_will_save_sum = 0
        self.character_will_base = 0
        self.character_will_magic_mod = 0
        self.character_will_misc_mod = 0

        self.character_bab = 0
        self.character_spell_resist = 0
        self.character_speed = 20

        self.character_cmb_sum = 0
        self.character_cmb_size_mod = 0
        self.character_cmd_sum = 0
        self.character_cmd_size_mod = 0

        self.skill_dict = {}

        self.str_score = 10
        self.str_increase = 0
        self.str_spell_bonus = 0
        self.str_item_bonus = 0
        self.str_other_bonuses = 0
        self.str_race_bonus = 0
        self.str_sum = 10
        self.str_mod = 0

        self.dex_score = 10
        self.dex_increase = 0
        self.dex_spell_bonus = 0
        self.dex_item_bonus = 0
        self.dex_other_bonuses = 0
        self.dex_race_bonus = 0
        self.dex_sum = 10
        self.dex_mod = 0

        self.con_score = 10
        self.con_increase = 0
        self.con_spell_bonus = 0
        self.con_item_bonus = 0
        self.con_other_bonuses = 0
        self.con_race_bonus = 0
        self.con_sum = 10
        self.con_mod = 0

        self.int_score = 10
        self.int_increase = 0
        self.int_spell_bonus = 0
        self.int_item_bonus = 0
        self.int_other_bonuses = 0
        self.int_race_bonus = 0
        self.int_sum = 10
        self.int_mod = 0

        self.wis_score = 10
        self.wis_increase = 0
        self.wis_spell_bonus = 0
        self.wis_item_bonus = 0
        self.wis_other_bonuses = 0
        self.wis_race_bonus = 0
        self.wis_sum = 10
        self.wis_mod = 0

        self.cha_score = 10
        self.cha_increase = 0
        self.cha_spell_bonus = 0
        self.cha_item_bonus = 0
        self.cha_other_bonuses = 0
        self.cha_race_bonus = 0
        self.cha_sum = 10
        self.cha_mod = 0

        self.acrobatics_sum = 0
        self.acrobatics_rank = 0
        self.acrobatics_misc_mod = 0
        self.appraise_sum = 0
        self.appraise_rank = 0
        self.appraise_misc_mod = 0
        self.bluff_sum = 0
        self.bluff_rank = 0
        self.bluff_misc_mod = 0
        self.climb_sum = 0
        self.climb_rank = 0
        self.climb_misc_mod = 0
        self.craft_sum = 0
        self.craft_rank = 0
        self.craft_misc_mod = 0
        self.diplomacy_sum = 0
        self.diplomacy_rank = 0
        self.diplomacy_misc_mod = 0
        self.disable_device_sum = 0
        self.disable_device_rank = 0
        self.disable_device_misc_mod = 0
        self.disguise_sum = 0
        self.disguise_rank = 0
        self.disguise_misc_mod = 0
        self.escape_artist_sum = 0
        self.escape_artist_rank = 0
        self.escape_artist_misc_mod = 0
        self.fly_sum = 0
        self.fly_rank = 0
        self.fly_misc_mod = 0
        self.handle_animal_sum = 0
        self.handle_animal_rank = 0
        self.handle_animal_misc_mod = 0
        self.heal_sum = 0
        self.heal_rank = 0
        self.heal_misc_mod = 0
        self.intimidate_sum = 0
        self.intimidate_rank = 0
        self.intimidate_misc_mod = 0
        self.knowledge_arcana_sum = 0
        self.knowledge_arcana_rank = 0
        self.knowledge_arcana_misc_mod = 0
        self.knowledge_dungeoneering_sum = 0
        self.knowledge_dungeoneering_rank = 0
        self.knowledge_dungeoneering_misc_mod = 0
        self.knowledge_engineering_sum = 0
        self.knowledge_engineering_rank = 0
        self.knowledge_engineering_misc_mod = 0
        self.knowledge_geography_sum = 0
        self.knowledge_geography_rank = 0
        self.knowledge_geography_misc_mod = 0
        self.knowledge_history_sum = 0
        self.knowledge_history_rank = 0
        self.knowledge_history_misc_mod = 0
        self.knowledge_local_sum = 0
        self.knowledge_local_rank = 0
        self.knowledge_local_misc_mod = 0
        self.knowledge_nature_sum = 0
        self.knowledge_nature_rank = 0
        self.knowledge_nature_misc_mod = 0
        self.knowledge_nobility_sum = 0
        self.knowledge_nobility_rank = 0
        self.knowledge_nobility_misc_mod = 0
        self.knowledge_planes_sum = 0
        self.knowledge_planes_rank = 0
        self.knowledge_planes_misc_mod = 0
        self.knowledge_religion_sum = 0
        self.knowledge_religion_rank = 0
        self.knowledge_religion_misc_mod = 0
        self.linguistics_sum = 0
        self.linguistics_rank = 0
        self.linguistics_misc_mod = 0
        self.perception_sum = 0
        self.perception_rank = 0
        self.perception_misc_mod = 0
        self.perform_sum = 0
        self.perform_rank = 0
        self.perform_misc_mod = 0
        self.profession_sum = 0
        self.profession_rank = 0
        self.profession_misc_mod = 0
        self.ride_sum = 0
        self.ride_rank = 0
        self.ride_misc_mod = 0
        self.sense_motive_sum = 0
        self.sense_motive_rank = 0
        self.sense_motive_misc_mod = 0
        self.sleight_of_hand_sum = 0
        self.sleight_of_hand_rank = 0
        self.sleight_of_hand_misc_mod = 0
        self.spellcraft_sum = 0
        self.spellcraft_rank = 0
        self.spellcraft_misc_mod = 0
        self.stealth_sum = 0
        self.stealth_rank = 0
        self.stealth_misc_mod = 0
        self.survival_sum = 0
        self.survival_rank = 0
        self.survival_misc_mod = 0
        self.swim_sum = 0
        self.swim_rank = 0
        self.swim_misc_mod = 0
        self.use_magic_device_sum = 0
        self.use_magic_device_rank = 0
        self.use_magic_device_misc_mod = 0

        self.spells_known_0 = 0
        self.spell_save_dc_0 = 0
        self.spells_per_day_0 = 0
        self.spells_known_1 = 0
        self.spell_save_dc_1 = 0
        self.spells_per_day_1 = 0
        self.spell_bonus_1 = 0
        self.spells_known_2 = 0
        self.spell_save_dc_2 = 0
        self.spells_per_day_2 = 0
        self.spell_bonus_2 = 0
        self.spells_known_3 = 0
        self.spell_save_dc_3 = 0
        self.spells_per_day_3 = 0
        self.spell_bonus_3 = 0
        self.spells_known_4 = 0
        self.spell_save_dc_4 = 0
        self.spells_per_day_4 = 0
        self.spell_bonus_4 = 0
        self.spells_known_5 = 0
        self.spell_save_dc_5 = 0
        self.spells_per_day_5 = 0
        self.spell_bonus_5 = 0
        self.spells_known_6 = 0
        self.spell_save_dc_6 = 0
        self.spells_per_day_6 = 0
        self.spell_bonus_6 = 0
        self.spells_known_7 = 0
        self.spell_save_dc_7 = 0
        self.spells_per_day_7 = 0
        self.spell_bonus_7 = 0
        self.spells_known_8 = 0
        self.spell_save_dc_8 = 0
        self.spells_per_day_8 = 0
        self.spell_bonus_8 = 0
        self.spells_known_9 = 0
        self.spell_save_dc_9 = 0
        self.spells_per_day_9 = 0
        self.spell_bonus_9 = 0

        self.gear_items = []
        self.head_list = []
        self.headband_list = []
        self.eyes_list = []
        self.shoulders_list = []
        self.neck_list = []
        self.chest_list = []
        self.body_list = []
        self.armor_list = []
        self.hand_list = []
        self.belt_list = []
        self.wrist_list = []
        self.hands_list = []
        self.ring_list = []
        self.feet_list = []
