# imports from pygame library

from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=1000, height=600, background="white")


# creates the size of the screen for the game

def setInitialValues():
    global RocketLength, yRocket, ySpeed, flame, startMessage, endMessage, gameRunning
# globals functions created so it can be used later in code
    RocketLength = 400
    yRocket = 100
    ySpeed = 0
    flame = 0
    endMessage = 0
# endmessage is 0 as this appears after gamerunning is false, flame only occurs when mouse is clicked
    startMessage = screen.create_text(600, 300, text="Click to move rocket up", font="Verdana 18", fill="red", anchor=W)
# pop-up msg at the start
    gameRunning = True


# boolean condition for the game to continue running


def drawRocket():
# drawing the rocket shape
    global RocketBody, RocketNose

    RocketBody = screen.create_rectangle(RocketLength, yRocket, RocketLength + 50, yRocket + 100, fill="black",
                                         outline="white")
    RocketNose = screen.create_polygon(RocketLength, yRocket, RocketLength + 25, yRocket - 25, RocketLength + 50,
                                       yRocket, fill="red", outline="white")


# mouse clicking process. It enables the movement of the rocket up.
def mouse_clicked(event):
    global ySpeed, flame

    if gameRunning == True:
# if statement used when game is running
        ySpeed = ySpeed - 10
# increase the rocket's upward speed
        flame = screen.create_polygon(RocketLength, yRocket + 100, RocketLength + 50, yRocket + 100, RocketLength + 25,
                                      yRocket + 210, fill="yellow")


def mouse_not_clicked(event):
# when mouse is not clicked, the flame will disappear
    global flame

    screen.delete(flame)


def endGame():
# variables for when the game ends
    global startMessage, endMessage, gameRunning

    gameRunning = False

    screen.delete(startMessage)

    endMessage = screen.create_text(600, 300, text="Game Over." + "Try again" + ".", font="Verdana 18", anchor=W,
                                    fill="red")

    screen.update()
    sleep(2)
    screen.delete(endMessage)


def startRocketProgram():
    global yRocket, ySpeed, flame, startMessage

    setInitialValues()

    while yRocket < 600:
# Keep the game running until the rocket goes below 600 in height level

        yRocket = yRocket + ySpeed
# Update the rocket's vertical position using its current speed
        ySpeed = ySpeed + 1
# Gravity is constantly increasing the rocket's downward speed
        drawRocket()
        screen.update()
        sleep(0.05)
        screen.delete(RocketBody, RocketNose, flame)

    endGame()

    startRocketProgram()
# restart the game


root.after(500, startRocketProgram)
# start the game on the screen
screen.bind("<Button-1>", mouse_clicked)
# makes the function of mouse clicking work when user clicks
screen.bind("<ButtonRelease-1>", mouse_not_clicked)
screen.pack()
screen.focus_set()
root.mainloop()
