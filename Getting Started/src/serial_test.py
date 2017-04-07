import serial
from time import sleep

class SerialWrapper:
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
        self.ser.baudrate = baud
        self.ser.port = device
        self.ser.timeout = time_out
        
    def getBaud():
        return self.ser.baudrate
        
    def getDevice():
        return self.ser.port
        
    def getTimeout():
        return self.ser.timeout

# Setup compass to output data with a checksum.        
def setup_compass_output():
    compass_serial.sendData('\x13')
    sleep(0.01)
    compass_serial.flushData()
    sleep(0.01)
    compass_serial.sendData('name di.\r')

def get_serial_value(size):
    return compass_serial.getData(size)

compass_serial = SerialWrapper()

def main():
    compass_serial.setParams('COM1', 115200, 1)
    compass_serial.portOpen()
    setup_compass_output()
    data = get_serial_value(0) # '0' is for Serial.readline()
    data = get_serial_value(0) # '0' is for Serial.readline()
    print(data.decode('cp1252'))
    compass_serial.flushData()

if __name__ == '__main__':
    main()
