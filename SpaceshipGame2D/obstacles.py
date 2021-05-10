import random
import collections

''' The Obstacles class is responsable for generate obstacles, update the location of obscales and the player, 
    and handling the collision.
'''
class Obstacles:
    def __init__(self, canvasLen, canvasHig, obstaclesRatio):
        self.canvasLen = canvasLen
        self.canvasHig = canvasHig
        self.obstaclesRatio = obstaclesRatio
    
    # Generate the initial canvas with 20 empty lines and (canvasHig-20) lines of obstacles.
    def generateObs(self):
        self.canvas = collections.deque()

        # num of obstacles in a line = canvasLen*obstaclesRatio
        self.obstaclesLine = ['-' for i in range(int(self.canvasLen*self.obstaclesRatio))]+[' ' for i in range(int(self.canvasLen*(1-self.obstaclesRatio)))]
        self.emptyLine = [" " for i in range(self.canvasLen)]

        # Append empty lines to the canvas. 
        for i in range(self.canvasHig):
            self.canvas.append([" " for i in range(self.canvasLen)])

        return self.canvas

    
    def updateObs(self, canvas, linePassed, player):
        
        # Leftappend obstacle line and empty line to the canvas alternatively. This design allows us to increase the 
        # refreshing rate (reduce the pauseTime) of the canvas without making the game too difficult to play.
        if linePassed%2==0:
            random.shuffle(self.obstaclesLine)
            canvas.appendleft(list(self.obstaclesLine))
        else:
            canvas.appendleft(self.emptyLine)

        canvas.pop()

        # Conllision check 
        if canvas[player.currPositionY][player.currPositionX] == '-':
            canvas[player.currPositionY][player.currPositionX]='X'
            for eachLine in canvas:
                print(''.join('{}'.format(i) for i in eachLine))
            print('Score: {}'.format((linePassed-19)//2 +player.maxPositionDown - player.currPositionY))
            exit()
        else:
            playerLine = canvas[player.currPositionY].copy()
            playerLine[player.currPositionX] = '*'
            canvas[player.currPositionY] = playerLine
            for eachLine in canvas:
                print(''.join('{}'.format(i) for i in eachLine))