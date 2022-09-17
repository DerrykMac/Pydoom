import json, csv, os, sys,math
import Main as m
import numpy as np


def castrayH(x, y, angle):

    global drr
    drr = 40
    ##o_x = x
    ##o_y = y

    dof = 0
    cutoff = 700
    subset = 1

    while dof < cutoff:
        #move x and y
        x += (math.cos(math.radians(angle))) / subset
        y += (math.sin(math.radians(angle))) / subset

        #difference
        ##diff_x = x - o_x
        ##diff_y = y - o_y

        #increment
        dof += 1

        #check if x and y are in a wall
        try :
            if intmap[int(y/16)][int(x/16)] != "0":
                (fx,fy) = (x,y)

                (x,y) = (x+1,y+1)
                if intmap[int(y/16)][int((x+2)/16)] == "0":
                    drr = 200
                elif intmap[int(y/16)][int((x-2)/16)] == "0":
                    drr = 150
                elif intmap[int((y+2)/16)][int(x/16)] == "0":
                    drr = 100
                elif intmap[int((y-2)/16)][int(x/16)] == "0":
                    drr = 170
                else:
                    drr = 40

                dof = cutoff
                return (fx,fy)
        except:
            print("out of bounds")
            dof = cutoff
            return (x,y)
    
    if dof == cutoff:
        drr = 255
        return (x,y)
        

    

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
                        m.draw.rect(m.screen, (150,150,150), m.Rect(m_row, m_col, 16, 16))
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
        m.draw.rect(m.screen, (74, 84, 107), m.Rect(1000 + (i * 5), 0, 5, 500 - (hight/2)))
        #wall
        m.draw.rect(m.screen, col, m.Rect(1000 + (i * 5), 500 - (hight/2), 5, hight))


        
   