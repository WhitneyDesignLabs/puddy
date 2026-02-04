#!/bin/bash
# gpio.sh - GPIO control script for SpecialAgentPuddy
# Location: /home/scott/.openclaw/workspace/skills/gpio-control/scripts/gpio.sh
# Usage: gpio.sh <command> [args]
#
# Commands:
#   led on|off|toggle|blink [N]
#   sensor read
#   status
#   ping
#   raw <COMMAND>

PORT="/dev/ttyACM0"
TIMEOUT=2

send_command() {
    local cmd="$1"
    # Send command and read response
    exec 3<>"$PORT"
    echo "$cmd" >&3
    read -t "$TIMEOUT" response <&3
    exec 3>&-
    echo "$response"
}

# Check port exists
if [[ ! -e "$PORT" ]]; then
    echo "ERR:PORT_NOT_FOUND:$PORT"
    exit 1
fi

# Parse command
case "${1,,}" in
    led)
        case "${2,,}" in
            on)
                send_command "LED_ON"
                ;;
            off)
                send_command "LED_OFF"
                ;;
            toggle)
                send_command "LED_TOGGLE"
                ;;
            blink)
                if [[ -n "$3" ]]; then
                    send_command "BLINK:$3"
                else
                    send_command "BLINK"
                fi
                ;;
            *)
                echo "ERR:UNKNOWN_LED_COMMAND:$2"
                echo "Usage: gpio.sh led on|off|toggle|blink [N]"
                exit 1
                ;;
        esac
        ;;
    sensor|dht)
        case "${2,,}" in
            read|"")
                send_command "DHT_READ"
                ;;
            *)
                echo "ERR:UNKNOWN_SENSOR_COMMAND:$2"
                echo "Usage: gpio.sh sensor read"
                exit 1
                ;;
        esac
        ;;
    status)
        send_command "STATUS"
        ;;
    ping)
        send_command "PING"
        ;;
    version)
        send_command "VERSION"
        ;;
    whoami)
        send_command "WHOAMI"
        ;;
    help)
        send_command "HELP"
        ;;
    raw)
        shift
        send_command "$*"
        ;;
    *)
        echo "GPIO Control for SpecialAgentPuddy"
        echo ""
        echo "Usage: gpio.sh <command> [args]"
        echo ""
        echo "Commands:"
        echo "  led on          Turn LED on"
        echo "  led off         Turn LED off"
        echo "  led toggle      Toggle LED"
        echo "  led blink [N]   Blink N times (default 3)"
        echo "  sensor read     Read DHT11 temperature/humidity"
        echo "  status          Get LED status"
        echo "  ping            Test connection"
        echo "  version         Get firmware version"
        echo "  whoami          Get agent name"
        echo "  raw <CMD>       Send raw command"
        exit 0
        ;;
esac
