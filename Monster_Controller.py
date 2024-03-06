import csv
import re

from Monster import Monster


def add_double_newline(input_str):
    pattern = re.compile(r'([A-Z][a-zA-Z\s]+)\s+(\(Ex\)|\(Su\)|\(Sp\))')
    result = pattern.sub(r'\n\n\1\2\n\n', input_str)
    return result


def analyze_number(input_value):
    try:
        number = int(input_value)
        if number > 0:
            result = f'+{number}'
            return result
        elif number < 0:
            result = f'-{abs(number)}'
            return result
        else:
            return '0'
    except ValueError:
        return None


class MonsterController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def load_data(self):
        # Loading CSV DataBase
        with open("DataBase/monster_bestiary_full - Updated 27Jul2015.csv", 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            cr_set = set()
            for row in csv_reader:
                monster = Monster(row)
                try:
                    cr_float = float(monster.cr)
                    cr_set.add(cr_float)
                    self.model.monster_list[monster.name] = monster
                except ValueError:
                    pass
            self.model.monster_cr_list = sorted(cr_set)
            self.model.monster_cr_list = [str(int(cr) if cr.is_integer() else cr) for cr in self.model.monster_cr_list]
        return self.model

    def update_listbox(self):
        selected_cr = self.view.monster_cr_combobox_var.get()
        filter_text = self.view.monster_entry_filter.get().lower()

        try:
            self.view.monster_list_box.delete(0, "end")
        except IndexError:
            pass

        # Filter the monsters based on the selected criteria and filter text
        filtered_monsters = self.filter_monsters(selected_cr)
        filtered_monsters = [monster for monster in filtered_monsters if filter_text in monster.name.lower()]

        # Populate the listbox with the filtered monsters
        for monster in filtered_monsters:
            self.view.monster_list_box.insert("end", monster.name)

    def filter_monsters(self, cr):
        filtered_monsters = []
        for monster in self.model.monster_list.values():
            if str(monster.cr) == cr:
                filtered_monsters.append(monster)
        return filtered_monsters

    def show_monster_data(self, selected_option):
        selected_monster = self.model.monster_list[selected_option]
        self.view.monster_name_var.set(value=selected_monster.name)
        self.view.monster_type_var.set(value=f"{selected_monster.alignment} {selected_monster.size} {selected_monster.type} {selected_monster.subtype}")
        self.view.monster_cr_var.set(value=f"CR: {selected_monster.cr}")
        self.view.monster_xp_var.set(value=f"XP: {selected_monster.xp}")
        self.view.monster_ability_scores_var.set(value=f"Ability Scores: {selected_monster.ability_scores}")
        self.view.monster_skills_var.set(value=f"Skills: {selected_monster.skills}")
        self.view.monster_feats_var.set(value=f"Feats: {selected_monster.feats}")
        self.view.monster_languages_var.set(value=f"Languages: {selected_monster.languages}")
        self.view.monster_environment_var.set(value=f"Environment: {selected_monster.environment}")
        self.view.monster_organization_var.set(value=f"Organization: {selected_monster.organization}")
        self.view.monster_treasure_var.set(value=f"Treasure: {selected_monster.treasure}")

        self.view.monster_senses_var.set(value=f"Senses: {selected_monster.senses}")
        self.view.monster_aura_var.set(value=f"Aura: {selected_monster.aura}")
        self.view.monster_defensive_abilities_var.set(value=f"Defensive Abilities: {selected_monster.defensive_abilities}")
        self.view.monster_sq_var.set(value=f"Special Qualities: {selected_monster.sq}")
        self.view.monster_special_abilities_var.set(value=add_double_newline(selected_monster.special_abilities))

        self.view.monster_init_var.set(value=f"Initiative: {analyze_number(selected_monster.init)}, Speed: {selected_monster.speed}")
        self.view.monster_ac_var.set(value=f"AC: {selected_monster.ac} {selected_monster.ac_mods}")
        self.view.monster_hp_var.set(value=f"HP: {selected_monster.hp} {selected_monster.hd} {selected_monster.hp_mods}")
        self.view.monster_saves_var.set(value=f"Saves: {selected_monster.saves} {selected_monster.save_mods}")
        self.view.monster_resistances_var.set(value=f"DR:{selected_monster.dr}, Immune:{selected_monster.immune}, Resist:{selected_monster.resist}, SR:{selected_monster.sr}, Weakness:{selected_monster.weaknesses}")
        self.view.monster_bab_var.set(value=f"BaB: {analyze_number(selected_monster.base_atk)}, CMB: {selected_monster.cmb}, CMD: {selected_monster.cmd}")
        self.view.monster_space_reach_var.set(value=f"Space/Reach: {selected_monster.space}/{selected_monster.reach}")
        self.view.monster_melee_var.set(value=f"Melee: {selected_monster.melee}")
        self.view.monster_ranged_var.set(value=f"Ranged: {selected_monster.ranged}")
        self.view.monster_special_attacks_var.set(value=f"Special Attacks: {selected_monster.special_attacks}")

        self.view.monster_spell_like_abilities_var.set(value=selected_monster.spell_like_abilities)
        self.view.monster_spells_known_var.set(value=selected_monster.spells_known)
        self.view.monster_spells_prepared_var.set(value=selected_monster.spells_prepared)
