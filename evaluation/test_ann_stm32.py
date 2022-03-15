"""

"""
import serial
import numpy as np
import matplotlib.pyplot as plt
from generateTemplate import generateTemplate

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

    # create a new waveform
    width = np.random.randint(16, 64)                    # width of 16 to 64
    position = np.random.randint(0, high=96-width) # arbitrary position
    noise = np.random.randint(1,30)/10.                 # 0.1 to 3 LSB noise
    height = np.random.randint(32,128)                  # pulse height of 32 to 128

    noise = 0.

    print(width, position, height)

    test_data = generateTemplate(position = position, pulse_length = width, height=height, noise=noise)
    test_data = test_data.astype(np.uint8)

    try:
        serial_port.write( test_data.tobytes() )
    except Exception as e:
        print(e)
        serial_port.close()
        return

    try:
        raw = serial_port.readline()
        raw = raw.decode("utf-8")[:-1]
        STM32waveform = np.array(raw.split(" "))

        raw = serial_port.readline()
        raw = raw.decode("utf-8")[:-1]

        width, position, height = raw.split("\t")

        print( width, position, height )
    except Exception as e:
        print(e)
        serial_port.close()
        return

    serial_port.close()

    plt.plot( STM32waveform, 'b.')
    plt.plot( test_data, 'r.')
    plt.show()

if __name__ == "__main__":
    main()

