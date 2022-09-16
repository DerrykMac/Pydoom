import os, sys, time, pygame, math
from pygame import *
from Builder import *
from Controller import *



(width, height) = (1600, 800)
screen = display.set_mode((width, height))
background_colour = (255,255,255)

def Main():
  init()
  display.flip()
  display.set_caption('PyDoom')
  screen.fill(background_colour)
  Start()

  running = True
  while running:
    for event in pygame.event.get():
      
      screen.fill(background_colour)
      Update()
      Update2()
      display.flip() 
      if event.type == pygame.QUIT:
        running = False


Player_x = 0
Player_y = 0
Player_angle = 0



if __name__ == "__main__":
    Main()