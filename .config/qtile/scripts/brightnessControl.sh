#!/usr/bin/env bash


# You can call this script like this:
# $ ./brightnessControl.sh up
# $ ./brightnessControl.sh down

# Script inspired by these wonderful people:
# https://github.com/dastorm/volume-notification-dunst/blob/master/volume.sh
# https://gist.github.com/sebastiencs/5d7227f388d93374cebdf72e783fbd6a

function get_brightness {
  # xbacklight -get | cut -d '.' -f 1
  brightnessctl -m -d intel_backlight | awk -F, '{ print substr($4, 0, length($4)-1) }'
}

function send_notification {
  icon="preferences-system-brightness-lock"
  brightness=$(get_brightness)
  bar=$(seq -s "─" 0 $((brightness / 5)) | sed 's/[0-9]//g')
  # Send the notification
  dunstify -i "$icon" -r 5555 -u normal "    $bar     $brightness%"
}

case $1 in
  up)
    # increase the backlight by 5%
    # xbacklight -inc 5
    brightnessctl s 5%+
    send_notification
    ;;
  down)
    # decrease the backlight by 5%
    # xbacklight -dec 5
    brightnessctl s 5%-
    send_notification
    ;;
  sup)
    # increase the backlight by 1%
    # xbacklight -inc 1
    brightnessctl s 1%+
    send_notification
    ;;
  sdown)
    # decrease the backlight by 1%
    # xbacklight -dec 1
    brightnessctl s 1%-
    send_notification
    ;;
esac
