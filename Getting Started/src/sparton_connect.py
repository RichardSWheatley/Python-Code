import serial
from time import sleep
 # Time in seconds.

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

    #This line sets clears all the output enables by setting them to zero
    sleep(0.01)    
    compass_serial.sendData("chan0Enables m[ 0 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]m set drop\r")

    # This line sets the output preamble to “x:”
    sleep(0.01)    
    compass_serial.sendData("chan0Preamble \"$\\x01CUS0,\" set drop\r")

    # This line sets the output postamble to “;”
    sleep(0.01)    
    compass_serial.sendData("chan0Postamble \"\\x02*\\x03\" set drop\r")

    # The lines below use the appropriate variable names to be turned on in the output stream
    # These lines will be output in their VID numbered order
    sleep(0.01)    
    compass_serial.sendData("chan0EnableBit quaternion dvid@ set drop\r") # VID == 15
    sleep(0.01)    
    compass_serial.sendData("chan0EnableBit accelp dvid@ set drop\r") # VID == 31
    sleep(0.01)    
    compass_serial.sendData("chan0EnableBit gyrop dvid@ set drop\r") # VID == 33
    sleep(0.01)    
    compass_serial.sendData("chan0EnableBit cputime dvid@ set drop\r") # VID == 83

    sleep(0.01)    
    compass_serial.sendData("chan0Format 3 set drop\r") # Sets the output stream to BitstreamASCII
    sleep(0.01)    
    compass_serial.sendData("chan0Trigger 5 set drop\r") # Sets the Trigger to CompassData
    sleep(0.01)    
    compass_serial.sendData("chan0TriggerDivisor 1 set drop\r") # Sets the divisor to (ODR / TriggerDivisor)
    sleep(0.01)    
    compass_serial.flushData()
    compass_serial.sendData('\x11')

def get_serial_value(self, size):
    return compass_serial.getData(size)

compass_serial = SerialWrapper()

def main():
    compass_serial.setParams('COM1', 115200, 1)
    compass_serial.portOpen()
    setup_compass_output()
    compass_serial.flushData()
    try:
        while True:
            data = compass_serial.getData(0) # '0' is for Serial.readline()
            print(data.decode('cp1252').strip('\n'))
    except KeyboardInterrupt:
        pass    

if __name__ == '__main__':
    main()
