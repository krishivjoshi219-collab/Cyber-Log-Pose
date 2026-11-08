# Cyber Log Pose - barebones MicroPython firmware
# ESP32-C3 SuperMini + SSD1306 OLED + IR tx/rx + 5-way nav
# this is just the starter build week firmware, not the final boss code yet lol

from machine import Pin, I2C, ADC
import time

# ===== pin map from the PCB =====
PIN_NAV_UP = 4
PIN_NAV_DOWN = 3
PIN_BATT = 2
PIN_IR_TX = 1
PIN_SDA = 0
PIN_SCL = 5
PIN_NAV_LEFT = 6
PIN_IR_RX = 7
PIN_NAV_RIGHT = 10
PIN_NAV_PRESS = 20

# ===== setup =====
nav_up = Pin(PIN_NAV_UP, Pin.IN, Pin.PULL_UP)
nav_down = Pin(PIN_NAV_DOWN, Pin.IN, Pin.PULL_UP)
nav_left = Pin(PIN_NAV_LEFT, Pin.IN, Pin.PULL_UP)
nav_right = Pin(PIN_NAV_RIGHT, Pin.IN, Pin.PULL_UP)
nav_press = Pin(PIN_NAV_PRESS, Pin.IN, Pin.PULL_UP)

ir_tx = Pin(PIN_IR_TX, Pin.OUT)
ir_rx = Pin(PIN_IR_RX, Pin.IN)

battery = ADC(Pin(PIN_BATT))
battery.atten(ADC.ATTN_11DB)

i2c = I2C(0, scl=Pin(PIN_SCL), sda=Pin(PIN_SDA), freq=400000)

# OLED is optional at boot so firmware does not just die if wiring is wrong
try:
    import ssd1306
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
except Exception as e:
    oled = None
    print("OLED not ready:", e)

menu = ["IR BLAST", "IR READ", "BATTERY", "ABOUT"]
index = 0


def pressed(pin):
    return pin.value() == 0


def battery_voltage():
    # divider is 100k/100k so ADC pin sees half the battery voltage
    raw = battery.read()
    # rough estimate for ESP32 ADC range with 11dB, good enough for first firmware
    v_adc = (raw / 4095) * 3.3
    return v_adc * 2


def draw():
    if oled is None:
        return
    oled.fill(0)
    oled.text("CYBER LOG POSE", 3, 0)
    oled.text("-" * 16, 0, 10)
    for i, item in enumerate(menu):
        prefix = ">" if i == index else " "
        oled.text(prefix + item, 0, 20 + i * 10)
    oled.show()


def blast_test():
    # simple visible debug burst, not real NEC yet
    # real IR remote codes come in build week
    for _ in range(80):
        ir_tx.value(1)
        time.sleep_us(13)
        ir_tx.value(0)
        time.sleep_us(13)


def show_battery():
    v = battery_voltage()
    if oled:
        oled.fill(0)
        oled.text("BATTERY", 0, 0)
        oled.text("%.2f V" % v, 0, 18)
        oled.text("press to back", 0, 45)
        oled.show()
    print("battery", v)


def show_about():
    if oled:
        oled.fill(0)
        oled.text("Cyber Log Pose", 0, 0)
        oled.text("IR fob thingy", 0, 14)
        oled.text("week 5 !!!", 0, 28)
        oled.text("press to back", 0, 50)
        oled.show()


draw()
last = time.ticks_ms()

while True:
    if time.ticks_diff(time.ticks_ms(), last) > 160:
        if pressed(nav_up):
            index = (index - 1) % len(menu)
            draw()
            last = time.ticks_ms()
        elif pressed(nav_down):
            index = (index + 1) % len(menu)
            draw()
            last = time.ticks_ms()
        elif pressed(nav_press):
            selected = menu[index]
            if selected == "IR BLAST":
                blast_test()
            elif selected == "BATTERY":
                show_battery()
            elif selected == "ABOUT":
                show_about()
            else:
                print("IR RX state:", ir_rx.value())
            last = time.ticks_ms()

    time.sleep_ms(10)
