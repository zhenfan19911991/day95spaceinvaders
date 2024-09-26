from turtle import Turtle
import random

BULLET_STEP = 5
ALIEN_DOWN_STEP = 1
ALIEN_MOVE_STEP = 1.5

class Aliens():
    def __init__(self):
        self.alien_list = []
        self.bullet_list = []
        for y in range(380, 170, -50):
            for x in range(-300, 320, 60):
                self.alien = Turtle()
                self.alien.penup()
                self.alien.shape("turtle")
                self.alien.goto((x, y))
                self.alien_list.append(self.alien)
        self.alien_count = len(self.alien_list)
        self.bullet_frequency = 1000
        self.point = 0
        self.alien_ycor_min = 170

    def move_aliens(self):
        self.alien_ycor_min = min([alien.ycor() for alien in self.alien_list])
        alien_xcor = [alien.xcor() for alien in self.alien_list]
        alien_xcor_max = max(alien_xcor)
        alien_xcor_min = min(alien_xcor)
        for alien in self.alien_list:
            alien.forward(ALIEN_MOVE_STEP)
            if random.randint(1, int(self.bullet_frequency)) == 1:
                self.create_bullets(alien)
            if alien_xcor_min <=- 390:
                alien.setheading(270)
                alien.forward(ALIEN_DOWN_STEP)
                alien.setheading(0)
            elif alien_xcor_max >= 380:
                alien.setheading(270)
                alien.forward(ALIEN_DOWN_STEP)
                alien.setheading(180)

        self.move_bullets()

    def create_bullets(self, alien):
        self.bullet = Turtle()
        self.bullet.penup()
        self.bullet.shape('square')
        self.bullet.shapesize(stretch_wid=0.2, stretch_len=0.6)
        self.bullet.color('gray')
        self.bullet.goto(alien.pos())
        self.bullet.setheading(270)
        self.bullet_list.append(self.bullet)

    def move_bullets(self):
        for bu in self.bullet_list:
            bu.forward(BULLET_STEP)
            if bu.ycor() <-460:
                bu.goto(-1000,1000)
                self.bullet_list.remove(bu)

    def alien_hit(self, weapons):
        for weapon in weapons:
            for alien in self.alien_list:
                if weapon.distance(alien.pos()) < 14:
                    alien.goto(-1000, 1000)
                    weapon.goto(-1000, 1000)
                    self.alien_list.remove(alien)
                    weapons.remove(weapon)
                    self.point += 1
        if len(self.alien_list) == int(self.alien_count/2):
            self.bullet_frequency = 500
        elif len(self.alien_list) == int(self.alien_count/4):
            self.bullet_frequency = 100


    def bullet_hit(self, weapon_list):
        for bullet in self.bullet_list:
            for weapon in weapon_list:
                if bullet.distance(weapon.pos()) <= 7:
                    bullet.goto(-1000,1000)
                    self.bullet_list.remove(bullet)
                    weapon.goto(-1000,1000)
                    weapon_list.remove(weapon)







