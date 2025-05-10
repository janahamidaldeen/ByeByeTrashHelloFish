###################
# Assignment 5
# Coded by Jana Hamidaldeen
# Made on January 18nd 2021
###################

#imports
from tkinter import *
from random import *
from math import *
from time import *
import random

#setup
root = Tk()
s = Canvas(root, width=1000, height=600, background="LightSteelBlue1")
s.pack()

#main globals
global itemSpeeds, numFish, numPlastic, numCan
itemSpeeds = []
numFish = 10
numPlastic = 10
numCan = 20 

#image imports
def imageImports():
  global startScreen, fisherman, fishImage, waterImage, canImage

  startScreen = PhotoImage(file = "startScreen")
  fisherman = PhotoImage(file = "fisherman")
  fishImage = PhotoImage(file = "fish.png")
  waterImage = PhotoImage(file="water.png")
  canImage = PhotoImage(file = "can.png")

#setting up all of the initial values
def setInitialValues():
  global score, scoreText, timing, timeText
  global xFish, yFish, xPlastic, yPlastic, xCan, yCan, fishDrawings, plasticDrawings, canDrawings
  global hookActive, hook, line, ySpeed, yLine, xLine, yHook, xHook
 
  #score board and countdown system
  score = 0
  scoreText = []
  timing = 30
  timeText = []

  #items in ocean array
  xFish = []
  yFish = []
  xPlastic = []
  yPlastic = []
  xCan = []
  yCan = []
  fishDrawings = []
  plasticDrawings = []
  canDrawings = []

  #hook variables
  hookActive = False
  hook = []
  line = []
  ySpeed = 20 
  yLine = 170
  xLine = 615
  yHook = yLine+100
  xHook = xLine+10

  #random x and y integers for each item
  for i in range(numFish):
    xFish.append(randint(-1000, 500 ))
    yFish.append(randint(400, 550))
    fishDrawings.append(0)
  for i in range(numPlastic):
    xPlastic.append(randint(-1000, 500))
    yPlastic.append(randint(400, 550))
    plasticDrawings.append(0)
  for i in range(numCan):
    xCan.append(randint(-1000, 500))
    yCan.append(randint(400, 550))
    canDrawings.append(0)


#setting up background
def backgroundSetup():
  global cloud1, cloud2, cloud3

  #clouds
  cloudColours = ["white", "seashell1"]
  for cloud in range(1,3):
    colour = random.choice(cloudColours)
    cloudX = randint(0,800)
    cloud1 = s.create_arc(cloudX+100, 75, cloudX+325, 225, fill = colour, start = 360, extent = 180, outline = "")
    cloud2 = s.create_arc(cloudX+225, 100, cloudX+400, 200, fill = colour, start = 360, extent = 180, outline = "")
    cloud3 = s.create_arc(cloudX+50, 125, cloudX+150, 175, fill = colour, start = 360, extent = 180, outline = "")

  #ocean
  s.create_rectangle(0,350, 1000, 600, fill="royalblue1", outline="")

  #fisherman
  s.create_image(500, 267, image=fisherman)

  #boat
  s.create_polygon(100, 300, 150, 400, 400, 400, 450, 300, fill="saddle brown", outline= "black", width=2)
  s.create_line(250, 150, 250, 300, fill
  ="black", width=3)
  s.create_polygon(250, 150, 250, 230, 350, 185, fill="firebrick1", outline="black", width=3)

  #countdown box
  s.create_rectangle(650, 200, 800, 300, fill = "royalblue1", outline = "royalblue1" )
  s.create_text(725, 220, text = "countdown", font = "Helvetica 15 bold", fill = "white" )

  #score box
  s.create_rectangle(850, 200, 950, 300, fill = "royalblue1", outline = "royalblue1" )
  s.create_text(900, 220, text = "score", font = "Helvetica 15 bold", fill = "white" )

#draw each item and update its position
def drawFish():
  global fishDrawings
  for i in range(numFish):
    fishDrawings[i] = s.create_image(xFish[i], yFish[i], image=fishImage)

def updateFishPositions():
  global fishDrawings
  
  for i in range(numFish):
    xFish[i] = xFish[i] + itemSpeeds[i]

def drawPlastic():
  global plasticDrawings
  for i in range(numPlastic):
    plasticDrawings[i] = s.create_image(xPlastic[i], yPlastic[i], image=waterImage)

def updatePlasticPositions():
  global plasticDrawings
  for i in range(numPlastic):
    xPlastic[i] = xPlastic[i] + itemSpeeds[i]

def drawCan():
  global canDrawings, xCan
  for i in range(numCan):
    canDrawings[i] = s.create_image(xCan[i], yCan[i], image=canImage)

def updateCanPositions():
  global canDrawings
  for i in range(numCan):
    xCan[i] = xCan[i] + itemSpeeds[i] 

#draw hook and update its position
def drawHook():
  global hook, line
  line = s.create_line(xLine, 170, xLine, yLine+100, width=2) 
  hook = s.create_line(xLine, yHook, xHook, yHook, width=2, fill="grey")

def updateHookPosition():
  global ySpeed, yLine, yHook, hookActive

  #only move hook is hookActive is true; aka if the space button is clicked
  if hookActive == True:
    yLine = yLine + ySpeed
    yHook = yHook + ySpeed
    if yLine == 490:
      ySpeed = -1 * ySpeed
    elif yLine == 170:
      ySpeed = 20
      hookActive = False

#check for what the hook collides with
def checkForCaught():
  global score, scoreText
  global yHook, xLine
  global distancePlastic, distanceCan, distanceFish
  global xPlastic, yPlastic, xCan, yCan, xFish, yFish
  global plasticDrawings, canDrawings, fishDrawings

  #check the distance between the hook and the item
  for i in range(numFish):
    distanceFish = sqrt( (xLine-xFish[i])**2 + (yHook-yFish[i])**2 )
    if distanceFish <= 16:
      #delete that fish
      s.delete(fishDrawings[i])
      xFish[i] = 0
      score = score - 1

  for i in range(numPlastic):
    distancePlastic = sqrt( (xLine-xPlastic[i])**2 + (yHook-yPlastic[i])**2 )
    if distancePlastic <= 16:
      #delete that plastic
      s.delete(plasticDrawings[i])
      xPlastic[i] = 0
      score = score + 3

  for i in range(numCan):
    distanceCan = sqrt( (xLine-xCan[i])**2 + (yHook-yCan[i])**2 )
    if distanceCan <= 16:
      #delete that can
      s.delete(canDrawings[i])
      xCan[i] = 0
      score = score + 1

  #display score
  scoreText = s.create_text(900, 260, text = score, font = "Helvetica 30 bold italic", fill = "white" )

#setup the game countdown
def countdown():
  global timing, timeText, timeStart
  timeNow = time()
  timeElapsed = timeNow - timeStart
  #if one second passes update the timing variable that is displayed on the screen
  if timeElapsed >= 1:
    timing = timing - 1
    timeStart = time()
  #display time
  timeText = s.create_text(725, 260, text = str(timing)+"s", font = "Helvetica 30 bold italic", fill = "white" )

def runGame():
  global ySpeed, yHook, hookActive, scoreText, timeStart, timeText
  imageImports()
  setInitialValues()
  backgroundSetup()
  timeStart = time()
  #while the countdown is still running, have the game run
  while timing > 0:
    countdown()
    updateFishPositions()
    updatePlasticPositions()
    updateCanPositions()
    updateHookPosition()
    drawFish()
    drawPlastic()
    drawCan()
    drawHook()
    checkForCaught() 

    s.update() 
    sleep(0.05)
    s.delete(hook, line, timeText, scoreText)

    for i in range(numFish):
      s.delete(fishDrawings[i])
    for i in range(numPlastic):
      s.delete(plasticDrawings[i])
    for i in range(numCan):
      s.delete(canDrawings[i])
  #if the countdown reaches 0, display endScreen
  else:
    endScreen()

def startingScreen():
  global start
  imageImports()
  setInitialValues()

  s.create_image(500, 267, image=startScreen)
  s.create_rectangle(450, 400, 650, 500, fill="LightSteelBlue1")
  s.create_rectangle(730, 400, 930, 500, fill="LightSteelBlue1")
  s.create_text(550, 450, text ="easy", font = "Helvetica 30 bold", fill = "royalblue1" )
  s.create_text(830, 450, text ="hard", font = "Helvetica 30 bold", fill = "royalblue1" )
  s.create_image(60, 458, image=fishImage)
  s.create_image(60, 502, image=canImage)
  s.create_image(60, 543, image=waterImage)
  s.create_text(140, 458, text ="= -1 point", font = "Helvetica 12 bold", fill = "white" )
  s.create_text(140, 500, text ="= +1 point", font = "Helvetica 12 bold", fill = "white" )
  s.create_text(140, 545, text ="= +3 points", font = "Helvetica 12 bold", fill = "white" )
  s.create_text(700, 550, text ="use spacebar to lower hook", font = "Helvetica 20 bold", fill = "LightSteelBlue1" )



  #once start is false, button 1 will not be active
  start = True
  if start == True:
    s.bind("<Button-1>", startScreenClick)

def startScreenClick(event):
  global  start, itemSpeeds
  
  #if start is true, check for the mouse x and y positions
  if start == True:
    xMouse = event.x
    yMouse = event.y 
    #if easy button is clicked, set the itemSpeeds low
    if 450 <= xMouse <= 650 and 400 <= yMouse <= 500:
      start = False
      itemSpeeds = []
      for i in range(numCan):
        itemSpeeds.append(randint(2, 4)) 
      runGame()
    #if the hard button is clicked, set the itemSpeeds high
    elif 730 <= xMouse <= 930 and 400 <= yMouse <= 500:
      start = False
      itemSpeeds = []
      for i in range(numCan):
        itemSpeeds.append(randint(4, 6))
      runGame()

def spacebarClick(event):
  global hookActive

  #if the space button is clicked, let hookActive run
  if event.keysym == "space":
    hookActive = True

def endScreen():
  global score, finalScoreText
  imageImports()

  s.create_image(500, 267, image=startScreen)
  s.create_rectangle(450, 400, 650, 500, fill="LightSteelBlue1")
  s.create_rectangle(730, 400, 930, 500, fill="LightSteelBlue1")
  s.create_text(550, 450, text = "replay", font = "Helvetica 30 bold", fill = "royalblue1" )
  s.create_text(830, 450, text ="stop", font = "Helvetica 30 bold", fill = "royalblue1" )
  finalScoreText = s.create_text(700, 200, text = "score = "+ str(score), font = "Helvetica 30 bold", fill = "royalblue1" )

  s.bind("<Button-1>", endScreenClick)

def endScreenClick(event):
  global finalScoreText, cloud1, cloud2, cloud3
  xMouse = event.x
  yMouse = event.y 
  #restart the game is the replay button is clicked
  if 450 <= xMouse <= 650 and 400 <= yMouse <= 500:   
    s.delete(finalScoreText, cloud1, cloud2, cloud3)
    startingScreen()
  #end the entire program if stop is clicked
  elif 730 <= xMouse <= 930 and 400 <= yMouse <= 500:
    s.destroy()

#setup
root.after( 0, startingScreen)
s.bind("<Key>", spacebarClick) 
s.focus_set() 
root.mainloop()