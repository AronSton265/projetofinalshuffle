import pygame
import pygame.freetype

def create(x, screen, font):
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
                if (mouse[0]>lrect and mouse[0]<(lrect + l) and mouse[1]>crect and mouse[1]<(crect + c)):
                    ccarta = (255, 255, 255)
                    if (pygame.mouse.get_pressed()[0]):
                        pygame.draw.rect(screen, ccarta, ( lrect, crect, l, c), 2) 
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
                    return False
    
    pygame.draw.rect(screen, cbback, (10, 660, 140, 37), 2)
    font.render_to(screen, (20, 670), "Back", cbback,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

    return True

 


