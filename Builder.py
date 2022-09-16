import json, csv, os, sys,math
import Main as m

def castray(x, y, angle):
    x = int(x)
    y = int(y)
    angle = int(angle)
    while True:
        x += math.cos(math.radians(angle))
        y += math.sin(math.radians(angle))
        try :
            if intmap[int(y/16)][int(x/16)] != "0":
                return (x,y)
        except:
            return (x,y)

dis = [0] * 30


def Start():
    with open('Maps/Sample/Walls.csv') as csvfile:
        global intmap
        read = csv.reader(csvfile, delimiter=',')
        intmap = list(read)
        csvfile.close()
    
    with open('Maps/Sample/data.json') as jsonfile:
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

    for i in range(-15, 15, 1):
        m.draw.line(m.screen, (0,0,0), (m.Player_x, m.Player_y), castray(m.Player_x, m.Player_y, i + m.Player_angle), 1)
        dis[(i + 15)] = math.sqrt((castray(m.Player_x, m.Player_y, i + m.Player_angle)[0] - m.Player_x)**2 + (castray(m.Player_x, m.Player_y, i + m.Player_angle)[1] - m.Player_y)**2)

    m.draw.rect(m.screen, (0,0,0), m.Rect(270, 0, 300, 300))
    for i in range(0, 30, 1):
        m.draw.rect(m.screen, (90,90,255), m.Rect((i*10) + 270, 0, 10, dis[i]))

        
   