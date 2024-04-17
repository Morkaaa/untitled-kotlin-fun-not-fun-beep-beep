from machine import Pin, PWM
from time import sleep_ms

e2 = const(659)
fis2 = const(740)
g2 = const(784)
h2 = const(988)
c3 = const(1047)
a2 = const(880)
cis3 = const(1109)
d3 = const(1175)
e3 = const(1319)
ais2 = const(932)
h1 = const(494)
e1 = const(330)
dis1 = const(311)
fis1 = const(370)
g1 = const(392)
a1 = const(440)
ais1 = const(466)
gis1 = const(415)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón*2, duty_u16=2**15)
    sleep_ms(trvanie//2)
    buzzer.duty_u16(0)
    sleep_ms(pauza//2)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep_ms(1000)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, h2, 498, 502)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, c3, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, e2, 498, 1002)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, e2, 498, 502)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 498, 502)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, e3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, e2, 498, 502)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 498, 502)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, e3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, e3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 498, 502)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, e3, 248, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 248, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, d3, 498, 2)
ZahrajTón(buzzer, cis3, 498, 2)
ZahrajTón(buzzer, cis3, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, h1, 498, 2)
ZahrajTón(buzzer, h1, 498, 502)
ZahrajTón(buzzer, e1, 498, 252)
ZahrajTón(buzzer, dis1, 248, 2)
ZahrajTón(buzzer, e1, 498, 2)
ZahrajTón(buzzer, fis1, 498, 2)
ZahrajTón(buzzer, g1, 498, 252)
ZahrajTón(buzzer, fis1, 248, 2)
ZahrajTón(buzzer, g1, 498, 2)
ZahrajTón(buzzer, a1, 498, 2)
ZahrajTón(buzzer, ais1, 498, 2)
ZahrajTón(buzzer, ais1, 498)
ZahrajTón(buzzer, a1, 123, 2)
ZahrajTón(buzzer, ais1, 498, 502)
ZahrajTón(buzzer, a1, 498, 2)
ZahrajTón(buzzer, a1, 498, 2)
ZahrajTón(buzzer, a1, 498, 502)
ZahrajTón(buzzer, e1, 498, 252)
ZahrajTón(buzzer, dis1, 248, 2)
ZahrajTón(buzzer, e1, 498, 2)
ZahrajTón(buzzer, fis1, 498, 2)
ZahrajTón(buzzer, g1, 498, 252)
ZahrajTón(buzzer, fis1, 248, 2)
ZahrajTón(buzzer, g1, 498, 2)
ZahrajTón(buzzer, g1, 498, 2)
ZahrajTón(buzzer, ais1, 498, 2)
ZahrajTón(buzzer, ais1, 498, 1002)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498)
ZahrajTón(buzzer, gis1, 498, 252)
ZahrajTón(buzzer, e2, 498, 252)
ZahrajTón(buzzer, h2, 498, 252)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 2)
ZahrajTón(buzzer, h2, 998, 502)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 502)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, h2, 498, 502)
ZahrajTón(buzzer, h2, 498, 252)
ZahrajTón(buzzer, ais2, 248, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, c3, 498, 2)
ZahrajTón(buzzer, h2, 998, 502)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 502)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498, 502)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, g2, 498, 1002)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, g2, 498, 1002)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, g2, 498, 1002)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, e2, 498, 1502)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498, 502)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, cis3, 248)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, h2, 248)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, d3, 248)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, cis3, 248)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, d3, 248)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, cis3, 248)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 498, 1002)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, g2, 498)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, g2, 498)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 498)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 498)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 248)
ZahrajTón(buzzer, g2, 248)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, fis2, 248)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498)
ZahrajTón(buzzer, e2, 498, 2)
ZahrajTón(buzzer, g2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, e2, 498)
ZahrajTón(buzzer, h1, 498)
ZahrajTón(buzzer, g1, 498)
ZahrajTón(buzzer, e1, 498, 1502)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, ais2, 498, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, c3, 498, 2)
ZahrajTón(buzzer, h2, 498, 2)
ZahrajTón(buzzer, e2, 498, 502)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, ais2, 248, 2)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, a2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, fis2, 498, 2)
ZahrajTón(buzzer, e2, 498, 1002)
ZahrajTón(buzzer, e2, 248, 2)
ZahrajTón(buzzer, fis2, 248, 2)
ZahrajTón(buzzer, g2, 498, 2)
ZahrajTón(buzzer, e2, 498, 2502)
ZahrajTón(buzzer, h2, 248, 2)
ZahrajTón(buzzer, h2, 248, 4002)
ZahrajTón(buzzer, h2, 998)
ZahrajTón(buzzer, ais2, 998)
ZahrajTón(buzzer, a2, 998)
ZahrajTón(buzzer, g2, 998)
