import argparse
import serial
from myserial import SimpleSerialWrapper
from time import sleep

def get_info(serial_port):
    serial_port.sendData('name di.\r')
    serial_port.sendData('serialnumber di.\r')  
    serial_port.sendData('VERSION di.\r')    
        
# Setup compass to output data with a checksum.        
def setup_compass_output(serial_port):
    serial_port.sendData('\x13')
    sleep(0.01)
    serial_port.flushData()
    sleep(0.01)

def get_serial_value(size, serial_port):
    return serial_port.getData(size)



def main(args):
    try:
        compass_serial = SimpleSerialWrapper()
        # The following line was a test to see if args contain the correct data
        # print(args)
        compass_serial.setParams(args.device, args.baud_rate, args.time_out)
        compass_serial.portOpen()
        setup_compass_output(compass_serial)
        get_info(compass_serial)
        count = 8
        while count != 0:
            data = get_serial_value(0, compass_serial) # '0' is for Serial.readline()
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
