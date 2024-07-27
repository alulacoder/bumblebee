from random import randint
import pgzrun

WIDTH = 800
HEIGHT = 600
score = 0

game_over = False

bee = Actor("bee")
bee.pos = (100, 100)
flower = Actor("flower")
flower.pos = (randint(0, WIDTH), randint(0, HEIGHT))
background = Actor("background")
background.pos = (WIDTH, HEIGHT)

def draw():
    screen.clear()
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score:" +str(score), color = "red" , topleft = (10,10))
    
    
    if game_over:
        screen.fill("green")
        screen.draw.text("Time's up! Your final score: " + str(score), midtop = (WIDTH/2,10), fontsize = 40, color = "red")


def time_up():
  global game_over
  game_over = True

def place_flower():
  flower.pos = (randint(0, WIDTH), randint(0, HEIGHT))

def update():
    global score
    if keyboard.left:
        bee.x -= 5
    if keyboard.right:
        bee.x += 5
    if keyboard.up:
        bee.y -= 5
    if keyboard.down:
        bee.y += 5
    
    flower_collected = bee.colliderect(flower)

    if flower_collected:
      score = score + 10
      place_flower()

clock.schedule(time_up, 30.0)

pgzrun.go()