from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import numpy as np
import signal
import time

from game_objects import*

sense = SenseHat()
sense.clear()
sense.low_light = True

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        sense.set_pixel(p1.x,p1.y,off)
        p1.x = abs(p1.x -1)
        sense.set_pixel(p1.x,p1.y,ball_dict[p1.pwr])
def pushed_right(event):
    if event.action != ACTION_RELEASED:
        sense.set_pixel(p1.x,p1.y,off)
        p1.x = min(p1.x+1,7)
        sense.set_pixel(p1.x,p1.y,ball_dict[p1.pwr])
def pushed_up(event):
    if event.action != ACTION_RELEASED:
        global shooting
        shooting = True
        print("shoot")
        sense.set_pixel(p1.x,p1.y,ball_dict[0])
        return shooting
def pushed_down(event):
    if event.action != ACTION_RELEASED:
        global charging
        charging = True
        print('charging')
        return charging
        
def pushed_middle(event):
    if event.action != ACTION_RELEASED:
        print('test1')
        global alive
        if alive == False:
            print('test2')
            alive = True
        else:
            print('test fail')
        
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle

def GameOver_Interrupt(signum,frame):
    sense.show_message("Game Over.",scroll_speed=0.1)
    exit()
        
signal.signal(signal.SIGINT, GameOver_Interrupt)

#Set Up
off = [0,0,0]
p_clr = [128,128,0]
ball_dict = {0: [128,128,0],
             1: [255,153,51],
             2: [255,85,0],
             3: [255,0,0],
             4: [255,102,204]}
block_dict = {0: [0,0,0],
              1: [128,128,128],
              2: [0,128,128],
              3: [0,128,255],
              4: [0,0,255],
              5: [0,0,80]}
alive = False
charging = False
shooting = False
balls = []
blocks = []
turn = 0
score = 0

p1 = Player()

def set_up():
    print('starting')
    global p1
    p1.pwr =0
    global score
    score = 0
    global turn
    turn = 0
    global blocks
    blocks = [0]*16
    global balls
    balls = []
    for idx in range(len(blocks)):
        blocks[-idx] = Block(idx % 8, int(np.floor(idx/8)),np.random.randint(0,6))
        sense.set_pixel(blocks[-idx].x,
                        blocks[-idx].y,
                        block_dict[blocks[-idx].pwr])
    
    for block in blocks:
        if block.pwr ==0:
            blocks.remove(block)
    
    sense.set_pixel(p1.x,p1.y,ball_dict[p1.pwr])
    global charging
    charging = False
    global shooting
    shooting = False
    global alive
    alive = True
    
    return blocks,p1,play()
#Game Loop
def play():
    print('playing')
    global turn
    global alive
    global shooting
    global charging
    global score
    while alive:
        turn = (turn +1) % 40
        time.sleep(0.5)
        if shooting == True:
            balls.append(FireBall(p1.x,6,0,1,p1.pwr))
            p1.shooting()
            shooting = False
        if charging == True:
            sense.set_pixel(p1.x,p1.y,ball_dict[(p1.pwr+1)%5])
            p1.charging()
            charging = False
        for ball in balls:
            ball.move()
            if (ball.x,ball.y) == (p1.x,p1.y):
                alive = False
                post_game()
                break
            for block in blocks:
                if (ball.x,ball.y) == (block.x,block.y):
                    ball.hit()
                    if ball.pwr <1:
                        try:
                            balls.remove(ball)
                        except ValueError:
                            pass
                    for pwr in range(0,ball.pwr):
                        balls.append(FireBall(ball.x,ball.y,
                                              2*np.random.randint(0,2)-1,
                                              ball.vy,ball.pwr))
                    block.hit()
                    sense.set_pixel(block.x,block.y,block_dict[block.pwr])
                    if block.pwr ==0:
                       blocks.remove(block)
                       score +=1
                
        for ball in balls:
            sense.set_pixel(ball.x,ball.y,ball_dict[ball.pwr])
        if turn == 39:
            print('new blocks!')
            for block in blocks:
                sense.set_pixel(block.x,block.y,off)
                block.y +=1
            #for idx in range(0,8):
             #   blocks.append(Block(idx % 8, 0,np.random.randint(0,6)))
            for new in range(0,8):
                blocks.append(Block(new,0,np.random.randint(0,6)))
            for idx in range(0,len(blocks)):
                sense.set_pixel(blocks[idx].x,
                                blocks[idx].y,
                                block_dict[blocks[idx].pwr])
                

def post_game(): 
    global alive
    alive = False
    sense.clear(255,0,0)
    time.sleep(2)
    sense.show_message("Game Over")
    time.sleep(0.5)
    sense.show_message(f'Score: {score}')
    while alive == False:
        sense.show_message("Play Again?")
    print('exit post')
    set_up()

set_up()
 