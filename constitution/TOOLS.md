# TOOLS.md - Local Hardware & Skills

## GPIO Control (RP2040)

The Radxa X2L has an onboard RP2040 microcontroller controlling the 40-pin GPIO header.

### Available Commands

```bash
# Turn LED on (GPIO25)
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led on

# Turn LED off
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led off

# Toggle LED
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led toggle

# Blink LED N times
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh led blink 3

# Check status
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh status

# Test connection
/home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh ping
```

### Hardware Info

- **Serial Port:** /dev/ttyACM0
- **LED Pin:** GPIO25 (Pin 21 on 40-pin header)
- **Voltage:** 3.3V logic
- **Safe State:** LED OFF

### Safety Classification (SOUL.md Article 15)

**Level 1 - Reversible Action**
- LED toggle is instantly reversible
- No confirmation required
- Safe state = OFF (0V)

When asked to control the LED, just run the script. No need for extensive safety analysis - this is pre-approved Level 1.

## Moltbook

See skills/moltbook-interact/SKILL.md for social posting commands.
