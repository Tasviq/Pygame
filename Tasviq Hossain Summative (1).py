'''
Tasviq Hossain
May 29th, 2019
'''
import pygame
import random
import time
#*************************************************
def collide(Rectx1 , Recty1, Rectx2,Recty2,Ballx1,Bally1, Ballx2,Bally2):
    if Ballx2<Rectx1 or Rectx2<Ballx2 or Bally2<Recty1 or Recty2<Bally2:
        return False
    else:
        return True

def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
        time.sleep(1)
        if n ==0:
            print('Begin!')
#*************************************************

#def colours and screen size, background
red,green,blue = (255,0,0),(0,255,0),(0,0,255)
torq,purple,yellow = (0,255,255),(255,0,255),(255,255,0)
black,white,grey = (0,0,0),(255,255,255),(180,180,180)
colours = [red,blue,white,grey,green,purple,yellow,torq]
rectColour = random.choice (colours)
ballColour = random.choice (colours)
size = (width,height)=(600,500)
background = pygame.image.load ("moon.jpg")
pygame.mixer.init ()
explosion = pygame.mixer.Sound ("explosion.ogg")
point = pygame.mixer.Sound ("bell.ogg")

#Initialize pygame and make screen
pygame.init ()
clock = pygame.time.Clock()
screen = pygame.display.set_mode (size)
xRect,yRect,xspeed = 300,445,0 #Rectangle coordinates, speed
xBall,yBall,xBallSpeed,yBallSpeed = random.randint (1,599),0,0,random.randint (4,9) #Bomb x position,speed, y position, speed  
score = 0
lives = 3

font = pygame.font.Font('freesansbold.ttf', 20)
font_= pygame.font.Font ('freesansbold.ttf',30)
text = font.render('Current Score: ', True, green, blue) 
textRect = text.get_rect()
textRect.center = (100, 50)
textRect2 = text.get_rect()
textRect2.center = (100, 100)
textRect3=text.get_rect()
textRect3.center = (450, 75)

#Main Loop
play = input ("Press 'Yes' to begin playing: ")
if play == 'yes' or play == 'Yes':
    running = True
    countdown (5)
else:
    running = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    yBall = yBall+yBallSpeed

    #key down event
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            xspeed=4
        if event.key == pygame.K_LEFT:
            xspeed=-4

    #key up event
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            xspeed=0
        if event.key == pygame.K_LEFT:
            xspeed=0

    #Collision
    #Check if collision occured(Need to call function 4 times)- one for each side
    Rx1,Ry1,Rw,Rh,Bx1,By1,r = xRect,yRect,100,100,xBall,yBall,13 
    if collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1 , By1, Bx1 + r, By1)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1 ,By1, Bx1 - r, By1)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1, By1, Bx1, By1 + r)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1, By1, Bx1, By1 -r): 
        yBall = 600
        score+=10
        point.play()
        print ("Current Score: ",score)
        rectColour,ballColour = random.choice (colours),random.choice (colours)
        if score == 100:
            print ("Level 1 Completed")
            running = False
    else:
        if yBall>=500:
            lives -= 1
            print ("                        Lives left: ",lives)
            explosion.play()
            rectColour,ballColour = random.choice (colours), random.choice (colours)
            if lives == 0 :
                running = False
                
    #logic
    if xRect>width-105:
        xRect = width - 105
    if xRect<0:
        xRect = 0
    if yBall>=499:
        yBall=0
        xBall = random.randint (1,599)
        yBallSpeed =random.randint (6,10)
    xRect= xRect +xspeed                
    xRect= xRect +xspeed
    
    #draw
    screen.blit(background,[-75,0])
    screen.blit(font.render('Current Score: ' +str(score), True, green, black),textRect)
    screen.blit(font.render('Lives: ' +str(lives), True, red, black),textRect2)
    screen.blit(font_.render('LEVEL 1', True, red, white),textRect3)
    pygame.draw.rect (screen,rectColour,[xRect,yRect,100,10])
    centre,radius = ([xBall,yBall],random.randint(8,20))
    pygame.draw.circle (screen,ballColour, centre,radius)
    clock.tick(80)
    pygame.display.flip ()

#-----------------------------------------------------------------------------------

#LEVEL 2 CODE
background = pygame.image.load ("oceanBack.jpg")
xRect,yRect,xspeed = 300,445,0 #Shield coordinates, speed
rangeSpeeds = [-6,-4,-2,0,2,4,6]
xBall,yBall,xBallSpeed,yBallSpeed = random.randint (1,599),0,random.choice(rangeSpeeds),random.randint (4,7) #Bomb x position,speed, y position, speed  
xBall2,yBall2,xBallSpeed2,yBallSpeed2 = random.randint (1,599),0,random.randint(-2,2),random.randint (2,4)
lives+=1
#****************************************************

#Main Loop
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    yBall,yBall2 = yBall+yBallSpeed,yBall2+yBallSpeed2
    xBall,xBall2 = xBall+xBallSpeed, xBall2+xBallSpeed2
    
    #key down event
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            xspeed=4
        if event.key == pygame.K_LEFT:
            xspeed=-4
    #key up event
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            xspeed=0
        if event.key == pygame.K_LEFT:
            xspeed=0

    #Collision
    #Check if collision occured(Need to call function 4 times)- one for each side
    Rx1,Ry1,Rw,Rh,Bx1,By1,r = xRect,yRect,100,100,xBall,yBall,13
    if collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1 , By1, Bx1 + r, By1)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1 ,By1, Bx1 - r, By1)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1, By1, Bx1, By1 + r)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, Bx1, By1, Bx1, By1 -r):
        yBall = 600
        point.play()
        score+=10
        print ("Current Score: ",score)
        rectColour,ballColour = random.choice (colours),random.choice (colours)
    else:
        if yBall>=500:
            lives -= 1
            print ("                        Lives left: ",lives)
            explosion.play()
            rectColour,ballColour = random.choice (colours), random.choice (colours)
            if lives == 0:
                running = False
                
    if collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, xBall2 , yBall2, xBall2 + r, yBall2)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, xBall2 ,yBall2, xBall2 - r, yBall2)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, xBall2, yBall2, xBall2, By1 + r)\
       or collide(Rx1,Ry1, Rx1 + Rw, Ry1 + Rh, xBall2, yBall2, xBall2, By1 -r):
        yBall2=600
        score+=10
        point.play ()
        print ("Current Score: ",score)
        rectColour,ballColour = random.choice (colours),random.choice (colours)
    else:
        if yBall2 >=500:
            lives-=1
            print ("                        Lives left: ",lives)
            explosion.play()
            rectColour,ballColour = random.choice (colours), random.choice (colours)
            if lives == 0:
                running = False

    #logic
    if xRect>width-105:
        xRect = width - 105
    if xBall >=width-10 or xBall<10:
        xBallSpeed= -xBallSpeed
    if xBall2 >=width-10 or xBall2<10:
        xBallSpeed2= -xBallSpeed2
    if xRect<0:
        xRect = 0
    if yBall>=499:
        yBall=0
        xBall = random.randint (1,599)
        yBallSpeed =random.randint (4,7)
    if yBall2>=499:
        yBall2=0
        xBall2 = random.randint (1,599)
        yBallSpeed2 =random.randint (2,4)
    xRect= xRect +xspeed                
    xRect= xRect +xspeed
    
    #draw
    screen.blit(background,[0,0])
    pygame.draw.rect (screen,rectColour,[xRect,yRect,100,10])
    centre,radius = ([xBall,yBall],random.randint(8,15))
    pygame.draw.circle (screen,random.choice (colours), centre,radius)
    pygame.draw.circle (screen,ballColour, [xBall2,yBall2],random.randint (4,9))
    screen.blit(font.render('Current Score:' +str(score), True, green, blue),textRect)
    screen.blit(font.render('Lives:' +str(lives), True, green, blue),textRect2)
    screen.blit (font_.render('LEVEL 2', True, black, yellow),textRect3)
    clock.tick(80)
    pygame.display.flip ()
pygame.quit ()
