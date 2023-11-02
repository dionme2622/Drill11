from pico2d import *
import game_framework

import game_world
from bird import Bird
from grass import Grass
from boy import Boy

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global bird1, bird2, bird3, bird4, bird5, bird6, bird7, bird8, bird9, bird10
    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    bird1 = Bird(400, 400)
    bird2 = Bird(440, 400)
    bird3 = Bird(480, 400)
    bird4 = Bird(520, 400)
    bird5 = Bird(560, 400)
    bird6 = Bird(400, 360)
    bird7 = Bird(440, 360)
    bird8 = Bird(480, 360)
    bird9 = Bird(520, 360)
    bird10 = Bird(560, 360)


    game_world.add_object(bird1, 1)
    game_world.add_object(bird2, 1)
    game_world.add_object(bird3, 1)
    game_world.add_object(bird4, 1)
    game_world.add_object(bird5, 1)
    game_world.add_object(bird6, 1)
    game_world.add_object(bird7, 1)
    game_world.add_object(bird8, 1)
    game_world.add_object(bird9, 1)
    game_world.add_object(bird10, 1)



def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    #delay(0.1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

