from machine import *
from pico_i2c_lcd import I2cLcd
import machine
import neopixel
import time
from machine import Pin, PWM


B0 =31
C1= 33
CS1 =35
D1 =37
DS1= 39
E1= 41
F1= 44
FS1= 46
G1= 49
GS1= 52
A1= 55
AS1= 58
B1= 62
C2= 65
CS2= 69
D2= 73
DS2= 78
E2= 82
F2= 87
FS2= 93
G2= 98
GS2= 104
A2= 110
AS2= 117
B2= 123
C3= 131
CS3= 139
D3= 147
DS3= 156
E3= 165
F3= 175
FS3= 185
G3= 196
GS3= 208
A3= 220
AS3= 233
B3= 247
C4= 262
CS4= 277
D4= 294
DS4= 311
E4= 330
F4= 349
FS4= 370
G4= 392
GS4= 415
A4= 440
AS4= 466
B4= 494
C5= 523
CS5= 554
D5= 587
DS5= 622
E5= 659
F5= 698
FS5= 740
G5= 784
GS5= 831
A5= 880
AS5= 932
B5= 988
C6= 1047
CS6= 1109
D6= 1175
DS6= 1245
E6= 1319
F6= 1397
FS6= 1480
G6= 1568
GS6= 1661
A6= 1760
AS6= 1865
B6= 1976
C7= 2093
CS7= 2217
D7= 2349
DS7= 2489
E7= 2637
F7= 2794
FS7= 2960
G7= 3136
GS7= 3322
A7= 3520
AS7= 3729
B7= 3951
C8= 4186
CS8 = 4435
D8= 4699
DS8= 4978

buzzer = PWM(Pin(15))


def playtone(frequency):
    buzzer.duty_u16(3000)
    buzzer.freq(frequency)


def buddy_holly():
    buzzer = PWM(Pin(15))
    playtone(A4)
    time.sleep(0.24)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(F4)
    time.sleep(0.24)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(A4)
    time.sleep(0.24)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(B5)
    time.sleep(0.24)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(E6)
    time.sleep(0.26)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(B5)
    time.sleep(0.24)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(A4)
    time.sleep(0.24)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(F4)
    time.sleep(0.22)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(E4)
    time.sleep(0.7)
    buzzer.deinit()
def no_surprises():
    buzzer = PWM(Pin(15))
    playtone(E5)
    time.sleep(0.5)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(G4)
    time.sleep(0.5)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(C5)
    time.sleep(0.5)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(G4)
    time.sleep(0.5)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(E5)
    time.sleep(0.5)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(G4)
    time.sleep(0.5)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(C5)
    time.sleep(0.5)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(G4)
    time.sleep(0.5)
    buzzer.deinit()

    # buzzer = PWM(Pin(15))
    # playtone(E5)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(G4)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(C5)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(G4)
    # time.sleep(0.5)
    # buzzer.deinit()

    #
    # buzzer = PWM(Pin(15))
    # playtone(E3)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(E4)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(C5)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(G5)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    #
    #
    # buzzer = PWM(Pin(15))
    # playtone(E5)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(G4)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(C5)
    # time.sleep(0.5)
    # buzzer.deinit()
    #
    # buzzer = PWM(Pin(15))
    # playtone(G4)
    # time.sleep(0.5)
    # buzzer.deinit()
def nokia():
    buzzer = PWM(Pin(15))
    playtone(E6)
    time.sleep(0.133)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(D6)
    time.sleep(0.133)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(FS5)
    time.sleep(0.267)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(GS5)
    time.sleep(0.267)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(CS6)
    time.sleep(0.133)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(B5)
    time.sleep(0.133)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(D5)
    time.sleep(0.267)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(E5)
    time.sleep(0.267)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(B5)
    time.sleep(0.133)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(A5)
    time.sleep(0.133)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(CS5)
    time.sleep(0.267)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(E5)
    time.sleep(0.267)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(A5)
    time.sleep(0.533)
    buzzer.deinit()
    # time.sleep(234)
def zelda():
    buzzer = PWM(Pin(15))
    playtone(1397)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1760)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1976)
    time.sleep(0.429)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1397)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1760)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1976)
    time.sleep(0.429)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1397)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1760)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1976)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(2637)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(2349)
    time.sleep(0.429)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1976)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(2093)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1976)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1568)
    time.sleep(0.214)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1319)
    time.sleep(0.857)
    buzzer.deinit()

    buzzer = PWM(Pin(15))
    playtone(1175)
    time.sleep(0.214)
    buzzer.deinit()

    # buzzer = PWM(Pin(15))
    # playtone(1319)
    # time.sleep(0.214)
    # buzzer.deinit()

    # buzzer = PWM(Pin(15))
    # playtone(1568)
    # time.sleep(0.214)
    # buzzer.deinit()

    # buzzer = PWM(Pin(15))
    # playtone(1319)
    # time.sleep(0.857)
    # buzzer.deinit()


np = neopixel.NeoPixel(machine.Pin(13), 8)

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

lcd.move_to(0,0)
lcd.putstr("Booting up")
time.sleep(0.2)
lcd.move_to(0,0)
lcd.putstr("Booting up.")
time.sleep(0.2)
lcd.move_to(0,0)
lcd.putstr("Booting up..")
time.sleep(0.2)
lcd.move_to(0,0)
lcd.putstr("Booting up...")
time.sleep(0.2)
lcd.clear()
lcd.move_to(0,0)
lcd.putstr("Booting up")
time.sleep(0.2)
lcd.move_to(0,0)
lcd.putstr("Booting up.")
time.sleep(0.2)
lcd.move_to(0,0)
lcd.putstr("Booting up..")
time.sleep(0.2)
lcd.move_to(0,0)
lcd.putstr("Waiting for     input...")
time.sleep(0.2)
kleurenlijst = [(204, 0, 1), (251, 148, 11), (255, 255, 1), (1, 204, 0), (3, 192, 198), (0, 0, 254), (48, 25, 52), (254, 152, 191)]
def regenboog(kleurenlijst):
    for i, rijst in enumerate(kleurenlijst):
        np[i] = [rijst[0], rijst[1], rijst[2]]
        np.write()
        time.sleep(0.05)
    for i in range(0, 8):
        np[i] = [0, 0, 0]
        np.write()
        time.sleep(0.05)

regenboog(kleurenlijst)
zelda()
nokia()



def lcd_display(data, line):
    # lcd.clear()
    if len(data) <= 16:
        lcd.move_to(0, line)
        lcd.putstr(data)
        time.sleep(0.4)
    else:
        for i in range(len(data) - 15):
            lcd.move_to(0, line)
            lcd.putstr(data[i:i + 16])
            time.sleep(0.4)
        lcd.move_to(0, line)
        if len(data) > 16:
            splitat = 16
            data = data[:splitat]
        lcd.putstr(data)


while True:
    time.sleep(3)
    data = input()
    datalist = data.split('ewigvuieflbhwuidbhiudgbwlhg', 2)
    data = datalist[0]
    naam = datalist[1]
    print(datalist)
    if datalist[2] != "gameplaying":
        gameplaying = datalist[2]
    else:
        gameplaying = "gameplaying"
    lcd.clear()
    lcd_display(naam, 0)
    lcd.move_to(0, 1)

    if data == "1":
        np[0] = [0, 0, 100]
        np.write()
        np[1] = [0, 0, 100]
        np.write()
        np[2] = [0, 255, 0]
        np.write()
        np[3] = [0, 255, 0]
        np.write()
        np[4] = [0, 255, 0]
        np.write()
        np[5] = [0, 255, 0]
        np.write()
        np[6] = [0, 0, 100]
        np.write()
        np[7] = [0, 0, 100]
        np.write()
        if gameplaying != "gameplaying":
            lcd_display(gameplaying, 1)
        else:
            lcd.move_to(0, 1)
            lcd.putstr(f'Online          ')


    elif data == "0":
        lcd.move_to(0, 1)
        lcd.putstr(f'Offline         ')
        np[0] = [0, 0, 200]
        np.write()
        np[1] = [0, 0, 200]
        np.write()
        np[2] = [255, 0, 0]
        np.write()
        np[3] = [255, 0, 0]
        np.write()
        np[4] = [255, 0, 0]
        np.write()
        np[5] = [255, 0, 0]
        np.write()
        np[6] = [0, 0, 200]
        np.write()
        np[7] = [0, 0, 200]
        np.write()
    elif data == "2":
        lcd.move_to(0, 1)
        lcd.putstr(f'Away            ')
        np[0] = [0, 0, 200]
        np.write()
        np[1] = [0, 0, 200]
        np.write()
        np[2] = [255, 50, 0]
        np.write()
        np[3] = [255, 50, 0]
        np.write()
        np[4] = [255, 50, 0]
        np.write()
        np[5] = [255, 50, 0]
        np.write()
        np[6] = [0, 0, 200]
        np.write()
        np[7] = [0, 0, 200]
        np.write()
    elif data == "3":
        lcd.move_to(0, 1)
        lcd.putstr(f'Snooze     ')
        np[0] = [0, 0, 200]
        np.write()
        np[1] = [0, 0, 200]
        np.write()
        np[2] = [255, 200, 0]
        np.write()
        np[3] = [255, 200, 0]
        np.write()
        np[4] = [255, 200, 0]
        np.write()
        np[5] = [255, 200, 0]
        np.write()
        np[6] = [0, 0, 200]
        np.write()
        np[7] = [0, 0, 200]
        np.write()
    else:
        np[0] = [255, 0, 0]
        np.write()
