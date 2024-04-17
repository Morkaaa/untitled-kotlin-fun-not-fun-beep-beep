from machine import Pin, PWM
from time import sleep_ms

f1 = const(349)
dis1 = const(311)
d1 = const(294)
fis1 = const(370)
gis1 = const(415)
ais1 = const(466)
h1 = const(494)
a1 = const(440)
f2 = const(698)
dis2 = const(622)
d2 = const(587)
fis2 = const(740)
cis2 = const(554)
c2 = const(523)
cis1 = const(277)
ais  = const(233)
g2 = const(784)
g1 = const(392)
c1 = const(262)
gis2 = const(831)
e2 = const(659)
ais2 = const(932)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón * 2, duty_u16=2**15)
    sleep_ms(trvanie // 2)
    buzzer.duty_u16(0)
    sleep_ms(pauza // 2)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep_ms(1000)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, fis1, 250, 750)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, ais1, 250, 750)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, fis2, 1000)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 125)
ZahrajTón(buzzer, cis2, 62)
ZahrajTón(buzzer, dis2, 62)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 125)
ZahrajTón(buzzer, cis2, 62)
ZahrajTón(buzzer, dis2, 62)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 125)
ZahrajTón(buzzer, cis2, 62)
ZahrajTón(buzzer, dis2, 125, 188)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, c2, 250)
ZahrajTón(buzzer, a1, 250, 250)
ZahrajTón(buzzer, ais1, 938, 62)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, fis1, 250, 750)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, ais1, 250, 750)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, fis2, 1000)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 125)
ZahrajTón(buzzer, cis2, 62)
ZahrajTón(buzzer, dis2, 62)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 125)
ZahrajTón(buzzer, cis2, 62)
ZahrajTón(buzzer, dis2, 62)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 125)
ZahrajTón(buzzer, cis2, 62)
ZahrajTón(buzzer, dis2, 125, 188)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, c2, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, c2, 250)
ZahrajTón(buzzer, a1, 250, 250)
ZahrajTón(buzzer, ais1, 938, 62)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, gis1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f1, 500)
ZahrajTón(buzzer, gis1, 1000)
ZahrajTón(buzzer, cis1, 500)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, gis1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f1, 1000)
ZahrajTón(buzzer, gis1, 1000)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, d1, 500)
ZahrajTón(buzzer, f1, 1000)
ZahrajTón(buzzer, ais , 500)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, d1, 1000)
ZahrajTón(buzzer, f1, 1000)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, fis1, 250, 750)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, ais1, 250, 750)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, fis2, 1000)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 250)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, d2, 250, 250)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, ais1, 250, 258)
ZahrajTón(buzzer, h1, 250, 242)
ZahrajTón(buzzer, gis1, 250, 250)
ZahrajTón(buzzer, fis1, 1000)
ZahrajTón(buzzer, f1, 125)
ZahrajTón(buzzer, fis1, 125)
ZahrajTón(buzzer, f1, 125)
ZahrajTón(buzzer, fis1, 125)
ZahrajTón(buzzer, f1, 8, 75)
ZahrajTón(buzzer, fis1, 83)
ZahrajTón(buzzer, f1, 83)
ZahrajTón(buzzer, dis1, 125)
ZahrajTón(buzzer, f1, 125)
ZahrajTón(buzzer, dis1, 938, 62)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, gis1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f1, 500)
ZahrajTón(buzzer, gis1, 1000)
ZahrajTón(buzzer, cis1, 500)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, gis1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, ais1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, cis2, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f1, 1000)
ZahrajTón(buzzer, gis1, 1000)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, d1, 500)
ZahrajTón(buzzer, f1, 1000)
ZahrajTón(buzzer, ais , 500)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, d1, 1000)
ZahrajTón(buzzer, f1, 1000)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, fis1, 250, 750)
ZahrajTón(buzzer, gis1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, f1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, ais1, 250, 750)
ZahrajTón(buzzer, h1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, a1, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, fis2, 1000)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 250)
ZahrajTón(buzzer, f2, 250, 250)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, d2, 250, 250)
ZahrajTón(buzzer, dis2, 250, 250)
ZahrajTón(buzzer, ais1, 250, 258)
ZahrajTón(buzzer, h1, 250, 242)
ZahrajTón(buzzer, gis1, 250, 250)
ZahrajTón(buzzer, fis1, 1000)
ZahrajTón(buzzer, f1, 125)
ZahrajTón(buzzer, fis1, 125)
ZahrajTón(buzzer, f1, 125)
ZahrajTón(buzzer, fis1, 125)
ZahrajTón(buzzer, f1, 8, 75)
ZahrajTón(buzzer, fis1, 83)
ZahrajTón(buzzer, f1, 83)
ZahrajTón(buzzer, dis1, 125)
ZahrajTón(buzzer, f1, 125)
ZahrajTón(buzzer, dis1, 938, 62)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 1000)
ZahrajTón(buzzer, g1, 1000)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, g1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, c2, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, d2, 500)
ZahrajTón(buzzer, d1, 500)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, ais , 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 1000)
ZahrajTón(buzzer, g1, 1000)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, g1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, c2, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, ais , 250, 250)
ZahrajTón(buzzer, dis2, 938)
ZahrajTón(buzzer, dis1, 938, 62)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 1000)
ZahrajTón(buzzer, g1, 1000)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, g1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, c2, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, d2, 500)
ZahrajTón(buzzer, d1, 500)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, ais , 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 1000)
ZahrajTón(buzzer, g1, 1000)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, g1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, dis2, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, c2, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, f2, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, d2, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, ais1, 250)
ZahrajTón(buzzer, ais , 250, 250)
ZahrajTón(buzzer, dis2, 938)
ZahrajTón(buzzer, dis1, 938, 62)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, gis2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, fis2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, gis2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, fis1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, fis1, 275, 912)
ZahrajTón(buzzer, g1, 938, 62)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, gis2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, h1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, fis2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, gis2, 275, 225)
ZahrajTón(buzzer, g2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, f2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, fis1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, a1, 275, 225)
ZahrajTón(buzzer, fis1, 275, 912)
ZahrajTón(buzzer, g1, 938, 62)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, gis1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, f1, 275, 225)
ZahrajTón(buzzer, dis1, 275, 225)
ZahrajTón(buzzer, f1, 275, 225)
ZahrajTón(buzzer, g1, 275, 225)
ZahrajTón(buzzer, gis1, 275, 225)
ZahrajTón(buzzer, ais1, 275, 225)
ZahrajTón(buzzer, c2, 275, 225)
ZahrajTón(buzzer, d2, 275, 215)
ZahrajTón(buzzer, dis2, 240, 10)
ZahrajTón(buzzer, dis2, 275, 225)
ZahrajTón(buzzer, d2, 275, 225)
ZahrajTón(buzzer, c2, 275, 215)
ZahrajTón(buzzer, ais1, 240, 10)
ZahrajTón(buzzer, ais1, 275, 225)