import pygame
import pygame.freetype

def create(x, screen):
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

 


def main():

    # Initialize pygame, with the default parameters
    pygame.init()

    #resolution
    res = (1280, 700)

    #creation of the window and fontt
    screen = pygame.display.set_mode(res)
    my_font = pygame.freetype.Font("HOMOARAK.ttf", 24)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()

            if (event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    exit()

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))

        #main screen creation
        #my_font.render_to(screen, (298.5, 50), "Shuffle", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 100)

        x=(5*4)/2
        create(x, screen)


        pygame.display.flip()

main()