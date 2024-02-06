import pygame as game
game.init()
screen=game.display.set_mode([960,720])
myasshurts=True
time=game.time.Clock()
cubey=screen.get_height()/2
yspeed=0
cube=lambda:game.draw.rect(screen,[0,10,255],[screen.get_width()/2,cubey,50,50],0,5)
pressed=0
def checkholding(key):
    global pressed
    if game.key.get_pressed()[key]:
        pressed=1
    else:
        pressed=0
def gravity(speed):
    global pressed
    global yspeed
    global cubey
    cube()
    yspeed=speed+1
    if game.key.get_pressed()[game.K_UP] and not pressed:
        yspeed=-12
    checkholding(game.K_UP)
    cubey=cubey+yspeed
    if cubey>=screen.get_height():
        yspeed=0
while myasshurts:
    for event in game.event.get():
        if event.type==game.QUIT:
            myasshurts=False
    screen.fill([255,255,255])
    gravity(yspeed)
    game.display.update()
    time.tick(60)
game.quit()