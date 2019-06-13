from collections import deque
from mcpi import minecraft 
import mcpi.block as block 
from random import randint 
import time 

class Snake:
   
    # Make a snake.... make it high in the air to avoid getting tanlged up
    def __init__(_self, xPos,yPos,zPos,length, headBlock, bodyBlock):
    
        _self.bits = deque([(xPos,_,zPos) for _ in range(yPos,yPos+length)])
        _self.head = headBlock
        _self.body = bodyBlock
        
    def runner(_self):
        
        # Draw the head, 
        _self.setBlock(_self.bits[0],_self.head)

        # wait a bit
        time.sleep(0.5)

        # Make it back to a body part
        _self.setBlock(_self.bits[0],_self.body)
        
        # work out the new head, add it on the end of the Q, clear the tail and remove from Q
        _self.bits.appendleft(_self.workOutNewHeadPosition(_self.bits[0]))
        
        # Erase the tail
        _self.setBlock(_self.bits.pop(),0)
        
    def setBlock(_self,position,block):
        print(*position,block)
        
    def workOutNewHeadPosition(_self,pos):
        x,y,z = pos
        x = x + 1
        return((x,y,z))
    
    def workOutNewHeadPositionEx(pos):

        #print "Work out new head position", headposition print "map:", map[1][0][0] if 
        #map[snake[position][0]][0] == 0:
        #    print "can move that way"
            # so here we can move down, forward, (left, right = 50/50), up in that order
        #snake[tailposition] = snake[headposition][0]+1, snake[headposition][1], snake[headposition][2]
        x,y,z = pos
        # Try to move down first of all
        print mc.getBlock(x, y-1, z)
        if mc.getBlock(x, y-1, z) == block.AIR:
            y = y-1
        else:
            # Check out the left, right, forward, backward options
            dirList = []
            if mc.getBlock(x+1, y, z) == block.AIR:
                dirList.append(1)
            if mc.getBlock(x-1, y, z) == block.AIR:
                dirList.append(2)
            if mc.getBlock(x, y, z+1) == block.AIR:
                dirList.append(3)
            if mc.getBlock(x, y, z-1) == block.AIR:
                dirList.append(4)
            print dirList
            print len(dirList)
            if len(dirList) > 0:
                selection = dirList[randint(0,len(dirList)-1)]
                print "Select: ", selection
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
                print "had to go up"
        return(x,y,z)
        
# Connect to the game
mc = minecraft.Minecraft.create() 
xPos,yPos,zPos = mc.player.getTilePos() 

snake = Snake(xPos,20,zPos,5,block.STONE,block.MARBLE)
snake.runner()
print(snake.bits)
snake.runner()
print(snake.bits)
snake.runner()
print(snake.bits)
