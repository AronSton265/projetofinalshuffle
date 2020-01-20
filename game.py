import pygame
import pygame.freetype
import random
import time

clicked=0
clicked1=0
card=[0,0,0,0]
deck = [0]
l=0
c=0
score = 0

def isinbotton(crect, lrect):
    mouse = pygame.mouse.get_pos()
    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
        return True
    else: return False

def setclick(x):
    global clicked
    global clicked1
    clicked=x
    clicked1=x

def click():
    global clicked
    return clicked

def cart(xcart, ismousein, lrect, crect,l,c, screen):
    lrect = int(lrect)
    crect = int(crect)
    
    if(xcart == 1):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255,255,255), ( lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255, 0, 0), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255, 0, 0), (lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
    elif(xcart == 2):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(lrect + l/2), int(crect + c/2)), 10, 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255, 0, 0), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 0, 0), (int(lrect + l/2), int(crect + c/2)), 10, 2)
    elif(xcart == 3):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 255, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255, 0, 0), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 0, 0), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 2)
    elif(xcart == 4):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255,255,255), ( lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (0, 255, 0), (lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
    elif(xcart == 5):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(lrect + l/2), int(crect + c/2)), 10, 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (0, 255, 0), (int(lrect + l/2), int(crect + c/2)), 10, 2)
    elif(xcart == 6):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 255, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (0, 255, 0), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 2)
    elif(xcart == 7):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255,255,255), ( lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (0, 0, 255), (lrect + l/2 -10, crect + c/2 -10, 20, 20), 2)
    elif(xcart == 8):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(lrect + l/2), int(crect + c/2)), 10, 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (0, 0, 255), (int(lrect + l/2), int(crect + c/2)), 10, 2)
    elif(xcart == 9):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 255, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 2)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (0, 0, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 2)
    elif(xcart == 10):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255,255,255), ( lrect + l/2 -10, crect + c/2 -10, 20, 20), 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255, 0, 0), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255, 0, 0), (lrect + l/2 -10, crect + c/2 -10, 20, 20), 0)
    elif(xcart == 11):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(lrect + l/2), int(crect + c/2)), 10, 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255, 0, 0), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 0, 0), (int(lrect + l/2), int(crect + c/2)), 10, 0)
    elif(xcart == 12):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 255, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255, 0, 0), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 0, 0), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 0)
    elif(xcart == 13):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255,255,255), ( lrect + l/2 -10, crect + c/2 -10, 20, 20), 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (0, 255, 0), (lrect + l/2 -10, crect + c/2 -10, 20, 20), 0)
    elif(xcart == 14):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(lrect + l/2), int(crect + c/2)), 10, 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (0, 255, 0), (int(lrect + l/2), int(crect + c/2)), 10, 0)
    elif(xcart == 15):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 255, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (0, 255, 0), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 0)
    elif(xcart == 16):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (255,255,255), ( lrect + l/2 -10, crect + c/2 -10, 20, 20), 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.rect(screen, (0, 0, 255), (lrect + l/2 -10, crect + c/2 -10, 20, 20), 0)
    elif(xcart == 17):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(lrect + l/2), int(crect + c/2)), 10, 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.circle(screen, (0, 0, 255), (int(lrect + l/2), int(crect + c/2)), 10, 0)
    elif(xcart == 18):
        if (ismousein == True):
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (255,255,255), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (255, 255, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 0)
        else:
            pygame.draw.rect(screen, (0,0,20), ( lrect, crect, l, c), 0)
            pygame.draw.rect(screen, (0, 255, 0), ( lrect, crect, l, c), 2)
            pygame.draw.polygon(screen, (0, 0, 255), [(lrect + l/2-10, crect + c/2-10),(lrect + l/2, crect + c/2+10), (lrect + l/2+10, crect + c/2-10)], 0)

def createdeck(x):
    if(x==6):
        global deck 
        deck =[ [1,1,2],[2,3,3],[4,4,5],[5,6,6] ]
        random.shuffle(deck)
    elif (x==8):
        deck =[ [1,1,2,2],[3,3,4,4],[5,5,6,6],[7,7,8,8] ]
        random.shuffle(deck)
    elif (x==10):
        deck =[ [1,1,2,2],[3,3,4,4],[5,5,6,6],[7,7,8,8],[9,9,10,10] ]
        random.shuffle(deck)
    elif (x==15):
        deck =[ [1,1,2,2,3,3],[4,4,5,5,6,6],[7,7,8,8,9,9],[10,10,11,11,12,12],[13,13,14,14,15,15] ]
        random.shuffle(deck)
    elif (x==18):
        deck =[ [1,1,2,2,3,3],[4,4,5,5,6,6],[7,7,8,8,9,9],[10,10,11,11,12,12],[13,13,14,14,15,15],[16,16,17,17,18,18] ]
        random.shuffle(deck)

    return deck

def create(x, screen, font, deck):
    global clicked
    global clicked1
    global card
    global l
    global c
    global score
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
                                clicked1 = 1
                                card[2]=i
                                card[3]=j
                                crect1=55 + card[1]*c + card[1]*10
                                lrect1=405 + card[0]*l + card[0]*10
                                cart(deck[card[0]][card[1]], isinbotton(crect1, lrect1), lrect1, crect1, l, c, screen)
                                cart(deck[i][j], True, lrect, crect, l, c, screen)
                                if (deck[card[0]][card[1]] == deck[i][j] and (i != card[0] or j != card[1])):
                                    score = score + 50
                                    deck[card[0]][card[1]] = 0
                                    deck[i][j] = 0
                                elif (i != card[0] or j != card[1]):
                                    score = score - 10
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
                                clicked1 = 1
                                card[2]=i
                                card[3]=j
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

    elif (x == 10):
        l=480/5 -10
        c=600/4 -10
        i=0
        while (i<5):
            j=0
            while (j<4):
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
                                clicked1 = 1
                                card[2]=i
                                card[3]=j
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

    elif (x == 15):
        l=480/6 -10
        c=600/5 -10
        i=0
        while (i<6):
            j=0
            while (j<5):
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
                                clicked1 = 1
                                card[2]=i
                                card[3]=j
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

    elif (x == 18):
        l=480/6 -10
        c=600/6 -10
        i=0
        while (i<6):
            j=0
            while (j<6):
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
                                clicked1 = 1
                                card[2]=i
                                card[3]=j
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
    
    font.render_to(screen, (20, 20), "Score:", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 30)
    font.render_to(screen, (200, 20), str(score), (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

    #botao para voltar atraz
    cbback = (255, 255, 0)

    if (mouse[0]>10 and mouse[0]<150 and mouse[1]>660 and mouse[1]<697):
                cbback = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    return False
    
    pygame.draw.rect(screen, cbback, (10, 660, 140, 37), 2)
    font.render_to(screen, (20, 670), "Back", cbback,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

    return True

 


