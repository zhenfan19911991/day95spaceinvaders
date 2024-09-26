from turtle import Turtle
import time
import turtle

WEAPON_STEP = 5
DEFENDER_STEP = 5


class Defender():
    def __init__(self):
        self.defender_0 = Turtle()
        self.defender_0.penup()
        self.defender_0.shape("tank")
        self.defender_0.goto(0, -360)
        self.defender_1 = Turtle()
        self.defender_1.penup()
        self.defender_1.shape("tank")
        self.defender_1.goto(-340, -400)
        self.defender_2 = Turtle()
        self.defender_2.penup()
        self.defender_2.shape("tank")
        self.defender_2.goto(-380, -400)
        self.weapon_list = []
        self.defender_life = 1

    def move_forward(self):
        if self.defender_0.xcor() <= 370:
            self.defender_0.forward(DEFENDER_STEP)

    def move_backward(self):
        if self.defender_0.xcor() >=-370:
            self.defender_0.backward(DEFENDER_STEP)

    def create_weapons(self):
        if len(self.weapon_list) > 0:
            if time.time() - self.weapon_list[-1].create_time >2:
                self.bullet = Turtle()
                self.bullet.create_time = time.time()
                self.bullet.penup()
                self.bullet.shape('circle')
                self.bullet.shapesize(stretch_wid=0.3, stretch_len=0.3)
                self.bullet.goto(self.defender_0.pos())
                self.bullet.setheading(90)
                self.weapon_list.append(self.bullet)
        elif len(self.weapon_list) == 0:
            self.bullet = Turtle()
            self.bullet.create_time = time.time()
            self.bullet.penup()
            self.bullet.shape('circle')
            self.bullet.shapesize(stretch_wid=0.3, stretch_len=0.3)
            self.bullet.goto(self.defender_0.pos())
            self.bullet.setheading(90)
            self.weapon_list.append(self.bullet)


    def move_weapons(self):
        for bu in self.weapon_list:
            bu.forward(WEAPON_STEP)
            if bu.ycor() > 460:
                self.weapon_list.remove(bu)
                bu.goto(-1000,1000)


    def defender_hit(self, bullet_list):
        for bullet in bullet_list:
            if self.defender_0.distance(bullet.pos())<13:
                bullet.goto(-1000,1000)
                bullet_list.remove(bullet)
                self.defender_0.goto(0, -365)
                if self.defender_1.pos() != (-1000,1000):
                    self.defender_1.goto(-1000,1000)
                elif self.defender_1.pos() == (-1000,1000) and self.defender_2.pos() != (-1000,1000):
                    self.defender_2.goto(-1000,1000)
                else:
                    self.defender_life = 0












