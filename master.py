# Imports
import pygame
import pygame.freetype
import game

#global variables
ingame = False
x = 0
firsttime = 0
t = 0
clicked = 0
deck =[ 0]
ind =[0]
music = 1

#essentials to play the game
def playgame(screen, font, deck, ind):
        global ingame
        global x
        global clicked
        global t

        ingame = game.create(x, screen, font, deck, ind)
        if (t<300 and game.clicked != 0 and game.deck[ind[game.card[0]][game.card[1]]] != 0):
            t=t+1
            crect=55 + game.card[1]*game.c + game.card[1]*10
            lrect=405 + game.card[0]*game.l + game.card[0]*10
            game.cart(game.deck[ind[game.card[0]][game.card[1]]], game.isinbotton(crect, lrect), lrect, crect, game.l, game.c, screen)
            if (game.clicked1 != 0):
                crect1=55 + game.card[3]*game.c + game.card[3]*10
                lrect1=405 + game.card[2]*game.l + game.card[2]*10
                game.cart(game.deck[ ind[game.card[2]] [game.card[3]] ], game.isinbotton(crect1, lrect1), lrect1, crect1, game.l, game.c, screen)

        else:
            t=0
            game.setclick(0)
            game.primeirav = 0

        if (game.wincheck(x) == 0):
            font.render_to(screen, (340, 300), "YOU WON", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 100)

#crete the main menu
def creatmeno(screen, my_font):
        global ingame
        global x
        global deck
        global ind
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
                    ind = game.indice(x)
                    ingame = True
                        
            if (mouse[1]>290 and mouse[1]<327):
                cb4x4 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb4x4= (255, 0, 0)
                    x = 8
                    deck = game.createdeck(x)
                    ind = game.indice(x)
                    ingame = True
                        
            if (mouse[1]>340 and mouse[1]<377):
                cb5x4 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb5x4= (255, 0, 0)
                    x = 10
                    deck = game.createdeck(x)
                    ind = game.indice(x)
                    ingame = True
                        
            if (mouse[1]>390 and mouse[1]<427):
                cb6x5 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb6x5= (255, 0, 0)
                    x = 15
                    deck = game.createdeck(x)
                    ind = game.indice(x)
                    ingame = True
                        
            if (mouse[1]>440 and mouse[1]<477):
                cb6x6 = (255, 255, 255)
                if (pygame.mouse.get_pressed()[0]):
                    cb6x6= (255, 0, 0)
                    x = 18
                    deck = game.createdeck(x)
                    ind = game.indice(x)
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

# main function
def main():
    global ingame
    global music

    # Initialize pygame, with the default parameters
    pygame.init()

    #resolution
    res = (1280, 700)

    #creation of the window and fontt
    screen = pygame.display.set_mode(res)
    my_font = pygame.freetype.Font("HOMOARAK.ttf", 24)

    #starts the music
    pygame.mixer.music.load('bensound-enigmatic.ogg')
    pygame.mixer.music.play(-1)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()

            if (event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_m):
                    if(music ==1):
                        pygame.mixer.music.stop()
                        music=0
                    else:
                        pygame.mixer.music.load('bensound-enigmatic.ogg')
                        pygame.mixer.music.play(-1)
                        music=1
                if(event.key == pygame.K_ESCAPE):
                    exit()

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))

        if (ingame == False):
            creatmeno(screen, my_font)
        else: playgame(screen, my_font, deck, ind)

        pygame.display.flip()

main()