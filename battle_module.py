# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:09:01 2017

@author: Rafi

BATTLE ENGINE MODULE
"""
import random
from monster_module import *
from skills_module import *

class BattleEngine: # Modify battles to include multiple enemies
    def __init__(self,player):
        self.player=player
        
        self.turn_order=[] # A list used to point to whose turn it is
        self.turn_order.append(self.player) # Adding player to turn order
        self.xp_reward=0 # XP that player will gain from fight
        
        # Adding monsters to turn order
        mon_count=random.randint(1,3)
        for i in range(mon_count):
            new_mon=self.spawn_monster()
            self.turn_order.append(new_mon)
            self.xp_reward+=new_mon.exp_val
            
        self.cursor=0 # Set first turn to player
            
        if mon_count==1:
            print("An evil "+self.turn_order[1].name.lower()+" has appeared!")
        else:
            print(str(mon_count)+" evil "+self.turn_order[1].name.lower()+"s have appeared")
        
    def spawn_monster(self):
        return Rat(self.player)
        
    def run(self):
        battle_on=True
        while battle_on: #If the player dies or all enemies are dead, battle is over
            
            # Player's Turn
            if self.turn_order[self.cursor]==self.player:
                if self.player.hp>0 and (len(self.turn_order)-1)!=0:
                    self.player_turn()
                    self.next_turn()
                else:
                    battle_on=False
                    
            # Enemies' Turn
            else:
                if self.player.hp>0 and (len(self.turn_order)-1)!=0:
                    self.enemy_turn(self.turn_order[self.cursor])
                    self.next_turn()
                else:
                    battle_on=False
        
        if self.player.hp<=0: #If player is dead, you lose
            return "Death"
        elif (len(self.turn_order)-1)==0: #If monsters are dead, you win
            print("You win!",self.xp_reward,"XP gained!")
            self.player.xp+=self.xp_reward
            hold_inp=input("Press enter to continue")
            return "LevelUpCheck"
            
    def next_turn(self):
        self.cursor+=1
        if self.cursor>=len(self.turn_order):
            self.cursor=0
        
    def player_turn(self):
        print("Your HP:"+str(self.player.hp)+" Your MP:"+str(self.player.mp)+
            " Your XP:"+str(self.player.xp)+"/"+str(self.player.xp_cap))
        for elem in self.turn_order[1:]:
            print(elem.name+" HP: "+str(elem.hp))
        print("\nACTIONS:\n1: Attack\n2: Skills\n\n3: Quit Game")
        player_action=input("> ")
        
        #Selecting from list
        if player_action=="1":
            self.player_attack()
        elif player_action=="2":
            self.player_skills()
        elif player_action=="3":
            self.player.hp=0
        else:
            print("Invalid Input")
            self.player_turn()
    
    def enemy_turn(self,monster):
        self.enemy_attack(monster)
            
    def player_attack(self):
        # Targeting
        print("Select an enemy to attack:\n")
        numbering=1
        mon_lst=""
        for elem in self.turn_order[1:]:
            mon_lst+=str(numbering)+": "+str(elem.name)+"\n"
            numbering+=1
        print(mon_lst+"\n"+str(numbering)+": Go Back")
        mon_num=(input("> "))
        if mon_num<str(numbering) and mon_num>="1":
            selected_mon=self.turn_order[int(mon_num)]
            self.player.basic_attack.use(selected_mon)
            
            if selected_mon.hp<=0: # Monsters are removed from the turn list when killed
                print(selected_mon.name,"has been slain!")
                self.turn_order.remove(selected_mon)
                
        elif mon_num==numbering: # If player enters "Go Back"
            self.player_turn()
        else:
            print("Invalid Input")
            self.player_attack()
            
    def player_skills(self):
        skill_list_str=""
        n=len(self.player.skillset)+1
        skill_list_str+=str(self.player.skillset)+"\n"+str(n)+": "+"Go Back"
        print(skill_list_str)
        skill_action=input("> ")
        
        if skill_action>="1" and skill_action<=str(n):    
            skill_action=int(skill_action)
            if skill_action==n:
                self.player_turn()
                
            else:
                selected_skill=self.player.skillset.skillset_dict[skill_action]
                if self.player.mp>selected_skill.mp_cost:
                
                    if isinstance(selected_skill,OffSkill):
                        # Targeting
                        print("Select an enemy to attack:\n")
                        numbering=1
                        for elem in self.turn_order[1:]:
                            print(str(numbering)+": "+str(elem.name))
                            numbering+=1
                        mon_num=(input("> "))
                        if mon_num<=str(len(self.turn_order)-1) and mon_num>="1":
                            selected_mon=self.turn_order[int(mon_num)]
                            selected_skill.use(selected_mon)
                            
                            if selected_mon.hp<=0: # Monsters are removed from the turn list when killed
                                self.turn_order.remove(selected_mon)
                                
                        else:
                            print("Invalid Input")
                            self.player_skills()
                            
                    elif isinstance(selected_skill,DefSkill):
                        selected_skill.use(self.player)
                        
                else:
                    print("Not enough MP")
                    self.player_skills()
        else:
            print("Invalid Input")
            self.player_skills()
            
    def enemy_attack(self,monster):
        print(monster.name,"attacked!")
        monster.basic_attack.use(self.player)