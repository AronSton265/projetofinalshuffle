import pygame
import pygame.freetype

def create(x, screen, font):
    if (x == 6):
        l=480/4 -10
        c=600/3 -10
        i=0
        while (i<4):
            j=0
            while (j<3):
                lrect=405 + i*l + i*10
                crect=55 + j*c + j*10
                pygame.draw.rect(screen, (9, 158, 9), ( lrect, crect, l, c), 0)
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
                pygame.draw.rect(screen, (9, 158, 9), ( lrect, crect, l, c), 0)
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
                pygame.draw.rect(screen, (9, 158, 9), ( lrect, crect, l, c), 0)
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
                pygame.draw.rect(screen, (9, 158, 9), ( lrect, crect, l, c), 0)
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
                pygame.draw.rect(screen, (9, 158, 9), ( lrect, crect, l, c), 0)
                j=j+1
            i=i+1

 


