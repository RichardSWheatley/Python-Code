from time import sleep
import myserial

# Setup compass to output data with a checksum.        
def setup_compass_output(serial_port):
    serial_port.sendData('\x13')

    #This line sets clears all the output enables by setting them to zero
    sleep(0.01)    
    serial_port.sendData("chan0Enables m[ 0 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]m set drop\r")

    # This line sets the output preamble to “x:”
    sleep(0.01)    
    serial_port.sendData("chan0Preamble \"$\\x01CUS0,\" set drop\r")

    # This line sets the output postamble to “;”
    sleep(0.01)    
    serial_port.sendData("chan0Postamble \"\\x02*\\x03\" set drop\r")

    # The lines below use the appropriate variable names to be turned on in the output stream
    # These lines will be output in their VID numbered order
    sleep(0.01)    
    serial_port.sendData("chan0EnableBit quaternion dvid@ set drop\r") # VID == 15
    sleep(0.01)    
    serial_port.sendData("chan0EnableBit accelp dvid@ set drop\r") # VID == 31
    sleep(0.01)    
    serial_port.sendData("chan0EnableBit gyrop dvid@ set drop\r") # VID == 33
    sleep(0.01)    
    serial_port.sendData("chan0EnableBit cputime dvid@ set drop\r") # VID == 83

    sleep(0.01)    
    serial_port.sendData("chan0Format 3 set drop\r") # Sets the output stream to BitstreamASCII
    sleep(0.01)    
    serial_port.sendData("chan0Trigger 5 set drop\r") # Sets the Trigger to CompassData
    sleep(0.01)    
    serial_port.sendData("chan0TriggerDivisor 1 set drop\r") # Sets the divisor to (ODR / TriggerDivisor)
    sleep(0.01)    
    serial_port.sendData('\x11')