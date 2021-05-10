from pynput import keyboard
import sys

''' Controler that handles the keyboard inputs.'''
class KeyboardControl:
    def __init__(self, player):
        self.player = player

    # Handle the keyboard inputs.
    def on_press(self, key):
        if key == keyboard.Key.right and self.player.currPosition < self.player.maxPosition:
            self.player.currPosition += 1
        if key == keyboard.Key.left and self.player.currPosition > 0:
            self.player.currPosition -= 1

    # Activate a non-blocking listener.
    def activate(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()