# transmits on designated frequency when transmit key is pressed
from pynput import keyboard

# Dictionary to map key codes to corresponding functions
key_mapping = {
    keyboard.Key.f1: 'transmit',
}

# Function to handle key presses
def on_press(key):
    if key in key_mapping:
        key_value = key_mapping[key]
        print(f"Key pressed: {key_value}")
        
# starts transmission on key press and transmits as long as key is held down
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# ends transmission on key release
def handle_duration(key, duration):
    if key == 'transmit':
        print(f"Duration: {duration:.4f} seconds")
        