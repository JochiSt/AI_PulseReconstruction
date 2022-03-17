"""

"""

import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import time

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
                                         timeout = 2)
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

    gene_params = []
    reco_params = []

    TEST_SIZE = 10000
    NOISE_ENABLE = False
    noise_str = "noise"
    for i in range(TEST_SIZE):
        if i % 10 == 0:
            print(i,"of", TEST_SIZE)

        # create a new waveform
        # parameters for template generation
        P_width    = ( 16,  32 )
        P_position = ( 16,  24 )
        P_height   = ( 32, 128 )

        # randomize the parameters
        width    = np.random.randint( *P_width )       # width of 16 to 64
        position = np.random.randint( *P_position ) # arbitrary position
        height   = np.random.randint( *P_height )     # pulse height of 32 to 128

        # generate some noise
        if NOISE_ENABLE:
            noise = np.random.randint(1,30)/10.                 # 0.1 to 3 LSB noise
            noise = 1
            noise_str = "noise_1LSB"
        else:
            noise_str = "quiet"
            noise = 0.

        #print(width, position, height)
        # scale parameters to get values between 0 and 1
        SCALE_WIDTH = 64
        SCALE_POS = 32
        SCALE_HEIGHT = 255

        gene_params.append( (width, position, height) )

        test_data = generateTemplate(position = position, pulse_length = width, height=height, noise=noise)
        test_data = test_data.astype(np.uint8)

        try:
            serial_port.write( test_data.tobytes() )
        except Exception as e:
            print(e)
            serial_port.close()
            break

        try:
            # readin waveform send to STM32 (it's echoed)
            raw = serial_port.readline()
            #print(raw)
            raw = raw.decode("utf-8")[:-1]
            STM32waveform = np.array(raw.split(" "))

            # float output
            #raw = serial_port.readline()
            #raw = raw.decode("utf-8")[:-1]
            #print(raw)

            # read reconstructed parameters
            raw = serial_port.readline()
            #print(raw)
            raw = raw.decode("utf-8")[:-1]
            width, position, height = raw.split("\t")[:-1]  # we have one trailing tab

            #print( width, position, height )
            reco_params.append( (
                    float(width)    * SCALE_WIDTH,
                    float(position) * SCALE_POS,
                    float(height)   * SCALE_HEIGHT
                    ) )
        except Exception as e:
            print(e)
            serial_port.close()
            break

    np.savez("stm32_eval_%s_%s_%d.npz"%(time.strftime("%Y%m%d_%H%M%S"), noise_str, TEST_SIZE),
             reco_params=reco_params,
             gene_params=gene_params
             )

    serial_port.close()
    plt.title("width")
    plt.ylabel("STM32 parameter")
    plt.xlabel("generated parameter")
    plt.hist2d( [ float(i[0]) for i in gene_params ], [ float(i[0]) for i in reco_params ], bins=32, cmin=1)
    plt.savefig("stm32_validation_width.png")
    plt.show()

    plt.title("position")
    plt.ylabel("STM32 parameter")
    plt.xlabel("generated parameter")
    plt.hist2d( [ float(i[1]) for i in gene_params ], [ float(i[1]) for i in reco_params ], bins=32,cmin=1)
    plt.savefig("stm32_validation_position.png")
    plt.show()

    plt.title("height")
    plt.ylabel("STM32 parameter")
    plt.xlabel("generated parameter")
    plt.hist2d( [ float(i[2]) for i in gene_params ], [ float(i[2]) for i in reco_params ], bins=32,cmin=1)
    plt.savefig("stm32_validation_height.png")
    plt.show()

if __name__ == "__main__":
    main()

