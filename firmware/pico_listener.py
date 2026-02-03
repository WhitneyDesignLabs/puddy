# pico_listener.py - SpecialAgentPuddy GPIO Command Listener
# Runs on RP2040 (MicroPython)
# Listens for commands from Linux host via USB serial

import machine
import sys
import select
import time

# Onboard LED (GPIO25 on standard Pico)
led = machine.Pin(25, machine.Pin.OUT)

# Version info
VERSION = "1.0.0"
AGENT = "SpecialAgentPuddy"

def blink(times=3, delay=0.2):
    """Blink the LED"""
    for _ in range(times):
        led.value(1)
        time.sleep(delay)
        led.value(0)
        time.sleep(delay)

def handle_command(cmd):
    """Process incoming command and return response"""
    cmd = cmd.strip().upper()

    if cmd == "LED_ON":
        led.value(1)
        return "OK:LED_ON"

    elif cmd == "LED_OFF":
        led.value(0)
        return "OK:LED_OFF"

    elif cmd == "LED_TOGGLE":
        led.value(not led.value())
        return f"OK:LED_TOGGLE:{led.value()}"

    elif cmd == "BLINK":
        blink(3, 0.2)
        return "OK:BLINK"

    elif cmd.startswith("BLINK:"):
        try:
            times = int(cmd.split(":")[1])
            blink(times, 0.2)
            return f"OK:BLINK:{times}"
        except:
            return "ERR:INVALID_BLINK_COUNT"

    elif cmd == "STATUS":
        return f"OK:LED={led.value()}"

    elif cmd == "VERSION":
        return f"OK:VERSION={VERSION}"

    elif cmd == "WHOAMI":
        return f"OK:AGENT={AGENT}"

    elif cmd == "PING":
        return "OK:PONG"

    elif cmd == "HELP":
        return "OK:COMMANDS=LED_ON,LED_OFF,LED_TOGGLE,BLINK,BLINK:N,STATUS,VERSION,WHOAMI,PING,HELP"

    elif cmd == "":
        return None  # Ignore empty lines

    else:
        return f"ERR:UNKNOWN_COMMAND:{cmd}"

# Startup blink to indicate we're running
blink(2, 0.1)
print(f"OK:READY:{AGENT}:v{VERSION}")

# Main loop - listen for commands
while True:
    try:
        if select.select([sys.stdin], [], [], 0.1)[0]:
            line = sys.stdin.readline()
            if line:
                response = handle_command(line)
                if response:
                    print(response)
    except Exception as e:
        print(f"ERR:EXCEPTION:{e}")
