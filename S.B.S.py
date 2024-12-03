stig = []

user1_sk = 1
user1_bl = 1
user1_st = 1

user2_sk = 1
user2_bl = 1
user2_st = 1


while True:
    
    while True:
        user1_input_sk = False
        user1_input_bl = True
        user1_input_st = False

        user2_input_sk = True
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
                break
            elif user1_input_bl and user2_input_st:
                stig.append("Blár")
                break
            elif user2_input_st and user1_input_sk:
                stig.append("Rautt")
                break
            elif user2_input_sk and user1_input_bl:
                stig.append("Rautt")
                break
            elif user2_input_bl and user1_input_st:
                stig.append("Rautt")
                break