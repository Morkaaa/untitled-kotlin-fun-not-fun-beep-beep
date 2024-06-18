from machine import Pin, PWM
from time import sleep

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
    sleep(trvanie)
    buzzer.duty_u16(0)
    sleep(pauza)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep(0.1)
ZahrajTón(buzzer, e3, 0.24166666666666667)
ZahrajTón(buzzer, d3, 0.25625)
ZahrajTón(buzzer, fis2, 0.46875)
ZahrajTón(buzzer, gis2, 0.475)
ZahrajTón(buzzer, cis3, 0.22083333333333333)
ZahrajTón(buzzer, h2, 0.2708333333333333)
ZahrajTón(buzzer, d2, 0.5291666666666667)
ZahrajTón(buzzer, e2, 0.5666666666666667)
ZahrajTón(buzzer, h2, 0.26458333333333334)
ZahrajTón(buzzer, a2, 0.3229166666666667)
ZahrajTón(buzzer, cis2, 0.60625)
ZahrajTón(buzzer, e2, 0.6770833333333334)
ZahrajTón(buzzer, a2, 2.0)
