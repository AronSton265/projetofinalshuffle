import pygame
import pygame.freetype
import random
import time

clicked=0
card=[0,0]
deck = [0]
l=0
c=0

def isinbotton(crect, lrect):
    mouse = pygame.mouse.get_pos()
    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
        return True
    else: return False

def setclick(x):
    global clicked
    clicked=x

def click():
    global clicked
    return clicked

def cart(xcart, ismousein, lrect, crect,l,c, screen):
    lrect = int(lrect)
    crect = int(crect)
    xcart =1
    
    if(xcart == 1):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255,255,255), ( lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255, 0, 0), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255, 0, 0), (lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
   

def createdeck(x):
    if(x==6):
        global deck 
        deck =[ [1,1,2],[2,3,3],[4,4,5],[5,6,6] ]
        random.shuffle(deck)

    return deck

def create(x, screen, font, deck):
    global clicked
    global card
    global l
    global c
    mouse = pygame.mouse.get_pos()
    ccarta = ( 9, 158, 9)
    
    
    if (x == 6):
        l=480/4 -10
        c=600/3 -10
        i=0
        while (i<4):
            j=0
            while (j<3):
                lrect=405 + i*l + i*10
                crect=55 + j*c + j*10
                if (deck[i][j] != 0):
                    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                        ccarta = (255, 255, 255)
                        if (pygame.mouse.get_pressed()[0]):
                            if (clicked == 0):
                                cart(deck[i][j], True, lrect, crect, l, c, screen)
                                clicked = 1
                                card[0]=i
                                card[1]=j
                            else:
                                crect1=55 + card[1]*c + card[1]*10
                                lrect1=405 + card[0]*l + card[0]*10
                                cart(deck[card[0]][card[1]], isinbotton(crect1, lrect1), lrect1, crect1, l, c, screen)
                                cart(deck[i][j], True, lrect, crect, l, c, screen)
                                if (deck[card[0]][card[1]] == deck[i][j] and (i != card[0] or j != card[1])):
                                    print ("you win")
                                    deck[card[0]][card[1]] = 0
                                    deck[i][j] = 0
                                elif (i != card[0] or j != card[1]):
                                    print ("/")
                                    print(deck[card[0]][card[1]], deck[i][j])
                        else: pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                    else: 
                        ccarta = ( 9, 158, 9)
                        pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                j=j+1
            i=i+1

    elif (x == 8):
        l=480/4 -10
        c=600/4 -10
        i=0
        while (i<4):
            j=0
            while (j<4):
                lrect=405 + i*l + i*10
                crect=55 + j*c + j*10
                if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                    ccarta = (255, 255, 255)
                else: ccarta = ( 9, 158, 9)
                pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                j=j+1
            i=i+1

    elif (x == 10):
        l=480/5 -10
        c=600/4 -10
        i=0
        while (i<5):
            j=0
            while (j<4):
                lrect=405 + i*l + i*10
                crect=55 + j*c + j*10
                if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                    ccarta = (255, 255, 255)
                else: ccarta = ( 9, 158, 9)
                pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                j=j+1
            i=i+1

    elif (x == 15):
        l=480/6 -10
        c=600/5 -10
        i=0
        while (i<6):
            j=0
            while (j<5):
                lrect=405 + i*l + i*10
                crect=55 + j*c + j*10
                if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                    ccarta = (255, 255, 255)
                else: ccarta = ( 9, 158, 9)
                pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                j=j+1
            i=i+1

    elif (x == 18):
        l=480/6 -10
        c=600/6 -10
        i=0
        while (i<6):
            j=0
            while (j<6):
                lrect=405 + i*l + i*10
                crect=55 + j*c + j*10
                if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                    ccarta = (255, 255, 255)
                else: ccarta = ( 9, 158, 9)
                pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                j=j+1
            i=i+1
    
    font.render_to(screen, (20, 20), "Score:", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

    #botao para voltar atraz
    cbback = (255, 255, 0)

    if (mouse[0]>10 and mouse[0]<150 and mouse[1]>660 and mouse[1]<697):
                cbback = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    firsttime = 0
                    return False
    
    pygame.draw.rect(screen, cbback, (10, 660, 140, 37), 2)
    font.render_to(screen, (20, 670), "Back", cbback,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

    return True

 


