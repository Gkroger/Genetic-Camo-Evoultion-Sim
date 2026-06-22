#------------------------------------------Credits---------------------------------------------------------
"""
Genetic Camo Evoultion Sim
Giles Roger 
Start: 20:45 22/06/26 
"""
#-------------------------------------------Notes---------------------------------------------------------

"""
Plan:
 >generate 100 random hex values 
 >compare to target (random)
   > break down into r g b components then measure difference of each add total difference
 > kill 50 worst values
 >50 best go through to next gen
 >50 new ones generated from 50 best "parents"
 >10% chance to mutate
 have anyalitics and bullshit 


 To do:
  >initalise window and stuff 

 Goblins:
  null
"""
#--------------------------------------------Set up--------------------------------------------------------
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Genetic Camo Evoultion Sim")
clock = pygame.time.Clock()

font = pygame.font.Font("courier", 36) #just set font to pixel font 


#-------------------------------------------Variables--------------------------------------------------------

running = True
testMessage = "Hello World!"
text = font.render(testMessage, True, "black")

#------------------------------------------Sub Programs------------------------------------------------------


#--------------------------------------------Classes---------------------------------------------------------


#---------------------------------------------Main-----------------------------------------------------------
while running:
    #check for inputs 
    for event in pygame.event.get():
        #end if user quits
        if event.type == pygame.QUIT:
            running = False


    # set screen white
    screen.fill(("white")) 
    
    #draw test text
    screen.blit(text, (100, 100))

    # Update screen
    pygame.display.flip()
    clock.tick(60)  # 50 fps

pygame.quit()