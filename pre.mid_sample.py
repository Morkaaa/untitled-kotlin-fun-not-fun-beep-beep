from machine import Pin, PWM
from time import sleep_ms

G = const(98)
d = const(147)
h = const(247)
a = const(220)
e = const(165)
c1 = const(262)
fis  = const(185)
g = const(196)
H = const(123)
cis  = const(139)
d1 = const(294)
cis1 = const(277)
E = const(82)
A = const(110)
gis  = const(208)
f = const(175)
c = const(131)
dis  = const(156)
Fis  = const(93)
D = const(73)
Cis  = const(69)
C = const(65)
dis1 = const(311)
ais  = const(233)
e1 = const(330)
f1 = const(349)
fis1 = const(370)
g1 = const(392)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón * 2, duty_u16=2**15)
    sleep_ms(trvanie // 2)
    buzzer.duty_u16(0)
    sleep_ms(pauza // 2)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep_ms(1000)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, cis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, E, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, E, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, E, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, cis1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, gis , 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, gis , 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, gis , 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, dis , 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, dis , 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, dis , 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, dis , 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, Fis , 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, Fis , 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, f, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, Fis , 250)
ZahrajTón(buzzer, E, 250)
ZahrajTón(buzzer, D, 250)
ZahrajTón(buzzer, Cis , 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, Cis , 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, C, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, C, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, C, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, cis1, 250)
ZahrajTón(buzzer, d1, 750)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, dis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, cis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, D, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, D, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, cis1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, ais , 250)
ZahrajTón(buzzer, ais , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, gis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, cis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, cis1, 250)
ZahrajTón(buzzer, d1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, cis , 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, G, 250)
ZahrajTón(buzzer, Fis , 250)
ZahrajTón(buzzer, E, 250)
ZahrajTón(buzzer, D, 500)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c, 250)
ZahrajTón(buzzer, H, 250)
ZahrajTón(buzzer, A, 250)
ZahrajTón(buzzer, g, 250)
ZahrajTón(buzzer, fis , 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, d, 250, 250)
ZahrajTón(buzzer, e, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, e, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, d, 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, e, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, d, 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, e, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, d, 250, 250)
ZahrajTón(buzzer, e, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, a, 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, d, 250, 250)
ZahrajTón(buzzer, a, 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, d, 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, a, 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, a, 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, a, 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, a, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, e, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, e, 250)
ZahrajTón(buzzer, f, 250, 250)
ZahrajTón(buzzer, fis , 250, 250)
ZahrajTón(buzzer, g, 250, 250)
ZahrajTón(buzzer, gis , 250, 250)
ZahrajTón(buzzer, a, 250, 250)
ZahrajTón(buzzer, ais , 250, 250)
ZahrajTón(buzzer, h, 250, 250)
ZahrajTón(buzzer, c1, 250, 250)
ZahrajTón(buzzer, cis1, 250, 250)
ZahrajTón(buzzer, d1, 250, 250)
ZahrajTón(buzzer, dis1, 250, 250)
ZahrajTón(buzzer, e1, 250, 250)
ZahrajTón(buzzer, f1, 250, 250)
ZahrajTón(buzzer, fis1, 250, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, h, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, g1, 250)
ZahrajTón(buzzer, a, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, d, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, fis1, 250)
ZahrajTón(buzzer, c1, 250)
ZahrajTón(buzzer, g1, 4000)
