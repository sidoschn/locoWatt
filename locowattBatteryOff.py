import locowattModbusRTU
import autoUpdate




autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
#modbusInterface.switchSystemState(0)
modbusInterface.switchSystemState(2) #this might need repeating in case of "no sun" because inverter looses power and forgets the state

print("battery switched Off")
