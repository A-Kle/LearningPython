import random


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh): #constructor
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

    def getHp(self):
        print("hp is ", self.hp)

enemy1 = Enemy(75, 90) #creating instance (not using new in python)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(40, 49)
enemy2.getAtk()
enemy2.getHp()
"""

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
    

    """