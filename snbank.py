import random
level = input("choose level:\n1:EASY\n2:MEDIUM\n3:HARD\nEnter Option:  ")

if(level=='1'):
    print("Difficulty: EASY")
    count=0
    luckynumber = random.randint(1,10)
    while(True):
        guess=int(input('Choose a number between 1 and 10...You have 6 trials '))

        if(guess>0 and guess<=10):

            if(guess==luckynumber):
                print('You Won the game')
                break
            else:

                count+=1
                if(count>=6):
                    print('Lost.... Game over')
                    break
                else:
                    print('Lost.... Try Again\nNumber of trials: '+str(count)+"\n")
                    continue
        else:
            print("Your guess is out of range!!!\n")
            continue

elif(level=='2'):
    print("Difficulty: MEDIUM")
    count=0
    luckynumber = random.randint(1,20)
    while(True):
        guess=int(input('Choose a number between 1 and 20...You have 4 trials '))

        if(guess>0 and guess<=20):

            if(guess==luckynumber):
                print('You Won the game')
                break
            else:

                count+=1
                if(count>=4):
                    print('Lost.... Game over')
                    break
                else:
                    print('Lost.... Try Again\nNumber of trials: '+str(count)+"\n")
                    continue
        else:
            print("Your guess is out of range!!!\n")
            continue
elif (level == '3'):
    print("Difficulty: HARD")
    count=0
    luckynumber = random.randint(1,50)
    while(True):
        guess=int(input('Choose a number between 1 and 10...You have 6 trials '))

        if(guess>0 and guess<=50):

            if(guess==luckynumber):
                print('You Won the game')
                break
            else:

                count+=1
                if(count>=3):
                    print('Lost.... Game over')
                    break
                else:
                    print('Lost.... Try Again\nNumber of trials: '+str(count)+"\n")
                    continue
        else:
            print("Your guess is out of range!!!\n")
            continue
else:
    print("Start Program again")
