from machine import Pin, PWM
from time import sleep

c2 = const(523)
g1 = const(392)
a1 = const(440)
h1 = const(494)
e1 = const(330)
f1 = const(349)
c1 = const(262)
d1 = const(294)
d2 = const(587)
e2 = const(659)
f2 = const(698)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón, duty_u16=2**15)
    sleep(trvanie * 0.5)
    buzzer.duty_u16(0)
    sleep(pauza)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep(1)
ZahrajTón(buzzer, c2, 3.0)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, g1, 0.75)
ZahrajTón(buzzer, a1, 0.25)
ZahrajTón(buzzer, h1, 1.0)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, a1, 1.0)
ZahrajTón(buzzer, g1, 0.75)
ZahrajTón(buzzer, f1, 0.25)
ZahrajTón(buzzer, g1, 1.0)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, d1, 1.0)
ZahrajTón(buzzer, d1, 0.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, f1, 1.0)
ZahrajTón(buzzer, f1, 0.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, a1, 1.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, d2, 1.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, e2, 1.0)
ZahrajTón(buzzer, d2, 0.75)
ZahrajTón(buzzer, c2, 0.25)
ZahrajTón(buzzer, d2, 1.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, h1, 0.75)
ZahrajTón(buzzer, a1, 0.25)
ZahrajTón(buzzer, h1, 1.0)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, a1, 1.0)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, f1, 0.5)
ZahrajTón(buzzer, g1, 1.0)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, h1, 0.75)
ZahrajTón(buzzer, a1, 0.25)
ZahrajTón(buzzer, g1, 2.0)
ZahrajTón(buzzer, e2, 2.0)
ZahrajTón(buzzer, d2, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, d2, 1.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, g1, 2.0)
ZahrajTón(buzzer, c2, 2.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, h1, 1.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, e1, 1.0)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, a1, 0.75)
ZahrajTón(buzzer, h1, 0.25)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, a1, 0.75)
ZahrajTón(buzzer, h1, 0.25)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, c2, 2.0)
ZahrajTón(buzzer, f2, 2.0)
ZahrajTón(buzzer, e2, 0.5)
ZahrajTón(buzzer, d2, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, d2, 0.5)
ZahrajTón(buzzer, e2, 1.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, c2, 2.0)
ZahrajTón(buzzer, d2, 2.0)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, c2, 1.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, a1, 2.0)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, g1, 1.0)
ZahrajTón(buzzer, c1, 0.75)
ZahrajTón(buzzer, c1, 0.25)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, h1, 0.75)
ZahrajTón(buzzer, a1, 0.25)
ZahrajTón(buzzer, g1, 1.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, g1, 0.75)
ZahrajTón(buzzer, a1, 0.25)
ZahrajTón(buzzer, h1, 1.0)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, a1, 1.0)
ZahrajTón(buzzer, g1, 0.75)
ZahrajTón(buzzer, f1, 0.25)
ZahrajTón(buzzer, g1, 1.0)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, d1, 1.0)
ZahrajTón(buzzer, d1, 0.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, f1, 1.0)
ZahrajTón(buzzer, f1, 0.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, a1, 1.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, d2, 1.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, e2, 1.0)
ZahrajTón(buzzer, d2, 0.75)
ZahrajTón(buzzer, c2, 0.25)
ZahrajTón(buzzer, d2, 1.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, h1, 0.75)
ZahrajTón(buzzer, a1, 0.25)
ZahrajTón(buzzer, h1, 1.0)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, a1, 1.0)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, f1, 0.5)
ZahrajTón(buzzer, g1, 1.0)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, c1, 0.5)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, h1, 0.75)
ZahrajTón(buzzer, a1, 0.25)
ZahrajTón(buzzer, g1, 2.0)
ZahrajTón(buzzer, e2, 2.0)
ZahrajTón(buzzer, d2, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, d2, 1.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, g1, 2.0)
ZahrajTón(buzzer, c2, 2.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, g1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, h1, 1.5)
ZahrajTón(buzzer, e1, 0.5)
ZahrajTón(buzzer, e1, 1.0)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, a1, 0.75)
ZahrajTón(buzzer, h1, 0.25)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, a1, 0.75)
ZahrajTón(buzzer, h1, 0.25)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, c2, 2.0)
ZahrajTón(buzzer, f2, 2.0)
ZahrajTón(buzzer, e2, 0.5)
ZahrajTón(buzzer, d2, 0.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, d2, 0.5)
ZahrajTón(buzzer, e2, 1.5)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, c2, 2.0)
ZahrajTón(buzzer, d2, 2.0)
ZahrajTón(buzzer, c2, 0.5)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, c2, 1.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, a1, 2.0)
ZahrajTón(buzzer, c2, 1.0)
ZahrajTón(buzzer, h1, 0.5)
ZahrajTón(buzzer, a1, 0.5)
ZahrajTón(buzzer, g1, 1.0)
ZahrajTón(buzzer, c1, 0.75)
ZahrajTón(buzzer, c1, 0.25)
ZahrajTón(buzzer, g1, 2.0)
ZahrajTón(buzzer, a1, 1.0)
ZahrajTón(buzzer, h1, 1.0)
ZahrajTón(buzzer, c2, 3.0)