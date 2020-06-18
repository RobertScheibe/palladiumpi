#!/usr/bin/python3
# Import the pygame library and initialise the game engine
import pygame, sys
from paddle import Paddle
from ball import Ball
from pygame.locals import *

# Open a new window was 700x500
WIDTH=640
HEIGHT=480

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

def terminate():
    pygame.quit()
    sys.exit()

def showTextScreen(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WIDTH / 2), int(HEIGHT / 2))
    screen.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WIDTH / 2) - 3, int(HEIGHT / 2) - 3)
    screen.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play. \'Select\' to quit. \'B\' to reset.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WIDTH / 2), int(HEIGHT / 2) + 100)
    screen.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        clock.tick() 

def checkForKeyPress():
    global scoreA, scoreB
    for event in pygame.event.get():
        if event.type == QUIT:      #event is quit 
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:   #event is escape key
                terminate()
            else:
                return event.key   #key found return with it
        elif event.type == JOYBUTTONDOWN or event.type == JOYAXISMOTION:
            if (js1.get_button(8) == 1 or js2.get_button(8) == 1):
                terminate()
            elif (js1.get_button(0) == 1 or js2.get_button(0) == 1):
                scoreA=0
                scoreB=0
            return 1
                                                                                                                                                                     # no quit or key events in queue so return None    
    return None

def main():
    global clock, screen, BASICFONT, BIGFONT, js1, js2
    pygame.init()
    pygame.mouse.set_visible(False)

    # Define some colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size, FULLSCREEN)
    pygame.display.set_caption("Pong")
    effect=pygame.mixer.Sound('Pong.wav')
     
    #joystick or gamepad init
    pygame.joystick.init()
    print ("Joystics: ", pygame.joystick.get_count())
    js1 = pygame.joystick.Joystick(0)
    js1.init()
    js2 = pygame.joystick.Joystick(1)
    js2.init()
     
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200
     
    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = WIDTH-30
    paddleB.rect.y = 200
     
    ball = Ball(WHITE,10,10)
    ball.rect.x = int(WIDTH/2-5)
    ball.rect.y = 195
     
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
     
    # Add the car to the list of objects
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)
     
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
     
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
     
    #Initialise player scores
    global scoreA, scoreB
    scoreA = 0
    scoreB = 0
     
    showTextScreen('Pong')
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                         carryOn=False
     
        #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)    
        """
        
        if js1.get_axis(1) < 0:
            paddleA.moveUp(5)
        if js1.get_axis(1) > 0:	
            paddleA.moveDown(5)
        if js2.get_axis(1) < 0:
            paddleB.moveUp(5)
        if js2.get_axis(1) > 0:	
            paddleB.moveDown(5)  
        if (js1.get_button(8) == 1 or js2.get_button(8) == 1):
            terminate()
        if (js1.get_button(9) == 1 or js2.get_button(9) == 1):
            showTextScreen('-Pause-')
            
        # --- Game logic should go here
        all_sprites_list.update()
        
        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=WIDTH-10:
            scoreA+=1
            ball.velocity[0] = -ball.velocity[0]
            effect.play()
        if ball.rect.x<=0:
            scoreB+=1
            ball.velocity[0] = -ball.velocity[0]
            effect.play()
        if ball.rect.y>HEIGHT-10:
            ball.velocity[1] = -ball.velocity[1]
            effect.play()
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]     
            effect.play()
            
        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
          ball.bounce()
          effect.play()
        
        # --- Drawing code should go here
        # First, clear the screen to black. 
        screen.fill(BLACK)
        #Draw the net
        pygame.draw.line(screen, WHITE, [int(WIDTH/2), 0], [int(WIDTH/2), HEIGHT], 5)
        
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 
     
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (int(WIDTH/2-WIDTH/4),10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (int(WIDTH/2+WIDTH/4),10))
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
         
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

if __name__ == '__main__':
    main()

