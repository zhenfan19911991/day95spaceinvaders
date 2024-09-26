from turtle import Turtle, Screen, TurtleScreen, Shape
import time
from functools import partial
from aliens import Aliens
from bunkers import Bunkers
from defenders import Defender
from tkinter import PhotoImage
from score import Score


screen = Screen()

tank = PhotoImage(file="tank.gif").subsample(15, 15)
screen.addshape("tank", Shape("image", tank))
TurtleScreen._RUNNING=True
screen.bgcolor('white')
screen.setup(width=800, height = 900)
screen.title('Space Invaders')
screen.tracer(0)

aliens = Aliens()
bunkers = Bunkers()
defenders = Defender()
score = Score()

screen.listen()

screen.onkey(fun = defenders.move_forward , key = "Right" )
screen.onkey(fun = defenders.move_backward, key = "Left" )
screen.onkey(fun = defenders.create_weapons, key = "space" )

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    aliens.move_aliens()
    defenders.move_weapons()
    aliens.alien_hit(defenders.weapon_list)
    bunkers.bunker_hit(defenders.weapon_list, aliens.bullet_list)
    defenders.defender_hit(aliens.bullet_list)
    aliens.bullet_hit(defenders.weapon_list)
    score.add_score(aliens.point)
    score.update()
    if defenders.defender_life ==0 or len(aliens.alien_list) ==0 or aliens.alien_ycor_min <= -355:
        game_is_on = False

screen.clear()
text = Turtle()
text.color('black')
text.penup()
text.hideturtle()
text.goto(0,0)

if defenders.defender_life ==0:
    text.write(f"Game Over. Your final Score is {score.score}.", align='center', font=("Counier", 30, 'normal'))
elif len(aliens.alien_list) ==0:
    text.write(f"Congrats, You have hit all aliens. Your final Score is {score.score}.", align='center', font=("Counier", 30, 'normal'))
elif aliens.alien_ycor_min <= -355:
    text.write(f"Game Over. The Aliens have arrived. Your final Score is {score.score}.", align='center',
               font=("Counier", 30, 'normal'))




screen.exitonclick()