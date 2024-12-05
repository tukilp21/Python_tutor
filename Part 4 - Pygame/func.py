import pygame

# Change background color, take screen as input
def change_background_color(screen, color):

    # set background color to our window
    screen.fill(color)
     
    # Update our window
    pygame.display.update()
     
    # if color is red change it to green and 
    # vice-versa
    if(color == "red"):
        color = "green"
         
    else:
        color = "red"

    return screen, color