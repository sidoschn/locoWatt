import locowattModbusRTU
import autoUpdate
import time

autoUpdate.performAutoupdate()

modbusInterface = locowattModbusRTU.modbusRTUInterface()
#modbusInterface.switchSystemState(0)

#modbusInterface.switchSystemState(2) #this might need repeating in case of "no sun" because inverter looses power and forgets the state

# empirically confirmed: when "no sun" (no power from solar collectors), the inverter loses Power when the battery switches off
# this results in the inverter losing the "battery off state" and immediately sending a wake up signal to the battery
print("switching Battery Off...")


#here a loop regularly monitors the system state and re-sends the "battery off command" if applicable
# this command is intentionally blocking to inhibit conflicting communication

print("confirming battery deactivation state...")
for i in range(20):
    currentSystemState = modbusInterface.readSingleHoldingRegister(0)
    print(currentSystemState)
    
    match currentSystemState: #todo: add correction actions in case undesired state switches are detected
        case 0:
            print("system went to standy")
        case 1:
            print("system went to on")
        case 2:
            print("battery stayed off (desired state)")
        case 3:
            print("battery turned back on")
        case _:
            print("unknown System state")
    time.sleep(1)


print("Battery Off procedure complete")
