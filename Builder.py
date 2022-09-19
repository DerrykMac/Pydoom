from cmath import atan
import json, csv, os, sys,math
import Main as m
import numpy as np


def castrayH(x, y, angle):

    global drr
    drr = 40
    rx = x
    ry = y
    ra = angle

    dof = 0
    cutoff = 8
    subset = 1

    if angle != 0:
        aTan = -1 / math.tan(math.radians(angle))
    else:
        aTan = 0

    if angle > 0 and angle < 180:
        ystep = -16
        ry = 16 * math.floor(y / 16) + 16
        rx = x + (ry - y) * aTan
        xstep = ystep * aTan
    else:
        ystep = 16
        ry = 16 * math.ceil(y / 16) + 0.001
        rx =x + (ry - y) * aTan
        xstep = ystep * aTan

    if angle == 0 or angle == 180:
        rx = x
        ry = y
        dof = 8
    

    while dof < cutoff:
        dof += 1

        m_col = int(rx / 16)
        m_row = int(ry / 16)
        if m_col >= 0 and m_col < len(intmap[0]) and m_row >= 0 and m_row < len(intmap):
            if intmap[m_row][m_col] != "0":
                dof = cutoff
                drr = 255
                print("hit")
            else:
                rx += xstep
                ry += ystep
                dof += 1
                print("no hit")
        else:
            dof = cutoff
            print("out")
    
    return(rx, ry)
    


    

    

    #while dof < cutoff:
    #    dof += 1
#
    #    rx += ((math.cos(math.radians(angle))) * 8)
    #    ry += ((math.sin(math.radians(angle))) * 8)
#
#
    #    try :
    #        if intmap[int(ry/16)][int(rx/16)] != "0":
    #            
    #            dof = cutoff
    #    except:
    #        print("out of bounds")
    #        dof = cutoff
    #
    #if dof == cutoff:
    #    drr = 255
        
        
    return (rx, ry)
        

    

dis = [0] * 120
dir = [0] * 120


def Start():
    with open('Maps/TestLv/simplified/Level_0/Wall.csv') as csvfile:
        global intmap
        read = csv.reader(csvfile, delimiter=',')
        intmap = list(read)
        csvfile.close()
    
    with open('Maps/TestLv/simplified/Level_0/data.json') as jsonfile:
        global data
        data = json.load(jsonfile)
        m.Player_x = data["entities"]["Player"][0]["x"]
        m.Player_y = data["entities"]["Player"][0]["y"]
        

def Update():
    m_col = 0
    m_row = 0
    for row in intmap:
            for num in row:
                if num != " ":
                    if num == "1":
                        m.draw.rect(m.screen, (150,150,150), m.Rect(m_row +1, m_col +1, 15, 15))
                    m_row += 16
            m_col += 16
            m_row = 0
    m.draw.circle(m.screen, (255,0,0), (m.Player_x, m.Player_y), 5)

    for i in range(-60, 60, 1):
        m.draw.line(m.screen, (10,200,10), (m.Player_x, m.Player_y), castrayH(m.Player_x, m.Player_y, i/2 + m.Player_angle), 1)

        #dis[(i + 60)] = math.sqrt((castrayH(m.Player_x, m.Player_y, i/2 + m.Player_angle)[0] - m.Player_x)**2 + (castrayH(m.Player_x, m.Player_y, i/2 + m.Player_angle)[1] - m.Player_y)**2) * math.cos(math.radians(i/2))
        #numpy version
        dis[(i + 60)] = np.sqrt((castrayH(m.Player_x, m.Player_y, i/2 + m.Player_angle)[0] - m.Player_x)**2 + (castrayH(m.Player_x, m.Player_y, i/2 + m.Player_angle)[1] - m.Player_y)**2) * np.cos(np.radians(i/2))

        dir[(i + 60)] = drr

        
    m.draw.rect(m.screen, (100,90,255), m.Rect(1000, 0, 800, 1000))
    for i in range(0, 120, 1):
        hight = ((90 * 200) / dis[i])
        col = (255 - (dis[i] / 10), dir[i], 90) 

        #floor
        floor = 499 + (hight/2)
        m.draw.rect(m.screen, (68, 219, 189), m.Rect(1000 + (i * 5), floor, 5, 1000 - floor))
        #ceiling
        #m.draw.rect(m.screen, (74, 84, 107), m.Rect(1000 + (i * 5), 0, 5, 500 - (hight/2)))
        #wall
        try:
            m.draw.rect(m.screen, col, m.Rect(1000 + (i * 5), 500 - (hight/2), 5, hight))
        except:
            m.draw.rect(m.screen, (20, 50, 90) , m.Rect(1000 + (i * 5), 500 - (hight/2), 5, hight))


        
   