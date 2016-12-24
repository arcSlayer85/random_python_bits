#! /usr/bin/python

import random, time

class Enemy():
    
    HP = 0;
    damage = 0;
    def __init__(self, health):
        self.HP = health;
        
    def attack(self):
        dmgList = [20, 30, 40, 50];
        dmgRand = random.randint(0, 3);
        self.damage = dmgList[dmgRand];
        enemyDmg = self.damage;
        print("enemy did %i damage..." % (self.damage));
        time.sleep(1);
        player.playerHealth(enemyDmg);
        
    def enemHealth(self, playerDam):
        self.HP -= playerDam;
        time.sleep(1);
        if self.HP <= 0:
            print("enemy has 0 health left");
            enemyDead();
        else:
            print("enemy has %i health left..." % (self.HP));

class Player():

    HP = 100;
    damage = 0;

    def attack(self):
        dmgList = [20, 30, 40, 50];
        dmgRand = random.randint(0, 3);
        self.damage = dmgList[dmgRand];
        playerDam = self.damage;
        print("you did %i damage..." % (self.damage));
        time.sleep(1);
        _enemy1.enemHealth(playerDam);

    def playerHealth(self, enemyDmg):
        self.HP -= enemyDmg;
        time.sleep(1);
        if self.HP <= 0:
            print("you have 0 health left");
            playerDead();
        else:
            print("you have %i health left..." % (self.HP));

def playerDead():
    print("You are Dead!!!")
    ending();

def enemyDead():
    print("Enemy is defeated!!!")
    ending();

def ending():
    time.sleep(2);
    print("Goodbye!");
    time.sleep(2);
    
def command():
    global _inp;
    _inp = str(input("Enter a command : "));

count = 0;    
_inp = "";
_enemy1 = Enemy(100);
player = Player();

command();

while count == 0:
    if _inp == "Attack" or _inp == "attack":
        print("You are attacking...");
        time.sleep(1);
        player.attack();
        if _enemy1.HP > 0:
            _enemy1.attack();
            command();
            print(count);
        else:
            count = 1;

        if player.HP <= 0:
            count = 1;

