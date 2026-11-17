import random
def play_game():

    secret_num = random.randint(1,100)
    user_guss=0
    attempt = 0
    
    while (user_guss != secret_num):
        attempt+=1
        user_guss = int(input("Enter your guss: "))
        if(user_guss == secret_num):
            print("You got it!")
        elif(user_guss > secret_num):
            print("its high")
        else:
            print("its low")    

    print("total attempts: ",attempt)
while (True):
    play_game()
    option = input("do u like to play again? (yes/no)")
    if(option.lower() !="yes"):
        print("thanks for playing")
        break  
