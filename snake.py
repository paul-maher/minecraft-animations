########
#
## DONT USE THIS FILE. ITS FOR REFERENCE ONLY
#
#######

from mcpi import minecraft 
import mcpi.block as block 
import time 
from random import randint 

#snake = [(-100,20,-70),(-99,19,-70),(-98,18,-70),(-97,17,-70),(-96,16,-70),(-95,15,-70)] 
snake = []

def init(x,y,z):
    print "Initialise snake"
    snake.append((x,y+20,z+1))
    snake.append((x,y+21,z+1))
    snake.append((x,y+22,z+1))
    snake.append((x,y+23,z+1))
    snake.append((x,y+24,z+1))
    snake.append((x,y+25,z+1))

# TODO: Rewrite this using tuples and a FIFO stack
def movingSnake(leaveTrail):
    print "Live snake "
    tailptr = 0
    headptr = 5
    while(True):
        print "Delete tail: ", snake[tailptr]
        mc.setBlock(snake[tailptr][0], snake[tailptr][1], snake[tailptr][2],block.AIR)
        workOutNewHeadPosition(headptr, tailptr)
        headptr = tailptr
        #headptr=headptr+1 if headptr==5:
        #    headptr=0
        tailptr = tailptr+1
        if tailptr==6:
            tailptr=0
        time.sleep(0.5) 

def workOutNewHeadPosition(headposition, tailposition):

    #print "Work out new head position", headposition print "map:", map[1][0][0] if 
    #map[snake[position][0]][0] == 0:
    #    print "can move that way"
        # so here we can move down, forward, (left, right = 50/50), up in that order
    #snake[tailposition] = snake[headposition][0]+1, snake[headposition][1], snake[headposition][2]
    x,y,z = snake[headposition]
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
    snake[tailposition] = x, y, z
    print "set block here", snake[tailposition]
    mc.setBlock(x,y,z,block.GLOWING_OBSIDIAN) 

# Connect to the game
mc = minecraft.Minecraft.create() 
xPos,yPos,zPos = mc.player.getTilePos() 

# Initialise a snake and set it moving 
init(xPos,yPos,zPos)
movingSnake(False)
