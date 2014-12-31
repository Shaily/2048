"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result= [0]*len(line)
    result1=[0]*len(line)
    done=[0]*len(line)
    count=0

    # replace with your code
    for itr in range(len(line)):
        if line[itr]>0:
           result[count]=line[itr]
           count=count+1
  
    itr=0
    count=0
    for itr in range(len(result)-1):
        if done[itr]==0:
            if result[itr]==result[itr+1]:
                result1[count]=result[itr]+result[itr+1]
                done[itr]=1
                done[itr+1]=1
                count=count+1
            else:
                result1[count]=result[itr]
                count=count+1
    
    #for the last element
    if done[len(result)-1]==0:
        if result[len(result)-1]>0:
            result1[count]=result[len(result)-1]
    return result1

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._rows=grid_height
        self._cols=grid_width
        self._cells = [[0 for col in range(self._cols)] for row in range(self._rows)]
        #print self._cells[1]
        #new_list = [for item in self._cells]
        #new_list=zip(*self._cells)
        #print "column", new_list
        
    
    def reset(self):
        """t 
        Reset the game so the grid is empty.
        """
        # replace with your code
        self._cells = [[0 for col in range(self._cols)] for row in range(self._rows)]
      
        
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return repr(self._cells)
        

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._rows
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._cols
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        itr=0 #column
        count=0 #row
        if direction==UP:
           #print "UP"
           new_list=zip(*self._cells)
           for item in new_list:
                merged_list=merge(item)
                count=0
                for val in merged_list:
                    self.set_tile(count,itr,val)
                    count=count+1
                itr=itr+1
           self.new_tile()
                           
        elif direction==DOWN:
           #print "DOWN"
           new_list=zip(*self._cells)
           for item in new_list:
                item=item[::-1]
                merged_list=merge(item)
                count=len(merged_list)-1
                for val in merged_list:
                    self.set_tile(count,itr,val)
                    count=count-1
                itr=itr+1
           self.new_tile()
        elif direction==LEFT:
           #print "LEFT"
           for item in self._cells:
               merged_list=merge(item)
               count=0
               for val in merged_list:
                    self.set_tile(itr,count,val)
                    count=count+1
               itr=itr+1
           self.new_tile() 
        elif direction==RIGHT:
           #print "RIGHT"
           for item in self._cells:
               item=item[::-1]
               merged_list=merge(item)
               count=len(merged_list)-1
               for val in merged_list:
                    self.set_tile(itr,count,val)
                    count=count-1
               itr=itr+1
           self.new_tile()    
        
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        #code for rowChoice
        rowlist=range(self._rows-1, -1, -1)
        rowchoice=[0]*(25*len(rowlist))
        count=0
        for var in rowlist:
           itr=0
           while itr <=24:
                rowchoice[count]=var
                count=count+1
                itr=itr+1
                
        #code for columnChoice
        collist=range(self._cols-1, -1, -1)
        colchoice=[0]*(25*len(collist))
        count=0
        for var in collist:
            itr=0
            while itr <=24:
                colchoice[count]=var
                count=count+1 
                itr=itr+1
              
        row=random.choice(rowchoice)
        col=random.choice(colchoice)
        choice= [2] * 90+ [4] * 10
        if(self._cells[row][col]==0):
               self._cells[row][col]=random.choice(choice)
               
                
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        self._cells[row][col]=value
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code  
        return self._cells[row][col]



