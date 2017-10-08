# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 21:06:25 2017

@author: Rafi

SCENE MAP MODULE
"""
import random
from battle_module import BattleEngine

class Scene:
    def enter(self,engine):
        print("SCENE NOT CONFIGURED")
        exit(1)
        
#class DebugMode(Scene):
#    def enter(self,engine):
#        engine.levelmap.debug_clear_map()
#        print("Debug Mode Active")
#        user_comm=input("Enter Command:")
#        if user_comm in engine.map:
#            return user_comm
#        else:
#            print("Invalid Input")
#            return "DebugMode"
#            
#class RestoreHPMP(Scene):
#    def enter(self,engine):
#        engine.player.hp=player.hp_cap
#        engine.player.mp=player.mp_cap
#        return "DebugMode"
#        
#class FastTravel(Scene):
#    def enter(self,engine):
#        print("Enter Coordinates:")
#        x,y=(input("x y: ")).split(" ")
#        engine.levelmap.cursor=engine.levelmap.grid[y][x]
        
class MainMenu(Scene):
    def enter(self,engine):
        print("Welcome to Rafi's Dungeon Game.\n\nInstructions: Select a number when given a list.\n\nPress enter to continue.")
        hold_inp=input()
        return "EnterStartRoom"
        
class Death(Scene):
    def enter(self,engine):
        print("You died!")
        return "Death"
        
class EnterBattle(Scene):
    def enter(self,engine):
        self.battle_engine=BattleEngine(engine.player)
        return self.battle_engine.run()
        
class LevelUpCheck(Scene):
    def enter(self,engine):
        if engine.player.xp>=engine.player.xp_cap:
            return "LevelUp"
        else:
            return "ChooseRoom"
        
class LevelUp(Scene):
    def enter(self,engine):        
        engine.player.level_up()
        print("You've leveled up!\nNow level",str(engine.player.lvl))
        hold_inp=input("Press enter to continue\n")
        return "ChooseRoom"
        
class EnterStartRoom(Scene):
    def enter(self,engine):
        print("You have entered the dungeon. Try to find the treasure.")
        return "ChooseRoom"
        
class EnterEmptyRoom(Scene):
    def enter(self,engine):
        print("This room is empty")
        return "ChooseRoom"
        
class EnterTrapRoom(Scene):
    def enter(self,engine):
        trap_type=random.randint(1,100)
        hit=random.randint(1,100)
        if trap_type>30:
            print("There was a hidden spike trap here!")
            if hit>90:
                print("You narrowly dodge it!")
                return "ChooseRoom"
            else:
                print("Ouch! -10 HP")
                engine.player.hp-=10
                if engine.player.hp<=0:
                    return "Death"
                else:
                    return "ChooseRoom"
        else:
            print("There was a hidden fire trap here!")
            if hit>75:
                print("You narrowly dodge it!")
                return "ChooseRoom"
            else:
                print("Ouch! -20 HP")
                engine.player.hp-=20
                if engine.player.hp<=0:
                    return "Death"
                else:
                    return "ChooseRoom"
                    
class ChooseRoom(Scene):
    def enter(self,engine):
        engine.levelmap.cursor.mark_cleared()
        print("Curr Room:",engine.levelmap.cursor.x,engine.levelmap.cursor.y)
        
        print("Choose direction:")
        dir_options_str=""
        opt_count=1
        dir_dict={}
        
        #Note that, in all other cases, the directions are listed North, East, South then West, in clockwise order.
        #It is different here for aesthetic purposes.
        if engine.levelmap.cursor.north:
            dir_options_str+=str(opt_count)+": North\n"
            dir_dict[opt_count]="North"
            opt_count+=1
        if engine.levelmap.cursor.west:
            dir_options_str+=str(opt_count)+": West\n"
            dir_dict[opt_count]="West"
            opt_count+=1
        if engine.levelmap.cursor.east:
            dir_options_str+=str(opt_count)+": East\n"
            dir_dict[opt_count]="East"
            opt_count+=1
        if engine.levelmap.cursor.south:
            dir_options_str+=str(opt_count)+": South\n"
            dir_dict[opt_count]="South"
            opt_count+=1
        print(dir_options_str+"\n"+str(opt_count)+": Options\n"+str(opt_count+1)+": Quit Game")

        opt_num=input("> ")
        if opt_num>="1" and opt_num<=str(opt_count-1):
            user_dir=dir_dict[int(opt_num)]
            if user_dir=="North":
                engine.levelmap.go_north()
            elif user_dir=="East":
                engine.levelmap.go_east()
            elif user_dir=="South":
                engine.levelmap.go_south()
            elif user_dir=="West":
                engine.levelmap.go_west()
        elif opt_num==str(opt_count):
            return "Options"
        elif opt_num==str(opt_count+1):
            return "Death"
        else:
            print("Please enter a valid option.")
            return "ChooseRoom"
            
        if engine.levelmap.cursor.room_val==1:
            return "EnterBattle"
        elif engine.levelmap.cursor.room_val==2:
            return "EnterTrapRoom"
        elif engine.levelmap.cursor.room_val==3:
            return "EnterEmptyRoom"
        elif engine.levelmap.cursor.room_val==100:
            return "EndGame"

            
class Options(Scene):
    def enter(self,engine):
        flag=True
        while flag:
            print("Options Menu\nSelect an option:\n1: Stats\n2: Back")
            
            user_in=input("> ")
            if user_in=="1":
                print(engine.player.skillset)
            elif user_in=="2":
                flag=False
        
        return "ChooseRoom"

class EndGame(Scene):
    def enter(self,player):
        print("You have found the hidden treasure! You've won the game!!!")
        return "EndGame"
        
class SceneMap:
    scenes={
        #"DebugMode": DebugMode(),
        "MainMenu": MainMenu(),
        "Death": Death(),
        "EnterBattle": EnterBattle(),
        "LevelUpCheck": LevelUpCheck(),
        "LevelUp": LevelUp(),
        "EnterStartRoom": EnterStartRoom(),
        "EnterEmptyRoom": EnterEmptyRoom(),
        "EnterTrapRoom": EnterTrapRoom(),
        "ChooseRoom": ChooseRoom(),
        "Options": Options(),
        "EndGame": EndGame()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = SceneMap.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)