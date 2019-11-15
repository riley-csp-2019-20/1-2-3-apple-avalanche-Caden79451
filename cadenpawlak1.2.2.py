# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb

#-----game configuration----
turtleshape = "turtle"
turtlesize = 10
turtlecolor = "Purple"

score = 0

#------countdown variable-------
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#scoreboard variables
leaderboard_file_name = "a112_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter your name.")


#-----initialize turtle-----
Mole1 = trtl.Turtle(shape = turtleshape)
Mole1.color(turtlecolor)
Mole1.shapesize(turtlesize)
Mole1.speed(0)
 
keeper = trtl.Turtle(shape = turtleshape)
keeper.color(turtlecolor)
keeper.shapesize(turtlesize)
keeper.ht()

keeper.penup()
keeper.goto(-370, 270)
keeper.pendown()

font_setup = ("Ariel", 30, "bold")
keeper.clear()
keeper.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(270, 270)


#-----game functions--------
def turtle_clicked(x,y):
    print("Mole1 got clicked")
    change_position()
    update_score()

def change_position():
    Mole1.penup()
    Mole1.ht()
    if not timer_up:
        Mole1x = random.randint(-400, 400)
        Mole1y = random.randint(-300, 300)
        Mole1.goto(Mole1x, Mole1y)
        Mole1.st()

def update_score():
    global score
    score += 1
    print(score)
    keeper.clear()
    keeper.write(score, font=font_setup)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global Mole1

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, Mole1, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, Mole1, score)


#-----events----------------

wn = trtl.Screen()

Mole1.onclick(turtle_clicked)

wn.ontimer(countdown, counter_interval) 

wn.mainloop()