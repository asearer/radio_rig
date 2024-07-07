# turns power on and off
from pynput import keyboard

# Dictionary to map key codes to corresponding functions
key_mapping = {
    keyboard.Key.f1: 'on',
    keyboard.Key.f2: 'off',
}