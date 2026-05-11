#import locowattMQTT
import locowattConfigHandler
import locowattModbusRTU

#mqtt = locowattMQTT()

configHandler = locowattConfigHandler.configHandler()

holdingRegisterVariables = configHandler.getRegisterVariables()
modbusInterface = locowattModbusRTU.modbusRTUInterface()

inputRetisterVariables = configHandler.getRegisterVariables("inputRegister")

for hrVariable in holdingRegisterVariables:

    
    if ((hrVariable["length"])>1):
        #multi register
        intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
        if (hrVariable["type"]=="char"):
            #intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
            
            #intValues = [104,105,103]
            bValues = b''
            for intVal in intValues:
                bValues = bValues + intVal.to_bytes(2,"big")
            #bValues = bytearray(intValues)
            
            #print(bValues)
            print(hrVariable["name"]+": "+ bValues.decode())
        elif (hrVariable["type"]=="int"):
            print("int format")
            print(intValues)
            bValues = b''
            for intVal in intValues:
                bValues = bValues + intVal.to_bytes(2,"big")
            print(bValues)
            

        else:
            print("format not implemented, skipping output")
        
    
    else:
        #single register
        value = modbusInterface.readSingleHoldingRegister(hrVariable["address"])
        #value = 1
        scaledValue = value*hrVariable["valueMultiplier"]
        print(hrVariable["name"]+": "+ str(scaledValue) + hrVariable["unit"])
        
        
#test = modbusInterface.readSingleHoldingRegisterString(209)

#print(test)
#print(test.to_bytes('little'))
#print(test.to_bytes('big'))


for hrVariable in inputRetisterVariables:

    
    if ((hrVariable["length"])>1):
        #multi register
        
        if (hrVariable["type"]=="char"):
            intValues = modbusInterface.readMultipleInputRegisters(hrVariable["address"],hrVariable["length"])
            #intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
            
            #intValues = [104,105,103]
            bValues = b''
            for intVal in intValues:
                bValues = bValues + intVal.to_bytes(2,"big")
            #bValues = bytearray(intValues)
            
            #print(bValues)
            print(hrVariable["name"]+": "+ bValues.decode())
        elif (hrVariable["type"]=="int"):
            print("int (long) format")
            intValues = modbusInterface.readLongInputRegisters(hrVariable["address"],hrVariable["length"])
            
            print(intValues)
            bValues = b''
            for intVal in intValues:
                bValues = bValues + intVal.to_bytes(2,"big")
            print(bValues)
            combInt = int.from_bytes(bValues, 'big')

        else:
            print("format not implemented, skipping output")
        
    
    else:
        #single register
        value = modbusInterface.readSingleInputRegister(hrVariable["address"])
        #value = 1
        scaledValue = value*hrVariable["valueMultiplier"]
        print(hrVariable["name"]+": "+ str(scaledValue) + hrVariable["unit"])
        

        
modbusInterface.forceCloseSerialPort()

    

