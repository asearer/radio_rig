# exits current program when button is pressed

from time import sleep
from gpiozero import Button
from signal import pause
from radio_rig import radio_rig

button = Button(17)

radio_rig.exit_program()

button.wait_for_press()
radio_rig.set_frequency_range(0)

pause()
