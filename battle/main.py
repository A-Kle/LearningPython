from classes.game import Person, bcolors
import colorama as col

magic = [{"name": "Fire", "cost": 10, "dmg": 160},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
col.init()
print(col.Fore.RED + "AN ENEMY ATTACKS!" + col.Style.RESET_ALL)

while running:
    print("===========================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()
        
        if cost > current_mp:
            print(col.Fore.RED + "\nNot enough MP\n" + col.Style.RESET_ALL)
            continue
        #todo

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(col.Fore.BLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + col.Style.RESET_ALL)
        


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())
    print("-----------------------------")
    print("Enemy HP:", col.Fore.RED + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + col.Style.RESET_ALL + "\n")

    print("Your HP:", col.Fore.GREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + col.Style.RESET_ALL + "\n")
    print("Your MP:", col.Fore.BLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + col.Style.RESET_ALL + "\n")

    if enemy.get_hp() == 0:
        print(col.Fore.GREEN + "You win!" + col.Style.RESET_ALL)
    elif player.get_hp() == 0:
        print(col.Fore.RED + "Your enemy has defeated you!" + col.Style.RESET_ALL)
        running = False