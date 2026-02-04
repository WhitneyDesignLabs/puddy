---
name: gpio
description: Control GPIO pins and read sensors on the RP2040 microcontroller. Toggle LED, blink patterns, read temperature/humidity from DHT11.
---

# GPIO Control Skill

Control the RP2040 GPIO pins on the Radxa X2L via serial commands.

## Script Location

**Always use the full path:**
```
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh
```

## Commands

### Turn LED On
```bash
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led on
```

### Turn LED Off
```bash
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led off
```

### Toggle LED
```bash
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led toggle
```

### Blink LED
```bash
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led blink [N]
```
- N = number of blinks (default 3)

### Check Status
```bash
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh status
```

### Test Connection
```bash
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh ping
```

### Read Temperature & Humidity (DHT11)
```bash
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh sensor read
```
- Returns JSON: `{"temp_c": 25, "temp_f": 77.0, "humidity": 45}`
- Sensor needs 2 seconds between reads (enforced by firmware)
- Use this when user asks about temperature, humidity, or environmental conditions

## Hardware Info

### LED
- **Pin:** GPIO25 (onboard LED)
- **Voltage:** 3.3V logic
- **Safe state:** OFF (0V)

### DHT11 Temperature/Humidity Sensor
- **Pin:** GPIO28
- **Wiring:** VCC=3.3V, GND=GND, Data=GPIO28
- **Read interval:** Minimum 2 seconds between reads
- **Accuracy:** ±2°C temperature, ±5% humidity

## Safety (SOUL.md Compliance)

This is **Article 15 Level 1** (Reversible action):
- LED toggle is instantly reversible
- No confirmation required for standard operation
- Safe state = LED OFF
- Failure mode = LED remains in last state (non-hazardous)
