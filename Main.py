import os, sys, pygame, math
from pygame import *
from Builder import *
from Controller import *
import time as tm



(width, height) = (1600, 800)
screen = display.set_mode((width, height))
background_colour = (255,255,255)
clock = pygame.time.Clock()
targetfps = 120


def Main():
  init()
  display.flip()
  
  screen.fill(background_colour)
  Start()
  
  os.system('cls' if os.name == 'nt' else 'clear')

  running = True
  while running:

    #get fps
    clock.tick(targetfps)
    
    fps = clock.get_fps()

    screen.fill(background_colour)
    Update()
    Update2()
    display.flip() 

    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        running = False
    display.set_caption('PyDoom' + " FPS: " + str(fps))


Player_x = 0
Player_y = 0
Player_angle = 0



if __name__ == "__main__":
    Main()