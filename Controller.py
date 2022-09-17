import Main as m
import math
import numpy as np

def Update2():
    # move player
    # get keys down
    keys = m.key.get_pressed()
    if keys[m.K_q]:
        m.Player_angle -= 5
    if keys[m.K_e]:
        m.Player_angle += 5
    if keys[m.K_w]:
        m.Player_x += math.cos(math.radians(m.Player_angle)) * 5
        m.Player_y += math.sin(math.radians(m.Player_angle)) * 5
    if keys[m.K_s]:
        m.Player_x -= math.cos(math.radians(m.Player_angle)) * 5
        m.Player_y -= math.sin(math.radians(m.Player_angle)) * 5
    if keys[m.K_a]:
        m.Player_x -= math.cos(math.radians(m.Player_angle + 90)) * 5
        m.Player_y -= math.sin(math.radians(m.Player_angle + 90)) * 5
    if keys[m.K_d]:
        m.Player_x += math.cos(math.radians(m.Player_angle + 90)) * 5
        m.Player_y += math.sin(math.radians(m.Player_angle + 90)) * 5
