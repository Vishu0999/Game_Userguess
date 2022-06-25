import random
randNumber = random.randint(1,100)
userguess = None
guesses = 0
while userguess!= randNumber:
    guesses+= 1
    userguess = int(input("enter number\n"))
    if userguess == randNumber:
        print(f" you guessed it right in {guesses} guesses")
    else:
        if userguess>randNumber:
            print("you guessed it wrong 'the guess you made is larger then a number''")
        else:
            print("you guessed it wrong 'the guess you made is smaller then a number'")
with open ("gamescore.txt", "r") as f:
    gamescore = int(f.read())
        
if(guesses<gamescore):
    with open ('gamescore.txt', 'w') as f:
        f.write(str(guesses))





