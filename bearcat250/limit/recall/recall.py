# recalls last key pressed
from pynput import keyboard

# Dictionary to map key codes to corresponding functions
key_mapping = {
    keyboard.Key.space: 'recall',
}

# Function to handle key presses
def on_press(key):
    if key in key_mapping:
        key_value = key_mapping[key]
        print(f"Key pressed: {key_value}")
        

# Function to handle key releases
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# function to store the last 100 key presses
def recall():
    pass

# Start the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
