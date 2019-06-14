from collections import deque
from mcpi import minecraft 
import mcpi.block as block 
from random import randint 
import time 

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

BIAS = 20

# A class to implment a moving snake in Minecraft
class Snake:
   
    # Make a snake.... make it high in the air to avoid getting tanlged up
    def __init__(_self, xPos,yPos,zPos,length, headBlock, bodyBlock):
    
        _self.bits = deque([(xPos,_,zPos) for _ in range(yPos,yPos+length)])
        _self.head = headBlock
        _self.body = bodyBlock
        _self.selection = 0

    # Animate the snakes body        
    def runner(_self):

	# Keep going forever
        while(True):

	    # Draw the head, 
            mc.setBlock(_self.bits[0],_self.head)

            # wait a bit
            time.sleep(0.5)

            # work out the new head position
            newPos = _self.workOutNewHeadPosition(_self.bits[0])

            # Make the head back to a body part
            mc.setBlock(_self.bits[0],_self.body)        

            _self.bits.appendleft(newPos)
        
            # Erase the tail
            mc.setBlock(_self.bits.pop(),0)
        
    # Work out the direction of movment for the next head position
    def workOutNewHeadPosition(_self, pos):

        x,y,z = pos

        # Try to move down first of all
        if mc.getBlock(x, y-1, z) == block.AIR.id:
            y = y-1
        else:

            # Check out the left, right, forward, backward options
            dirList = []
            if mc.getBlock(x+1, y, z) == block.AIR.id:
                dirList.append(NORTH)
            if mc.getBlock(x-1, y, z) == block.AIR.id:
                dirList.append(SOUTH)
            if mc.getBlock(x, y, z+1) == block.AIR.id:
                dirList.append(EAST)
            if mc.getBlock(x, y, z-1) == block.AIR.id:
                dirList.append(WEST)

            # Add a bias here to try and keep going in the same direction as last time if possible. Add
            # the same option in as many times as appropriate to suit the bias level
            if _self.selection in dirList:
                for _ in range(BIAS):
                    dirList.append(_self.selection)

            # Now pick an option from the list at random
            if len(dirList) > 0:
                _self.selection = dirList[randint(0,len(dirList)-1)]
                if _self.selection == NORTH:
                    x = x + 1
                if _self.selection == SOUTH:
                    x = x - 1
                if _self.selection == EAST:
                    z = z + 1
                if _self.selection == WEST:
                    z = z - 1
            else:
                # If there are no options, last resort is to go up. This will overwrite blocks
                y = y+1

        # And return the new position  
        return(x,y,z)
        
# Connect to the game
mc = minecraft.Minecraft.create() 
xPos,yPos,zPos = mc.player.getTilePos() 

# Make a snake and animate it
snake = Snake(xPos,30,zPos,10,block.LAPIS_LAZULI_ORE,block.LAPIS_LAZULI_BLOCK)
snake.runner()

