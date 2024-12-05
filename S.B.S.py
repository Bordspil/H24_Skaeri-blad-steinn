from machine import Pin, PWM, ADC
from time import sleep_ms
ljospinnar = [11,12,13,14,15,16]
def ljosoff():
    for i in ljospinnar:
        i.value(0)
    sleep_ms(2000)
    
        
stig = []

user1_sk = Pin(7, Pin.IN, Pin.PULL_UP)
user1_bl = Pin(15, Pin.IN, Pin.PULL_UP)
user1_st = Pin(16, Pin.IN, Pin.PULL_UP)

user2_sk = Pin(17, Pin.IN, Pin.PULL_UP)
user2_bl = Pin(18, Pin.IN, Pin.PULL_UP)
user2_st = Pin(8, Pin.IN, Pin.PULL_UP)

user1_rautt = Pin(41, Pin.OUT)
user1_graent = Pin(40, Pin.OUT)
user1_blatt = Pin(39, Pin.OUT)

user2_rautt = Pin(38, Pin.OUT)
user2_graent = Pin(37, Pin.OUT)
user2_blatt = Pin(36, Pin.OUT)


while True:
    
    while True:
        user1_rautt.value(1)
        user1_graent.value(1)
        user1_blatt.value(1)

        user2_rautt.value(1)
        user2_graent.value(1)
        user2_blatt.value(1)
        
        user1_input_sk = False
        user1_input_bl = False
        user1_input_st = False

        user2_input_sk = False
        user2_input_bl = False
        user2_input_st = False
        if len(stig) == 3:
            print(stig)
            break
        
        while True:
            if user1_sk == 0 and user1_input_bl == False and user1_input_st == False:
                user1_input_sk = True
            elif user1_bl == 0 and user1_input_sk == False and user1_input_st == False:
                user1_input_bl = True
            elif user1_st == 0 and user1_input_sk == False and user1_input_bl == False :
                user1_input_st = True

            if user2_sk == 0 and user2_input_bl == False and user2_input_st == False:
                user2_input_sk = True
            elif user2_bl == 0 and user2_input_sk == False and user2_input_st == False:
                user2_input_bl = True
            elif user2_st == 0 and user2_input_sk == False and user2_input_bl == False :
                user2_input_st = True
            
            if user1_input_st and user2_input_sk:
                stig.append("Blár")
                
                break
            elif user1_input_sk and user2_input_bl:
                stig.append("Blár")
                ljosoff()
                break
            elif user1_input_bl and user2_input_st:
                stig.append("Blár")
                ljosoff()
                break
            elif user2_input_st and user1_input_sk:
                stig.append("Rautt")
                ljosoff()
                break
            elif user2_input_sk and user1_input_bl:
                stig.append("Rautt")
                ljosoff()
                break
            elif user2_input_bl and user1_input_st:
                stig.append("Rautt")
                ljosoff()
                break
            elif user1_input_bl and user2_input_bl or user1_input_sk and user2_input_sk or user1_input_st and user2_input_st:
                print("jafntefli")

                stig.append("Rautt")
                break
