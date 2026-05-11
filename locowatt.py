#import locowattMQTT
import locowattConfigHandler
import locowattModbusRTU

#mqtt = locowattMQTT()

configHandler = locowattConfigHandler.configHandler()

holdingRegisterVariables = configHandler.getRegisterVariables()
modbusInterface = locowattModbusRTU.modbusRTUInterface()

for hrVariable in holdingRegisterVariables:

    print (len(hrVariable["addresses"]))
    if len(hrVariable["addresses"])>1:
        #single register
        value = modbusInterface.readSingleHoldingRegister(hrVariable["addresses"][0])
        value = 1
        print(hrVariable["name"]+": "+ str(value))
        
        
    else:
        #multi register
        intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["addresses"],len(hrVariable["addresses"]))
        
        #intValues = [104,105,103]
        bValues = b''
        for intVal in intValues:
            bValues = bValues + intVal.to_bytes(2,"little")
        #bValues = bytearray(intValues)
        print(hrVariable["addresses"][0])
        print(bValues)
        print(hrVariable["name"]+": "+ bValues.decode())
        
modbusInterface.forceCloseSerialPort()

    

