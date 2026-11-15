import locowattModbusRTU
import autoUpdate
import time
from datetime import datetime

#this script is supposed to be run as a service, it will track time of day and SOC 
#it will force the Battery to sleep at night if it is empty
#it will awaken the battery in the morning 

autoUpdate.performAutoupdate()

systemStateRegister = 0 #holding register
onGridStateRegister = 3282 #input register
bmsSocRegister = 3215 # input register
dischargeLimitRegister = 3067 #holding register




modbusInterface = locowattModbusRTU.modbusRTUInterface()

sleepTimeStart = 19
sleepTimeEnd = 5

#run a permanent loop
bRunning = True

def putBatteryToSleep():
    print("switching Battery Off...")
    modbusInterface.switchSystemState(2) #this might need repeating in case of "no sun" because inverter looses power and forgets the state
    
    print("confirming and enforcing battery deactivation state...", end="")
    
    for i in range(30):
        try:
            currentSystemState = modbusInterface.readSingleHoldingRegister(systemStateRegister)
        
        except:
            print("no connection to system")
            currentSystemState = -1
        
        #print(currentSystemState)    
        match currentSystemState:
            case 0:
                print("system state turned to standy")
            case 1:
                print("system state turned to on!")
                print("re-sending battery Off command")
                modbusInterface.switchSystemState(2)
            case 2:
                print(".", end="")
            case 3:
                print("battery turned back on")
            case _:
                print("unknown System state (system probably unpowered)")
        
        time.sleep(1)
    
    print("Battery Off procedure complete")

def wakeBatteryUp():
    print("waking battery up...")

while bRunning:
    #check the time
    timeOfDay = datetime.now()
    print("current hour: " +str(timeOfDay.hour))
    if timeOfDay.hour < sleepTimeEnd or timeOfDay.hour > sleepTimeStart:
        # check if we are running off-grid
        #self.inverter.read_register(3282,0,4) # 0 is off-grid, 1 is on-grid, 2 is generator mode
        gridState = modbusInterface.readSingleInputRegister(onGridStateRegister)
        print ("Grid state: "+str(gridState))
        if gridState == 1:
            bOnGrid = True
        else:        
            bOnGrid = False

        if bOnGrid:
            # get SOC of BMS1
            socOfBms = modbusInterface.readSingleInputRegister(bmsSocRegister)
            print("Current SOC: "+ str(socOfBms))
            # get discharge limit
            minSoc = modbusInterface.readSingleHoldingRegister(dischargeLimitRegister)
            print("Minimum allowable SOC: "+str(minSoc))

            if socOfBms <= minSoc:
                print ("Putting Battery to sleep...")
                putBatteryToSleep()
            else:
                print ("no action required")
                            
    time.sleep(10)


