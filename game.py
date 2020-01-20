import pygame
import pygame.freetype
import random

#global variables
clicked=0
clicked1=0
primeirav=0
card=[0,0,0,0]
deck = [0]
l=0
c=0
score = 0
ind =[0]
relesed=0
penalty=0

#verefys if the player find all the cards
def wincheck (x):
    global deck
    i=0
    j=0
    wonnot = 0
    if (x == 6):
        while (i<4):
            j = 0
            while (j<3):
                if (deck[ind[i][j]] != 0):
                    wonnot = 1
                j=j+1
            i=i+1
    elif (x == 8):
        while (i<4):
            j = 0
            while (j<4):
                if (deck[ind[i][j]] != 0):
                    wonnot = 1
                j=j+1
            i=i+1
    elif (x == 10):
        while (i<5):
            j = 0
            while (j<4):
                if (deck[ind[i][j]] != 0):
                    wonnot = 1
                j=j+1
            i=i+1
    elif (x == 15):
        while (i<6):
            j = 0
            while (j<5):
                if (deck[ind[i][j]] != 0):
                    wonnot = 1
                j=j+1
            i=i+1
    elif (x == 18):
        while (i<6):
            j = 0
            while (j<6):
                if (deck[ind[i][j]] != 0):
                    wonnot = 1
                j=j+1
            i=i+1

    return wonnot

#verefys if the mouse is the botton of the cordenates crect and lrect
def isinbotton(crect, lrect):
    mouse = pygame.mouse.get_pos()
    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
        return True
    else: return False

#sets the varuables clicked and clicked1 to x 
def setclick(x):
    global clicked
    global clicked1
    clicked=x
    clicked1=x

#index of all the visual parts of each card
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

#indice to the deck, a esiear way to find the card of a list with one variable using two variables
def indice (x):
    global ind
    if(x==6):
        ind=[ [0,1,2],[3,4,5],[6,7,8],[9,10,11] ]
    elif (x==8):
        ind=[ [0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15] ]
    elif (x==10):
        ind=[ [0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,17,18,19] ]
    elif (x==15):
        ind=[ [0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24], [25,26,27,28,29] ]
    elif (x==18):
        ind=[ [0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29], [30,31,32,33,34,35] ]

    return ind

#creates and shufles the deck, only the data of the deck
def createdeck(x):
    global deck 
    if(x==6):
        deck =[1,1,2,2,3,3,4,4,5,5,6,6]
        random.shuffle(deck)
    elif (x==8):
        deck =[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
        random.shuffle(deck)
    elif (x==10):
        deck =[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
        random.shuffle(deck)
    elif (x==15):
        deck =[ 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
        random.shuffle(deck)
    elif (x==18):
        deck =[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
        random.shuffle(deck)

    return deck

#main function of this class, it brings almost every other function here to crete the game
#from the visal aspect to the data aspect of the game 
def create(x, screen, font, deck, ind):
    global clicked
    global clicked1
    global card
    global l
    global c
    global score
    global primeirav
    global relesed
    global penalty
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
                if (deck[ind[i][j]] != 0):
                    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                        ccarta = (255, 255, 255)
                        if (pygame.mouse.get_pressed()[0]):
                            if (clicked == 0):
                                cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                clicked = 1
                                card[0]=i
                                card[1]=j
                                relesed=0
                            else:
                                if(relesed==1):
                                    clicked1 = 1
                                    card[2]=i
                                    card[3]=j
                                    crect1=55 + card[1]*c + card[1]*10
                                    lrect1=405 + card[0]*l + card[0]*10
                                    cart(deck[ind[card[0]][card[1]]], isinbotton(crect1, lrect1), lrect1, crect1, l, c, screen)
                                    cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                    if (deck[ind[card[0]][card[1]]] == deck[ind[i][j]] and (i != card[0] or j != card[1])):
                                        score = score + 100
                                        deck[ind[card[0]][card[1]]] = 0
                                        deck[ind[i][j]] = 0
                                        primeirav = 0
                                    elif ((i != card[0] or j != card[1]) and primeirav == 0):
                                        score = score - penalty
                                        if(score<0):
                                            score=0
                                        primeirav = 1
                                        penalty=penalty+20
                                    relesed=0
                        else: 
                            pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                            relesed = 1
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
                if (deck[ind[i][j]] != 0):
                    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                        ccarta = (255, 255, 255)
                        if (pygame.mouse.get_pressed()[0]):
                            if (clicked == 0):
                                cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                clicked = 1
                                card[0]=i
                                card[1]=j
                                relesed=0
                            else:
                                if(relesed==1):
                                    clicked1 = 1
                                    card[2]=i
                                    card[3]=j
                                    crect1=55 + card[1]*c + card[1]*10
                                    lrect1=405 + card[0]*l + card[0]*10
                                    cart(deck[ind[card[0]][card[1]]], isinbotton(crect1, lrect1), lrect1, crect1, l, c, screen)
                                    cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                    if (deck[ind[card[0]][card[1]]] == deck[ind[i][j]] and (i != card[0] or j != card[1])):
                                        score = score + 100
                                        deck[ind[card[0]][card[1]]] = 0
                                        deck[ind[i][j]] = 0
                                        primeirav = 0
                                    elif ((i != card[0] or j != card[1]) and primeirav == 0):
                                        score = score -penalty
                                        if(score<0):
                                            score=0
                                        primeirav = 1
                                        penalty=penalty+20
                                    relesed = 0
                        else: 
                            pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                            relesed = 1
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
                if (deck[ind[i][j]] != 0):
                    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                        ccarta = (255, 255, 255)
                        if (pygame.mouse.get_pressed()[0]):
                            if (clicked == 0):
                                cart(deck[ind], True, lrect, crect, l, c, screen)
                                clicked = 1
                                card[0]=i
                                card[1]=j
                                relesed=0
                            else:
                                if(relesed==1):
                                    clicked1 = 1
                                    card[2]=i
                                    card[3]=j
                                    crect1=55 + card[1]*c + card[1]*10
                                    lrect1=405 + card[0]*l + card[0]*10
                                    cart(deck[ind[card[0]][card[1]]], isinbotton(crect1, lrect1), lrect1, crect1, l, c, screen)
                                    cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                    if (deck[ind[card[0]][card[1]]] == deck[ind[i][j]] and (i != card[0] or j != card[1])):
                                        score = score + 100
                                        deck[ind[card[0]][card[1]]] = 0
                                        deck[ind[i][j]] = 0
                                        primeirav = 0
                                    elif ((i != card[0] or j != card[1]) and primeirav == 0):
                                        score = score -penalty
                                        if(score<0):
                                            score=0
                                        primeirav = 1
                                        penalty=penalty+20
                                    relesed=0
                        else: 
                            pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                            relesed=1
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
                if (deck[ind[i][j]] != 0):
                    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                        ccarta = (255, 255, 255)
                        if (pygame.mouse.get_pressed()[0]):
                            if (clicked == 0):
                                cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                clicked = 1
                                card[0]=i
                                card[1]=j
                                relesed=0
                            else:
                                if(relesed==1):
                                    clicked1 = 1
                                    card[2]=i
                                    card[3]=j
                                    crect1=55 + card[1]*c + card[1]*10
                                    lrect1=405 + card[0]*l + card[0]*10
                                    cart(deck[ind[card[0]][card[1]]], isinbotton(crect1, lrect1), lrect1, crect1, l, c, screen)
                                    cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                    if (deck[ind[card[0]][card[1]]] == deck[ind[i][j] ]and (i != card[0] or j != card[1])):
                                        score = score + 100
                                        deck[ind[card[0]][card[1]]] = 0
                                        deck[ind[i][j]] = 0
                                        primeirav = 0
                                    elif ((i != card[0] or j != card[1]) and primeirav == 0):
                                        score = score - penalty
                                        if(score<0):
                                            score=0
                                        primeirav = 1
                                        penalty=penalty+20
                                    relesed=0
                        else: 
                            pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                            relesed=1
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
                if (deck[ind[i][j]] != 0):
                    if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                        ccarta = (255, 255, 255)
                        if (pygame.mouse.get_pressed()[0]):
                            if (clicked == 0):
                                cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                clicked = 1
                                card[0]=i
                                card[1]=j
                                relesed=0
                            else:
                                if(relesed==1):
                                    clicked1 = 1
                                    card[2]=i
                                    card[3]=j
                                    crect1=55 + card[1]*c + card[1]*10
                                    lrect1=405 + card[0]*l + card[0]*10
                                    cart(deck[ind[card[0]][card[1]]], isinbotton(crect1, lrect1), lrect1, crect1, l, c, screen)
                                    cart(deck[ind[i][j]], True, lrect, crect, l, c, screen)
                                    if (deck[ind[card[0]][card[1]]] == deck[ind[i][j] ]and (i != card[0] or j != card[1])):
                                        score = score + 100
                                        deck[ind[card[0]][card[1]]] = 0
                                        deck[ind[i][j]] = 0
                                        primeirav = 0
                                    elif ((i != card[0] or j != card[1]) and primeirav == 0):
                                        score = score - penalty
                                        if(score<0):
                                            score=0
                                        primeirav = 1
                                        penalty=penalty+20
                                    relesed=0
                        else: 
                            pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                            relesed=1
                    else: 
                        ccarta = ( 9, 158, 9)
                        pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 0)
                j=j+1
            i=i+1
    
    font.render_to(screen, (20, 20), "Score:", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 30)
    font.render_to(screen, (200, 20), str(score), (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

    #if(wincheck(x) == 0):
    #        return False

    #botao para voltar atraz
    cbback = (255, 255, 0)

    if (mouse[0]>10 and mouse[0]<150 and mouse[1]>660 and mouse[1]<697):
                cbback = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    penalty=0
                    score = 0
                    return False
    
    pygame.draw.rect(screen, cbback, (10, 660, 140, 37), 2)
    font.render_to(screen, (20, 670), "Back", cbback,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

    return True

 


