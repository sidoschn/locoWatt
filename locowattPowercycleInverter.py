import locowattModbusRTU
import autoUpdate
import time



autoUpdate.performAutoupdate()

#this will only work if there is no sun but the battery is on
#this will help clear the "waiting... " issue


modbusInterface = locowattModbusRTU.modbusRTUInterface()
#modbusInterface.switchSystemState(1)
modbusInterface.switchSystemState(2) #this will turn off the battery, triggering a power cycle in the inverter and a subsequent restart of the battery

print("tracking system state...")
for i in range(30):

    try:
        currentSystemState = modbusInterface.readSingleHoldingRegister(0)    
    except:
        print("no connection to system")
        currentSystemState = -1
    
    print(currentSystemState)
    
    match currentSystemState: 
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


print("done")
