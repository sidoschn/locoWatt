#import locowattMQTT
import locowattConfigHandler
import locowattModbusRTU

#mqtt = locowattMQTT()

configHandler = locowattConfigHandler.configHandler()

holdingRegisterVariables = configHandler.getRegisterVariables()
modbusInterface = locowattModbusRTU.modbusRTUInterface()

for hrVariable in holdingRegisterVariables:

    
    if ((hrVariable["length"])>1):
        #multi register
        intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
        
        #intValues = [104,105,103]
        bValues = b''
        for intVal in intValues:
            bValues = bValues + intVal.to_bytes(2,"little")
        #bValues = bytearray(intValues)
        
        print(bValues)
        print(hrVariable["name"]+": "+ bValues.decode())
    
    else:
        #single register
        value = modbusInterface.readSingleHoldingRegister(hrVariable["address"])
        #value = 1
        print(hrVariable["name"]+": "+ str(value))
        
        
test = modbusInterface.readSingleHoldingRegisterString(23)

print(test)
#print(test.to_bytes('little'))
#print(test.to_bytes('big'))
        
        
modbusInterface.forceCloseSerialPort()

    

