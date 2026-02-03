---
name: gpio
description: Control GPIO pins on the RP2040 microcontroller. Toggle LED, blink patterns, check status.
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

## Hardware Info

- **Pin:** GPIO25 (Pin 21 on 40-pin header)
- **Voltage:** 3.3V logic
- **Current state tracking:** Maintained by RP2040 firmware
- **Safe state:** OFF (0V)

## Safety (SOUL.md Compliance)

This is **Article 15 Level 1** (Reversible action):
- LED toggle is instantly reversible
- No confirmation required for standard operation
- Safe state = LED OFF
- Failure mode = LED remains in last state (non-hazardous)
