''' Player that contains its current location the max range it can reach.'''
class Player:
    def __init__(self, currPosition, maxPosition):
        self.currPosition = currPosition
        # maxPosition will be set to the left boundary of the canvas.
        self.maxPosition = maxPosition         