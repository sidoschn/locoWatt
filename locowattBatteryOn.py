import locowattModbusRTU
import autoUpdate




autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
modbusInterface.switchSystemState(1)
modbusInterface.switchSystemState(3)

print("battery switched On")
