# Skæri blað steinn (best af þremur)
**Höfundar:** Kristján Skjóldal Haraldsson, Kormákur Breki Gunnarsson og Þorsteinn Heiðar Hreimsson  
<br>
Myndbönd:
- [Spilun](https://youtu.be/quDSV1-hbAI)
- [Lóðun](https://youtube.com/shorts/Qcu3lhDtAlo?feature=share)

---

![borðspil](https://github.com/Bordspil/H24_Skaeri-blad-steinn/blob/main/bordspil.jpg)
![IMG_20241211_105943](https://github.com/user-attachments/assets/1f6ab7be-8acc-4a5b-88c8-1b8a9537add6)
![hönnun](https://github.com/Bordspil/H24_Skaeri-blad-steinn/blob/main/bordspil%20toppur%20og%20hitt.svg)

```python
from machine import Pin, PWM, ADC
from time import sleep_ms
from neopixel import NeoPixel

# segir hvar allir pinnar eru
neo1 = NeoPixel(Pin(12), 3)   
neo2 = NeoPixel(Pin(13), 3)   
stig = []
passiveBuzzer = PWM(Pin(41))
user1_sk = Pin(7, Pin.IN, Pin.PULL_UP)
user1_bl = Pin(15, Pin.IN, Pin.PULL_UP)
user1_st = Pin(16, Pin.IN, Pin.PULL_UP)

user2_sk = Pin(17, Pin.IN, Pin.PULL_UP)
user2_bl = Pin(18, Pin.IN, Pin.PULL_UP)
user2_st = Pin(8, Pin.IN, Pin.PULL_UP)

user1_rautt = Pin(35, Pin.OUT)
user1_graent = Pin(40, Pin.OUT)
user1_blatt = Pin(39, Pin.OUT)

user2_rautt = Pin(38, Pin.OUT)
user2_graent = Pin(37, Pin.OUT)
user2_blatt = Pin(36, Pin.OUT)

#leikur byrjar
while True:
    rautt_wins = 0
    blatt_wins = 0
    neo1.fill([0, 0, 0])
    neo1.write()
    neo2.fill([0, 0, 0])
    neo2.write()

    round = 0
        
    #kveikjir á ljósum og setur input false og checkar fyrir sigurvegara
    while True:
        user1_rautt.value(1)
        user1_graent.value(1)
        user1_blatt.value(1)

        user2_rautt.value(1)
        user2_graent.value(1)
        user2_blatt.value(1)
        print("ljos on")
        user1_input_sk = False
        user1_input_bl = False
        user1_input_st = False

        user2_input_sk = False
        user2_input_bl = False
        user2_input_st = False
        
        if rautt_wins + blatt_wins == 3:
            print(stig)
            if rautt_wins > blatt_wins:
                neo1.fill([255, 0, 0])
                neo1.write()
                neo2.fill([255, 0, 0])
                neo2.write()
            elif rautt_wins < blatt_wins:
                neo1.fill([0, 0, 255])
                neo1.write()
                neo2.fill([0, 0, 255])
                neo2.write()
            #sigurlag
            for i in range(5):
                
                passiveBuzzer.init()          # enable PWM pinna
                passiveBuzzer.duty(512)       
                
                passiveBuzzer.freq(100)       # freq er notað til að vinna með tíðni,
                time.sleep_ms(100)
                
                passiveBuzzer.freq(400)
                time.sleep_ms(100)
                
                passiveBuzzer.freq(800)
                time.sleep_ms(100)
                
                passiveBuzzer.duty(0)         # skrifar út 0V, slökkva á hljóði
            else:
                passiveBuzzer.deinit()
            
            break
            
        # leitar af input
        while True:
            if user1_sk.value() == 0 and user1_input_bl == False and user1_input_st == False:
                user1_input_sk = True
                print(stig)
            elif user1_bl.value() == 0 and user1_input_sk == False and user1_input_st == False:
                user1_input_bl = True
                print(stig)
            elif user1_st.value() == 0 and user1_input_sk == False and user1_input_bl == False:
                user1_input_st = True
                print(stig)
            if user2_sk.value() == 0 and user2_input_bl == False and user2_input_st == False:
                user2_input_sk = True
                print(stig)
            elif user2_bl.value() == 0 and user2_input_sk == False and user2_input_st == False:
                user2_input_bl = True
                print(stig)
            elif user2_st.value() == 0 and user2_input_sk == False and user2_input_bl == False:
                user2_input_st = True
                print(stig)
            
            #checkar hver vann roundið og lætur stigið í led ljósið
            if user1_input_st and user2_input_sk:
                stig.append("Blar")
                neo1[round] = [0, 0, 255]
                neo1.write()
                neo2[round] = [0, 0, 255]
                neo2.write()
                user1_rautt.value(0)
                user1_graent.value(0)
                user1_blatt.value(0)

                user2_rautt.value(0)
                user2_graent.value(0)
                user2_blatt.value(0)
                sleep_ms(1000)
                round = round + 1
                blatt_wins = blatt_wins + 1
                break
            elif user1_input_sk and user2_input_bl:
                stig.append("Blar")
                neo1[round] = [0, 0, 255]
                neo1.write()
                neo2[round] = [0, 0, 255]
                neo2.write()
                user1_rautt.value(0)
                user1_graent.value(0)
                user1_blatt.value(0)

                user2_rautt.value(0)
                user2_graent.value(0)
                user2_blatt.value(0)
                sleep_ms(1000)
                round = round + 1
                blatt_wins = blatt_wins + 1
                break
            elif user1_input_bl and user2_input_st:
                stig.append("Blar")
                neo1[round] = [0, 0, 255]
                neo1.write()
                neo2[round] = [0, 0, 255]
                neo2.write()
                user1_rautt.value(0)
                user1_graent.value(0)
                user1_blatt.value(0)

                user2_rautt.value(0)
                user2_graent.value(0)
                user2_blatt.value(0)
                sleep_ms(1000)
                round = round + 1
                blatt_wins = blatt_wins + 1
                break
            elif user2_input_st and user1_input_sk:
                stig.append("Rautt")
                neo1[round] = [255, 0, 0]
                neo1.write()
                neo2[round] = [255, 0, 0]
                neo2.write()
                user1_rautt.value(0)
                user1_graent.value(0)
                user1_blatt.value(0)

                user2_rautt.value(0)
                user2_graent.value(0)
                user2_blatt.value(0)
                sleep_ms(1000)
                round = round + 1
                rautt_wins = rautt_wins + 1
                break
            elif user2_input_sk and user1_input_bl:
                stig.append("rautt")
                neo1[round] = [255, 0, 0]
                neo1.write()
                neo2[round] = [255, 0, 0]
                neo2.write()
                user1_rautt.value(0)
                user1_graent.value(0)
                user1_blatt.value(0)

                user2_rautt.value(0)
                user2_graent.value(0)
                user2_blatt.value(0)
                sleep_ms(1000)
                round = round + 1
                rautt_wins = rautt_wins + 1
                break
            elif user2_input_bl and user1_input_st:
                neo1[round] = [255, 0, 0]
                neo1.write()
                neo2[round] = [255, 0, 0]
                neo2.write()
                stig.append("Rautt")
                user1_rautt.value(0)
                user1_graent.value(0)
                user1_blatt.value(0)

                user2_rautt.value(0)
                user2_graent.value(0)
                user2_blatt.value(0)
                sleep_ms(1000)
                round = round + 1
                rautt_wins = rautt_wins + 1
                break
            
            
            elif user1_input_bl and user2_input_bl or user1_input_sk and user2_input_sk or user1_input_st and user2_input_st:
                neo1[round] = [0, 255, 0]
                neo1.write()
                neo2[round] = [0, 255, 0]
                neo2.write()
                user1_rautt.value(0)
                user1_graent.value(0)
                user1_blatt.value(0)

                user2_rautt.value(0)
                user2_graent.value(0)
                user2_blatt.value(0)
                sleep_ms(1000)
                neo1[round] = [0, 0, 0]
                neo1.write()
                neo2[round] = [0, 0, 0]
                neo2.write()
                break
                
                


```
