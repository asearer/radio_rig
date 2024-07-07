# adjusts squelch up and down
from pynput import keyboard

# Dictionary to map key codes to corresponding functions
key_mapping = {
    keyboard.Key.left: 'down',
    keyboard.Key.right: 'up',
}