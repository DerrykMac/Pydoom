import Main as m
import math
import numpy as np

def Update2():
    # move player
    # get keys down

    speed = 1

    keys = m.key.get_pressed()
    if keys[m.K_q]:
        m.Player_angle -= speed
        if m.Player_angle < 0:
            m.Player_angle = 360
    if keys[m.K_e]:
        m.Player_angle += speed
        if m.Player_angle > 360:
            m.Player_angle = 0
    if keys[m.K_w]:
        m.Player_x += math.cos(math.radians(m.Player_angle)) * speed
        m.Player_y += math.sin(math.radians(m.Player_angle)) * speed
    if keys[m.K_s]:
        m.Player_x -= math.cos(math.radians(m.Player_angle)) * speed
        m.Player_y -= math.sin(math.radians(m.Player_angle)) * speed
    if keys[m.K_a]:
        m.Player_x -= math.cos(math.radians(m.Player_angle + 90)) * speed
        m.Player_y -= math.sin(math.radians(m.Player_angle + 90)) * speed
    if keys[m.K_d]:
        m.Player_x += math.cos(math.radians(m.Player_angle + 90)) * speed
        m.Player_y += math.sin(math.radians(m.Player_angle + 90)) * speed

    if keys[m.K_ESCAPE]:
        m.quit()
        m.sys.exit()
