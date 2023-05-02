#guess the number user will get 3 chance to guess 
a=6
for n in range(0,3):
    guess=int(input("Guess the number\n"))
    if guess==a:
        print("You guessed it right")
        break
    elif guess<a:
        print("Your guessed number is wrong. please guess the higher number")
    elif guess>a:
        print("Your guessed number is wrong. please guess lower number")
else:
    print("Sorry your limitation is over")


