import pyvisa
from time import sleep
from quantiphy import Quantity

rm = pyvisa.ResourceManager()

mp_dmm = rm.open_resource('ASRL/dev/ttyUSB0')  # 'ASRL/dev/ttyUSB0::INSTR'

mp_dmm.baud_rate = 115200

print(mp_dmm.query("*IDN?"))



