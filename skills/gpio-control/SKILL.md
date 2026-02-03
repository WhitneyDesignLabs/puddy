# GPIO Control Skill

Control the RP2040 GPIO pins on the Radxa X2L via serial commands.

## Commands

- `gpio led on` - Turn onboard LED on
- `gpio led off` - Turn onboard LED off
- `gpio led toggle` - Toggle LED state
- `gpio led blink [N]` - Blink LED N times (default 3)
- `gpio status` - Get current LED status
- `gpio ping` - Test connection to RP2040

## Usage

```
/gpio led on
/gpio blink 5
/gpio status
```

## Requirements

- RP2040 must be running pico_listener.py (MicroPython)
- Serial port /dev/ttyACM0 must be accessible
- User must be in dialout group

## Safety

This skill controls physical hardware. Per SOUL.md Article 12 (Safety Hierarchy):
- LED control is low-risk (no harm potential)
- Future GPIO extensions must implement appropriate safeguards
