from time import sleep
from os import system
import sys, getopt
from player import Player
from control import KeyboardControl
from obstacles import Obstacles


'''Main function, which performs argument check,  assign parameters, create instances and run the game.'''
def main(argv):
    # Set up default values for the following arguements.
    canvasLen = 50
    canvasHig = 40
    diff = "medium"
    obstaclesRatio = 0.1
    pauseTime = 0.2

    # Perfrom the arguements check.
    try:
       opts, args = getopt.getopt(argv,"l:h:d:",["canvasLen=", "canvasHig=", "diff="])
    except getopt.GetoptError:
       print ("game.py -l <int> -h <int> -d <easy/medimu/hard>")
       sys.exit(2)
    
    for opt, arg in opts:

        # Width of the canvas is cliped between 20 and 120.
        if opt in ("-l", "--canvasLen"):
            try: 
                if int(arg) > 120:
                    canvasLen = 120
                elif int(arg) < 20:
                    canvasLen = 20
                else:
                    canvasLen = int(arg)
            except ValueError:
                print ("Error: --canvasLen can only take <int> type.")
                sys.exit(2)                

        # Height of the canvas is cliped between 20 and 40.
        if opt in ("-h", "--canvasHig"):
            try:
                if int(arg) > 40:
                    canvasHig = 40
                elif int(arg) < 20:
                    canvasHig = 20
                else:
                    canvasHig = int(arg)
            except ValueError:
                print(arg)
                print ("Error: --canvasHig can only take <int> type.")
                sys.exit(2) 

        # Three levels of difficults are available.
        if opt in ("-d", "--diff"):
            if arg == "easy":
                obstaclesRatio = 0.05
            elif arg == "medium":
                obstaclesRatio = 0.1
            elif arg == "hard":
                obstaclesRatio = 0.2
            else:
                print ("Error: --diff can only take 'easy', 'medimu', or 'hard'.")
                sys.exit(2)

    # Create a player, the spaceship, centered at the middle of the canvas.
    player = Player(canvasLen//2, canvasHig//2, canvasLen-1, canvasHig-1)

    # Create a controler to handle the keyboard inputs.
    control = KeyboardControl(player)
    control.activate()
    
    # Create obstacles.
    obstacles = Obstacles(canvasLen, canvasHig, obstaclesRatio)
    canvas = obstacles.generateObs()

    # Count how many line the spaceship has acrossed.
    linePassed = 0
    while True:
        system('cls')

        # Update the position of the spaceship and obstacles. Perform the collision check. 
        obstacles.updateObs(canvas, linePassed, player)

        linePassed+=1
        sleep(pauseTime)

if __name__ == "__main__":
   main(sys.argv[1:])
