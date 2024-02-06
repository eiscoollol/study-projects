import pygame as game
game.init()
screen=game.display.set_mode([960,720])
clock=game.time.Clock()
myasshurts=True
cubex=screen.get_width()/2
cubey=screen.get_height()/2
def move(x,y):
    global cubex
    global cubey
    global cube
    cube=game.draw.rect(screen,[0,10,255],[cubex,cubey,50,50],0,5)
    if game.key.get_pressed()[game.K_UP]:
        cubey=y-5
    if game.key.get_pressed()[game.K_DOWN]:
        cubey=y+5
    if game.key.get_pressed()[game.K_LEFT]:
        cubex=x-5
    if game.key.get_pressed()[game.K_RIGHT]:
        cubex=x+5
while myasshurts:
    for event in game.event.get():
        if event.type==game.QUIT:
            myasshurts=False
    screen.fill([255,255,255])
    move(cubex,cubey)
    game.display.update()
    clock.tick(60)
game.quit()