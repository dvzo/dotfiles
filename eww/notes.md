# notes

### commands
$ sensors -> CPU temps
$ brightnessctl -> brightness
$ df -H -> storage
$ top | grep "MiB Mem" -> calculate CPU usage

### battery
- using EWW_BATTERY
    - statuses:
    - Not charging -> charging but 50% with uefi settings
    - Charging
    - Discharing -> unplugged

### listen for workspace/ hyprctl changes
$ socat -U - UNIX-CONNECT:/tmp/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock | grep -w "workspace"
