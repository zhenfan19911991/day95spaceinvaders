from turtle import Turtle
import random



BUNKER_SIZE = 0.5


class Bunkers():
    def __init__(self):
        self.bunker_list = []
        x_list = [*range(-300, -150, int(20*BUNKER_SIZE)), *range(-75, 75, int(20*BUNKER_SIZE)), *range(150,300, int(20*BUNKER_SIZE))]
        for y in range(-150, -230, int(-20*BUNKER_SIZE)):
            for x in x_list:
                self.bunker = Turtle()
                self.bunker.penup()
                self.bunker.shape('square')
                self.bunker.shapesize(stretch_wid=BUNKER_SIZE, stretch_len=BUNKER_SIZE)
                self.bunker.color(random.choice(['gray', 'black']))
                self.bunker.goto((x, y))
                self.bunker_list.append(self.bunker)

    def bunker_hit(self, weapon_list, bullet_list):
        for bunker in self.bunker_list:
            for weapon in weapon_list:
                if bunker.distance(weapon.pos()) <= 10*BUNKER_SIZE+1:
                    bunker.goto(-1000,1000)
                    self.bunker_list.remove(bunker)
                    weapon.goto(-1000,1000)
                    weapon_list.remove(weapon)

        #for bunker in self.bunker_list:
            for bullet in bullet_list:
                if bunker.distance(bullet.pos()) <= 10*BUNKER_SIZE+1:
                    bunker.goto(-1000,1000)
                    self.bunker_list.remove(bunker)
                    bullet.goto(-1000, 1000)
                    bullet_list.remove(bullet)





