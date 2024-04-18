from machine import Pin, PWM
from time import sleep_ms

e2 = const(659)
fis2 = const(740)
g2 = const(784)
h2 = const(988)
h1 = const(494)
c3 = const(1047)
a2 = const(880)
cis3 = const(1109)
d3 = const(1175)
e3 = const(1319)
ais2 = const(932)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón * 2, duty_u16=2**15)
    sleep_ms(trvanie // 2)
    buzzer.duty_u16(0)
    sleep_ms(pauza // 2)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep_ms(1000)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, e2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h1, 250, 750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, c3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250, 1250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, e2, 250, 750)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250, 750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, e2, 250, 750)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250, 750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250, 1250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250, 1250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, e3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, d3, 250, 250)
ZahrajTón(buzzer, cis3, 250, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, e2, 250, 3250)
ZahrajTón(buzzer, h2, 750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 250)
ZahrajTón(buzzer, h2, 750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 750)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250, 250)
ZahrajTón(buzzer, h2, 250, 750)
ZahrajTón(buzzer, h2, 750)
ZahrajTón(buzzer, ais2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, c3, 250, 250)
ZahrajTón(buzzer, h2, 750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 750)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250, 250)
ZahrajTón(buzzer, e2, 250, 750)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, e2, 250, 1750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, c3, 250)
ZahrajTón(buzzer, h2, 250, 3250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, e2, 250, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, e2, 250, 1750)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, c3, 250)
ZahrajTón(buzzer, h2, 250, 3250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, fis2, 250, 1500)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, fis2, 250, 1500)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, ais2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, d3, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, h2, 250, 1250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 250)
ZahrajTón(buzzer, e2, 250, 1750)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, ais2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, c3, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, e2, 250, 750)
ZahrajTón(buzzer, h1, 250, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, cis3, 250, 250)
ZahrajTón(buzzer, cis3, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, h2, 250, 1250)
ZahrajTón(buzzer, e2, 250)
ZahrajTón(buzzer, fis2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 250)
ZahrajTón(buzzer, h2, 250, 250)
ZahrajTón(buzzer, h1, 250, 750)
ZahrajTón(buzzer, h1, 250, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, c3, 250)
ZahrajTón(buzzer, h2, 250)
ZahrajTón(buzzer, a2, 250)
ZahrajTón(buzzer, g2, 250, 250)
ZahrajTón(buzzer, fis2, 250, 250)
ZahrajTón(buzzer, e2, 250)
