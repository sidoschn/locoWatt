import locowattModbusRTU
import autoUpdate
import time

# quick tool to check variable states

autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
#modbusInterface.switchSystemState(1)
#modbusInterface.switchSystemState(1)
targetRegister = 19
newVal = 10
print("writing start time to :"+str(newVal))
print("old value:")
print(modbusInterface.readSingleHoldingRegister(targetRegister))

modbusInterface.writeSingleVariable(targetRegister,newVal)

print("new value:")
print(modbusInterface.readSingleHoldingRegister(targetRegister))

# print("reg delay time:")
# print(modbusInterface.readSingleHoldingRegister(19))

