import random
import math
import tkinter  as tk


#arrays
races = ["Deva", "Dragonborn", "Dwarf", "Eladrin", "Half-Elf", "Elf", "Halfling", "Tiefling", "Human", 
         "Gnome", "Goliath", "Half-Orc", "Shifter", "Githzerai", "Minotaur", "Shardmind", "Wilden"]
classes = ["Avenger", "Paladin", "Cleric", "Invoker", "Ardent", 
          "Fighter", "Warlord", "Ranger", "Rogue", 
          "Barbarian", "Druid", "Shaman", "Warden", "Bard", 
          "Warlock", "Wizard", "Sorcerer", 
          "Monk", "Battlemind", "Psion", "Runepriest", "Seeker"]
ability_scores = [16, 14, 13, 12, 11, 10]
stat_mods = {}
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
languages_known = []
speed = 0
maxHP = 0
bloodied_value = 0
surge_value = 0
surge_day = 0
weapon_list = []
weapon_group = []
simple_onehand = ["Club", "Dagger", "Javelin", "Mace", "Sickle", "Spear"]
simple_twohand = ["Greatclub", "Morningstar", "Quarterstaff", "Scythe"]
simple_range = ["Hand Crossbow", "Crossbow"]
mili_onehand = ["Battleaxe", "Flail", "Handaxe", "Longsword", "Scimitar", "Shortsword", "Throwing Hammer", "Warhammer", "War Pick"]
mili_twohand = ["Falchion", "Glaive", "Greataxe", "Greatsword", "Halberd", "Heavy Flail", "Longspear", "Maul"]
mili_range = ["Longbow", "Shortbow"]
armor_list = []
implement_list = []
weapon = ""
armor = ""
#implement/off-hand
other = ""

def generateSheet(name):
    #allocation
    char_name = name
    char_race = random.choice(races)
    char_class = random.choice(classes)
    stats = { 
            "Str" : ability_scores.pop(random.randrange(len(ability_scores))),
            "Const" : ability_scores.pop(random.randrange(len(ability_scores))),
            "Dex" : ability_scores.pop(random.randrange(len(ability_scores))),
            "Int" : ability_scores.pop(random.randrange(len(ability_scores))),
            "Wis" : ability_scores.pop(random.randrange(len(ability_scores))),
            "Cha" : ability_scores.pop(random.randrange(len(ability_scores))),
        }#unknown empty range randrange() error

    #racial bonuses
    #TODO: add racial Feats & racial powers
    if char_race == "Deva":
        stats["Int"] += 2
        stats["Wis"] += 2   
        skills["History"][0] += 2
        skills["Religion"][0] += 2
        languages_known = ["Common", languages.pop(random.randrange(len(languages[1:]))), languages.pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Dragonborn":
        stats["Str"] += 2
        stats["Cha"] += 2
        skills["History"][0] += 2
        skills["Intimidate"][0] += 2
        languages_known = ["Common", "Draconic"]
        speed = 6
    elif char_race == "Dwarf":
        stats["Const"] += 2
        stats["Wis"] += 2
        skills["Dungeoneering"][0] += 2
        skills["Endurance"][0] += 2
        languages_known = ["Common", "Dwarven"]
        speed = 6
    elif char_race == "Eladrin":
        stats["Dex"] += 2
        stats["Int"] += 2
        skills["Arcana"][0] += 2
        skills["History"][0] += 2
        languages_known = ["Common", "Elven"]
        speed = 6
    elif char_race == "Half-Elf":
        stats["Const"] += 2
        stats["Cha"] += 2
        skills["History"][0] += 2
        skills["Religion"][0] += 2
        sub_language = ["Deep Speech", "Draconic", "Dwarven", "Giant", "Goblin", "Primordial", "Supernal", "Abyssal"]
        languages_known = ["Common", "Elven", random.choice(sub_language)]
        speed = 6
    elif char_race == "Elf":
        stats["Dex"] += 2
        stats["Wis"] += 2
        skills["Nature"][0] += 2
        skills["Perception"][0] += 2
        languages_known = ["Common", "Elven"]
        speed = 6
    elif char_race == "Halfling":
        stats["Dex"] += 2
        stats["Cha"] += 2
        skills["Acrobatics"][0] += 2
        skills["Thievery"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Tiefling":
        stats["Int"] += 2
        stats["Cha"] += 2
        skills["Bluff"][0] += 2
        skills["Stealth"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Human":
        stats[random.choice(list(stats.keys()))] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Gnome":
        stats["Int"] += 2
        stats["Cha"] += 2
        skills["Arcana"][0] += 2
        skills["Stealth"][0] += 2
        languages_known = ["Common", "Elven"]
        speed = 5
    elif char_race == "Goliath":
        stats["Str"] += 2
        stats["Const"] += 2
        skills["Athletics"][0] += 2
        skills["Nature"][0] += 2
        sub_language = ["Dwarven", "Giant"]
        languages_known = ["Common", random.choice(sub_language)]
        speed = 6
    elif char_race == "Half-Orc":
        stats["Str"] += 2
        stats["Dex"] += 2
        skills["Endurance"][0] += 2
        skills["Intimidate"][0] += 2
        languages_known = ["Common", "Giant"]
        speed = 6
    elif char_race == "Shifter":
        stats["Str"] += 2
        stats["Wis"] += 2
        skills["Athletics"][0] += 2
        skills["Endurance"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Githzerai":
        stats["Wis"] += 2
        substat = ["Int", "Dex"]
        stats[random.choice(substat)] += 2
        skills["Acrobatics"][0] += 2
        skills["Athletics"][0] += 2
        languages_known = ["Common", "Deep Speech"]
        speed = 6
    elif char_race == "Minotaur":
        stats["Str"] += 2
        substat = ["Const", "Wis"]
        stats[random.choice(substat)] += 2
        skills["Nature"][0] += 2
        skills["Perception"][0] += 2
        languages_known = ["Common", languages[1:].pop(random.randrange(len(languages[1:])))]
        speed = 6
    elif char_race == "Shardmind":
        stats["Int"] += 2
        substat = ["Wis", "Cha"]
        stats[random.choice(substat)] += 2
        skills["Arcana"][0] += 2
        skills["Endurance"][0] += 2
        skills[random.choice(list(skills.keys()))][0] += 2
        languages_known = ["Common", "Deep Speech", languages[2:].pop(random.randrange(len(languages[2:])))]
        speed = 6
    elif char_race == "Wilden":
        stats["Wis"] += 2
        substat = ["Const", "Dex"]
        stats[random.choice(substat)] += 2
        skills["Nature"][0] += 2
        skills["Stealth"][0] += 2
        languages_known = ["Common", "Elven"]
        speed = 6

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
        skills["Religion"][2] = True
        available_skills = ["Acrobatics", "Athletics", "Endurance", "Heal", "Intimidate", "Perception", "Stealth", "Streetwise"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
        skills["Religion"][2] = True
        available_skills = ["Diplomacy", "Endurance", "Heal", "History", "Insight", "Intimidate"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
        skills["Religion"][2] = True
        available_skills = ["Arcana", "Diplomacy", "Heal", "History", "Insight"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Will"] += 2
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
        skills["Religion"][2] = True
        available_skills = ["Arcana", "Diplomacy", "Endurance", "History", "Insight", "Intimidate"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Will"] += 1
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
            skills[x][2] = True
        defenses["Fortitude"] += 2
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
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Will"] += 1
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
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Reflex"] += 1
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
        skills["Stealth"][2] = True
        skills["Thievery"][2] = True
        available_skills = ["Acrobatics", "Athletics", "Bluff", "Dungeoneering", "Insight", "Intimidate", "Perception", "Streetwise"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Reflex"] += 2
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
            skills[x][2] = True
        defenses["Fortitude"] += 2
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
        skills["Nature"][2] = True
        available_skills = ["Arcana", "Athletics", "Diplomacy", "Endurance", "Heal", "History", "Insight", "Perception"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
        skills["Nature"][2] = True
        available_skills = ["Arcana", "Athletics", "Endurance", "Heal", "History", "Insight", "Perception", "Religion"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Will"] += 1
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
        skills["Nature"][2] = True
        available_skills = ["Athletics", "Dungeoneering", "Endurance", "Heal", "Intimidate", "Perception"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Will"] += 1
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
        skills["Arcana"][2] = True
        available_skills = ["Acrobatics", "Athletics", "Bluff", "Diplomacy", "Dungeoneering", "Heal", "History", "Insight", "Intimidation", "Nature", "Perception", "Religion", "Streetwise"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
            skills[x][2] = True
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
        skills["Arcana"][2] = True
        available_skills = ["Diplomacy", "Dungeoneering", "History", "Insight", "Nature", "Religion"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Will"] += 2
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
        skills["Arcana"][2] = True
        available_skills = ["Athletics", "Bluff", "Diplomacy", "Dungeoneering", "Endurance", "History", "Insight", "Intimidate", "Nature"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Will"] += 2
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
            skills[x][2] = True
        defenses["Fortitude"] += 1
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
            skills[x][2] = True
        defenses["Will"] += 2
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
            skills[x][2] = True
        defenses["Will"] += 2
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
        skills["Religion"][2] = True
        available_skills = ["Arcana", "Athletics", "Endurance", "Heal", "History", "Insight", "Thievery"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True
        defenses["Will"] += 2
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
        skills["Nature"][2] = True
        available_skills = ["Acrobatics", "Athletics", "Endurance", "Heal", "Insight", "Intimidate", "Perception", "Stealth"]
        sub_skills = [available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills))), available_skills.pop(random.randrange(len(available_skills)))]
        for x in sub_skills:
            skills[x][2] = True    
        defenses["Reflex"] += 1
        defenses["Will"] += 1
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
    
    #alters defenses according to armor types, other benefits, and mods
    if armor == "Cloth":
        defenses["AC"] += max(stat_mods["Dex.mod"], stat_mods["Int.mod"])
    elif armor == "Leather":
        defenses["AC"] += 3 + max(stat_mods["Dex.mod"], stat_mods["Int.mod"])
    elif armor == "Hide":
        defenses["AC"] += 4 
    elif armor == "Chainmail":
        defenses["AC"] += 5 
    elif armor == "Scale":
        defenses["AC"] += 6 
        speed -= 1
        for x in skills:
            if skills[x][1] == "Dex" or skills[x][1] == "Str":
                skills[x][0] -= 1
    elif armor == "Plate":
        defenses["AC"] += 8
        speed -= 2
        for x in skills:
            if skills[x][1] == "Dex" or skills[x][1] == "Str":
                skills[x][0] -= 1

    if "Light Shield" in other and any("onehand" in x for x in weapon_list):
        defenses["AC"] += 2
    elif "Heavy Shield" in other and any("onehand" in x for x in weapon_list):
        defenses["AC"] += 3
        speed -= 1
        
    defenses["Fortitude"] += max(stat_mods["Str.mod"], stat_mods["Const.mod"])
    defenses["Reflex"] += max(stat_mods["Dex.mod"], stat_mods["Int.mod"])
    defenses["Will"] += max(stat_mods["Wis.mod"], stat_mods["Cha.mod"])

    #skill mod setter, input is a String - the name of the Skill
    def mod_skills(skill):
        if skills[skill][2] == True:
            skills[skill][0] += 5
        if skills[skill][1] == "Str":
            skills[skill][0] += stat_mods["Str.mod"]
        elif skills[skill][1] == "Const":
            skills[skill][0] += stat_mods["Const.mod"]
        elif skills[skill][1] == "Dex":
            skills[skill][0] += stat_mods["Dex.mod"]
        elif skills[skill][1] == "Int":
            skills[skill][0] += stat_mods["Int.mod"]
        elif skills[skill][1] == "Wis":
            skills[skill][0] += stat_mods["Wis.mod"]
        elif skills[skill][1] == "Cha":
            skills[skill][0] += stat_mods["Cha.mod"]
    for x in skills:
        mod_skills(x)

    #OUTPUT
    #outputList = (
    sheetOutput = (
        "Basic Information------------------------------------------",
        char_name, char_race,  char_class,
        "Speed : ", speed,
        "Ability Scores----------------------------------------------",
        stats,
        "Ability Modifiers--------------------",
        stat_mods,
        "Defenses----------------------------------------------------",
        defenses,
        "Health------------------------------------------------------",
        "Max HP : ", maxHP,
        "Bloodied value : " , bloodied_value,
        "Surge value : " , surge_value,
        "Surges per day : " , surge_day,
        "Skills------------------------------------------------------",
        skills,
        "Languages---------------------------------------------------",
        languages_known,
        "Items-------------------------------------------------------",
        weapon, armor, other
        )
    
    #print(sheetOutput)
    return sheetOutput
    
#TODO: create a GUI

#TODO: add a main menu => choose [Random || Checkmarks] 
#Random => single button + name => full character sheet
#Checkmarks/Slots => Checkmarks the things you want => full character sheet

def generateMainMenu():
    main = tk.Tk()
    main.geometry("500x150")
    main.title("Dungeons & Dragons 4th Edition - Character Sheet Creator")

    def generateRandomSheet():
        root = tk.Tk()
        root.geometry("800x900")
        root.title("Dungeons & Dragons 4th Edition - Randomized Sheet")

        def Take_Input():
            name = input.get()
            print(name)
            sheetOutput = generateSheet(name)
            output.insert(tk.END, generateSheet(name))#Printing problem

        prompt = tk.Label(text = "Name your Fantasy Dungeons & Dragons character: ")#gets printed into main window MUST FIX
        input = tk.Entry(root)
        output = tk.Text(root, height = 50, width = 95, bg = "light gray")
        output.configure(state = "disabled")
        displayButton = tk.Button(root, text = "Generate Character", command = lambda:Take_Input())
        saveButton = tk.Button(root, text = "Save as PDF")
        exitButton = tk.Button(root, text = "Close", command = root.destroy)    
        
        prompt.pack()
        input.pack()
        output.pack()
        displayButton.pack()
        saveButton.pack()
        exitButton.pack()    
        tk.mainloop()

    
    mainLabel = tk.Label(text = "Choose to have your Dungeons & Dragons character randomly generated\n or choose the parameters of your character.")
    randomButton = tk.Button(main, text = "Randomized Character", command = lambda:generateRandomSheet())
    checkButton = tk.Button(main, text = "Personalized Character", command = lambda:generatePersonalSheet())

    mainLabel.pack()
    randomButton.pack()
    checkButton.pack()
    tk.mainloop()


def main():
    generateMainMenu()

if __name__ == '__main__':
    main()