import numpy as np
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED

sense = SenseHat()

off = [0,0,0]

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
        if self.x in (-1,8) and self.y in (-1,8):
            print('corner ball!')
            self.x += self.vx
            self.y += self.vy
            self.vx *= -1
            self.vy *= -1
            self.move()
        if self.x in (-1,8):
            self.x += self.vx
            self.vx *= -1
            if self.vy ==0:
                self.vy = 2*np.random.randint(0,2)-1 
            self.move()
        if self.y in (-1,8):
            self.y +=self.vy
            self.vy *= -1
            if self.vx ==0 and self.y ==7:
                self.vx = 2*np.random.randint(0,2)-1
            self.move()
        
class Block:
    def __init__(self,x,y,pwr):
        self.x = x; self.y = y
        self.pwr = pwr
    def hit(self):
        self.pwr = max(0,self.pwr-1)
        if self.pwr == 0:
            print(f'{self} was destroyed')

class Player:
    def __init__(self):
        self.x = np.random.randint(0,8); self.y = 7
        self.pwr =0
    def charging(self):
        self.pwr = (self.pwr +1) % 5
        print(f'Power is now: ',{self.pwr})
        
    def shooting(self):
        print('p1 shoot')
        self.pwr = 0