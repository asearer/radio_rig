# opens menu when button is pressed and held for 2 seconds and remains open until selection is made or exit key is pressed

from time import sleep
from gpiozero import Button
from signal import pause
from radio_rig import radio_rig

button = Button(17)

radio_rig.open_menu()

button.wait_for_press()
radio_rig.set_frequency_range(0)

pause()

# enters input character . when button is pressed
button = Button(17)

radio_rig.input_character('.')

button.wait_for_press()
radio_rig.set_frequency_range(0)

pause()