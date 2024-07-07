from pynput import keyboard

# Dictionary to map key codes to corresponding digits
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
}

def on_press(key):
    if key in key_mapping:
        print(f"Key pressed: {key_mapping[key]}")

def on_release(key):
    # Optionally, you can handle key release events if needed
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
