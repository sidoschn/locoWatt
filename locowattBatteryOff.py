import locowattModbusRTU
import autoUpdate




autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
modbusInterface.switchSystemState(2)

print("battery switched Off")
