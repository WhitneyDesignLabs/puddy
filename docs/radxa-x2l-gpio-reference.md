# Radxa X2L GPIO Reference

## Architecture Overview

The Radxa X2L has a unique architecture:
- **Intel J4125 CPU** (main processor running Linux)
- **RP2040 MCU** (onboard Raspberry Pi Pico chip controlling GPIO)
- Communication: USB and UART between Intel and RP2040
- The 40-pin GPIO header is controlled by the RP2040, NOT directly by Linux

```
┌─────────────────────┐      USB/UART      ┌─────────────────────┐
│  Intel J4125 CPU    │◄──────────────────►│   RP2040 MCU        │
│  (Linux/Ubuntu)     │                    │   (MicroPython/C)   │
│                     │                    │                     │
│  pyserial scripts   │    /dev/ttyACM0    │   GPIO control      │
│  OpenClaw agent     │◄──────────────────►│   40-pin header     │
└─────────────────────┘                    └─────────────────────┘
```

## Key Commands

### Put RP2040 in BOOTSEL Mode (for flashing firmware)
```bash
#!/bin/bash
sudo gpioset gpiochip1 60=1
sudo gpioset gpiochip1 61=1
sleep 1
sudo gpioset gpiochip1 60=0
sudo gpioset gpiochip1 61=0
```
After running, RP2040 appears as USB mass storage. Drag .uf2 file to flash.

### Reset RP2040 (when script crashes)
```bash
#!/bin/bash
sudo gpioset gpiochip1 60=1
sleep 1
sudo gpioset gpiochip1 60=0
```

### Check if RP2040 is visible
```bash
lsusb | grep -i pico
ls /dev/ttyACM*
```

## GPIO Pinout (40-pin header)

| Pin# | GPIO | Function1 | Function2 | Function3 | Function4 | Notes |
|------|------|-----------|-----------|-----------|-----------|-------|
| 1 | - | +3.3V | | | | Power |
| 2 | GPIO28 | SPI1 RX | UART0 TX | I2C0 SDA | PWM6 A | ADC capable |
| 3 | GPIO29 | SPI1 CSn | UART0 RX | I2C0 SCL | PWM6 B | ADC capable |
| 4 | GPIO04 | SPI0 RX | UART1 TX | I2C0 SDA | PWM2 A | |
| 5 | - | GND | | | | Ground |
| 6 | GPIO05 | SPI0 CSn | UART1 RX | I2C0 SCL | PWM2 B | |
| 7 | GPIO06 | SPI0 SCK | UART1 CTS | I2C1 SDA | PWM3 A | |
| 8 | GPIO03 | SPI0 TX | UART0 RTS | I2C1 SCL | PWM1 B | |
| 9 | - | +3.3V | | | | Power |
| 10 | GPIO11 | SPI1 TX | UART1 RTS | I2C1 SCL | PWM5 B | |
| 11 | GPIO08 | SPI1 RX | UART1 TX | I2C0 SDA | PWM4 A | |
| 12 | GPIO10 | SPI1 SCK | UART1 CTS | I2C1 SDA | PWM5 A | |
| 13 | - | GND | | | | Ground |
| 14 | GPIO16 | SPI0 RX | UART0 TX | I2C0 SDA | PWM0 A | |
| 15 | GPIO07 | SPI0 TX | UART1 RTS | I2C1 SCL | PWM3 B | |
| 16 | GPIO12 | SPI1 RX | UART0 TX | I2C0 SDA | PWM6 A | |
| 17 | GPIO13 | SPI1 CSn | UART0 RX | I2C0 SCL | PWM6 B | |
| 18 | GPIO15 | SPI1 TX | UART0 RTS | I2C1 SCL | PWM7 B | |
| 19 | GPIO14 | SPI1 SCK | UART0 CTS | I2C1 SDA | PWM7 A | |
| 20 | - | GND | | | | Ground |
| 21 | GPIO25 | SPI1 CSn | UART1 RX | I2C0 SCL | PWM4 B | Onboard LED on Pico |
| 22 | GPIO02 | SPI0 SCK | UART0 CTS | I2C1 SDA | PWM1 A | |
| 23 | GPIO26 | SPI1 SCK | UART1 CTS | I2C1 SDA | PWM5 A | ADC capable |
| 24 | - | GND | | | | Ground |
| 25 | GPIO19 | SPI0 TX | UART0 RTS | I2C1 SCL | PWM1 B | |
| 26 | - | GND | | | | Ground |
| 27 | GPIO17 | SPI0 CSn | UART0 RX | I2C0 SCL | PWM0 B | |
| 28 | GPIO18 | SPI0 SCK | UART0 CTS | I2C1 SDA | PWM1 A | |
| 29 | GPIO09 | SPI1 CSn | UART1 RX | I2C0 SCL | PWM4 B | |
| 30 | GPIO24 | SPI1 RX | UART1 TX | I2C0 SDA | PWM4 A | |
| 31 | - | GND | | | | Ground |
| 32 | GPIO27 | SPI1 TX | UART1 RTS | I2C1 SCL | PWM5 B | ADC capable |
| 33 | GPIO22 | SPI0 SCK | UART1 CTS | I2C1 SDA | PWM3 A | |
| 34 | - | GND | | | | Ground |
| 35 | GPIO23 | SPI0 TX | | | | |
| 36 | GPIO21 | SPI0 CSn | UART1 RX | I2C0 SCL | PWM2 B | |
| 37 | GPIO20 | SPI0 RX | UART1 TX | I2C0 SDA | PWM2 A | |
| 38 | - | GND | | | | Ground |
| 39 | - | +5.0V | | | | Power |
| 40 | - | +5.0V | | | | Power |

**Note:** GPIO25 is the onboard LED on standard Pico boards. May work for testing.

## Firmware Options

### Option 1: MicroPython (Recommended for quick start)
1. Download MicroPython .uf2: https://micropython.org/download/RPI_PICO (v1.22.0 tested)
2. Put RP2040 in BOOTSEL mode (script above)
3. Drag .uf2 to the USB drive that appears
4. Install Thonny: `sudo apt-get install thonny -y`
5. Connect to RP2040 via Thonny (select MicroPython interpreter)

### Option 2: CircuitPython
Similar to MicroPython, download from circuitpython.org

### Option 3: C/C++ SDK (pico-sdk)
```bash
sudo apt install -y git cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib
git clone https://github.com/raspberrypi/pico-sdk.git
git clone https://github.com/raspberrypi/pico-examples.git
```

## Communication Pattern (Linux ↔ RP2040)

### On RP2040 (MicroPython) - Listen for commands:
```python
import machine
import sys
import select

led = machine.Pin(25, machine.Pin.OUT)

while True:
    if select.select([sys.stdin], [], [], 0)[0]:
        cmd = sys.stdin.readline().strip()
        if cmd == "LED_ON":
            led.value(1)
            print("OK:LED_ON")
        elif cmd == "LED_OFF":
            led.value(0)
            print("OK:LED_OFF")
        elif cmd == "STATUS":
            print(f"OK:LED={led.value()}")
```

### On Linux (Python) - Send commands:
```python
import serial

# Find the port: ls /dev/ttyACM*
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

def send_command(cmd):
    ser.write((cmd + '\n').encode())
    response = ser.readline().decode().strip()
    return response

print(send_command("LED_ON"))   # Turn LED on
print(send_command("LED_OFF"))  # Turn LED off
print(send_command("STATUS"))   # Get status
```

## I2C Pin Mapping
- **I2C0 SDA**: GPIO28 (Pin 2) or GPIO04 (Pin 4)
- **I2C0 SCL**: GPIO29 (Pin 3) or GPIO05 (Pin 6)
- **I2C1 SDA**: GPIO06 (Pin 7) or GPIO10 (Pin 12)
- **I2C1 SCL**: GPIO07 (Pin 15) or GPIO11 (Pin 10)

## ADC Pins (Analog Input)
- GPIO26 (Pin 23) - ADC0
- GPIO27 (Pin 32) - ADC1
- GPIO28 (Pin 2) - ADC2
- GPIO29 (Pin 3) - ADC3 (also internal temp sensor)

## Safety Notes

1. **3.3V logic only** - Do not apply 5V to GPIO pins
2. **Max 16mA per pin** - Use transistor/MOSFET for motors/relays
3. **RP2040 can crash** - Use reset script to recover
4. **Serial port may change** - Check /dev/ttyACM* after reset

## OpenClaw Integration Pattern

For SAP (SpecialAgentPuddy) to control GPIO:

1. Flash MicroPython with command listener to RP2040
2. Create OpenClaw skill that:
   - Opens serial connection to RP2040
   - Sends commands (LED_ON, LED_OFF, READ_SENSOR, etc.)
   - Parses responses
   - Returns results to agent

3. Skill script example:
```bash
#!/bin/bash
# gpio-control.sh
# Usage: gpio-control.sh LED_ON|LED_OFF|STATUS

COMMAND="$1"
PORT="/dev/ttyACM0"

# Send command and read response
echo "$COMMAND" > "$PORT"
sleep 0.1
head -n1 < "$PORT"
```

## References

- Radxa X2L GPIO Docs: https://docs.radxa.com/en/x/x2l/software-development/gpio
- MicroPython Docs: https://docs.radxa.com/en/x/x2l/software-development/micro_python
- C SDK Examples: https://docs.radxa.com/en/x/x2l/software-development/c_sdk_examples
- DPHacks X2L Guide: https://dphacks.com/2024/02/18/radxa-x2l-a-mini-pc-and-a-raspberry-pi-crossover/

---

*Generated for Project Opengates - SpecialAgentPuddy GPIO development*
