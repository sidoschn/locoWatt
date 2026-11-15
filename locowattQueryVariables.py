import locowattModbusRTU
import autoUpdate
import time

# quick tool to check variable states

autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
#modbusInterface.switchSystemState(1)
#modbusInterface.switchSystemState(1)

print("reg start time:")
print(modbusInterface.readSingleHoldingRegister(18))

print("reg delay time:")
print(modbusInterface.readSingleHoldingRegister(19))

