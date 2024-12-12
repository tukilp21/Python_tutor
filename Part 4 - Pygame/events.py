import pygame
import time

pygame.init() 

# Creating window 
gameWindow = pygame.display.set_mode((800, 300)) 
pygame.display.set_caption("Event Handling") 


exit_game = False
game_over = False

# Creating a game loop 
while not exit_game:
    
    for event in pygame. event.get(): 
        if event.type == pygame.QUIT: 
            raise SystemExit 
        elif event.type == pygame.MOUSEMOTION:
            # print(event.rel)
            mousePos = event.pos
            print(event.pos)
            pygame.draw.circle(gameWindow, "white", (mousePos[0], mousePos[1]), 10)
            # if event.rel[0] > 0: 
            #     print("Mouse moving to the right") 
            # elif event.rel[1] > 0: 
            #     print("Mouse moving down")
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 3: 
                print("Right mouse button pressed")
            elif event.button == 1:
                print("Left mouse button pressed") 
        elif event.type == pygame.MOUSEBUTTONUP:
            print("Mouse button has been released") 

    
    # update
    pygame.display.update()

pygame.quit() 
quit() 
