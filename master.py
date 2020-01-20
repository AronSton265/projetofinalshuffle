# Import pygame into our program
import pygame
import pygame.freetype
import game

ingame = False
x = 0
firsttime = 0
t = 0
clicked = 0
deck =[ [0,0,0],[0,0,0],[0,0,0],[0,0,0] ]

def playgame(screen, font, deck):
        global ingame
        global x
        global clicked
        global t
        
        ingame = game.create(x, screen, font, deck)
        if (t<300 and game.clicked != 0):
            t=t+1
            crect=55 + game.card[1]*game.c + game.card[1]*10
            lrect=405 + game.card[0]*game.l + game.card[0]*10
            game.cart(game.deck[game.card[0]][game.card[1]], game.isinbotton(crect, lrect), lrect, crect, game.l, game.c, screen)
        else:
            t=0
            game.setclick(0)

        k = pygame.key.get_pressed()
        if (k[pygame.K_l]):
            pygame.draw.rect(screen, (255, 255, 255), ( 405, 55, 480/4 -10, 600/3 -10), 2)

def creatmeno(screen, my_font):
        global ingame
        global x
        global deck
    #main screen creation
        my_font.render_to(screen, (298.5, 50), "Shuffle", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 100)

        #defenition of the collors
        cb4x3= (255, 255, 0)
        cb4x4= (255, 255, 0)
        cb5x4= (255, 255, 0)
        cb6x5= (255, 255, 0)
        cb6x6= (255, 255, 0)
        cbexit= (255, 255, 0)

        mouse = pygame.mouse.get_pos()

        #bottons code
        if (mouse[0]>590 and mouse[0]<690):  
            if (mouse[1]>240 and mouse[1]<277):
                cb4x3 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb4x3= (255, 0, 0)
                    x = 6
                    deck = game.createdeck(x)
                    ingame = True
                        
            if (mouse[1]>290 and mouse[1]<327):
                cb4x4 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb4x4= (255, 0, 0)
                    x = 8
                    ingame = True
                        
            if (mouse[1]>340 and mouse[1]<377):
                cb5x4 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb5x4= (255, 0, 0)
                    x = 10
                    ingame = True
                        
            if (mouse[1]>390 and mouse[1]<427):
                cb6x5 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb6x5= (255, 0, 0)
                    x = 15
                    ingame = True
                        
            if (mouse[1]>440 and mouse[1]<477):
                cb6x6 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb6x6= (255, 0, 0)
                    x = 18
                    ingame = True
                        
            if (mouse[1]>540 and mouse[1]<577):
                cbexit = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    exit()
                        
        

        #botton 4x3
        pygame.draw.rect(screen, cb4x3, (590, 240, 100, 37), 2)
        my_font.render_to(screen, (598, 250), "4x3", cb4x3,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

        #botton 4x4
        pygame.draw.rect(screen, cb4x4, (590, 290, 100, 37), 2)
        my_font.render_to(screen, (598, 300), "4x4", cb4x4,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

        #botton 5x4
        pygame.draw.rect(screen, cb5x4, (590, 340, 100, 37), 2)
        my_font.render_to(screen, (599, 350), "5x4", cb5x4,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

        #botton 6x5
        pygame.draw.rect(screen, cb6x5, (590, 390, 100, 37), 2)
        my_font.render_to(screen, (599, 400), "6x5", cb6x5,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

        #botton 6x6
        pygame.draw.rect(screen, cb6x6, (590, 440, 100, 37), 2)
        my_font.render_to(screen, (599, 450), "6x6", cb6x6,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

        #botton exit
        pygame.draw.rect(screen, cbexit, (590, 540, 100, 37), 2)
        my_font.render_to(screen, (598, 550), "Exit", cbexit,  None, pygame.freetype.STYLE_DEFAULT, 0, 30)

# Define a main function, just to keep things nice and tidy
def main():
    global ingame

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

        if (ingame == False):
            creatmeno(screen, my_font)
        else: playgame(screen, my_font, deck)

        pygame.display.flip()

main()