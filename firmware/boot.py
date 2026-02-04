# boot.py - SpecialAgentPuddy Boot Configuration
# Runs before main.py on RP2040 startup

import machine
import time

# Brief delay to let USB serial stabilize after power-on
time.sleep_ms(200)

# main.py runs automatically after this
