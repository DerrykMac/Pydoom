import json, csv, os, sys,math
import Main as m

def castrayH(x, y, angle):

    global drr
    drr = 40

    while True:
        x += math.cos(math.radians(angle))
        y += math.sin(math.radians(angle))
        try :
            if intmap[int(y/16)][int(x/16)] != "0":
                (fx,fy) = (x,y)
                if intmap[int(y/16)][int((x+1)/16)] == "0":
                    drr = 200
                elif intmap[int(y/16)][int((x-1)/16)] == "0":
                    drr = 150
                elif intmap[int((y+1)/16)][int(x/16)] == "0":
                    drr = 100
                elif intmap[int((y-1)/16)][int(x/16)] == "0":
                    drr = 170
                return (fx,fy)
        except:
            print("out of bounds")
            return (x,y)
        

    
    

#get normal from castray
 

dis = [0] * 60
dir = [0] * 60


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

    for i in range(-30, 30, 1):
        m.draw.line(m.screen, (255,0,0), (m.Player_x, m.Player_y), castrayH(m.Player_x, m.Player_y, i + m.Player_angle), 1)

        
        dir[(i + 30)] = drr

        dis[(i + 30)] = math.sqrt((castrayH(m.Player_x, m.Player_y, i + m.Player_angle)[0] - m.Player_x)**2 + (castrayH(m.Player_x, m.Player_y, i + m.Player_angle)[1] - m.Player_y)**2) * math.cos(math.radians(i))
    
    m.draw.rect(m.screen, (100,90,255), m.Rect(1000, 0, 800, 1000))
    for i in range(0, 60, 1):
        Bar = m.Rect((i*10) + 1000, 70, 10, (((90 * 200) / dis[i]) ))
        col = (90, dir[i], 90)
        m.draw.rect(m.screen, col, Bar)
        floor = m.Rect((i*10) + 1000, (70) + (((90 * 200) / dis[i]) ), 10, 1000)
        m.draw.rect(m.screen, (35, 148, 146), floor)

        
   