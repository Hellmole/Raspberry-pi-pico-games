
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import time
import random
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
hra = 0

oled.fill(0)  
oled.text("SnackBox v1.0", 5, 6)
oled.text("By Kuba", 30, 23)
oled.text("&", 55, 35)
oled.text("Stepan", 35, 47)
oled.rect(0, 0, 128, 20 , 1)
oled.show()
time.sleep(2)


# game  pong ---------------------------------------------------------------------------------------

def hra_pong():

    # def variables, buzzer and buttons pins
    x_pos = 2
    smer = 0
    ran = 1
    smer2 = 1
    smer3 = 1
    x_pos2 = 2
    y_pos2 = 2
    score = 0
    tlacitko = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko2 = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(3, Pin.IN, Pin.PULL_UP)

    buzzer = PWM(Pin(16))
    posun = 0
    zvuk = 0

    while True:


        if not tlacitko3.value():  
            return

        if not tlacitko.value():  
            x_pos = x_pos + 2  
  
        if not tlacitko2.value():  
            x_pos = x_pos - 2 

        # Vymazání displeje aZobrazení Score
        oled.fill(0)  
        oled.text("Score " + str(score), 0, 0)
   

        # Vykreslení palky
        oled.rect(x_pos, 58, 10, 2, 1)

        # Vykresleni mice
        oled.rect(x_pos2 + 5 , 56 - y_pos2, 2, 2, 1)
   

        if posun == 0:
            x_pos2 = x_pos2 + ran 
            y_pos2 = y_pos2 + smer3

    
        if x_pos2 <= 0 or x_pos2 >= 116:  
            smer2 = -smer2
            ran = -ran
            zvuk = 1
       
        if x_pos <= x_pos2 + 8 and x_pos >= x_pos2 - 8 and y_pos2 == 0:   
            posun = 0
            ran = random.randint(1, 3)
            score = score + 1
            zvuk = 1

        elif y_pos2 == 0 :       
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2) 
            x_pos = 2
            smer = 0
            ran = 1
            smer2 = 1
            smer3 = 1
            x_pos2 = 2
            y_pos2 = 2
            score = 0
   
    
        if y_pos2 <= 0 or y_pos2 >= 54:  
            smer3 = -smer3
            zvuk = 1
        

        # Zobrazení na displeji
        oled.show()

        # Krátká pauza pro hladší animaci

        if zvuk == 1:
            buzzer.freq(200)
            buzzer.duty_u16(32768)
            time.sleep(0.02)
            buzzer.duty_u16(0)
            zvuk = 0
            buzzer.deinit()
        else:
            time.sleep(0.02)



# HRA Modul ---------------------------------------------------------------------------------------

def hra_modul():

    
    level = 1
    x_pos = 2
    smer = 0
    ran = 1
    smer2 = 1
    smer3 = 1
    x_pos2 = 2
    y_pos2 = 2
    ggg= 1
    fuel = 25
    tryska = 0
    
    tlacitko2 = Pin(20, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(3, Pin.IN, Pin.PULL_UP)
    posun = 0

    while True:


        if not tlacitko3.value():  
           return
    
        if not tlacitko2.value():
            tryska = 1
            ggg = ggg - 5
            fuel = fuel - 1 

    
    
        # Vymazání displeje aZobrazení Score
        oled.fill(0)  
        oled.text("Fuel " + str(fuel), 0, 55)
        oled.text("m/s " + str(ggg), 80, 1)
    
   

        # Vykreslení modulu
        oled.rect(6 + x_pos2, 3 + y_pos2, 5, 5, 1)
        oled.vline(5 + x_pos2, 5 + y_pos2, 5, 1)
        oled.vline(11 + x_pos2, 5 + y_pos2, 5, 1)
        oled.rect(7 + x_pos2, 1 + y_pos2, 3, 4 , 1)

        # Vykresleni plochy
        oled.rect(100, 62, 14, 2, 1)
        
        if tryska == 1:
            oled.vline(8 + x_pos2, 11 + y_pos2, 8, 1)
            tryska = 0

        x_pos2 = x_pos2 + ran 
        y_pos2 = y_pos2 + smer3
        y_pos2 = y_pos2 +  1 + ggg // 10
        ggg = ggg + 1
       
        if x_pos2 > 90 and x_pos2 < 110 and y_pos2 >=  56 and ggg < 4:
            oled.text("Pristani OK", 25, 20)
            level = level + 1
            oled.text("Level " + str(level), 25, 30)
            oled.show()
            time.sleep(2) 
            x_pos = 2
            smer = 0
            ggg = 1
            ran = ran + 1
            smer2 = 1
            smer3 = 1
            x_pos2 = 2
            y_pos2 = 2
            fuel = 25

        elif y_pos2 >=  56 or fuel < 1:       
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2) 
            x_pos = 2
            smer = 0
            ggg = 1
            ran = 1
            smer2 = 1
            smer3 = 1
            x_pos2 = 2
            y_pos2 = 2
            fuel = 25
            level = 1
   

        # Zobrazení na displeji
        oled.show()

        # Krátká pauza pro hladší animaci
        time.sleep(0.1)


# HRA Moto ---------------------------------------------------------------------------------------

def hra_moto():
    x = 1
    y = 1
    prekazka = 1
    smer = 0
    ran = 0
    smer2 = 1
    smer3 = 1
    x_pos = 2
    qqq = 0
    naklon = 0
    y_pos2 = 1
    score = 1
    speed= 1
    zrychleni = 1
    level = 1
    posun = 0
    y_pos3 = 1
    y_souper = 0
    naraz = 0

    tlacitko = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko2 = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(3, Pin.IN, Pin.PULL_UP)



    while True:
    
        oled.fill(0) 
        naklon = 0
        if not tlacitko3.value():  
           return

        if not tlacitko.value():  
            x_pos = x_pos + 2
            naklon = 4 
  
        if not tlacitko2.value():  
            x_pos = x_pos - 2
            naklon = -4
    
        # Vymazání displeje aZobrazení Score
        y_souper = ran + y
        oled.text("Score:" + str(score), 0, 0)
        oled.text(str(score * 5) + " km/h", 70, 0)
    
        x = x + 1
        y = y + smer3
        prekazka = prekazka + speed

    
        # Vykreslení hor
        oled.line(20 + y // 5, 35 + y // 10 , 9 + y // 4 , 39 + y // 10, 1)
        oled.line(20 + y // 5, 35 + y // 10, 29 + y // 4, 39 + y // 10, 1)
        # Vykreslení silnice
    
    
        oled.rect(0, 40 + y //10, 128, 2, 1)

        oled.line(50 + y, 40 + y // 10, 30 , 50, 1)
        oled.line(70 + y , 40 + y // 10, 90, 50, 1)
    
        oled.line(30, 50, 10, 63, 1)
        oled.line(90, 50, 118, 63, 1)
    
        oled.rect(0, 42 + x//2, 128, 4, 0)
    
        oled.rect(0, 52 + x, 128, 8, 0)
    
        # Vykreslení motorky
        oled.rect(60 + x_pos, 58, 2, 4, 1)
        oled.rect(59  + x_pos + naklon // 2, 55, 5, 4, 1)

        oled.rect(60 + x_pos + naklon, 52, 2, 2, 1)

        # prekazka
        if prekazka > 10: 
            oled.rect(60 + ran + y, 38 + prekazka , 2, 4, 1)
            oled.rect(59 + y // 20  + ran + y, 35 + prekazka, 5, 4, 1)

            oled.rect(60 + y // 10  + ran + y, 32 + prekazka, 2, 2, 1)
        
        if prekazka <= 10: 
            oled.rect(60 + ran + y, 38 + prekazka , 2, 4, 1)
    
        oled.show()
    
        if x== 4:  
            x = 0

        if prekazka >= 30:  
            ran = random.randint(-5, 5)
            ran = ran * 2
            prekazka = 0
            score = score + 1
            zrychleni = zrychleni + 0.05
            speed = round(zrychleni)
    

        if y <= -35  or y >= 25:  
            smer3 = -smer3

        if y <= -15:  
            x_pos = x_pos + 2
        
        if y > 15 :  
            x_pos = x_pos - 2
            
        if x_pos >=  46 or x_pos < -46:       
            naraz = 1

        if x_pos <= y_souper + 4  and x_pos >= y_souper - 4 and prekazka >= 15:       
            naraz = 1


        if  naraz ==  1:  

            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2)
            x = 1
            y = 1
            prekazka = 1
            smer = 0
            ran = 0
            smer2 = 1
            smer3 = 1
            x_pos = 2
            qqq = 0
            naklon = 0
            y_pos2 = 1
            score = 1
            speed= 1
            zrychleni = 1
            level = 1
            posun = 0
            y_pos3 = 1
            y_souper = 0
            naraz = 0

        time.sleep(0.1)  


    

def hlavni_menu():

    while True:
         
        oled.fill(0)  
        oled.text("Pong v1.0", 25, 26)
        oled.show()
        time.sleep(2)
        hra_pong() 

        oled.fill(0)  
        oled.text("Modul v1.0", 25, 26)
        oled.show()
        time.sleep(2)
        hra_modul()         

        oled.fill(0)  
        oled.text("Moto v1.0", 25, 26)
        oled.show()
        time.sleep(2)
        hra_moto()      
hlavni_menu()

