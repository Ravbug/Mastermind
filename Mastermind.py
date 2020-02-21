"""
Created By Ravbug, Summer 2010
Mastermind recreated in Python!
Requires pygame and easygui
"""

import pygame, random, time, easygui
pygame.init()
screen = pygame.display.set_mode([747,994])
screen.fill([0,130 ,255])
orange = [255, 127, 0]
red = [255, 0, 0]
yellow = [255, 255, 0]
green = [0,255,0]
purple =[100,0,127]
blue = [0, 0, 255]
lb = [0, 130, 255]
black = [0,0,0]
y = 960
x = 323
p_colors = ["blank","blank","blank","blank"]
yrect = 924

#Draws player's circles
for looper2 in range(4):
    for looper in range(10):
        pygame.draw.circle(screen, [255,255,255], [x, y], 30, 0)
        y = y -100
    x = x+100
    y = 960
#Draws checking circles
x = 50
for loopre in range(10):
    for looper in range(4):
        pygame.draw.circle(screen, blue, [x,y], 20, 0)
        x = x + 50
    x = 50
    y = y-100
pygame.display.flip()
code = []
blanks = easygui.buttonbox("Do you want to include the possibility of blanks?",
                           choices = ["Yes", "No"])
if blanks == "Yes":
    for looper in range(4):
        color = random.choice(["red", "yellow", "orange", "blue", "green", "purple", "blank", "blank","blank"])
        code.append(color)
else:
    for looper in range(4):
        color = random.choice(["red", "yellow", "orange", "blue", "green", "purple"])
        code.append(color)
y_cir = 960
xrect = 288
#defines "Check"
def check():
    global yrect
    global p_colors
    global colors
    global code
    global y_cir
    global xrect
    color2 = 3
    stats = []
    r_pegs = 0
    
    colors = []
    colors.extend(code)
    for looper in range(4):
        if colors[color2] == p_colors[color2]:
            stats.append("True")
            r_pegs = r_pegs + 1
            del colors[color2]
            del p_colors[color2]
        else:
            stats.append("False")
        color2 = color2 - 1
    w_pegs = 0
    index = len(p_colors)-1
    for i in range(4):
        if stats[index] == "False":
            if p_colors[index] in colors:
                w_pegs= w_pegs + 1
        index = index - 1
    x_cir = 50
    if r_pegs == 0 and w_pegs == 0:
        pygame.draw.rect(screen, red, [25, y_cir- 3, 200, 5], 0)
    for looper in range(r_pegs):
        pygame.draw.circle(screen, red, [x_cir, y_cir], 20, 0)
        x_cir = x_cir + 50
    for looper in range(w_pegs):
        pygame.draw.circle(screen, [255,255,255], [x_cir, y_cir], 20, 0)
        x_cir = x_cir + 50
    if r_pegs == 4:
        easygui.msgbox("You win!")
        pygame.quit()
    del stats[:]
    del p_colors[:]
    p_colors = ["blank","blank","blank","blank"]
    if yrect == -76 and r_pegs != 4:
        joined_code = " ".join(code)
        easygui.msgbox("You Lose!")
        easygui.msgbox("The code was: '"+ joined_code  +"'.")
        pygame.quit()
#defines "Main"
def main():
    global yrect
    global y_cir
    xrect = 288
    left = 70
    right = 70
    pygame.draw.rect(screen, [0,0,0], [xrect, yrect,left, right], 1)
    circlenum = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and xrect > 290:
                    pygame.draw.rect(screen, lb, [xrect, yrect,left, right], 2)
                    xrect = xrect - 100
                    circlenum = circlenum- 1
                    pygame.draw.rect(screen, black, [xrect, yrect,left, right], 1)
                elif event.key == pygame.K_RIGHT and xrect < 580:
                    pygame.draw.rect(screen, lb, [xrect, yrect,left, right], 2)
                    xrect = xrect + 100
                    circlenum = circlenum + 1
                    pygame.draw.rect(screen, black, [xrect, yrect,left, right], 1)
                elif event.key == pygame.K_r:
                    pygame.draw.circle(screen, red, [xrect+35, yrect+36], 30, 0)
                    p_colors[circlenum] = "red"
                elif event.key == pygame.K_o:
                    pygame.draw.circle(screen, orange, [xrect+35, yrect+36], 30, 0)
                    p_colors[circlenum] = "orange"
                elif event.key == pygame.K_y:
                    p_colors[circlenum] = "yellow"
                    pygame.draw.circle(screen, yellow, [xrect+35, yrect+36], 30, 0)
                elif event.key == pygame.K_g:
                    p_colors[circlenum] = "green"
                    pygame.draw.circle(screen, green, [xrect+35, yrect+36], 30, 0)
                elif event.key == pygame.K_p:
                    p_colors[circlenum] = "purple"
                    pygame.draw.circle(screen, purple, [xrect+35, yrect+36], 30, 0)
                elif event.key == pygame.K_b:
                    p_colors[circlenum] = "blue"
                    pygame.draw.circle(screen, blue, [xrect + 35, yrect + 36], 30, 0)
                elif event.key == pygame.K_SPACE:
                    p_colors[circlenum] = "blank"
                    pygame.draw.circle(screen, [255,255,255], [xrect + 35, yrect + 36], 30, 0)
                elif event.key == pygame.K_RETURN:
                    check()
                    pygame.draw.rect(screen, lb, [xrect, yrect, 70, 70],1)
                    yrect = yrect - 100
                    y_cir = y_cir - 100
                    pygame.draw.rect(screen, black, [xrect, yrect, 70, 70],1)
                pygame.display.flip()


main()
