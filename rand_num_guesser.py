import random

dict = {}
want_to_play = 1
won = False
while(want_to_play == 1):
    user_name = input("Greetings User! Welcome to the number guesser\nCould you tell us your name : ")
    attempts = 5
    level = int(input(f"\n\nHi {user_name}!! Would you like to play the -\n 1) Easy Level - [range 1 - 10]\n 2) Hard Level - [range 1 - 100]\n Your input ->"))
    if(level == 1):
        max = 10
        rand_num = random.randint(1,11)
    elif(level == 2):
        max = 100
        rand_num = random.randint(1,101)
    while(attempts):
        user_num = int(input(f"Enter a number between 1 and {max} : "))
        attempts -= 1
        if(user_num == rand_num):
            print("YOU WON!!")
            won = True
            if user_name in dict:
                dict[user_name] += 1
            else:
                dict[user_name] = 1
            break
        elif(user_num < rand_num):
            print("Think Larger!!\n")
        else:
            print("Think a bit smaller!!\n") 
    if won == True: 
        print(f"You won this competition in {5-attempts} attempts\nThe number was {rand_num}")
    elif won == False: 
        print("Better Luck Next time\n")  
    while want_to_play != 1 or want_to_play !=2:
        want_to_play = int(input("\nDo you want to play\n 1)Yes\n 2)No\n 3) Leader Board\n Your Input -> "))
        if(want_to_play == 3):
            print(f"\n{dict}")
    