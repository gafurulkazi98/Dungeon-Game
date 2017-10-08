# -*- coding: utf-8 -*-
"""
Created on Sun May 21 13:23:42 2017

@author: Rafi

ENGINE
"""
from levelmap_module import LevelMap
from scenemap_module import SceneMap
from player_module import Player

class MainEngine:
    def __init__(self):
        self.player=Player()
        self.map=SceneMap('EnterStartRoom')
        self.levelmap=LevelMap()
        self.debug_mode=False # Modify engine to allow input-based Debug Mode
        
    def play(self):
        #Map debug functions
        #self.level_map.print_room_coords()
        #self.levelmap.print_rooms_exits()
        #self.levelmap.print_room_neighbors()
    
        curr_scene=self.map.opening_scene()
        death_scene=self.map.next_scene('Death')
        win_scene=self.map.next_scene('EndGame')
        
        while curr_scene!=death_scene and curr_scene!=win_scene:
            next_scene_name=curr_scene.enter(self)
            curr_scene=self.map.next_scene(next_scene_name)
            
        curr_scene.enter(self.player)


game=MainEngine()
game.play()