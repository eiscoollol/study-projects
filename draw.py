#setup
import pygame as game
game.init()
screen=game.display.set_mode([960,720])
frames=game.time.Clock()
myasshurts=True

#draw (lol)
def draw():
    global sexyline
    global block
    sexyline=game.draw.line(screen,[0,0,0],[0,screen.get_height()-7],[screen.get_width(),screen.get_height()-7],12)
    block=game.draw.rect(screen,[0,10,255],[480,360,50,50],0,5)

#main
while myasshurts:
    for event in game.event.get():
        if event.type==game.QUIT:
            myasshurts=False
    game.Surface.fill(screen,[255,255,255])
    draw()
    game.display.update()
    frames.tick(60)
game.quit()