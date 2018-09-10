import random
import colorama as col
from .magic import Spell

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("\n" + col.Fore.CYAN + "    " + self.name + col.Style.RESET_ALL)
        print(col.Fore.BLUE + "    ACTIONS:" + col.Style.RESET_ALL)
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + col.Fore.RED + "    TARGET:" + col.Style.RESET_ALL)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice

    def choose_magic(self):
        i = 1
        print(col.Fore.MAGENTA + "    MAGIC:" + col.Style.RESET_ALL)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(col.Fore.GREEN + "    ITEMS:" + col.Style.RESET_ALL)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            i += 1

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 /2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        chp = str(self.hp)
        maxhp = str(self.maxhp)
        shp = chp #hp display with space
        if len(chp) < len(maxhp):
            shp = ""
            for i in range(len(maxhp) - len(chp)):
                shp += " "
            shp += str(self.hp)

        print("                     __________________________________________________")
        print(col.Fore.RED + self.name + "    " + col.Style.RESET_ALL + 
        shp + "/" + str(self.maxhp) + "|" + col.Fore.RED + hp_bar + col.Style.RESET_ALL + "|")

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        hp_bar_ticks = (self.hp / self.maxhp) * 100 / 4
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        
        while len(mp_bar) < 10:
            mp_bar += " "

        chp = str(self.hp)
        maxhp = str(self.maxhp)
        shp = chp #hp display with space
        if len(chp) < len(maxhp):
            shp = ""
            for i in range(len(maxhp) - len(chp)):
                shp += " "
            shp += str(self.hp)

        cmp = str(self.mp)
        maxmp = str(self.maxmp)
        smp = cmp #mp display with space
        if len(cmp) < len(maxmp):
            smp = ""
            for i in range(len(maxmp) - len(cmp)):
                smp += " "
            smp += str(self.mp)

        print("                    _________________________          __________")
        print(col.Fore.CYAN + self.name + "    " + col.Style.RESET_ALL + 
        shp + "/" + str(self.maxhp) + "|" + col.Fore.GREEN + hp_bar + col.Style.RESET_ALL + 
        "| " + smp + "/" + str(self.maxmp) + "|" + col.Fore.BLUE + mp_bar + col.Style.RESET_ALL + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg