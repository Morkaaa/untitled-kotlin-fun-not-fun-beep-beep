from machine import Pin, PWM
from time import sleep_ms

e2 = const(659)
gis2 = const(831)
fis2 = const(740)
h2 = const(988)
a2 = const(880)
dis2 = const(622)
h1 = const(494)
cis3 = const(1109)
dis3 = const(1245)
e3 = const(1319)
fis3 = const(1480)
gis1 = const(415)
a1 = const(440)
cis2 = const(554)
ais2 = const(932)
c3 = const(1047)
gis3 = const(1661)
c2 = const(523)
d3 = const(1175)
e1 = const(330)
fis1 = const(370)
d2 = const(587)
g2 = const(784)
dis1 = const(311)
h = const(247)
f2 = const(698)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón * 2, duty_u16=2**15)
    sleep_ms(trvanie // 2)
    buzzer.duty_u16(0)
    sleep_ms(pauza // 2)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep_ms(1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, h2, 1500)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, h2, 1500)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 500)
ZahrajTón(buzzer, dis2, 500)
ZahrajTón(buzzer, h1, 500)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, h2, 1500)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, h2, 1500)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 1000, 500)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 1000, 500)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 10)
ZahrajTón(buzzer, h2, 55, 3)
ZahrajTón(buzzer, cis3, 55, 3)
ZahrajTón(buzzer, h2, 885)
ZahrajTón(buzzer, h2, 55, 3)
ZahrajTón(buzzer, cis3, 55, 3)
ZahrajTón(buzzer, h2, 1000, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125, 500)
ZahrajTón(buzzer, h2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 1000, 500)
ZahrajTón(buzzer, h2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 1000, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, dis3, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, dis3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250, 500)
ZahrajTón(buzzer, h2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 1000, 500)
ZahrajTón(buzzer, h2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 1000)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, dis3, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, dis3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250, 1500)
ZahrajTón(buzzer, e3, 500)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, e3, 500)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, e3, 250, 250)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125, 1000)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125, 1000)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125, 1000)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, h2, 1250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 1250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250, 1250)
ZahrajTón(buzzer, e3, 250, 750)
ZahrajTón(buzzer, e3, 250, 750)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, e3, 250, 750)
ZahrajTón(buzzer, e3, 250, 750)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125)
ZahrajTón(buzzer, fis3, 125)
ZahrajTón(buzzer, e3, 125, 500)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, h2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, cis3, 500)
ZahrajTón(buzzer, h2, 1000)
ZahrajTón(buzzer, a2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, gis2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, gis1, 1000, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, a2, 2000)
ZahrajTón(buzzer, gis2, 2000)
ZahrajTón(buzzer, fis2, 2000)
ZahrajTón(buzzer, gis2, 2000)
ZahrajTón(buzzer, a2, 2000)
ZahrajTón(buzzer, gis2, 2000)
ZahrajTón(buzzer, fis2, 1000, 500)
ZahrajTón(buzzer, h1, 500)
ZahrajTón(buzzer, fis2, 500)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, fis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 1000)
ZahrajTón(buzzer, h1, 500)
ZahrajTón(buzzer, fis2, 500)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, fis2, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 1000)
ZahrajTón(buzzer, h1, 500)
ZahrajTón(buzzer, gis2, 500)
ZahrajTón(buzzer, fis2, 1000)
ZahrajTón(buzzer, e2, 500)
ZahrajTón(buzzer, dis2, 500)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, dis2, 125)
ZahrajTón(buzzer, cis2, 125)
ZahrajTón(buzzer, dis2, 125)
ZahrajTón(buzzer, cis2, 125)
ZahrajTón(buzzer, dis2, 125)
ZahrajTón(buzzer, cis2, 125)
ZahrajTón(buzzer, dis2, 125)
ZahrajTón(buzzer, cis2, 125)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, cis2, 125)
ZahrajTón(buzzer, dis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, h2, 125, 1000)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, cis2, 125)
ZahrajTón(buzzer, dis2, 125)
ZahrajTón(buzzer, e2, 125)
ZahrajTón(buzzer, fis2, 125)
ZahrajTón(buzzer, gis2, 125)
ZahrajTón(buzzer, a2, 125)
ZahrajTón(buzzer, h2, 125, 1000)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, h1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, a1, 125)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, gis2, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, gis2, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, gis2, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, gis2, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, h2, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, cis3, 1000, 1000)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, ais2, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, ais2, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, ais2, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, ais2, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, cis3, 167)
ZahrajTón(buzzer, e3, 167)
ZahrajTón(buzzer, dis3, 1000, 1000)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, c3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, gis3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, gis3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, c3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, gis3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, gis3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, c3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, c3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, dis3, 167)
ZahrajTón(buzzer, fis3, 167)
ZahrajTón(buzzer, e3, 1000, 1000)