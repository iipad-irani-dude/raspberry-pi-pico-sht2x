from machine import Pin, I2C, UART 
import utime
import time

#this is fpr cpmmecting and send over data to arduino 

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))


# Import the SHT2x driver file
from sht2x import SHT2x 
led=Pin(15,Pin.OUT)
led.value(0)

led2=Pin(16,Pin.OUT)
led2.value(0)

led3=Pin(10,Pin.OUT)
led3.value(0)
# Define the I2C bus pins on the Pico
# I2C 0 is typically used with these pins:
I2C_SCL = 5 # GPIO 5
I2C_SDA = 4  # GPIO 4

# Initialize the I2C communication interface
# Note: Ensure these pins match your wiring.
i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=100000)
SHT2X_ADDR = const(0x40)

# Wait for the sensor to be ready
utime.sleep_ms(50) 

try:
    # Check if the SHT2x sensor is connected (it should respond at 0x40)
    devices = i2c.scan()
    if SHT2X_ADDR not in devices:
        led.value(1)
     
        led2.value(0)
      
        led3.value(0)
        time.sleep(1)
   
        led.value(0)
        time.sleep(1)
        led.value(1)
        
        time.sleep(1)

        
        
        raise OSError("SHT2x sensor not found at I2C address 0x40.")
        
        
    # Create the SHT2x object
    sensor = SHT2x(i2c)
    print("SHT2x Sensor initialized successfully.")
    
except Exception as e:
    print(f"Error: {e}")
    # Loop indefinitely or stop execution if the sensor isn't found
    while True:
        utime.sleep(5)

# Main loop to read and display data
while True:
    # Read the data from the sensor properties
    temp_c = sensor.temperature
    humi_rh = sensor.humidity
    print(f"🌡️ Temperature: {temp_c:0.2f} °C")
    uart.write('T {temp_c:0.2f} \n')
    
    if humi_rh > 50:
        print(f"Humidity:    {temp_c:0.2f} %RH HIGH")
        uart.write('H {humi_rh:0.2f} \n')
        # Turn on LED 1 (High indication)
        led.value(1)  
        led2.value(0)
        led3.value(0)
        
    elif humi_rh < 30 :
        print(f"💧 Humidity:    {humi_rh:0.2f} %RH   LOW")
        uart.write('H {humi_rh:0.2f} \n')
        # Turn on LED 3 (Low indication)
        led.value(1)
        led2.value(0)
        led3.value(0)

    else:
        print(f"💧 Humidity:    {humi_rh:0.2f} %RH   NORMAL")
        uart.write('H {humi_rh:0.2f} \n')
        # Turn on LED 2 (Normal indication)
        led.value(0)
        led2.value(1)
        led3.value(0)
        
    # Wait before the next reading
    utime.sleep(1)  
