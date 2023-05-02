#word guessing game
import random
Name=input("Enter your name\n")

print(f"Hi {Name}, Best of luck")
#creatig the words
def words():
    ch_word=["Messi","Mountain","Nepal","paraskhadka","mteverest","ghorahi","dipendra","khanal","rukum","bsccsit","python"]
    #it chooses the random word from the list
    word=random.choice(ch_word).lower()
    return word


word=words()

guesses=""
#creating turns that how much user can try to guess if user failed to guess..
turns=10
# Some code here
while turns>0:
    wrong_guess=0
    #it generates the each word from the list
    for char in word:
        #checking whether the guessed character is in list or not
        if char in guesses:
            print(char) #if guessed character in word then print the charcter
        else:
            print("_")#if no then print the given data and increase the wrong guesses by 1
            wrong_guess+=1

    if wrong_guess==0:
        print("Your guess correct\n")

        print(f"The word is {word}")
        #if user wants to play again or not ..is yes then continue and if no then break the statememt
        choice=input("Would you like to play again.\n Type 'y' for yes and 'n' for no\n")
        if choice=='y':
            guesses=""
            turns=10
            word=words()
            continue
        else:
            break
    
    #giving character input 
    guess=input("Guess the character:  ")
    #every guess character willbe stored in guesses variable
    guesses+=guess

#if guesses character is not in the word then you will get chance to guess again,.It depends on how much turns number you have declared 


    if guess not in word:
        turns-=1
        print("Your guess is wrong")
        print(f"You have {turns} left")
    

#if users turns becomes 0 then user will lose
    if turns==0:
        print("You lose")


        choice=input("Would you like to play again.\n Type 'y' for yes and 'n' for no\n")
        if choice.lower()=='y':
            word=words()
            guesses=''
            turns=10
            continue
        else:
            break