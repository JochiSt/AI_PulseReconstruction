"""
    script for reading the PeakTech DMM 3315

    inspired by pyUSBtin
"""

import serial
import numpy as np

def main():

    serial_port = None
    try:
        # open serial port
        serial_port = serial.Serial("COM8",
                                         baudrate= 115200,
                                         bytesize = serial.EIGHTBITS,
                                         parity = serial.PARITY_NONE,
                                         stopbits = serial.STOPBITS_ONE,
                                         timeout = 10)
    except Exception as e:
        print(e)
        serial_port.close()
        return

    try:
        # clear input and output
        serial_port.flush()
        serial_port.flushInput()
    except Exception as e:
        print(e)
        serial_port.close()
        return

    # some debug info
    print("connected to AI test")

    test_data = np.arange(0,128, dtype=np.uint8)
    print(len(test_data))
    print(test_data.tobytes())

    try:
        serial_port.write( test_data.tobytes() )
    except Exception as e:
        print(e)
        serial_port.close()
        return

    try:
        raw = serial_port.readline()
        print(len(raw))
        print(raw)
        raw = serial_port.readline()
        print(len(raw))
        print(raw)
    except Exception as e:
        print(e)
        serial_port.close()
        return

    serial_port.close()

if __name__ == "__main__":
    main()

