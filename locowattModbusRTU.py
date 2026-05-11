import minimalmodbus
import time

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
    
    def readMultipleHoldingRegisters(self, registerAddress, nRegisters):
        
        readValues = self.inverter.read_registers(registerAddress,nRegisters)
        return readValues
    
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