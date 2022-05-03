import random
import math
import tkinter  as tk
import copy
from fpdf import FPDF


#lists & dictionaries, selected from & not to be edited
races = ["Deva", "Dragonborn", "Dwarf", "Eladrin", "Half-Elf", "Elf", "Halfling", "Tiefling", "Human", 
         "Gnome", "Goliath", "Half-Orc", "Shifter", "Githzerai", "Minotaur", "Shardmind", "Wilden"]
classes = ["Avenger", "Paladin", "Cleric", "Invoker", "Ardent", 
          "Fighter", "Warlord", "Ranger", "Rogue", 
          "Barbarian", "Druid", "Shaman", "Warden", "Bard", 
          "Warlock", "Wizard", "Sorcerer", 
          "Monk", "Battlemind", "Psion", "Runepriest", "Seeker"]
ability_scores = [16, 14, 13, 12, 11, 10]
defenses = { "AC" : 10,
            "Fortitude" : 10,
            "Reflex" : 10,
            "Will" : 10
    }
skills = {"Acrobatics" : [0, "Dex", False],
          "Arcana" : [0, "Int", False],
          "Athletics" : [0, "Str", False],
          "Bluff" : [0, "Cha", False],
          "Diplomacy" : [0, "Cha", False],
          "Dungeoneering" : [0, "Wis", False],
          "Endurance" : [0, "Const", False],
          "Heal" : [0, "Wis", False],
          "History" : [0, "Int", False],
          "Insight" : [0, "Wis", False],
          "Intimidate" : [0, "Cha", False],
          "Nature" : [0, "Wis", False],
          "Perception" : [0, "Wis", False],
          "Religion" : [0, "Int", False],
          "Stealth" : [0, "Dex", False],
          "Streetwise" : [0, "Cha", False],
          "Thievery" : [0, "Dex", False]
    }
languages = ["Common", "Deep Speech", "Draconic", "Dwarven", "Elven", "Giant", "Goblin", "Primordial", "Supernal", "Abyssal"]
simple_onehand = ["Club", "Dagger", "Javelin", "Mace", "Sickle", "Spear"]
simple_twohand = ["Greatclub", "Morningstar", "Quarterstaff", "Scythe"]
simple_range = ["Hand Crossbow", "Crossbow"]
mili_onehand = ["Battleaxe", "Flail", "Handaxe", "Longsword", "Scimitar", "Shortsword", "Throwing Hammer", "Warhammer", "War Pick"]
mili_twohand = ["Falchion", "Glaive", "Greataxe", "Greatsword", "Halberd", "Heavy Flail", "Longspear", "Maul"]
mili_range = ["Longbow", "Shortbow"]

#file management
dir = r"C:\Users\Yaoi Boy\source\repos\DnD_Character_Sheet"

#creates header for PDF file
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(90)
        self.cell(0,0, "4th Edition - Character Sheet", 1, 0, 'C')
        self.ln(10)

def generateSheet(name):
    #allocation
    #name, race, class
    char_name = name
    char_race = random.choice(races)
    char_class = random.choice(classes)

    stat_mods = {}
    languages_known = []
    speed = 0
    maxHP = 0
    bloodied_value = 0
    surge_value = 0
    surge_day = 0
    weapon_list = []
    weapon_group = []
    armor_list = []
    implement_list = []
    weapon = ""
    armor = ""
    #implement/off-hand
    other = ""

    #create deep copies for lists & dictionaries
    character_abilties = copy.deepcopy(ability_scores)
    character_defenses = copy.deepcopy(defenses)
    character_skills = copy.deepcopy(skills)


    stats = { 
        "Str" : character_abilties.pop(random.randrange(0, len(character_abilties))),
        "Const" : character_abilties.pop(random.randrange(0, len(character_abilties))),
        "Dex" : character_abilties.pop(random.randrange(0, len(character_abilties))),
        "Int" : character_abilties.pop(random.randrange(0, len(character_abilties))),
        "Wis" : character_abilties.pop(random.randrange(0, len(character_abilties))),
        "Cha" : character_abilties.pop(random.randrange(0, len(character_abilties))),
    }

    #racial bonuses
    #TODO: add racial Feats & racial powers
    if char_race == "Deva":
            stats["Int"] += 2
            stats["Wis"] += 2   
            character_skills["History"][0] += 2
            character_skills["Religion"][0] += 2
            languages_known = ["Common", languages.pop(random.randrange(len(languages[1:]))), languages.pop(random.randrange(len(languages[1:])))]
            speed = 6
    elif char_race == "Dragonborn":
            stats["Str"] += 2
            stats["Cha"] += 2
            character_skills["History"][0] += 2
            character_skills["Intimidate"][0] += 2
            languages_known = ["Common", "Draconic"]
            speed = 6
    elif char_race == "Dwarf":
            stats["Const"] += 2
            stats["Wis"] += 2
            character_skills["Dungeoneering"][0] += 2
            character_skills["Endurance"][0] += 2
            languages_known = ["Common", "Dwarven"]
            speed = 6
    elif char_race == "Eladrin":
            stats["Dex"] += 2
            stats["Int"] += 2
            character_skills["Arcana"][0] += 2
            character_skills["History"][0] += 2
            languages_known = ["Common", "Elven"]
            speed = 6
    elif char_race == "Half-Elf":
        stats["Const"] += 2
        stats["Cha"] += 2
        character_skills["History"][0] += 2
        character_skills["Religion"][0] += 2
        sub_language = ["Deep Speech", "Draconic", "Dwarven", "Giant", "Goblin", "Primordial", "Supernal", "Abyssal"]
        languages_known = ["Common", "Elven", random.choice(sub_language)]
        speed = 6
    elif char_race == "Elf":
        stats["Dex"] += 2
        stats["Wis"] += 2
        character_skills["Nature"][0] += 2
        character_skills["Perception"][0] += 2
        languages_known = ["Common", "Elven"]
        speed = 6
    elif char_race == "Halfling":
        stats["Dex"] += 2
        stats["Cha"] += 2
        character_skills["Acrobatics"][0] += 2
        character_skills["Thievery"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Tiefling":
        stats["Int"] += 2
        stats["Cha"] += 2
        character_skills["Bluff"][0] += 2
        character_skills["Stealth"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Human":
        stats[random.choice(list(stats.keys()))] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Gnome":
        stats["Int"] += 2
        stats["Cha"] += 2
        character_skills["Arcana"][0] += 2
        character_skills["Stealth"][0] += 2
        languages_known = ["Common", "Elven"]
        speed = 5
    elif char_race == "Goliath":
        stats["Str"] += 2
        stats["Const"] += 2
        character_skills["Athletics"][0] += 2
        character_skills["Nature"][0] += 2
        sub_language = ["Dwarven", "Giant"]
        languages_known = ["Common", random.choice(sub_language)]
        speed = 6
    elif char_race == "Half-Orc":
        stats["Str"] += 2
        stats["Dex"] += 2
        character_skills["Endurance"][0] += 2
        character_skills["Intimidate"][0] += 2
        languages_known = ["Common", "Giant"]
        speed = 6
    elif char_race == "Shifter":
        stats["Str"] += 2
        stats["Wis"] += 2
        character_skills["Athletics"][0] += 2
        character_skills["Endurance"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Githzerai":
        stats["Wis"] += 2
        substat = ["Int", "Dex"]
        stats[random.choice(substat)] += 2
        character_skills["Acrobatics"][0] += 2
        character_skills["Athletics"][0] += 2
        languages_known = ["Common", "Deep Speech"]
        speed = 6
    elif char_race == "Minotaur":
        stats["Str"] += 2
        substat = ["Const", "Wis"]
        stats[random.choice(substat)] += 2
        character_skills["Nature"][0] += 2
        character_skills["Perception"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Shardmind":
        stats["Int"] += 2
        substat = ["Wis", "Cha"]
        stats[random.choice(substat)] += 2
        character_skills["Arcana"][0] += 2
        character_skills["Endurance"][0] += 2
        character_skills[random.choice(list(character_skills.keys()))][0] += 2
        languages_known = ["Common", "Deep Speech", languages[2:].pop(random.randrange(len(languages[2:])))]
        speed = 6
    elif char_race == "Wilden":
        stats["Wis"] += 2
        substat = ["Const", "Dex"]
        stats[random.choice(substat)] += 2
        character_skills["Nature"][0] += 2
        character_skills["Stealth"][0] += 2
        languages_known = ["Common", "Elven"]
        speed = 6


    #generate Abilities Modifiers
    #get ability mod from stat number, input is a String
    def mod_getter(stat):
        ability = stats.get(stat)
        ability_mod = stat + ".mod"
        if ability == 10 or ability == 11:
            stat_mods[ability_mod] = 0
        elif ability == 12 or ability == 13:
            stat_mods[ability_mod] = 1
        elif ability == 14 or ability == 15:
            stat_mods[ability_mod] = 2
        elif ability == 16 or ability == 17:
            stat_mods[ability_mod] = 3
        elif ability == 18 or ability == 19:
            stat_mods[ability_mod] = 4
    for x in stats:
        mod_getter(x)

    #class bonuses
    #TODO: add class feat option
    if char_class == "Avenger":
            character_skills["Religion"][2] = True
            available_skills = ["Acrobatics", "Athletics", "Endurance", "Heal", "Intimidate", "Perception", "Stealth", "Streetwise"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 1
            character_defenses["Reflex"] += 1
            character_defenses["Will"] += 1
            maxHP = 7 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 10 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, mili_onehand, mili_twohand, simple_range]
            weapon_list = random.choice(weapon_group)    
            weapon = random.choice(weapon_list)
            armor = "Cloth"    
            other = "Holy Symbol"
    elif char_class == "Paladin":
            character_skills["Religion"][2] = True
            available_skills = ["Diplomacy", "Endurance", "Heal", "History", "Insight", "Intimidate"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 1
            character_defenses["Reflex"] += 1
            character_defenses["Will"] += 1
            maxHP = 15 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 10 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, mili_onehand, mili_twohand, simple_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide", "Chainmail", "Scale", "Plate"]
            shield_list = ["Light Shield", "Heavy Shield"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            if simple_onehand == weapon_list or mili_onehand == weapon_list:
                other = ["Holy Symbol", random.choice(shield_list)]        
            else: 
                other = "Holy Symbol"
    elif char_class == "Cleric":
            character_skills["Religion"][2] = True
            available_skills = ["Arcana", "Diplomacy", "Heal", "History", "Insight"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Will"] += 2
            maxHP = 12 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 7 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, simple_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide", "Chainmail"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            other = "Holy Symbol"
    elif char_class == "Invoker":
            character_skills["Religion"][2] = True
            available_skills = ["Arcana", "Diplomacy", "Endurance", "History", "Insight", "Intimidate"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 1
            character_defenses["Reflex"] += 1
            character_defenses["Will"] += 1
            maxHP = 10 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 6 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, simple_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide", "Chainmail"]
            implement_list = ["Rod", "Staff"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            other = random.choice(implement_list)
    elif char_class == "Ardent":
            available_skills = ["Arcana", "Athletics", "Bluff", "Diplomacy", "Endurance", "Heal", "Insight", "Intimidate", "Streetwise"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 1
            character_defenses["Will"] += 1
            maxHP = 12 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 7 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, mili_onehand, mili_twohand, simple_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide", "Chainmail"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            other = ""
    elif char_class == "Fighter":
            available_skills = ["Athletics", "Endurance", "Heal", "Intimidate", "Streetwise"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 2
            maxHP = 15 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 9 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, mili_onehand, mili_twohand, simple_range, mili_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide", "Chainmail", "Scale"]
            shield_list = ["Light Shield", "Heavy Shield"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            if simple_onehand == weapon_list or mili_onehand == weapon_list:
                other = random.choice(shield_list)
            else: 
                other = ""
    elif char_class == "Warlord":
            available_skills = ["Athletics", "Diplomacy", "Endurance", "Heal", "History", "Intimidate"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 1
            character_defenses["Will"] += 1
            maxHP = 12 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 7 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, mili_onehand, mili_twohand, simple_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide", "Chainmail"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)    
            if simple_onehand == weapon_list or mili_onehand == weapon_list:
                other = "Light Shield"
            else: 
                other = ""
    elif char_class == "Ranger":
            main_skills = ["Dungeoneering", "Nature"]
            available_skills = ["Acrobatics", "Athletics", "Endurance", "Heal", "Perception", "Stealth"]
            sub_skills = [random.choice(main_skills), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 1
            character_defenses["Reflex"] += 1
            maxHP = 12 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 6 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_twohand, mili_onehand, mili_twohand, simple_range, mili_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            other = ""
    elif char_class == "Rogue":
            character_skills["Stealth"][2] = True
            character_skills["Thievery"][2] = True
            available_skills = ["Acrobatics", "Athletics", "Bluff", "Dungeoneering", "Insight", "Intimidate", "Perception", "Streetwise"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Reflex"] += 2
            maxHP = 12 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 6 + stat_mods["Const.mod"] 
            weapon_list = ["Dagger", "Hand Crossbow", "Shuriken", "Sling", "Shortsword"]
            armor_list = ["Cloth", "Leather"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            other = ""
    elif char_class == "Barbarian":
            available_skills = ["Acrobatics", "Athletics", "Endurance", "Heal", "Intimidate", "Nature", "Perception"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 2
            maxHP = 15 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 8 + stat_mods["Const.mod"] 
            weapon_group = [simple_twohand, mili_twohand]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            other = ""
    elif char_class == "Druid":
            character_skills["Nature"][2] = True
            available_skills = ["Arcana", "Athletics", "Diplomacy", "Endurance", "Heal", "History", "Insight", "Perception"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Reflex"] += 1
            character_defenses["Will"] += 1
            maxHP = 12 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 7 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, simple_range]
            weapon_list = random.choice(weapon_group)
            armor_list = ["Cloth", "Leather", "Hide"]
            implement_list = ["Staff", "Totem"]
            weapon = random.choice(weapon_list)
            armor = random.choice(armor_list)
            other = random.choice(implement_list)
    elif char_class == "Shaman":
            character_skills["Nature"][2] = True
            available_skills = ["Arcana", "Athletics", "Endurance", "Heal", "History", "Insight", "Perception", "Religion"]
            sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
            for x in sub_skills:
                character_skills[x][2] = True
            character_defenses["Fortitude"] += 1
            character_defenses["Will"] += 1
            maxHP = 12 + stats["Const"]
            bloodied_value = math.floor(maxHP/2)
            surge_value = math.floor(bloodied_value/2)
            surge_day = 7 + stat_mods["Const.mod"] 
            weapon_group = [simple_onehand, "Longspear"]
            if weapon_group == simple_onehand:
                weapon_list = random.choice(weapon_group) 
                weapon = random.choice(weapon_list)
            else: 
                weapon = "Longspear"    
            armor_list = ["Cloth", "Leather"]   
            armor = random.choice(armor_list)
            other = "Totem"
    elif char_class == "Warden":
           character_skills["Nature"][2] = True
           available_skills = ["Athletics", "Dungeoneering", "Endurance", "Heal", "Intimidate", "Perception"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Fortitude"] += 1
           character_defenses["Will"] += 1
           maxHP = 17 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 9 + stat_mods["Const.mod"] 
           weapon_group = [simple_onehand, mili_onehand]
           weapon_list = random.choice(weapon_group)
           armor_list = ["Cloth", "Leather", "Hide"]
           shield_list = ["Light Shield", "Heavy Shield"]
           weapon = random.choice(weapon_list)
           armor = random.choice(armor_list)
           other = random.choice(shield_list)
    elif char_class == "Bard":
           character_skills["Arcana"][2] = True
           available_skills = ["Acrobatics", "Athletics", "Bluff", "Diplomacy", "Dungeoneering", "Heal", "History", "Insight", "Intimidation", "Nature", "Perception", "Religion", "Streetwise"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Reflex"] += 1
           character_defenses["Will"] += 1
           maxHP = 12 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 7 + stat_mods["Const.mod"]     
           weapon_group = [simple_onehand, "Longsword", "Scimitar", "Shortsword", simple_range, mili_range]
           weapon_list = random.choice(weapon_group)
           armor_list = ["Cloth", "Leather", "Hide", "Chainmail"]
           shield_list = "Light Shield"
           implement_list = "Wand"
           weapon = random.choice(weapon_list)
           armor = random.choice(armor_list)
           if simple_range == weapon_list or mili_range == weapon_list:
               other = implement_list
           else:
               other = [implement_list, shield_list]
    elif char_class == "Warlock":
           available_skills = ["Arcana", "Bluff", "History", "Insight", "Intimidate", "Religion", "Streetwise", "Thievery"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Reflex"] += 1
           character_defenses["Will"] += 1
           maxHP = 12 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 6 + stat_mods["Const.mod"]     
           weapon_list = simple_onehand
           armor_list = ["Cloth", "Leather"]
           weapon = random.choice(weapon_list)
           armor = random.choice(armor_list)
           implement_list = ["Rod", "Wand"]
           other = random.choice(implement_list)
    elif char_class == "Wizard":
           character_skills["Arcana"][2] = True
           available_skills = ["Diplomacy", "Dungeoneering", "History", "Insight", "Nature", "Religion"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Will"] += 2
           maxHP = 10 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 6 + stat_mods["Const.mod"] 
           weapon_list = ["Dagger", "Quarterstaff"]
           weapon = random.choice(weapon_list)
           armor = "Cloth"
           implement_list = ["Orb", "Staff", "Wand"]
           other = random.choice(implement_list)
    elif char_class == "Sorcerer":
           character_skills["Arcana"][2] = True
           available_skills = ["Athletics", "Bluff", "Diplomacy", "Dungeoneering", "Endurance", "History", "Insight", "Intimidate", "Nature"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Will"] += 2
           maxHP = 12 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 6 + stat_mods["Const.mod"] 
           weapon_group = [simple_onehand, simple_range]
           weapon_list = random.choice(weapon_group)
           implement_list = ["Dagger", "Staff"]
           weapon = random.choice(weapon_list)
           armor = "Cloth"
           other = random.choice(implement_list)
    elif char_class == "Monk":
           available_skills = ["Acrobatics", "Athletics", "Diplomacy", "Endurance", "Heal", "Insight", "Perception", "Religion", "Stealth", "Thievery"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Fortitude"] += 1
           character_defenses["Reflex"] += 1
           character_defenses["Will"] += 1
           maxHP = 12 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 7 + stat_mods["Const.mod"] 
           weapon_list = ["Club", "Dagger", "Unarmed", "Quarterstaff", "Shuriken", "Sling", "Spear"]
           weapon = random.choice(weapon_list)
           armor = "Cloth"
           other = "Ki Focus"
    elif char_class == "Battlemind":    
           available_skills = ["Arcana", "Athletics", "Bluff", "Diplomacy", "Endurance", "Heal", "Insight", "Intimidate"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Will"] += 2
           maxHP = 15 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 9 + stat_mods["Const.mod"] 
           weapon_group = [simple_onehand, simple_twohand, mili_onehand, mili_twohand, simple_range]
           weapon_list = random.choice(weapon_group)
           armor_list = ["Cloth", "Leather", "Hide", "Chainmail", "Scale"]
           shield_list = ["Light Shield", "Heavy Shield"]
           weapon = random.choice(weapon_list)
           armor = random.choice(armor_list)
           if simple_onehand == weapon_list or mili_onehand == weapon_list:
               other = random.choice(shield_list)
           else: 
               other = ""
    elif char_class == "Psion":
           available_skills = ["Arcana", "Bluff", "Diplomacy", "Dungeoneering", "History", "Insight", "Intimidate", "Perception"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Will"] += 2
           maxHP = 12 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 6 + stat_mods["Const.mod"] 
           weapon_group = [simple_onehand, simple_range]
           weapon_list = random.choice(weapon_group)
           implement_list = ["Orb", "Staff"]
           weapon = random.choice(weapon_list)
           armor = "Cloth"
           other = random.choice(implement_list)
    elif char_class == "Runepriest":
           character_skills["Religion"][2] = True
           available_skills = ["Arcana", "Athletics", "Endurance", "Heal", "History", "Insight", "Thievery"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True
           character_defenses["Will"] += 2
           maxHP = 12 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 7 + stat_mods["Const.mod"] 
           weapon_group = [simple_onehand, simple_twohand, simple_range]
           weapon_list = random.choice(weapon_group)
           armor_list = ["Cloth", "Leather", "Hide", "Chainmail", "Scale"]    
           weapon = random.choice(weapon_list)
           armor = random.choice(armor_list)
           if simple_onehand == weapon_list:
               other = "Light Shield"
           else: 
               other = ""
    elif char_class == "Seeker":
           character_skills["Nature"][2] = True
           available_skills = ["Acrobatics", "Athletics", "Endurance", "Heal", "Insight", "Intimidate", "Perception", "Stealth"]
           sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
           for x in sub_skills:
               character_skills[x][2] = True    
           character_defenses["Reflex"] += 1
           character_defenses["Will"] += 1
           maxHP = 12 + stats["Const"]
           bloodied_value = math.floor(maxHP/2)
           surge_value = math.floor(bloodied_value/2)
           surge_day = 7 + stat_mods["Const.mod"] 
           weapon_group = [simple_onehand, simple_twohand, simple_range, mili_range]
           weapon_list = random.choice(weapon_group)
           armor_list = ["Cloth", "Leather"]
           weapon = random.choice(weapon_list)
           armor = random.choice(armor_list)
           other = ""

    #generates Defense Values
    #alters defenses according to armor types, other benefits, and mods
    #-armors
    if armor == "Cloth":
        character_defenses["AC"] += max(stat_mods["Dex.mod"], stat_mods["Int.mod"])
    elif armor == "Leather":
        character_defenses["AC"] += 3 + max(stat_mods["Dex.mod"], stat_mods["Int.mod"])
    elif armor == "Hide":
        character_defenses["AC"] += 4 
    elif armor == "Chainmail":
        character_defenses["AC"] += 5 
    elif armor == "Scale":
        character_defenses["AC"] += 6 
        speed -= 1
        for x in character_skills:
            if character_skills[x][1] == "Dex" or character_skills[x][1] == "Str":
                character_skills[x][0] -= 1
    elif armor == "Plate":
        character_defenses["AC"] += 8
        speed -= 2
        for x in character_skills:
            if character_skills[x][1] == "Dex" or character_skills[x][1] == "Str":
                character_skills[x][0] -= 1
    #-shields
    if "Light Shield" in other and any("onehand" in x for x in weapon_list):
        character_defenses["AC"] += 2
    elif "Heavy Shield" in other and any("onehand" in x for x in weapon_list):
        character_defenses["AC"] += 3
        speed -= 1
    #-other defenses
    character_defenses["Fortitude"] += max(stat_mods["Str.mod"], stat_mods["Const.mod"])
    character_defenses["Reflex"] += max(stat_mods["Dex.mod"], stat_mods["Int.mod"])
    character_defenses["Will"] += max(stat_mods["Wis.mod"], stat_mods["Cha.mod"])

    #generate Skill Bonuses
    #skill mod setter, input is a String - the name of the Skill
    def mod_skills(skill):
        if character_skills[skill][2] == True:
            character_skills[skill][0] += 5
        if character_skills[skill][1] == "Str":
            character_skills[skill][0] += stat_mods["Str.mod"]
        elif character_skills[skill][1] == "Const":
            character_skills[skill][0] += stat_mods["Const.mod"]
        elif character_skills[skill][1] == "Dex":
            character_skills[skill][0] += stat_mods["Dex.mod"]
        elif character_skills[skill][1] == "Int":
            character_skills[skill][0] += stat_mods["Int.mod"]
        elif character_skills[skill][1] == "Wis":
            character_skills[skill][0] += stat_mods["Wis.mod"]
        elif character_skills[skill][1] == "Cha":
            character_skills[skill][0] += stat_mods["Cha.mod"]
    for x in character_skills:
        mod_skills(x)

    #OUTPUT optmization
    str_character_abilities = ""
    for x in stats:
        str_character_abilities += " - " + x + ": " + str(stats[x]) + "\n"
    str_character_modifiers = ""
    for x in stat_mods:
        str_character_modifiers += " - " + x + ": +" + str(stat_mods[x]) + "\n"
    str_character_defenses = ""
    for x in character_defenses:
        str_character_defenses += " - " + x + ": " + str(character_defenses[x]) + "\n"
    str_character_skills = ""
    for x in character_skills:
        str_character_skills += " - " + x + ": " + str(character_skills[x]) + "\n"

    sheetOutput = str(
        "Basic Information------------------------------------------\n" +
        "  -  " + char_name + "  -  " + char_race + "  -  " + char_class + "\n" +
        " Speed : " + str(speed) + "\n"  +
        "Ability Scores----------------------------------------------\n" +
        str_character_abilities +
        "Ability Modifiers--------------------\n" +
        str_character_modifiers +
        "Defenses----------------------------------------------------\n" +
        str_character_defenses +
        "Health------------------------------------------------------\n" +
        " Max HP : " + str(maxHP) + "\n" +
        " Bloodied value : " + str(bloodied_value) + "\n" +
        " Surge value : " + str(surge_value) + "\n" +
        " Surges per day : " + str(surge_day) + "\n" +
        "Skills------------------------------------------------------\n" +
        str_character_skills +
        "Languages---------------------------------------------------\n" +
        " " + str(languages_known) + "\n" +
        "Items---------------------------------------------------------\n" +
        " - " + weapon + "\n" + " - " + armor + "\n" + " - " + other + "\n" +
        "-----------------------------------------------------------------"
        )
    return sheetOutput
    
#TODO: create a GUI

#TODO: add a main menu => choose [Random] (|| Checkmarks => Java project] )
#Random => single button + name => full character sheet
#Checkmarks/Slots => Checkmarks the things you want => full character sheet

def generateMainMenu():

    main = tk.Tk()
    main.geometry("500x100")
    main.title("Dungeons & Dragons 4th Edition - Character Sheet Creator")

    def generateRandomSheet():
               
        root = tk.Tk()
        root.geometry("800x930")
        root.title("Dungeons & Dragons 4th Edition - Randomized Creator")
        prompt = tk.Label(root, text = "Name your Fantasy Dungeons & Dragons character: ")    
        input = tk.Entry(root, state = "normal")
        output = tk.Label(root, state = "disabled")
        displayButton = tk.Button(root, text = "Generate Character", command = lambda:[Take_Input(), disableState(), enableSave()])
        #blocked until generate/displaybutton is not clicked
        saveButton = tk.Button(root, text = "Save as PDF", state = "disabled", command = lambda:generatePDF())
        #reset button, that resets all variables, buttons, and input
        resetButton = tk.Button(root, text = "Reset", command = lambda:[enableState(), reset_Option()])        
        exitButton = tk.Button(root, text = "Cancel", command = root.quit)          

        #blocks Input & generateButton after first use.
        def disableState():
            if (input['state'] == "normal" and displayButton['state'] == "normal"):
                input['state'] = "disabled"
                displayButton['state'] = "disabled"

        #enables Save button/option after character is generated
        def enableSave():
            if (saveButton['state'] == "disabled"):
                saveButton['state'] = "normal"

        #reenable Input & generateButton 
        def enableState():
            if (input['state'] == "disabled" and displayButton['state'] == "disabled"):
                input['state'] = "normal"
                displayButton['state'] = "normal"

        #takes name input
        def Take_Input():
            name = input.get()
            print(name)
            sheetOutput = generateSheet(name)
            output.config(text=sheetOutput) 

        #reset
        def reset_Option():
            input.delete(0, tk.END)
            output.configure(text = "")

        #create PDF for saveButton
        #ideally copy an actual DnD sheet & and inserts generateSheet() output into the file, matching the slots
        def generatePDF():
            name = input.get()
            sheetOutput = generateSheet(name)

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Times", '', size = 10)
            pdf.multi_cell(0, 10, txt = sheetOutput)
            pdf.output(name + "-Character Sheet.pdf")

        
        prompt.pack()
        input.pack()
        output.pack()
        displayButton.pack()
        saveButton.pack()
        resetButton.pack()
        exitButton.pack()
        root.mainloop()

    mainLabel = tk.Label(main, text = "Choose to have a randomly generated Dungeons & Dragons character.\n You can also save the character sheet as a PDF.")
    randomButton = tk.Button(main, text = "Randomize Character", command = lambda:generateRandomSheet())
    exitMainButton = tk.Button(main, text = "Exit", command = main.destroy)
    creatorLabel = tk.Label(main, text = "Created by Duc Huy Bui")

    mainLabel.pack()
    randomButton.pack()
    exitMainButton.pack()
    creatorLabel.pack( side = "right")
    main.mainloop()



def main():
    generateMainMenu()

if __name__ == '__main__':
    main()