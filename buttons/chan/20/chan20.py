# selects frequency range 20 when button is pressed

from time import sleep
from gpiozero import Button
from signal import pause
from radio_rig import radio_rig

button = Button(17)

radio_rig.set_frequency_range(20)

button.wait_for_press()
radio_rig.set_frequency_range(0)
