from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import numpy as np
import signal
import time

sense = SenseHat()
sense.clear()
sense.low_light = True

class FireBall:
    def __init__(self,x,y,vx,vy,pwr):
        self.x = x; self.y = y
        self.vx = vx; self.vy = vy
        self.pwr = pwr 
    def charge(self):
        self.pwr += 1
    def launch(self):
        self.x = 0; self.y = 1
    def hit(self):
        self.pwr -= 1
        print('ball hit')
        if self.pwr >=0:
            self.vx *= -1
            self.vy *= -1
            self.move()
    def move(self):
        sense.set_pixel(self.x,self.y,off)
        self.x -= self.vx; self.y -= self.vy
        if self.x in (-1,8):
            self.x += self.vx
            self.vx *= -1
            self.move()
        if self.y in (-1,8):
            self.y +=self.vy
            self.vy *= -1
            self.move()
        
class Block:
    def __init__(self,x,y,pwr):
        self.x = x; self.y = y
        self.pwr = pwr
    def hit(self):
        self.pwr -= 1
        if self.pwr <= 0:
            print(f'{self} was destroyed')
            del self

class Player:
    def __init__(self):
        self.x = np.random.randint(0,8); self.y = 7
        self.pwr =0
    def charging(self):
        self.pwr = (self.pwr +1) % 4
        print(f'Power is now: ',{self.pwr})
        
    def shooting(self):
        print('p1 shoot')
        self.pwr = 0
    
#Controls
def pushed_left(event):
    if event.action != ACTION_RELEASED:
        sense.set_pixel(p1.x,p1.y,off)
        p1.x = abs(p1.x -1)
        sense.set_pixel(p1.x,p1.y,p_clr)
def pushed_right(event):
    if event.action != ACTION_RELEASED:
        sense.set_pixel(p1.x,p1.y,off)
        p1.x = min(p1.x+1,7)
        sense.set_pixel(p1.x,p1.y,p_clr)
def pushed_up(event):
    if event.action != ACTION_RELEASED:
        global shooting
        shooting = True
        print("shoot")
        return shooting
def pushed_down(event):
    if event.action != ACTION_RELEASED:
        global charging
        charging = True
        print('charging')
        return charging
    
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right

def GameOver_Interrupt(signum,frame):
    sense.show_message("Game Over.",scroll_speed=0.1)
    exit()
        
signal.signal(signal.SIGINT, GameOver_Interrupt)

#Set Up
off = [0,0,0]
p_clr = [128,128,0]
ball_dict = {0: [255,153,51],
             1: [255,85,0],
             2: [255,0,0],
             3: [255,102,204]}
block_dict = {0: [0,0,0],
              1: [192,192,192],
              2: [128,128,128],
              3: [0,128,128],
              4: [0,0,128],
              5: [0,0,255]}

level_blocks = [0]*16
for idx in range(len(level_blocks)):
    level_blocks[-idx] = Block(idx % 8, int(np.floor(idx/8)),np.random.randint(0,6))
    sense.set_pixel(level_blocks[-idx].x,
                    level_blocks[-idx].y,
                    block_dict[level_blocks[-idx].pwr])
    
for block in level_blocks:
    if block.pwr ==0:
        level_blocks.remove(block)

print(level_blocks)
p1 = Player()
sense.set_pixel(p1.x,p1.y,p_clr)

balls = []

charging = False
shooting = False

alive = True
#Game Loop
while alive:
    time.sleep(0.5)
    #respond to user input
    if shooting == True:
        balls.append(FireBall(p1.x,6,0,1,p1.pwr))
        p1.shooting()
        shooting = False
    if charging == True:
        p1.charging()
        #balls.append(FireBall(p1.x,6,0,0,1))
        #charging == False
        print("charge loop")
        charging = False
    #update positions
    #check for collisions
    for ball in balls:
        ball.move()
        if (ball.x,ball.y) == (p1.x,p1.y):
             alive = False
             print('gameover')
             break
        for block in level_blocks:
            if (ball.x,ball.y) == (block.x,block.y):
                ball.hit()
                if ball.pwr <0:
                    balls.remove(ball)
                block.hit()
                sense.set_pixel(block.x,block.y,block_dict[block.pwr])
                if block.pwr <=0:
                    level_blocks.remove(block)
                break
    for ball in balls:
        sense.set_pixel(ball.x,ball.y,ball_dict[ball.pwr])

            
#repeat
    #display final results
    #loop
    #eval(input('test'))
