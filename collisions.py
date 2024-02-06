import pygame as game
game.init()
screen=game.display.set_mode([960,720])
clock=game.time.Clock()
myasshurts=True
while myasshurts:
    for events in game.event.get():
        if events.type==game.QUIT:
            myasshurts=False
    screen.fill('white')
    game.display.update()
    clock.tick(60)