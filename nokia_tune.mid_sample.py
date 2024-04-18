from machine import Pin, PWM
from time import sleep_ms

e3 = const(1319)
d3 = const(1175)
fis2 = const(740)
gis2 = const(831)
cis3 = const(1109)
h2 = const(988)
d2 = const(587)
e2 = const(659)
a2 = const(880)
cis2 = const(554)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón, duty_u16=2**15)
    sleep_ms(trvanie)
    buzzer.duty_u16(0)
    sleep_ms(pauza)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep_ms(1000)
ZahrajTón(buzzer, e3, 242, 8)
ZahrajTón(buzzer, d3, 256, 21)
ZahrajTón(buzzer, fis2, 469, 15)
ZahrajTón(buzzer, gis2, 475, 4)
ZahrajTón(buzzer, cis3, 221, 2)
ZahrajTón(buzzer, h2, 271, 2)
ZahrajTón(buzzer, d2, 529, 2)
ZahrajTón(buzzer, e2, 567, 2)
ZahrajTón(buzzer, h2, 265, 6)
ZahrajTón(buzzer, a2, 323, 2)
ZahrajTón(buzzer, cis2, 606, 4)
ZahrajTón(buzzer, e2, 677)
ZahrajTón(buzzer, a2, 2000)