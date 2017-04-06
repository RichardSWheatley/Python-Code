import serial

class SerialWrapper:
    def __init__(self):
        self.ser = serial.Serial()
        
    def portOpen(self):
        self.ser.open()

    def sendData(self, data):
        self.ser.write(data.encode())
        
    def getData(self, read_size):
        return self.ser.read(read_size)
        
    def set_params(self, device, baud, time_out):
        self.ser.baudrate = baud
        self.ser.port = device
        self.ser.timeout = time_out

# Setup compass to output data with a checksum.        
def setup_compass_output():
    compass_serial.sendData("DeezNutz")

def get_serial_value(size):
    return compass_serial.getData(size)

compass_serial = SerialWrapper()

def main():
    compass_serial.set_params('COM1', 115200, 1)
    compass_serial.portOpen()
    setup_compass_output()
    data = compass_serial.getData(100)
    print(data.decode());

if __name__ == '__main__':
    main()
