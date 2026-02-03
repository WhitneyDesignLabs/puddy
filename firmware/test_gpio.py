#!/usr/bin/env python3
"""
test_gpio.py - Test script for SpecialAgentPuddy GPIO control
Sends commands to RP2040 via serial and displays responses
"""

import serial
import time
import sys

PORT = "/dev/ttyACM0"
BAUD = 115200

def send_command(ser, cmd):
    """Send a command and get response"""
    ser.write((cmd + '\n').encode())
    time.sleep(0.1)
    response = ser.readline().decode().strip()
    return response

def main():
    print(f"Connecting to RP2040 on {PORT}...")

    try:
        ser = serial.Serial(PORT, BAUD, timeout=2)
        time.sleep(0.5)  # Wait for connection

        # Clear any pending data
        ser.reset_input_buffer()

        # Test commands
        commands = ["PING", "WHOAMI", "VERSION", "STATUS", "LED_ON", "STATUS", "LED_OFF", "STATUS", "BLINK", "HELP"]

        print("\n--- Testing GPIO Commands ---\n")

        for cmd in commands:
            response = send_command(ser, cmd)
            print(f"  {cmd:15} -> {response}")
            time.sleep(0.3)

        print("\n--- Test Complete ---")
        ser.close()

    except serial.SerialException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
