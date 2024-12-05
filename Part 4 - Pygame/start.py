
# import package pygame 
import pygame
import func

# variable
color = "red"
# color = (0, 0, 255)

import pygame
# create display
screen = pygame.display.set_mode(size=(400, 400))
screen = pygame.display.set_mode(size=(1000, 400))
  
# set title 
pygame.display.set_caption('My screen') 

# on-going loop to keep the "game" going
running = True
while running: 
    
    # check for all event about to happen
    print(pygame.event)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    # screen, color = func.change_background_color(screen, color)

    pygame.draw.circle(screen, "yellow", (0, 100), 75)
    pygame.draw.rect(screen, "red", pygame.Rect(100,100,100,60))

    # Update GUI
    pygame.display.update()

pygame.quit() 