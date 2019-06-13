from collections import deque
from mcpi import minecraft 
import mcpi.block as block 
from random import randint 
import time 

# A class to implment a moving snake in Minecraft
class Snake:
   
    # Make a snake.... make it high in the air to avoid getting tanlged up
    def __init__(_self, xPos,yPos,zPos,length, headBlock, bodyBlock):
    
        _self.bits = deque([(xPos,_,zPos) for _ in range(yPos,yPos+length)])
        _self.head = headBlock
        _self.body = bodyBlock

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
        
    #def setBlock(_self,position,block):
    #    print(*position,block)
        
    def workOutNewHeadPositionOld(_self,pos):
        x,y,z = pos
        x = x + 1
        return((x,y,z))
    
    def workOutNewHeadPosition(_self, pos):

        x,y,z = pos

        # Try to move down first of all
        if mc.getBlock(x, y-1, z) == block.AIR.id:
            y = y-1
        else:
            # Check out the left, right, forward, backward options
            dirList = []
            if mc.getBlock(x+1, y, z) == block.AIR.id:
                dirList.append(1)
            if mc.getBlock(x-1, y, z) == block.AIR.id:
                dirList.append(2)
            if mc.getBlock(x, y, z+1) == block.AIR.id:
                dirList.append(3)
            if mc.getBlock(x, y, z-1) == block.AIR.id:
                dirList.append(4)
            if len(dirList) > 0:
                selection = dirList[randint(0,len(dirList)-1)]
                if selection == 1:
                    x = x + 1
                if selection == 2:
                    x = x - 1
                if selection == 3:
                    z = z + 1
                if selection == 4:
                    z = z - 1
            else:
                # Last resort is to go up else if getblock(x, y+1, z)
                y = y+1
        return(x,y,z)
        
# Connect to the game
mc = minecraft.Minecraft.create() 
xPos,yPos,zPos = mc.player.getTilePos() 

# Make a snake and animate it
snake = Snake(xPos,30,zPos,50,block.LAPIS_LAZULI_ORE,block.LAPIS_LAZULI_BLOCK)
snake.runner()

LAPIS_LAZULI_ORE
