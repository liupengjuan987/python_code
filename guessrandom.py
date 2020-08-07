age_of_oldBoy = 66

count =0
while(count<3):
    guess_num = int(input("age_of_oldBoy:"))
    if guess_num == age_of_oldBoy:
        print("Yes,You got if!")
        break
    elif guess_num < age_of_oldBoy:
        print("think bigger")
    else: print("think smaller")
    count=count+1
    if count==3:
        continue_confirm=input("do you want to keep tring..?")
        if continue_confirm != 'n':
            count=0

#else:
    #print("you have tried too many times...fuck off")