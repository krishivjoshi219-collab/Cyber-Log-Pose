# firmware

this is the tiny starter micropython firmware for cyber log pose.

## how to run

1. flash MicroPython on the ESP32-C3 SuperMini
2. copy `main.py` to the board
3. add `ssd1306.py` to the board too if your firmware does not already have it
4. reboot and pray the oled wakes up lol

## pins

- SDA = GPIO0
- SCL = GPIO5
- IR TX = GPIO1
- IR RX = GPIO7
- battery sense = GPIO2
- nav up/down/left/right/press = GPIO4/GPIO3/GPIO6/GPIO10/GPIO20

this is just barebones so build week me will write the real IR cloning stuff later.
