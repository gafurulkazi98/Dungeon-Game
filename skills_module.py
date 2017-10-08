# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:22:41 2017

@author: Rafi

SKILLS MODULE
"""
import random

class Skill:
    def __init__(self,user):
        print("Skill/Category not implemented")
        exit(1)
        
class DefSkill(Skill):
    def __init__(self,user):
        print("Defensive Skill not implemented")
        exit(1)
        
class OffSkill(Skill):
    def __init__(self,user):
        print("Offensive Skill not implemented")
        exit(1)
        
class Basic_Heal(DefSkill):
    def __init__(self,user,heal_pwr=10):
        self.heal_power=heal_pwr
        self.skill_name="Basic Heal"
        self.user=user
        self.mp_cost=10
        
    def use(self,target):
        target.hp+=self.heal_power
        print(self.user.name,"healed!")
        if target.hp>target.hp_cap:
            target.hp=target.hp_cap
        self.user.mp-=self.mp_cost
        
    def upgrade(self):
        print("Basic Heal power increased by 5!")
        self.heal_power+=5
        
class Heavy_Attack(OffSkill):
    def __init__(self,user,atk_pwr=10):
        self.attack_power=atk_pwr
        self.skill_name="Heavy Attack"
        self.user=user
        self.mp_cost=15
        
    def use(self,target):
        ran_val=random.randint(1,100)
        if ran_val<(self.user.accuracy*0.85):
            print(self.user.name,"used a Heavy Attack.",target.name,"lost",self.attack_power,"HP!")
            target.hp-=self.attack_power
        else:
            print(self.user.name,"used a Heavy Attack, but missed!")
        self.user.mp-=self.mp_cost
        
    def upgrade(self):
        print("Heavy Attack power increased by 5!")
        self.attack_power+=5
            
class Full_Skill_List: #The full set of skills that the player and monsters can have
    def __init__(self,user):
        self.dict={1:Basic_Heal(user),
                   2:Heavy_Attack(user)}
        
class Skillset:
    def __init__(self,user,preset_skill_lst=None):
        self.full_skill_dict=Full_Skill_List(user)
        self.skillset_dict={}
        self.n=0
        if preset_skill_lst!=None:
            for skill_num in preset_skill_lst:
                skill=self.full_skill_dict.dict[skill_num]
                self.skillset_dict[skill_num]=skill
            self.n=len(preset_skill_lst)
        
    def add_skill(self,skill_num):
        skill=self.full_skill_dict.dict[skill_num]
        self.skillset_dict[skill_num]=skill
        self.n+=1
        print("New skill gained:",skill.skill_name)
      
    def __str__(self):
        str_lst="Skills:\n"
        for key in self.skillset_dict:
            skill=self.skillset_dict[key]
            str_lst+=str(key)+": "+skill.skill_name+"\n"
        return str_lst
        
    def __len__(self):
        return self.n