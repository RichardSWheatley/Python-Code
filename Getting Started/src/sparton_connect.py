import argparse
from myserial import SimpleSerialWrapper
from sparton_configure import setup_compass_output
from time import sleep
 # Time in seconds.

def main(args):
    try:
        compass_serial = SimpleSerialWrapper()
        compass_serial.setParams(args.device, args.baud_rate, args.time_out)
        compass_serial.portOpen()
        setup_compass_output(compass_serial)
        compass_serial.flushData()
        while True:
            data = compass_serial.getData(0) # '0' is for Serial.readline()
            if data is not None:
                print(data.decode('cp1252').strip('\n'))
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
