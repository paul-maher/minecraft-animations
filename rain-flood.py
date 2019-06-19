from mcpi import minecraft
import mcpi.block as block
import time
from random import randint

# Create a flood plain
def causeFlood():

        print('"Flooding at player position....')

        # Get the height of the land at the players position
        xPos,yPos,zPos = mc.player.getTilePos()
        y = mc.getHeight(xPos,zPos)

        for n in range(1,200):

		# Set a nearby block to water and wait a short while before doing again
                mc.setBlock(xPos+randint(-3, 3),y,zPos+randint(-3,3),block.WATER.id)
                time.sleep(0.1)

# Create a rain storm
def makeItRain():

    # Keep running forever
    while(True):

            # Get the player position, so the rain cloud follows the player
            xPos,yPos,zPos = mc.player.getTilePos()

            # sapling? Gravel?

            # Set a nearby block (somewhere above the player) to a block which will fall. Note they 
            # dont all do this.... some will hover in the sky. Water also bizarelly doesnt give a good effect
            # Potential candidates are, SAPLING, GRAVEL
            mc.setBlock(xPos+randint(-3,3),yPos+randint(20,29),zPos+randint(-3,3),block.GRAVEL.id)
            time.sleep(1)

# Connect to game
mc = minecraft.Minecraft.create()
xPos,yPos,zPos = mc.player.getTilePos()

# And make it rain
# makeItRain()

# And cause a flood
causeFlood()


