import locowattModbusRTU
import autoUpdate
import time



autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
#modbusInterface.switchSystemState(1)
modbusInterface.switchSystemState(1)

print("confirming battery actication state...")
for i in range(10):
    currentSystemState = modbusInterface.readSingleHoldingRegister(0)
    print(currentSystemState)
    
    match currentSystemState: #todo: add correction actions in case undesired state switches are detected
        case 0:
            print("system went to standy")
        case 1:
            print("system went to on")
        case 2:
            print("battery turned back off")
        case 3:
            print("battery turned on (desired state)")
        case _:
            print("unknown System state")
    time.sleep(1)




print("battery switched On")
