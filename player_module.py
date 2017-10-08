# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:17:09 2017

@author: Rafi

PLAYER MODULE
"""
import random
from skills_module import Skillset

class Player:
    def __init__(self):
        self.name="You"
        self.hp=100
        self.hp_cap=100
        self.mp=50
        self.mp_cap=50
        self.xp=0
        self.xp_cap=20
        self.accuracy=90
        self.lvl=1
        self.basic_attack=BasicAttack(5,self.accuracy)
        self.skillset=Skillset(self,[1]) # Adds Basic Heal at start
#        self.skillset.add_skill(1)
    
    def level_up(self):
        self.xp-=self.xp_cap
        self.hp_cap+=10
        self.hp=self.hp_cap
        self.mp_cap+=5
        self.mp=self.mp_cap
        self.lvl+=1
        self.xp_cap=int(self.xp_cap*1.1)
        if (self.lvl/5)<=len(self.skillset.full_skill_dict.dict):
            if self.lvl%5==0:
                self.skillset.add_skill(int(self.lvl/5))
                self.basic_attack=BasicAttack(5,self.accuracy)
                
class BasicAttack:
    def __init__(self,power,u_acc):
        self.power=power
        self.user_accuracy=u_acc
        
    def use(self,target):
        ran_val=random.randint(1,100)
        if ran_val<self.user_accuracy:
            target.hp-=self.power
            print(target.name,"lost",str(self.power),"health!")
        else:
            print("You missed, dumbass!")