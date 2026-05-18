import minimalmodbus
import time
import locowattConfigHandler

class modbusRTUInterface:
    inverter = None
    stateDictionary = {0:"Inverter Off", 1:"Inverter On", 2:"Battery On", 4:"Battery Off"}
    
    # can be re-written in init
    device = '/dev/ttyUSB0'
    slaveAddress = 1
    baudRate = 9600
    bClosePortAfterCall = True

    def __init__(self, usbDevice = device, slaveAddress = slaveAddress, baudRate = baudRate, bClosePortAfterCall = bClosePortAfterCall):
        self.inverter = inverter = minimalmodbus.Instrument(usbDevice,slaveAddress) # throws error here if USB device not found, if the slave is not found it throws an error on access
        self.inverter.serial.baudrate = baudRate
        self.inverter.close_port_after_each_call = bClosePortAfterCall

        self.device = usbDevice
        self.slaveAddress = slaveAddress
        self.baudRate = baudRate
        self.bClosePortAfterCall = bClosePortAfterCall
        print("RTU controller initialized for "+ self.device)
        

    def readSingleHoldingRegister(self,registerAddress):
        readValue = self.inverter.read_register(registerAddress,0)
        return readValue
    
    # def readSingleHoldingRegisterString(self,registerAddress):
    #     readValue = self.inverter.read_string(registerAddress,1)
    #     return readValue
    
    def readMultipleHoldingRegisters(self, registerAddress, nRegisters):
        #print(registerAddress)
        readValues = self.inverter.read_registers(registerAddress,nRegisters)
        return readValues
    
    def readSingleInputRegister(self,registerAddress):
        readValue = self.inverter.read_register(registerAddress,0,4)
        return readValue

    def readMultipleInputRegisters(self, registerAddress, nRegisters):
        #print(registerAddress)
        readValues = self.inverter.read_registers(registerAddress,nRegisters,4)
        return readValues
    
    def readLongInputRegisters(self, registerAddress, nRegisters):
        #print(registerAddress)
        #readValues = self.inverter.read_registers(registerAddress,nRegisters,4)
        readValues = self.inverter.read_long(registerAddress,4)
        return readValues
    
    #def readSingleVariable(self, registerVariable):

    def readSingleVariable(self, registerVariable = locowattConfigHandler.registerVariable()):

        if (registerVariable.type == "int"):
            return (self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier
        elif(registerVariable.type == "long"):
            #readValue = (self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier
            return (self.inverter.read_long(registerVariable.address, registerVariable.register) )*registerVariable.valueMultiplier
        elif(registerVariable.type == "char"):
            #readValue = (self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier
            intValues = self.inverter.read_registers(registerVariable.address,registerVariable.length,registerVariable.register)
            bValues = b''
            for intVal in intValues:
                bValues = bValues + intVal.to_bytes(2,"big")
            return bValues.decode()


    def readVariableDict(self, registerVariables = {"OnOff":locowattConfigHandler.registerVariable()}): #todo: implement a check/interrupt for NA controller signals in this loop
        self.inverter.close_port_after_each_call = False
        data = {}
        for varName, registerVariable in registerVariables.items():
            if (registerVariable.type == "int"):
                data[varName] = ((self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier)
                #((self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier)
            elif(registerVariable.type == "long"):
                #readValue = (self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier
                data[varName] = (self.inverter.read_long(registerVariable.address, registerVariable.register) )*registerVariable.valueMultiplier
            elif(registerVariable.type == "char"):
                #readValue = (self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier
                intValues = self.inverter.read_registers(registerVariable.address,registerVariable.length,registerVariable.register)
                bValues = b''
                for intVal in intValues:
                    bValues = bValues + intVal.to_bytes(2,"big")
                data[varName]= bValues.decode()
            elif(registerVariable.type == "byte"):
                
                bytePos = registerVariable.length
                intValues = self.inverter.read_register(registerVariable.address,0,registerVariable.register)
                
                binValues = bin(intValues)
                
                # for intVal in intValues:
                #     bValues = bValues + intVal.to_bytes(2,"big")
                if (bytePos == 1):
                    data[varName]= int(binValues[:8],2)*registerVariable.valueMultiplier # convert the first byte of the binary string to int and multiply by multiplier
                elif(bytePos == 2):
                    data[varName]= int(binValues[-8:],2)*registerVariable.valueMultiplier # convert the last byte of the binary string to int and multiply by multiplier
            elif(registerVariable.type == "bin"):
                intValues = self.inverter.read_register(registerVariable.address,0,registerVariable.register)
                binValues = bin(intValues)
                data[varName] = binValues

        self.inverter.close_port_after_each_call = True
        self.inverter.serial.close()
        return data

    #this is a legacy method 
    def readVariableList(self, registerVariables = [locowattConfigHandler.registerVariable()]):
        data = {}
        for registerVariable in registerVariables:
            if (registerVariable.type == "int"):
                data[registerVariable.name] = ((self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier)
                #((self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier)
            elif(registerVariable.type == "long"):
                #readValue = (self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier
                data[registerVariable.name] = (self.inverter.read_long(registerVariable.address, registerVariable.register) )*registerVariable.valueMultiplier
            elif(registerVariable.type == "char"):
                #readValue = (self.inverter.read_register(registerVariable.address,0,registerVariable.register))*registerVariable.valueMultiplier
                intValues = self.inverter.read_registers(registerVariable.address,registerVariable.length,registerVariable.register)
                bValues = b''
                for intVal in intValues:
                    bValues = bValues + intVal.to_bytes(2,"big")
                data[registerVariable.name]= bValues.decode()
        
        return data
        
        
    

    def forceCloseSerialPort(self):
        if self.inverter.serial.is_open:
            self.inverter.serial.close()
            print("serial port closed")
        else:
            print("serial port was already closed")
        


    def switchInverterState(self, bTurnOff):
        if bTurnOff:
            newSystemState = 0
        else:
            newSystemState = 1

        print("connecting to Slave "+str(self.slaveAddress))
        startTime = time.time()
        self.inverter.write_register(0,newSystemState,0) # takes aprox 37 ms to complete, throws error if slave id is not existing
        endTime = time.time()

        deltaTime = endTime-startTime

        print("switched State to "+ self.stateDictionary[newSystemState] + "(took "+str(deltaTime)+"seconds)")
        
    
    
    def switchSystemState(self, newSystemState):
        
        print("connecting to Slave "+str(self.slaveAddress))
        self.inverter.write_register(0,newSystemState,0)
        print("switched State to "+ self.stateDictionary[newSystemState])