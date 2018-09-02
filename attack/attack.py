import random


playerhp = 290
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg
    if playerhp >= 30:
        print("Enemy strikes for {} points of damage. Current HP is {}.".format(dmg, playerhp))
    elif playerhp < 30 and playerhp > 0:
        print("You are low health.")
    elif playerhp == 0:
        print("You are dead.")
    

    