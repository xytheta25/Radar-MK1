import spidev
import time
from gpiozero import LED

# Create an SPI instance
spi = spidev.SpiDev()

# Open a connection to a specific SPI device (bus 0, device 0)
spi.open(0, 0)

# Set SPI speed and mode
spi.max_speed_hz = 200000
spi.mode = 0

CS_FREQ= LED(20)
#CS_BEAM = LED(3)
CS_FREQ.on() # set the chip select for freq synth. high (CS is active low).
#CS_BEAM.on()

def write_data(data):
    """Write data to the SPI device."""
    CS_FREQ.off() # set CS low
    spi.xfer(data)
    CS_FREQ.on() # set CS high again

def read_data(length):
    """Read data from the SPI device."""
    return spi.readbytes(length)

def read_write_data(data):
    """Write data to the SPI device and read the response."""
    return spi.xfer2(data)

try:
    while True:

        # Example read/write data (sending and receiving 3 bytes)
        send_data1 = [0x09, 0xFF, 0x0B]
        send_data2 = [0x09, 0xFF, 0x0B]
        write_data(send_data1)
        print([hex(x) for x in send_data2])

        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    spi.close()
