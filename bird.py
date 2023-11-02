# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework

# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'




# Bird Run Speed
# fill here
PIXEL_PER_METER = (20.0 / 0.6)      # 10 pixel 당 30cm   100 pixel에 3m
RUN_SPEED_KMPH = 20.0       # 시속
RUN_SPEED_MPH = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPH / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER
# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5
# fill here




class Idle:

    @staticmethod
    def enter(bird, e):
        bird.frame = 0
        pass

    @staticmethod
    def exit(bird, e):
        pass

    @staticmethod
    def do(bird):
        if bird.action == 2 or bird.action == 1:
            if bird.frame == 5:
                bird.action -= 1
            bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        elif bird.action == 0:
            if bird.frame == 4:
                bird.action = 2
            bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time
        if bird.x >= 1600 - 20:
            bird.dir = -1
        elif bird.x <= 20:
            bird.dir = 1
        # if bird.frame == 0:
        #     bird.action = bird.action - 1
        #     if bird.action == -1:
        #         bird.action = 2
    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 183, bird.action * 168, 183, 168, bird.x, bird.y, 50, 50)
        elif bird.dir == -1:
            bird.image.clip_composite_draw(int(bird.frame) * 183, bird.action * 168, 183, 168, 0, 'h', bird.x, bird.y, 50, 50)







class StateMachine:
    def __init__(self, bird):
        self.bird = bird
        self.cur_state = Idle

    def start(self):
        self.cur_state.enter(self.bird, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.bird)

    def handle_event(self, e):
        pass

    def draw(self):
        self.cur_state.draw(self.bird)





class Bird:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.action = 2
        self.face_dir = 1
        self.dir = 1
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.state_machine.draw()
