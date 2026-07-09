# Raspberry Pi Pico SHT2x Driver

Hello! 👋

This is a MicroPython driver for the **Sensirion SHT2x** temperature and humidity sensor, designed for the **Raspberry Pi Pico** series (RP2040 and RP2350).

The driver is intended to be used with the included `sensor.py` example. Make sure to upload the driver file to your Pico before running the example.

## Features

* 📡 Reads temperature and humidity from SHT2x sensors over I²C.
* 🔄 Includes optional UART (`TX`/`RX`) support for sending sensor data over serial.
* 🤖 Originally developed for using a sht2x sencor and can be used for sending sensor readings from a Raspberry Pi Pico to an Arduino, but it can be used with any compatible serial device.

---

`# ⚠️ WARNING ⚠️`

**YOU MUST USE A PROPER LOGIC LEVEL SHIFTER (OR ANOTHER SAFE VOLTAGE TRANSLATION METHOD) WHEN CONNECTING A RASPBERRY PI PICO TO ANY 5 V DEVICE. FAILURE TO DO SO MAY PERMANENTLY` DAMAGE YOUR HARDWARE.**

**THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, AS DESCRIBED IN THE APACHE LICENSE 2.0.**`

**THE AUTHOR PROVIDES NO GUARANTEE THAT THIS SOFTWARE IS SUITABLE FOR YOUR APPLICATION. YOU ARE SOLELY RESPONSIBLE FOR VERIFYING YOUR WIRING, VOLTAGE LEVELS, AND THE SAFE OPERATION ``OF YOUR HARDWARE.**`

**THE AUTHOR SHALL NOT BE HELD RESPONSIBLE FOR ANY DAMAGE, DATA LOSS, HARDWARE FAILURE, OR ANY OTHER ISSUES RESULTING FROM THE USE OR MISUSE OF THIS SOFTWARE.**`

---

## License

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for details.
