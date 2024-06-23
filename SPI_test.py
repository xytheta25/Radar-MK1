import spidev
import time

class SPIDriver:
    def __init__(self, bus=0, device=0, max_speed_hz=50000, mode=0):
        self.bus = bus
        self.device = device
        self.max_speed_hz = max_speed_hz
        self.mode = mode

        # Initialize SPI
        self.spi = spidev.SpiDev()
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = self.max_speed_hz
        self.spi.mode = self.mode

    def write_data(self, data):
        """
        Write data to the SPI device.
        :param data: List of bytes to send
        """
        self.spi.xfer2(data)

    def read_data(self, length):
        """
        Read data from the SPI device.
        :param length: Number of bytes to read
        :return: List of bytes read from the device
        """
        return self.spi.readbytes(length)

    def close(self):
        """
        Close the SPI connection.
        """
        self.spi.close()

if __name__ == "__main__":
    # Example usage
    spi_driver = SPIDriver(bus=0, device=0, max_speed_hz=50000, mode=0)

    # Write data to SPI device
    spi_driver.write_data([0x01, 0x02, 0x03])

    # Read data from SPI device
    received_data = spi_driver.read_data(3)
    print("Received data:", received_data)

    # Close the SPI connection
    spi_driver.close()