import locowattModbusRTU
import autoUpdate




autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
modbusInterface.switchSystemState(0)
modbusInterface.switchSystemState(2)

print("battery switched Off")
