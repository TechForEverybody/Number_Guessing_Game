import random
print("*"*10,"Number Guessing game","*"*10,"\n")
with open("Highscore.txt") as f:
    HighScore=int(f.read())
print(f"\tlast Highscore is {HighScore}\n")

r=random.randint(1,100)
userguess=None
NumberOfGuesses=0
while(r!=userguess):
    userguess=int(input("enter your number : "))
    if userguess==r:
        print("Your Guess is Right")
    else:
        if userguess<r:
            print("you guess the wrong number ! please think about Larger number")
        else:
            print("you guess the wrong number ! please think about Smaller number")
    NumberOfGuesses+=1
print(f"You guess the number in {NumberOfGuesses} Guesses")
if HighScore>NumberOfGuesses:
    print("You have Broken the last highscore \n")
    with open("Highscore.txt","w") as f:
        f.write(str(NumberOfGuesses))

print("\n\n"+"*"*10,"Number Guessing game","*"*10)