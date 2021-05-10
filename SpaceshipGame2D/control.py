from pynput import keyboard
import sys

''' Controler that handles the keyboard inputs.'''
class KeyboardControl:
    def __init__(self, player):
        self.player = player

    # Handle the keyboard inputs.
    def on_press(self, key):
        if key == keyboard.Key.right and self.player.currPositionX < self.player.maxPositionRight:
            self.player.currPositionX += 1
        if key == keyboard.Key.left and self.player.currPositionX > 0:
            self.player.currPositionX -= 1
        if key == keyboard.Key.up and self.player.currPositionY > 0:
            self.player.currPositionY -= 1
        if key == keyboard.Key.down and self.player.currPositionY < self.player.maxPositionDown:
            self.player.currPositionY += 1
    # Activate a non-blocking event listener.
    def activate(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()