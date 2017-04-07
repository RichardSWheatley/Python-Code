import serial
from time import sleep

import argparse

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

def get_info():
    compass_serial.sendData('name di.\r')
    compass_serial.sendData('serialnumber di.\r')  
    compass_serial.sendData('VERSION di.\r')    
        
# Setup compass to output data with a checksum.        
def setup_compass_output():
    compass_serial.sendData('\x13')
    sleep(0.01)
    compass_serial.flushData()
    sleep(0.01)


def get_serial_value(size):
    return compass_serial.getData(size)

compass_serial = SerialWrapper()

def main(args):
    try:
        # The following line was a test to see if args contain the correct data
        # print(args)
        compass_serial.setParams(args.device, args.baud_rate, args.time_out)
        compass_serial.portOpen()
        setup_compass_output()
        get_info()
        count = 8
        while count != 0:
            data = get_serial_value(0) # '0' is for Serial.readline()
            print(count)
            if "=" in data.decode('cp1252'): 
                print(data.decode('cp1252').strip('\r\n'))
            count = count - 1
        compass_serial.flushData()
    except KeyboardInterrupt:
        pass   

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sparton Serial Wrapper (Basic) CTRL-C if you get the wrong baud rate')
    parser.add_argument('-d', '--device', help="COM Port Device Name", nargs='?', default='COM5')
    parser.add_argument('-b', '--baud_rate', help="COM Port Device Baud Rate", nargs='?', default=115200, type=int)
    parser.add_argument('-t', '--time_out', help="COM Port Device Timeout in seconds", nargs='?', default=1, type=int)
    parser.add_argument('-p', '--printargs', help="Print Args to Screen", nargs='?', default=False, type=bool)
    args = parser.parse_args()
    if args.printargs == True:
        print("Device=%s Baud=%d Timeout=%d" % (args.device, args.baud_rate, args.time_out))
    main(args)
