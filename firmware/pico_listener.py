# pico_listener.py - SpecialAgentPuddy GPIO Command Listener
# Runs on RP2040 (MicroPython)
# Listens for commands from Linux host via USB serial

import machine
import sys
import select
import time
import dht
import json

# Onboard LED (GPIO25 on standard Pico)
led = machine.Pin(25, machine.Pin.OUT)

# DHT11 sensor on GPIO28
dht_pin = machine.Pin(28)
dht_sensor = dht.DHT11(dht_pin)

# Track last DHT read time (needs 1-2s between reads)
last_dht_read = 0
DHT_MIN_INTERVAL = 2  # seconds

# Version info
VERSION = "1.1.0"
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

    elif cmd == "DHT_READ":
        global last_dht_read
        now = time.time()
        # Enforce minimum interval between reads
        if now - last_dht_read < DHT_MIN_INTERVAL:
            time.sleep(DHT_MIN_INTERVAL - (now - last_dht_read))
        try:
            dht_sensor.measure()
            last_dht_read = time.time()
            temp_c = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            temp_f = temp_c * 9 / 5 + 32
            result = {
                "temp_c": temp_c,
                "temp_f": round(temp_f, 1),
                "humidity": humidity
            }
            return "OK:DHT:" + json.dumps(result)
        except OSError as e:
            return "ERR:DHT_READ_FAILED:sensor_error"
        except Exception as e:
            return f"ERR:DHT_READ_FAILED:{e}"

    elif cmd == "HELP":
        return "OK:COMMANDS=LED_ON,LED_OFF,LED_TOGGLE,BLINK,BLINK:N,DHT_READ,STATUS,VERSION,WHOAMI,PING,HELP"

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
