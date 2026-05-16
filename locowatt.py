import locowattMQTT
import locowattConfigHandler
import locowattModbusRTU
import autoUpdate
import time

autoUpdate.performAutoupdate()


mqtt = locowattMQTT.mqttInterface()

#registerVariables = [locowattConfigHandler.registerVariable()]



configHandler = locowattConfigHandler.configHandler()

#holdingRegisterVariables = configHandler.getRegisterVariables()
modbusInterface = locowattModbusRTU.modbusRTUInterface()

for i in range(5):


    data = modbusInterface.readVariableList(configHandler.registerVariableDict)

    print (data)

    payload = mqtt.compilePyload(data)

    mqtt.publishPayload(payload, payload["device"])
    time.sleep(1)

# searchFor = 'Ppv'
# searchResult = None

# for varContent in configHandler.registerVariableList:
#     if varContent.name == searchFor:
#         # print(searchFor)
#         # print(varContent.name)
#         # print(varContent.content())
#         searchResult = varContent


# print(searchResult.content())




# for hrVariable in holdingRegisterVariables:

    
#     if ((hrVariable["length"])>1):
#         #multi register
#         intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
#         if (hrVariable["type"]=="char"):
#             #intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
            
#             #intValues = [104,105,103]
#             bValues = b''
#             for intVal in intValues:
#                 bValues = bValues + intVal.to_bytes(2,"big")
#             #bValues = bytearray(intValues)
            
#             #print(bValues)
#             print(hrVariable["name"]+": "+ bValues.decode())
#         elif (hrVariable["type"]=="int"):
#             print("int format")
#             print(intValues)
#             bValues = b''
#             for intVal in intValues:
#                 bValues = bValues + intVal.to_bytes(2,"big")
#             print(bValues)
            

#         else:
#             print("format not implemented, skipping output")
        
    
#     else:
#         #single register
#         value = modbusInterface.readSingleHoldingRegister(hrVariable["address"])
#         #value = 1
#         scaledValue = value*hrVariable["valueMultiplier"]
#         print(hrVariable["name"]+": "+ str(scaledValue) + hrVariable["unit"])
        
        
# #test = modbusInterface.readSingleHoldingRegisterString(209)

# #print(test)
# #print(test.to_bytes('little'))
# #print(test.to_bytes('big'))


# for hrVariable in inputRetisterVariables:

    
#     if ((hrVariable["length"])>1):
#         #multi register
        
#         if (hrVariable["type"]=="char"):
#             intValues = modbusInterface.readMultipleInputRegisters(hrVariable["address"],hrVariable["length"])
#             #intValues = modbusInterface.readMultipleHoldingRegisters(hrVariable["address"],hrVariable["length"])
            
#             #intValues = [104,105,103]
#             bValues = b''
#             for intVal in intValues:
#                 bValues = bValues + intVal.to_bytes(2,"big")
#             #bValues = bytearray(intValues)
            
#             #print(bValues)
#             print(hrVariable["name"]+": "+ bValues.decode())
#         elif (hrVariable["type"]=="int"):
#             print("int (long) format")
#             intValue = modbusInterface.readLongInputRegisters(hrVariable["address"],hrVariable["length"])
#             scaledValue = intValue*hrVariable["valueMultiplier"]
#             print(hrVariable["name"]+": "+str(scaledValue)+ hrVariable["unit"])
#             print(intValue)
#             # bValues = b''
#             # for intVal in intValues:
#             #     bValues = bValues + intVal.to_bytes(2,"big")
#             # print(bValues)
#             # combInt = int.from_bytes(bValues, 'big')

#         else:
#             print("format not implemented, skipping output")
        
    
#     else:
#         #single register
#         value = modbusInterface.readSingleInputRegister(hrVariable["address"])
#         #value = 1
#         scaledValue = value*hrVariable["valueMultiplier"]
#         print(hrVariable["name"]+": "+ str(scaledValue) + hrVariable["unit"])
        

        
#modbusInterface.forceCloseSerialPort()

    

