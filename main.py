#-------imports-------
import turtle as trtl
import turtle as bird
import random as ran
import time as times


#-------setting background and images-------
bird.speed(0)
wn = trtl.Screen()
wn.tracer(False)
wn.setup(width=1.0, height=1.0)
pipeSpeed = 3
wn.bgpic("background.gif")
pipe = "pipe.gif"
pipe2 = "pipe2.gif"
back2 = "background2.gif"
redbird = "redbird.gif"
bluebird = "bluebird.gif"
yellowbird = "yellowbird.gif"
explosion = "explosion.gif"
redbird2 = "redbirdfall.gif"
redbirdfall = "redbirdfall.gif"
yellowbirdfall = "yellowbirdfall.gif"
bluebirdfall = "bluebirdfall.gif"
redbirdup = "redbirdup.gif"
bluebirdup = "bluebirdup.gif"
yellowbirdup = "yellowbirdup.gif"
wn.addshape(explosion)
wn.addshape(yellowbird)
wn.addshape(bluebird)
wn.addshape(redbird)
wn.addshape(back2)
wn.addshape(pipe)
wn.addshape(pipe2)
wn.addshape(redbird2)
wn.addshape(bluebirdfall)
wn.addshape(yellowbirdfall)
wn.addshape(redbirdfall)
wn.addshape(redbirdup)
wn.addshape(bluebirdup)
wn.addshape(yellowbirdup)
#-------setting up score writing-------
font_setup = ("Times New Roman", 30, "normal")
font_setup2 = ("Times New Roman", 70, "normal")
font_setup3 = ("Times New Roman", 40, "normal")
sc = trtl.Turtle()
sc.pu()
sc.hideturtle()
sc.goto(0, 300)

score_writer = trtl.Turtle()
score_writer.pu()
score_writer.hideturtle()
score_writer.goto(-295, 230)

#-------preparing for code-------
global click
global answer
global v1
global v2
global birdfall_type
boolz = True
bool2 = True
temp = True
click = 0
v1 = 0
v2 = 0
birdfall_type = redbirdfall
answer = 0
global choose_time
choose_time = True
global done
done = True
global score
score = 0
time = 0
y_vel = 0
ycord = 0
distance = 400

p = trtl.Turtle()
p2 = trtl.Turtle()
p3 = trtl.Turtle()
p4 = trtl.Turtle()
p5 = trtl.Turtle()
p6 = trtl.Turtle()
p.pu()
p2.pu()
p3.pu()
p4.pu()
p5.pu()
p6.pu()
p.shape(pipe2)
p2.shape(pipe)
p3.shape(pipe2)
p4.shape(pipe)
p5.shape(pipe2)
p6.shape(pipe)
bird.pu()
bird_type = redbird

p.hideturtle()
p2.hideturtle()
p3.hideturtle()
p4.hideturtle()
p5.hideturtle()
p6.hideturtle()

b0 = trtl.Turtle()
b0.pu()
b0.shape(back2)

b1 = trtl.Turtle()
b1.pu()
b2 = trtl.Turtle()
b2.pu()
b3 = trtl.Turtle()
b3.pu()

box = trtl.Turtle()
box.hideturtle()

def updateHeight(num):
  global height
  global height2
  global height3
  if num == 1:
    height = ran.randint(350, 720)
    wn.update()
    return height
  elif num == 2:
    height2 = ran.randint(350, 720)
    wn.update()
    return height2
  elif num == 3:
    height3 = ran.randint(350, 720)
    wn.update()
    return height3


#-------Choosing a bird-------
def choose_bird():
  global bool2
  while (bool2):
    sc.goto(-130, 150)
    sc.write("Pick A Bird", font=font_setup)
    b1.goto(-200, 50)
    b1.shape(yellowbird)
    b2.goto(0, 50)
    b2.shape(bluebird)
    b3.goto(200, 50)
    b3.shape(redbird)
    bool2 = False


def yellow_dos(x, y):
  sc.goto(0, 300)
  sc.clear()
  global click
  global answer
  global bird_type
  global birdfall_type
  bird_type = yellowbirdup
  birdfall_type = yellowbirdfall
  b1.hideturtle()
  b2.hideturtle()
  b3.hideturtle()
  answer == 1
  click += 1
  choose_time == False


def blue_dos(x, y):
  sc.goto(0, 300)
  sc.clear()
  global click
  global answer
  global bird_type
  global birdfall_type
  bird_type = bluebirdup
  birdfall_type = bluebirdfall
  b1.hideturtle()
  b2.hideturtle()
  b3.hideturtle()
  answer == 2
  click += 1
  choose_time == False


def red_dos(x, y):
  sc.goto(0, 300)
  sc.clear()
  global click
  global answer
  global bird_type
  global birdfall_type
  bird_type = redbirdup
  birdfall_type = redbirdfall
  b1.hideturtle()
  b2.hideturtle()
  b3.hideturtle()
  answer == 3
  click += 1
  choose_time == False


#-------bird falling and going up-------
def run_gravity():
  global birdfall_type
  global ycord
  ycord = bird.ycor()
  global y_vel
  bird.goto(bird.xcor(), bird.ycor() + y_vel)
  y_vel -= 5
  global v1
  global v2
  if (answer == 1):
    v1 = 27
    v2 = 32
  if (answer == 2):
    v1 = 35
    v2 = 33
  if (answer == 3):
    v1 = 32
    v2 = 28
  if y_vel <= -20:
    global birdfall_type
    bird.shape(birdfall_type)
    bird.update()
  else:
    bird.shape(bird_type)
    bird.update()
  if (ycord > -240):
    bird.ontimer(run_gravity, 50)
  else:
    bird.goto(-400, -250)
    bird.update()
    bird.shape(birdfall_type)
    times.sleep(0.5)
    bird.hideturtle()
    wn.update()


def mouse_going_up(x, y):
  global v1
  global v2
  if (answer == 1):
    v1 = 28
    v2 = 27
  if (answer == 2):
    v1 = 28
    v2 = 25
  if (answer == 3):
    v1 = 26
    v2 = 26
  global ycord
  ycord = bird.ycor()
  global y_vel
  y_vel = 0
  bird.goto(bird.xcor(), bird.ycor() + y_vel)
  y_vel += 23
  bird.update()


def going_up():
  global v1
  global v2
  if (answer == 1):
    v1 = 28
    v2 = 27
  if (answer == 2):
    v1 = 28
    v2 = 25
  if (answer == 3):
    v1 = 26
    v2 = 26
  global ycord
  ycord = bird.ycor()
  global y_vel
  y_vel = 0
  bird.goto(bird.xcor(), bird.ycor() + y_vel)
  y_vel += 19
  bird.update()

#-------checking if the bird collides with every indvidual pipe-------
def pipe_collison():
  global v1
  global v2
  if (bird.xcor() + 30 == p.xcor()):
    if ((bird.ycor() + v1 <= height - 380
         and bird.ycor() - v2 >= height - 510)):
      global score
      sc.clear()
      score += 1
      sc.write(score, font=font_setup)
      if score == score:
        box.clear()
      wn.update()
    else:
      bird.hideturtle()
      bird.shape(explosion)
      bird.stamp()
      stop_pipes()
      wn.update()
      game_over(score)
      times.sleep(0.3)
      bird.clear()

  if (bird.xcor() + 30 == p3.xcor()):
    if (bird.ycor() + v1 <= height2 - 380
        and bird.ycor() - v2 >= height2 - 510):
      sc.clear()
      score += 1
      sc.write(score, font=font_setup)
      if score == score:
        box.clear()
        
      wn.update()
    else:
      bird.hideturtle()
      bird.shape(explosion)
      bird.stamp()
      stop_pipes()
      wn.update()
      game_over(score)
      times.sleep(0.3)
      bird.clear()

  if (bird.xcor() + 30 == p5.xcor() + 23):
    if (bird.ycor() + v1 <= height3 - 380
        and bird.ycor() - v2 >= height3 - 520):
      sc.clear()
      score += 1
      sc.write(score, font=font_setup)
      if score == score:
        box.clear()
      wn.update()
    else:
      bird.hideturtle()
      bird.shape(explosion)
      bird.stamp()
      stop_pipes()
      wn.update()
      game_over(score)
      times.sleep(0.3)
      bird.clear()


#-------stopping pipes-------
def stop_pipes():
  p.goto(-700, p.ycor())
  p2.goto(-700, p2.ycor())
  p.hideturtle()
  p2.hideturtle()
  p3.goto(-700, p3.ycor())
  p4.goto(-700, p4.ycor())
  p4.hideturtle()
  p3.hideturtle()
  p5.goto(-700, p5.ycor())
  p6.goto(-700, p6.ycor())
  p5.hideturtle()
  p6.hideturtle()
  wn.update()


#-------drawing and moving the pipes-------
def move_pipe():
  height = updateHeight(1)
  height2 = updateHeight(2)
  height3 = updateHeight(3)
  p.goto(800, height)
  p2.goto(800, height - 950)
  p3.goto(1300, height2)
  p4.goto(1300, height2 - 950)
  p5.goto(1800, height3)
  p6.goto(1800, height3 - 950)
  p.showturtle()
  p2.showturtle()
  p3.showturtle()
  p4.showturtle()
  p5.showturtle()
  p6.showturtle()

  while True:
    if (bird.ycor() == -250):
      stop_pipes()
      game_over(score)
    else:
      if p.xcor() <= -650 or p2.xcor() <= -650:
        height = updateHeight(1)
        p.goto(900, height)
        p2.goto(900, height - 950)
      else:
        p.backward(pipeSpeed)
        p2.backward(pipeSpeed)
      if p3.xcor() <= -650 or p4.xcor() <= -650:
        height2 = updateHeight(2)
        p3.goto(900, height2)
        p4.goto(900, height2 - 950)
      else:
        p3.backward(pipeSpeed)
        p4.backward(pipeSpeed)
      if p5.xcor() <= -650 or p6.xcor() <= -650:
        height3 = updateHeight(3)
        p5.goto(900, height3)
        p6.goto(900, height3 - 950)
      else:
        p5.backward(pipeSpeed)
        p6.backward(pipeSpeed)
      pipe_collison()
      wn.update()
      box.clear()


def game_over(score):
  global bool
  global boolz
  while (bool == True):
    bird.goto(-400, -250)
    sc.clear()
    sc.goto(-270, 240)
    sc.write("Game Over", font=font_setup2)
    sc.goto(-190, 160)
    sc.write("Final Score:", font=font_setup3)
    sc.goto(160, 160)
    sc.write(score, font=font_setup3)
    box.clear()
    bool = False

def starter():
  global temp
  if (click == 0 and temp == True):
    bird.goto(-400, 150)
    bird.hideturtle()
    bird.update()
    if (choose_time == True):
      choose_bird()
      b1.onclick(yellow_dos)
      b2.onclick(blue_dos)
      b3.onclick(red_dos)
      starter()
    if click == 1:
      temp = False
      wn.update()

starter()

#moving the bird to its jumping spot and key press setup
bird.hideturtle()
bird.goto(-400, 250)
bird.showturtle()
bird.shape(bird_type)
bird.onkeypress(going_up, "space")
bird.onkeypress(going_up, "Up")
bird.onkeypress(going_up, "w")
bird.onscreenclick(mouse_going_up)
run_gravity()
bird.listen()
sc.write(score, font=font_setup)
bool = True
  
#if bird hits the ground the pipes stop otherwise the pipes move
while (bool == True and click == 1):
  move_pipe()
if (bird.ycor() <= -250):
  stop_pipes()
  game_over(score)
  bool = False

wn.mainloop()