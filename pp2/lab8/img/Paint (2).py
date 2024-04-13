import pygame, sys
import pygame.gfxdraw

pygame.init()
clock = pygame.time.Clock()
screen_width = 700
screen_height =500


# Colors
white = (255, 255, 255)
blue = (67,238,250)
red = (255, 0, 0)
black = (0, 0, 0)
green = (38,245,45)
pink = (255,192,203)
orange = (255,165,0)
yellow = (255,255,0)
violet = (177, 3, 252)
pencolour = black

# Create screen
screen =  pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Paint")
screen.fill((white))

# Backgound
backimg = pygame.image.load("paint.jpg").convert_alpha()
backimg = pygame.transform.scale(backimg, (screen_width, screen_height))
screen.blit(backimg, (0,0))

#rect for the drawing area
draw_area = (119, 17, 562, 465)

# Value of rect (x,y, width, height)
col1= (22, 81, 30, 34)
col2= (56, 81, 34, 34)
col3= (22, 120, 30, 33)
col4= (56, 120, 34, 32)
col5= (22, 156, 30, 33)
col6= (56, 156, 34, 32)
col7= (22, 192, 30, 33)
col8= (56, 192, 34, 32)

#Rect that highlight which button is selected
buttonselect = (22, 81, 30, 34)

#Function to draw color box
def drawrectangle():    
    pygame.draw.rect(screen, black, col1)
    pygame.draw.rect(screen,blue, col2,)
    pygame.draw.rect(screen, red, col3)
    pygame.draw.rect(screen, green, col4)
    pygame.draw.rect(screen, pink, col5)
    pygame.draw.rect(screen, orange, col6)
    pygame.draw.rect(screen, yellow, col7)
    pygame.draw.rect(screen, violet, col8)
    # figure
    pygame.draw.rect(screen, black, (13, 320, 40, 20))
    pygame.draw.circle(screen, black, (80, 330), 12 )    
drawrectangle()


#Set mouse cursor for pencil 
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
is_rect = False
is_circle = False

#Gameloop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
      # Create border
        pygame.draw.rect(screen, white, buttonselect, 2)


        t = pygame.mouse.get_pressed()
        if t[0] == 1:     
            mousepos = pygame.mouse.get_pos()

            # Drawing on screen
            if 122 < mousepos[0] < 678 and 21 < mousepos[1] < 480:
                
                if is_rect:
                    pygame.draw.rect(screen, pencolour, (mousepos[0], mousepos[1], 100, 70), 2)
                elif is_circle:
                    pygame.draw.circle(screen, pencolour, (mousepos[0], mousepos[1]), 40, 2 )

                else: 
                    pygame.draw.ellipse(screen, pencolour, (mousepos[0], mousepos[1], 12,12))

                

            
            # Rectangle
            elif 13 < mousepos[0] < 53 and 320< mousepos[1] < 340:
                is_rect = True
                is_circle = False
                drawrectangle()  
                pygame.draw.rect(screen, black, (13, 320, 40, 20))
                pygame.draw.rect(screen, white, (13, 320, 40, 20), 2)
                
            # Circle
            elif 68 < mousepos[0] < 92 and 318< mousepos[1] < 342:
                is_circle = True
                is_rect = False
                drawrectangle() 
                pygame.draw.circle(screen, black, (80, 330), 12)    
                pygame.draw.circle(screen, white, (80, 330), 12, 2 )
                 
            # Colors    
            elif 22 < mousepos[0] < 52 and 81 < mousepos[1] < 115:
                pencolour = black
                drawrectangle()         
                buttonselect = (22, 81, 30, 34)
                is_rect = False
                is_circle = False
                
            elif 56 < mousepos[0] < 90 and 81 < mousepos[1] < 115:
                pencolour = blue
                drawrectangle()
                buttonselect = (56, 81, 34, 34)
                is_rect = False
                is_circle = False
                
            elif 22 < mousepos[0] < 52 and 120 < mousepos[1] < 153:
                pencolour = red
                drawrectangle()
                buttonselect = (22, 120, 30, 33)
                is_rect = False
                is_circle = False
                
            elif 56 < mousepos[0] < 90 and 120 < mousepos[1] < 152:
                pencolour = green
                drawrectangle()
                buttonselect = (56, 120, 34, 32)
                is_rect = False
                is_circle = False
                
            elif 22 < mousepos[0] < 52 and 156 < mousepos[1] < 189:
                pencolour = pink
                drawrectangle()
                buttonselect = (22, 156, 30, 33)
                is_rect = False
                is_circle = False
                
            elif 56 < mousepos[0] < 90 and 156 < mousepos[1] < 188:
                pencolour = orange
                drawrectangle()
                buttonselect = (56, 156, 34, 32)
                is_rect = False
                is_circle = False
                
            elif 22 < mousepos[0] < 52 and 192 < mousepos[1] < 225:
                pencolour = yellow
                drawrectangle()
                buttonselect = (22, 192, 30, 33)
                is_rect = False
                is_circle = False
                
            elif 56 < mousepos[0] < 90 and 192 < mousepos[1] < 224:
                pencolour = violet
                drawrectangle()
                buttonselect = (56, 192, 34, 32)
                is_rect = False
                is_circle = False
            #Eraser
            elif 13 < mousepos[0] < 54 and 247 < mousepos[1] < 285:
                pencolour = white
                drawrectangle()
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
                is_rect = False
                is_circle = False
            #Pencil
            elif 59 < mousepos[0] < 97 and 247 < mousepos[1] < 288:
                pencolour = black
                drawrectangle()
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                buttonselect = (22, 81, 30, 34)
                is_rect = False
                is_circle = False
                
            elif 15 < mousepos[0] < 96 and 363 < mousepos[1] < 400:                
                pygame.draw.rect(screen, white, draw_area)
                is_rect = False
                is_circle = False

        
        pygame.display.update()
        clock.tick(120)