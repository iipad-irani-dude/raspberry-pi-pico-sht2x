# sht2x.py MicroPython Driver
# Driver for SHT2x (SHT20, SHT21, SHT25) Temperature and Humidity Sensors

from machine import I2C
import utime

# I2C Slave Address (default for SHT2x)
SHT2X_ADDR = const(0x40)

# Command Codes
CMD_TEMP_NO_HOLD = const(0xF3)
CMD_HUMI_NO_HOLD = const(0xF5)
CMD_SOFT_RESET = const(0xFE)

class SHT2x:
    def __init__(self, i2c):
        self._i2c = i2c
        self.reset()
        
    def reset(self):
        """Perform a soft reset of the sensor."""
        self._i2c.writeto(SHT2X_ADDR, bytes([CMD_SOFT_RESET]))
        utime.sleep_ms(20) # Wait for the sensor to reset

    def _read_data(self, command):
        """Send the command and read the 3 bytes (2 data, 1 CRC)."""
        
        # 1. Send measurement command
        self._i2c.writeto(SHT2X_ADDR, bytes([command]))
        
        # 2. Wait for measurement to complete (max 85ms for high resolution)
        utime.sleep_ms(90) 
        
        # 3. Read 3 bytes (2 data bytes + 1 CRC byte)
        data = self._i2c.readfrom(SHT2X_ADDR, 3)
        
        # 4. Combine data bytes into a single 16-bit raw value
        raw_data = data[0] << 8 | data[1] 
        
        # Note: CRC check is omitted here for simplicity, but recommended for production.
        return raw_data

    @property
    def temperature(self):
        """Read and return temperature in Celsius."""
        raw_temp = self._read_data(CMD_TEMP_NO_HOLD)
        
        # Apply temperature conversion formula (from SHT2x datasheet)
        # Temp [°C] = -46.85 + 175.72 * (raw_temp / 2^16)
        temp_c = -46.85 + 175.72 * (raw_temp / 65536.0)
        return temp_c

    @property
    def humidity(self):
        """Read and return relative humidity in %RH."""
        raw_humi = self._read_data(CMD_HUMI_NO_HOLD)
        
        # Apply humidity conversion formula (from SHT2x datasheet)
        # RH [%] = -6 + 125 * (raw_humi / 2^16)
        humi_rh = -6.0 + 125.0 * (raw_humi / 65536.0)
        
        # Clamp to 0-100% range
        if humi_rh > 100: humi_rh = 100
        if humi_rh < 0: humi_rh = 0
        
        return humi_rh

# --- End of sht2x.py ---
