from pymodbus.constants import Endian

from battery import Battery
import custom_config
from powers import *
# Uncomment the option you want to test

configuration = "CUSTOM"
# configuration = "DEFAULT" # default configuration; floats are stored in "SCALE"

# if it is custom user provides information and config is modified, here it is hardcoded for now
if configuration == "CUSTOM":
    float_mode = "SCALE"  # uncomment if user wants to store float using scaling and one register
    # float_mode = "COMB"  # uncomment if user wants to store float in IEEE  754 format
    endian = Endian.Big
    scaling_factor = 100
    addresses = list(range(310, 355, 2)) + list(range(110, 114))

    # this will be defined by a function based on the num of digits in address, for now hardcoded
    fx_addr_separator = 100
    custom_config.modify(float_mode, fx_addr_separator, scaling_factor, endian, endian, addresses)

address = ("localhost", 5030)
id = "GREENER_001"

# battery is instantiated, only constants are in the input
battery = Battery(id, address, 1, 5, 1, 1)

power_source = PowerIn((0, 200), (-65, 185))
power_load = PowerOut((-11, 25), (-15, 25))

# connect battery to the power
battery.connect_power_in(power_source)

# connect battery to the load
battery.connect_power_out(power_load)

# fill in all dependent fields
battery.update()

# at this point battery starts to update its state
battery.run()
