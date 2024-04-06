from machine import Pin, PWM
from time import sleep

d1 = const(294)
ais  = const(233)
f1 = const(349)
ais1 = const(466)
d2 = const(587)
c2 = const(523)
e1 = const(330)
a1 = const(440)
g1 = const(392)
dis2 = const(622)
f2 = const(698)

def ZahrajTón(buzzer, tón, trvanie, pauza=0):
    buzzer.init(freq=tón, duty_u16=2**15)
    sleep(trvanie)
    buzzer.duty_u16(0)
    sleep(pauza)

buzzer = PWM(Pin(2))
buzzer.deinit()
sleep(1)
ZahrajTón(buzzer, d1, 0.18958333333333333)
ZahrajTón(buzzer, ais , 0.9125)
ZahrajTón(buzzer, d1, 0.90625)
ZahrajTón(buzzer, f1, 0.9791666666666666)
ZahrajTón(buzzer, ais1, 1.6666666666666667)
ZahrajTón(buzzer, d2, 0.48333333333333334)
ZahrajTón(buzzer, c2, 0.20416666666666666)
ZahrajTón(buzzer, ais1, 0.93125)
ZahrajTón(buzzer, d1, 0.8958333333333334)
ZahrajTón(buzzer, e1, 0.925)
ZahrajTón(buzzer, f1, 1.64375)
ZahrajTón(buzzer, f1, 0.3)
ZahrajTón(buzzer, f1, 0.325)
ZahrajTón(buzzer, d2, 1.2770833333333333)
ZahrajTón(buzzer, c2, 0.3770833333333333)
ZahrajTón(buzzer, ais1, 0.8791666666666667)
ZahrajTón(buzzer, a1, 1.65)
ZahrajTón(buzzer, g1, 0.3729166666666667)
ZahrajTón(buzzer, a1, 0.36875)
ZahrajTón(buzzer, ais1, 0.8916666666666667)
ZahrajTón(buzzer, ais1, 0.8458333333333333)
ZahrajTón(buzzer, f1, 0.9833333333333333)
ZahrajTón(buzzer, d1, 0.9854166666666667)
ZahrajTón(buzzer, ais , 0.7)
ZahrajTón(buzzer, f1, 0.5229166666666667)
ZahrajTón(buzzer, d1, 0.23125)
ZahrajTón(buzzer, ais , 0.8541666666666666)
ZahrajTón(buzzer, d1, 0.875)
ZahrajTón(buzzer, f1, 0.8791666666666667)
ZahrajTón(buzzer, ais1, 1.7104166666666667)
ZahrajTón(buzzer, d2, 0.5104166666666666)
ZahrajTón(buzzer, c2, 0.19166666666666668)
ZahrajTón(buzzer, ais1, 0.9270833333333334)
ZahrajTón(buzzer, d1, 0.9104166666666667)
ZahrajTón(buzzer, e1, 0.8479166666666667)
ZahrajTón(buzzer, f1, 1.71875)
ZahrajTón(buzzer, f1, 0.30625)
ZahrajTón(buzzer, f1, 0.4083333333333333)
ZahrajTón(buzzer, d2, 1.3625)
ZahrajTón(buzzer, c2, 0.37916666666666665)
ZahrajTón(buzzer, ais1, 0.85)
ZahrajTón(buzzer, a1, 1.81875)
ZahrajTón(buzzer, g1, 0.40625)
ZahrajTón(buzzer, a1, 0.3645833333333333)
ZahrajTón(buzzer, ais1, 0.7979166666666667)
ZahrajTón(buzzer, ais1, 0.8645833333333334)
ZahrajTón(buzzer, f1, 0.85625)
ZahrajTón(buzzer, d1, 0.9541666666666667)
ZahrajTón(buzzer, ais , 0.6979166666666666)
ZahrajTón(buzzer, d2, 0.42291666666666666)
ZahrajTón(buzzer, d2, 0.20208333333333334)
ZahrajTón(buzzer, d2, 0.875)
ZahrajTón(buzzer, dis2, 0.8791666666666667)
ZahrajTón(buzzer, f2, 0.8625)
ZahrajTón(buzzer, f2, 1.8270833333333334)
ZahrajTón(buzzer, dis2, 0.3)
ZahrajTón(buzzer, d2, 0.36041666666666666)
ZahrajTón(buzzer, c2, 0.9229166666666667)
ZahrajTón(buzzer, d2, 0.8875)
ZahrajTón(buzzer, dis2, 0.8479166666666667)
ZahrajTón(buzzer, dis2, 1.7791666666666666)
ZahrajTón(buzzer, dis2, 0.875)
ZahrajTón(buzzer, d2, 1.3479166666666667)
ZahrajTón(buzzer, c2, 0.41041666666666665)
ZahrajTón(buzzer, ais1, 0.9270833333333334)
ZahrajTón(buzzer, a1, 1.74375)
ZahrajTón(buzzer, g1, 0.3729166666666667)
ZahrajTón(buzzer, a1, 0.3416666666666667)
ZahrajTón(buzzer, ais1, 0.9729166666666667)
ZahrajTón(buzzer, d1, 0.9145833333333333)
ZahrajTón(buzzer, e1, 0.93125)
ZahrajTón(buzzer, f1, 1.8875)
ZahrajTón(buzzer, f1, 0.91875)
ZahrajTón(buzzer, ais1, 0.9125)
ZahrajTón(buzzer, ais1, 0.8270833333333333)
ZahrajTón(buzzer, ais1, 0.36666666666666664)
ZahrajTón(buzzer, a1, 0.4)
ZahrajTón(buzzer, g1, 0.8916666666666667)
ZahrajTón(buzzer, g1, 0.85625)
ZahrajTón(buzzer, g1, 0.9458333333333333)
ZahrajTón(buzzer, c2, 0.9645833333333333)
ZahrajTón(buzzer, dis2, 0.475)
ZahrajTón(buzzer, d2, 0.3645833333333333)
ZahrajTón(buzzer, c2, 0.5125)
ZahrajTón(buzzer, ais1, 0.3645833333333333)
ZahrajTón(buzzer, ais1, 0.9645833333333333)
ZahrajTón(buzzer, a1, 1.7666666666666666)
ZahrajTón(buzzer, f1, 0.29583333333333334)
ZahrajTón(buzzer, f1, 0.39375)
ZahrajTón(buzzer, ais1, 1.3833333333333333)
ZahrajTón(buzzer, c2, 0.43125)
ZahrajTón(buzzer, d2, 0.4270833333333333)
ZahrajTón(buzzer, dis2, 0.3625)
ZahrajTón(buzzer, f2, 1.85)
ZahrajTón(buzzer, ais1, 0.3875)
ZahrajTón(buzzer, c2, 0.41875)
ZahrajTón(buzzer, d2, 1.33125)
ZahrajTón(buzzer, dis2, 0.44583333333333336)
ZahrajTón(buzzer, c2, 0.7854166666666667)
ZahrajTón(buzzer, ais1, 3.0770833333333334)