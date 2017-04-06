import serial

class SerialWrapper:
    def __init__(self):
        self.ser = serial.Serial('COM1', 115200, timeout=1)

    def sendData(self, data):
        self.ser.write(data.encode())

    def getData(self, size):
        return self.ser.read(size)

# Setup compass to output data with a checksum.        
def setup_compass_output():
    compass_serial.sendData("DeezNutz")

def get_serial_value(size):
    return compass_serial.getData(size)

compass_serial = SerialWrapper()

def main():
    setup_compass_output()
    data = get_serial_value(100)
    print(data.decode());

if __name__ == '__main__':
    main()
