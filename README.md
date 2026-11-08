# 🏴‍☠️ Cyber Log Pose

YO HACK CLUB REVIEWERS !!!!!!!!!!

this is **Cyber Log Pose**, my tiny pocket IR hacker fob thingy for Half-Life Week 5 freestyle. i was first trying to do a whole smartwatch and then my brain basically melted so i scoped it down into something i can ACTUALLY build in build week without crying lol.

it is like a little straw-hat themed remote cloner / IR blaster with an OLED and a 5-way nav button. basically point it at a TV / projector / random remote and later it can replay commands. the firmware right now is barebones because this week was mostly design week, but the pcb + case + bom are ready.

---

## screenshots from my devlog

schematic / pcb / cad chaos from the Half-Life journal:

![schematic screenshot](https://halflife.hackclub-assets.com/sessions/juuCZTVxWjBD33E1UrFKdMsSuU9pEnCH/192d2cb264aaa1268223e0ef6d01c72e8547f6af53f64a36693669b2dc4f0615.png)

![pcb routing screenshot](https://halflife.hackclub-assets.com/sessions/juuCZTVxWjBD33E1UrFKdMsSuU9pEnCH/e8f17d1e970dd476198782e450a2071693c00d335f432d99b98a526c175d3c53.png)

![cad screenshot](https://halflife.hackclub-assets.com/sessions/juuCZTVxWjBD33E1UrFKdMsSuU9pEnCH/66ee71bf8e9ba216e5f0615250f5a8bc586b75db74a6516eca6524c25daffe85.png)

![final-ish screenshot](https://halflife.hackclub-assets.com/sessions/juuCZTVxWjBD33E1UrFKdMsSuU9pEnCH/801849ba7e4e9a532a29cb71d6d4b397dd63870a01fe6eff192c2da640d5d3c8.png)

---

## what it does

- uses an **ESP32-C3 SuperMini** as the brain
- has a **0.96 inch I2C OLED** for menus
- has an **IR transmitter** for blasting remote commands
- has a **VS1838B IR receiver** for learning / reading remote signals
- has a **5-way navigation button** so it feels like a tiny gadget not a random breadboard mess
- runs from a **420mAh LiPo** with a **TP4056 Type-C charger**
- has a custom pcb with straw-hat-ish silkscreen because plain rectangles are BORING
- has a 2-piece 3d printed case, and i even added a charger U-cutout so the usb cable can actually go inside

---

## repo map

```txt
├── BOM.csv                 <- parts + prices, kept around $32-$33 with print reserve
├── JOURNAL.md              <- synced Half-Life devlog with my screenshots
├── PCB/
│   ├── Cyber Log Pose.kicad_pro
│   ├── Cyber Log Pose.kicad_sch
│   ├── Cyber Log Pose.kicad_pcb
│   └── Cyber Log Pose.step
├── CAD/
│   ├── Cyber Log Pose - Base - Charger U Cutout.stl
│   └── Cyber Log Pose - Top.stl
├── firmware/
│   ├── main.py
│   └── README.md
└── production/             <- gerbers will go here when i export final fab files
```

---

## pinout

| thing | GPIO |
| --- | --- |
| OLED SDA | GPIO0 |
| OLED SCL | GPIO5 |
| IR TX | GPIO1 |
| IR RX | GPIO7 |
| Battery sense | GPIO2 |
| Nav up | GPIO4 |
| Nav down | GPIO3 |
| Nav left | GPIO6 |
| Nav right | GPIO10 |
| Nav press | GPIO20 |

important: **ESP32-C3 GPIO is 3.3V ONLY**. no 5v signal jumpscare pls.

---

## budget

latest BOM is around:

```txt
₹2869 / about $32.63
```

that includes pcb at ₹949 and 3d print reserve for around 15g print weight. it is TIGHT but still under my $33 target.

---

## current status

- schematic done
- pcb routed
- DRC = 0 errors
- case STL exported
- charger cutout added to base
- barebones firmware added
- build week me still has to write the real IR decode/replay firmware

---

## why i made it

because i wanted something with the hacker energy of my crazy smartwatch idea but actually buildable in time. this is still cool, still useful, and doesn't need 100 tiny smartwatch parts. also it is One Piece themed because obviously.

ok bye reviewers pls approve this tiny chaos machine :D
