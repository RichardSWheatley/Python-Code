import serial

class SimpleSerialWrapper:
    def __init__(self):
        self.ser = serial.Serial()
        
    def portOpen(self):
        self.ser.open()
        
    def flushData(self):
        self.ser.flush()

    def sendData(self, data):
        self.ser.write(data.encode())
        
    def getData(self, read_size):
        if read_size == 0:
            return self.ser.readline()
        
        return self.ser.read(read_size)
        
    def setParams(self, device, baud, time_out):
        # The following line was just a test
        # print(device, baud, time_out)
        self.ser.baudrate = baud
        self.ser.port = device
        self.ser.timeout = time_out
        
    def getBaud(self):
        return self.ser.baudrate
        
    def getDevice(self):
        return self.ser.port
        
    def getTimeout(self):
        return self.ser.timeout