# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:10:35 2017

@author: Rafi

MONSTERS MODULE
"""
import random

class Monster:
    def __init__(self,player):
        print("MONSTER NOT CONFIGURED")
        exit(1)
        
class Rat(Monster):
    def __init__(self,player):
        self.name="Rat"
        self.hp=9+player.lvl
        self.accuracy=60
        self.basic_attack=BasicAttack(1+player.lvl,self.accuracy)
        self.exp_val=10
        
class BasicAttack:
    def __init__(self,power,u_acc):
        self.power=power
        self.user_accuracy=u_acc
        
    def use(self,target):
        ran_val=random.randint(1,100)
        if ran_val<self.user_accuracy:
            target.hp-=self.power
            print("You lost",str(self.power),"health!")
        else:
            print("You dodged it!")