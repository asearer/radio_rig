# adjustment for speed
from pynput import keyboard
import time

# Dictionary to map key codes to corresponding digits and functions
key_mapping = {
    keyboard.KeyCode.from_char('0'): '0',
    keyboard.KeyCode.from_char('1'): '1',
    keyboard.KeyCode.from_char('2'): '2',
    keyboard.KeyCode.from_char('3'): '3',
    keyboard.KeyCode.from_char('4'): '4',
    keyboard.KeyCode.from_char('5'): '5',
    keyboard.KeyCode.from_char('6'): '6',
    keyboard.KeyCode.from_char('7'): '7',
    keyboard.KeyCode.from_char('8'): '8',
    keyboard.KeyCode.from_char('9'): '9',
    keyboard.Key.f1: 'chan10',
    keyboard.Key.f2: 'chan20',
    keyboard.Key.f3: 'chan30',
    keyboard.Key.f4: 'chan40',
    keyboard.Key.f5: 'chan50',
}

# Dictionary to store the start times of key presses
key_press_times = {}

# Function to handle key presses
def on_press(key):
    if key in key_mapping:
        key_value = key_mapping[key]
        if key_value not in key_press_times:
            key_press_times[key_value] = time.time()
            print(f"Key pressed: {key_value} at {key_press_times[key_value]}")
            

# Function to handle key releases
def on_release(key):
    if key in key_mapping:
        key_value = key_mapping[key]
        if key_value in key_press_times:
            start_time = key_press_times.pop(key_value)
            end_time = time.time()
            duration = end_time - start_time
            print(f"Key released: {key_value} at {end_time}")
            print(f"Duration: {duration:.4f} seconds")
            handle_duration(key_value, duration)

    if key == keyboard.Key.esc:
        # Stop listener
        return False
    

# Function to handle duration
def handle_duration(key_value, duration):
    if key_value == 'chan10':
        # Perform action for chan10
        print(f"Action for chan10 with duration {duration:.4f} seconds.")
    elif key_value == 'chan20':
        # Perform action for chan20
        print(f"Action for chan20 with duration {duration:.4f} seconds.")
    elif key_value == 'chan30':
        # Perform action for chan30
        print(f"Action for chan30 with duration {duration:.4f} seconds.")
    elif key_value == 'chan40':
        # Perform action for chan40
        print(f"Action for chan40 with duration {duration:.4f} seconds.")
    elif key_value == 'chan50':
        # Perform action for chan50
        print(f"Action for chan50 with duration {duration:.4f} seconds.")
        

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
