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
        print(hrVariable["address"])
        intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
        
        #intValues = [104,105,103]
        bValues = b''
        for intVal in intValues:
            bValues = bValues + intVal.to_bytes(2,"little")
        #bValues = bytearray(intValues)
        print(hrVariable["address"][0])
        print(bValues)
        print(hrVariable["name"]+": "+ bValues.decode())
    
    else:
        #single register
        value = modbusInterface.readSingleHoldingRegister(hrVariable["address"][0])
        #value = 1
        print(hrVariable["name"]+": "+ str(value))
        
        
    
        
        
modbusInterface.forceCloseSerialPort()

    

