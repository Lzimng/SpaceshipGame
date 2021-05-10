''' Player that contains its current location the max range it can reach.'''
class Player:
    def __init__(self, currPositionX, currPositionY, maxPositionRight, maxPositionDown):
        self.currPositionX = currPositionX
        self.currPositionY = currPositionY

        # maxPositionRight will be set to the left boundary of the canvas.
        self.maxPositionRight = maxPositionRight         
        # maxPositionDown will be set to the bottom boundary of the canvas.
        self.maxPositionDown = maxPositionDown         