# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:12:57 2017

@author: Rafi

LEVEL MAP MODULE
"""

import random

#       Level Map:
#     __ __ \/ __ __ 
# 0  |   __      |  |
# 1  |  |   __|__   |
# 2  |  |__ __   |  |
# 3  |__   |   __|  |
# 4  |__ __|  |__ __|
#     0  1  2  3  4
class LevelMap:
    class Room:
        def __init__(self,room_num,exit_type,type_val=None):
            if type_val==None:
                type_val=random.randint(1,99)
            self.x=room_num%5
            self.y=room_num//5
            
            if type_val>0 and type_val<61:
                self.room_val=1  #Monster Room
            elif type_val>60 and type_val<81:
                self.room_val=2  #Trap Room
            elif type_val>80 and type_val<100:
                self.room_val=3  #Clear Room
            elif type_val==0:
                self.room_val=0  #Start Room
            elif type_val==100:
                self.room_val=100 #Exit room
                
            self.exit_type=exit_type
                
            self.north=False
            self.east=False
            self.south=False
            self.west=False
            
        def mark_cleared(self):
            self.room_val=3
            
            # Implement a new system that uses files to store grid layouts
    def __init__(self): #Grid stores a list of every Y-Level, every list stores a room in X-Level order
        self.grid=[[LevelMap.Room(0,8),LevelMap.Room(1,9),LevelMap.Room(2,14,0),LevelMap.Room(3,10),LevelMap.Room(4,3)],
                    [LevelMap.Room(5,6),LevelMap.Room(6,8),LevelMap.Room(7,7),LevelMap.Room(8,5),LevelMap.Room(9,13)],
                    [LevelMap.Room(10,6),LevelMap.Room(11,5),LevelMap.Room(12,9),LevelMap.Room(13,10),LevelMap.Room(14,6)],
                    [LevelMap.Room(15,5),LevelMap.Room(16,10),LevelMap.Room(17,8),LevelMap.Room(18,7),LevelMap.Room(19,6)],
                    [LevelMap.Room(20,2),LevelMap.Room(21,7),LevelMap.Room(22,1,100),LevelMap.Room(23,2),LevelMap.Room(24,7)]
                    ]
                    
        for row in self.grid:
            for room in row:
                if room.exit_type==1:   # |_|
                    room.north=True
                    
                #                          _
                elif room.exit_type==2: # |_
                    room.east=True
                    
                #                          _
                elif room.exit_type==3: # | |
                    room.south=True
                    
                #                         _
                elif room.exit_type==4: # _|
                    room.west=True
                
                #                           .
                elif room.exit_type==5: # |_
                    room.north=True
                    room.east=True
                    
                    
                elif room.exit_type==6: # | |
                    room.north=True
                    room.south=True
                    
                #                        .
                elif room.exit_type==7: # _|
                    room.north=True
                    room.west=True
                
                #                          _
                elif room.exit_type==8: # | .
                    room.east=True
                    room.south=True
                    
                #                         _
                elif room.exit_type==9: # _
                    room.east=True
                    room.west=True
                
                #                           _
                elif room.exit_type==10: # . |
                    room.west=True
                    room.south=True
                    
                #                            .
                elif room.exit_type==11: # | .
                    room.north=True
                    room.east=True
                    room.south=True
                    
                #                         . .
                elif room.exit_type==12: # _
                    room.north=True
                    room.east=True
                    room.west=True
                    
                #                         .
                elif room.exit_type==13: #. |
                    room.north=True
                    room.south=True
                    room.west=True
                    
                #                           _
                elif room.exit_type==14: # . .
                    room.east=True
                    room.south=True
                    room.west=True
                    
                #                          . .
                elif room.exit_type==15: # . .
                    room.north=True
                    room.east=True
                    room.south=True
                    room.west=True
                    
        self.cursor=self.grid[0][2]
                    
    def get_room_north(self,room):
        return self.grid[room.y-1][room.x]
        
    def get_room_east(self,room):
        return self.grid[room.y][room.x+1]
        
    def get_room_south(self,room):
        return self.grid[room.y+1][room.x]
        
    def get_room_west(self,room):
        return self.grid[room.y][room.x-1]
        
        
    def go_north(self):
        self.cursor=self.get_room_north(self.cursor)
        print("You go north")
            
    def go_east(self):
        self.cursor=self.get_room_east(self.cursor)
        print("You go east")
        
    def go_south(self):
        self.cursor=self.get_room_south(self.cursor)
        print("You go south")
            
    def go_west(self):
        self.cursor=self.get_room_west(self.cursor)
        print("You go west")
            
            
            
    #Map debugs
    def debug_clear_map(self): #Debug function to make every room empty
        for row in self.grid:
            for room in row:
                room.mark_cleared()

    def print_room_types(self): #Debug function used to see room types
        print("0: Start, 1: Monsters, 2:Trap, 3:Clear, 10:End")
        for row in self.grid:
            row_type_str=""
            for room in row:
                row_type_str+=str(room.room_val)
            print(row_type_str)
    
    def print_room_coords(self): #Debug function used to see room coordinates
        for row in self.grid:
            row_coord_str=""
            for room in row:
                row_coord_str+=str(room.x)+", "+str(room.y)+"\t"
            print(row_coord_str)
            
    def print_rooms_exits(self): #Debug function used to see the room exit types
        for row in self.grid:
            row_exit_str=""
            for room in row:
                row_exit_str+=str(room.exit_type)+" "
            print(row_exit_str)
            
    def print_room_neighbors(self): #Debug function used to see room connections
        print("ROOM, NORTH, EAST, SOUTH, WEST\n")
        for row in self.grid:
            row_neighbor_str=""
            for room in row:
                north_coords="None"
                east_coords="None"
                south_coords="None"
                west_coords="None"
                
                if room.north!=None:
                    north_coords=str(room.north.x)+","+str(room.north.y)
                if room.east!=None:
                    east_coords=str(room.east.x)+","+str(room.east.y)
                if room.south!=None:
                    south_coords=str(room.south.x)+","+str(room.south.y)
                if room.west!=None:
                    west_coords=str(room.west.x)+","+str(room.west.y)
                
                row_neighbor_str+="["+str(room.x)+","+str(room.y)+" "+north_coords+" "+east_coords+" "+south_coords+" "+west_coords+"]"
            print(row_neighbor_str)