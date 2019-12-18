# Import pygame into our program
import pygame
import pygame.freetype

# Define a main function, just to keep things nice and tidy
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
        my_font.render_to(screen, (298.5, 50), "Shuffle", (255, 255, 0),  None, pygame.freetype.STYLE_DEFAULT, 0, 100)

        cb4x3= (255, 255, 0)
        cb4x4= (255, 255, 0)
        cb5x4= (255, 255, 0)
        cb6x5= (255, 255, 0)
        cb6x6= (255, 255, 0)
        cbexit= (255, 255, 0)

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


        pygame.display.flip()

main()