# Importing the library
import pygame
 
# Initializing Pygame modules
pygame.init()
 
# Initializing surface
surface = pygame.display.set_mode((400, 300))
 
# Initializing RGB Color
color = (0, 0, 255)
 
# Changing surface color
surface.fill(color)
# update window
pygame.display.flip()

# Set window name
pygame.display.set_caption('GeeksforGeeks')
 
# Set window icon
Icon = pygame.image.load('gfglogo.png')
pygame.display.set_icon(Icon)