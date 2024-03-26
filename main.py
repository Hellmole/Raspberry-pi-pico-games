from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import time
import random
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
hra = 0

oled.fill(0)  
oled.text("PicoBox v1.0", 5, 6)
oled.text("By Kuba", 30, 23)
oled.text("&", 55, 35)
oled.text("Stepan", 35, 47)
oled.rect(0, 0, 128, 20 , 1)
oled.show()
time.sleep(2)


# Game:  Pong ---------------------------------------------------------------------------------------

def game_pong():

    x_pos = 2
    direction = 0
    ran = 1
    direction2 = 1
    direction3 = 1
    x_pos2 = 2
    y_pos2 = 2
    score = 0
    tlacitko = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko2 = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(3, Pin.IN, Pin.PULL_UP)
    buzzer = PWM(Pin(16))
    shift = 0
    sound = 0

    while True:


        if not tlacitko3.value():  
            return

        if not tlacitko.value():  
            x_pos = x_pos + 2  
  
        if not tlacitko2.value():  
            x_pos = x_pos - 2 

        
        oled.fill(0)  
        oled.text("Score " + str(score), 0, 0)
   

        # bat
        oled.rect(x_pos, 58, 10, 2, 1)

        # ball
        oled.rect(x_pos2 + 5 , 56 - y_pos2, 2, 2, 1)
   

        if shift == 0:
            x_pos2 = x_pos2 + ran 
            y_pos2 = y_pos2 + direction3

    
        if x_pos2 <= 0 or x_pos2 >= 116:  
            direction2 = -direction2
            ran = -ran
            sound = 1
       
        if x_pos <= x_pos2 + 8 and x_pos >= x_pos2 - 8 and y_pos2 == 0:   
            shift = 0
            ran = random.randint(1, 3)
            score = score + 1
            sound = 1

        elif y_pos2 == 0 :       
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2) 
            x_pos = 2
            direction = 0
            ran = 1
            direction2 = 1
            direction3 = 1
            x_pos2 = 2
            y_pos2 = 2
            score = 0
   
    
        if y_pos2 <= 0 or y_pos2 >= 54:  
            direction3 = -direction3
            sound = 1
        

        oled.show()


        if sound == 1:
            buzzer.freq(200)
            buzzer.duty_u16(32768)
            time.sleep(0.02)
            buzzer.duty_u16(0)
            sound = 0
            buzzer.deinit()
        else:
            time.sleep(0.02)



# Game: Lunar module ---------------------------------------------------------------------------------------

def game_modul():

    
    level = 1
    x_pos = 2
    direction = 0
    ran = 1
    direction2 = 1
    direction3 = 1
    x_pos2 = 2
    y_pos2 = 2
    gravity= 1
    fuel = 25
    fire = 0
    
    tlacitko2 = Pin(20, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(3, Pin.IN, Pin.PULL_UP)
    shift = 0

    while True:


        if not tlacitko3.value():  
           return
    
        if not tlacitko2.value():
            fire = 1
            gravity = gravity - 5
            fuel = fuel - 1 

  
        oled.fill(0)  
        oled.text("Fuel " + str(fuel), 0, 55)
        oled.text("m/s " + str(gravity), 80, 1)
    
   
        # Lunar modul
        
        oled.rect(6 + x_pos2, 3 + y_pos2, 5, 5, 1)
        oled.vline(5 + x_pos2, 5 + y_pos2, 5, 1)
        oled.vline(11 + x_pos2, 5 + y_pos2, 5, 1)
        oled.rect(7 + x_pos2, 1 + y_pos2, 3, 4 , 1)

        # landing area
        oled.rect(100, 62, 14, 2, 1)
        
        if fire == 1:
            oled.vline(8 + x_pos2, 11 + y_pos2, 8, 1)
            fire = 0

        x_pos2 = x_pos2 + ran 
        y_pos2 = y_pos2 + direction3
        y_pos2 = y_pos2 +  1 + gravity // 10
        gravity = gravity + 1
       
        if x_pos2 > 90 and x_pos2 < 110 and y_pos2 >=  56 and gravity < 4:
            oled.text("Landing OK!", 25, 20)
            level = level + 1
            oled.text("Level " + str(level), 25, 30)
            oled.show()
            time.sleep(2) 
            x_pos = 2
            direction = 0
            gravity = 1
            ran = ran + 1
            direction2 = 1
            direction3 = 1
            x_pos2 = 2
            y_pos2 = 2
            fuel = 25

        elif y_pos2 >=  56 or fuel < 1:       
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2) 
            x_pos = 2
            direction = 0
            gravity = 1
            ran = 1
            direction2 = 1
            direction3 = 1
            x_pos2 = 2
            y_pos2 = 2
            fuel = 25
            level = 1
   

        oled.show()

        time.sleep(0.1)


# Game: Full speed ---------------------------------------------------------------------------------------

def game_moto():
    x = 1
    y = 1
    prekazka = 1
    ran = 0
    direction3 = 1
    x_pos = 2
    tilt = 0
    score = 1
    speed= 1
    acceleration = 1
    level = 1
    y_rival = 0
    crasch = 0

    tlacitko = Pin(7, Pin.IN, Pin.PULL_UP)
    tlacitko2 = Pin(15, Pin.IN, Pin.PULL_UP)
    tlacitko3 = Pin(3, Pin.IN, Pin.PULL_UP)



    while True:
    
        oled.fill(0) 
        tilt = 0
        if not tlacitko3.value():  
           return

        if not tlacitko.value():  
            x_pos = x_pos + 2
            tilt = 4 
  
        if not tlacitko2.value():  
            x_pos = x_pos - 2
            tilt = -4
    
        y_rival = ran + y
        oled.text("Score:" + str(score), 0, 0)
        oled.text(str(score * 5) + " km/h", 70, 0)
    
        x = x + 1
        y = y + direction3
        prekazka = prekazka + speed

    
        # horizont
        oled.line(20 + y // 5, 35 + y // 10 , 9 + y // 4 , 39 + y // 10, 1)
        oled.line(20 + y // 5, 35 + y // 10, 29 + y // 4, 39 + y // 10, 1)
        
        # road
    
    
        oled.rect(0, 40 + y //10, 128, 2, 1)

        oled.line(50 + y, 40 + y // 10, 30 , 50, 1)
        oled.line(70 + y , 40 + y // 10, 90, 50, 1)
    
        oled.line(30, 50, 10, 63, 1)
        oled.line(90, 50, 118, 63, 1)
    
        oled.rect(0, 42 + x//2, 128, 4, 0)
    
        oled.rect(0, 52 + x, 128, 8, 0)
    
        # your moto
        oled.rect(60 + x_pos, 58, 2, 4, 1)
        oled.rect(59  + x_pos + tilt // 2, 55, 5, 4, 1)

        oled.rect(60 + x_pos + tilt, 52, 2, 2, 1)

        # rival
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
            acceleration = acceleration + 0.05
            speed = round(acceleration)
    

        if y <= -35  or y >= 25:  
            direction3 = -direction3

        if y <= -15:  
            x_pos = x_pos + 2
        
        if y > 15 :  
            x_pos = x_pos - 2
            
        if x_pos >=  46 or x_pos < -46:       
            crasch = 1

        if x_pos <= y_rival + 4  and x_pos >= y_rival - 4 and prekazka >= 15:       
            crasch = 1


        if  crasch ==  1:  
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2)
            x = 1
            y = 1
            prekazka = 1
            ran = 0
            direction3 = 1
            x_pos = 2
            tilt = 0
            score = 1
            speed= 1
            acceleration = 1
            level = 1
            y_rival = 0
            crasch = 0

        time.sleep(0.1)  


    

def main_menu():

    while True:
         
        oled.fill(0)  
        oled.text("   Pong  ", 18, 25)
        oled.show()
        time.sleep(2)
        game_pong() 

        oled.fill(0)  
        oled.text("Lunar module", 18, 25)
        oled.show()
        time.sleep(2)
        game_modul()         

        oled.fill(0)  
        oled.text(" Full speed", 18, 25)
        oled.show()
        time.sleep(2)
        game_moto()      
main_menu()

