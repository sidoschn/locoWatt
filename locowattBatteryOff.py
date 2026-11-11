import locowattModbusRTU
import autoUpdate




autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
modbusInterface.switchSystemState(4)

print("battery switched off")
