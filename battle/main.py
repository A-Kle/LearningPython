from classes.game import Person
from classes.magic import Spell
from classes.inventory import Item
import colorama as col
import random
import re

col.init()

#black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 20, 300, "black")
meteor = Spell("Meteor", 15, 200, "black")
quake = Spell("Quake", 15, 140, "black")

#white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 1200, "white")
curamax = Spell("Curamax", 50, 6000, "white")

#create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("Elixir", "eilxir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy_magic = [fire, meteor, curamax]

player_items = [{"item":potion,"quantity":15},
                {"item":hipotion, "quantity":5},
                {"item":superpotion, "quantity":5},
                {"item":elixir, "quantity":5},
                {"item":hielixir, "quantity":2},
                {"item":grenade, "quantity":1}]


#instantiate people
player1 = Person("Valos:", 3260, 174, 300, 34, player_magic, player_items)
player2 = Person("Nick: ", 4160, 132, 311, 34, player_magic, player_items)
player3 = Person("Robot:", 3089, 144, 288, 34, player_magic, player_items)

enemy1 = Person("Imp    ", 1250, 130, 560, 325, enemy_magic, [])
enemy2 = Person("Magus", 11200, 702, 525, 25, enemy_magic, [])
enemy3 = Person("Imp    ", 1250, 130, 560, 325, enemy_magic, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

while running:
    print("\n")
    print("NAME                  HP                              MP")
    for player in players:
        player.get_stats()

    print('\n')

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)

            print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage. Enemy HP:", enemies[enemy].get_hp())
        
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()  

            current_mp = player.get_mp()
            
            if spell.cost > current_mp:
                print(col.Fore.RED + "\nNot enough MP.\n" + col.Style.RESET_ALL)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)

                print(col.Fore.BLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + col.Style.RESET_ALL)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print(col.Fore.BLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace(" ", "") + "." + col.Style.RESET_ALL)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]
        
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(col.Fore.RED + "\n" + "None left..." + col.Style.RESET_ALL)
                continue
            player.items[item_choice]["quantity"] -= 1


            if item.type == "potion":
                player.heal(item.prop)
                print(col.Fore.GREEN + "\n" + item.name + " heals for", str(item.prop), "HP." + col.Style.RESET_ALL)
            elif item.type == "elixir":

                if item.name == "MegaElixir":
                    for i in players:
                        i.hp == i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp == player.maxhp
                    player.mp = player.maxmp
                print(col.Fore.GREEN + "\n" + item.name + " fully restores HP/MP." + col.Style.RESET_ALL)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(col.Fore.RED + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name.replace(" ", "") + col.Style.RESET_ALL + ".")

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

    #check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    #check if player won
    if defeated_enemies == 2:
        print(col.Fore.GREEN + "You win!" + col.Style.RESET_ALL)
        running = False
    #check if enemy won
    elif defeated_players == 2:
        print(col.Fore.RED + "Your enemies have defeated you!" + col.Style.RESET_ALL)
        running = False

    print("\n")
    print(col.Fore.RED + "AN ENEMY ATTACKS!" + col.Style.RESET_ALL)
    #enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        
        if enemy_choice == 0:
            #chose attack
            target = random.randrange(0, 3)
            
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(col.Fore.RED + enemy.name.replace(" ","") + " attacks " + re.sub("[ :]", "", players[target].name) + " for " + str(enemy_dmg) + "." + col.Style.RESET_ALL)
    
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)

                print(col.Fore.BLUE + spell.name + " heals " + enemy.name.replace(" ", "") + " for", str(magic_dmg), "HP." + col.Style.RESET_ALL)
            elif spell.type == "black":
                target = random.randrange(0, 2)
                players[target].take_damage(magic_dmg)

                print(col.Fore.BLUE + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage to " + re.sub("[ :]", "", players[target].name) + "." + col.Style.RESET_ALL)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace('[ :]', "") + " has died.")
                    del players[target]
           # print("Enemy chose", spell, " damage is ", magic_dmg)
