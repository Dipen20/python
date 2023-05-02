import random
print("Welcome to the Rock,paper,scissor game")
user_choice=int(input("Enter your choice .. '0' for rock '1' for paper '2' for  scissor\n"))

computer_choice=random.randint(0,2)
print(f"computer_choice is {computer_choice}")
print(f"Your choice is {user_choice}")
if user_choice>2  or user_choice<0:
        print("You entered invalid! number please enter valid number\n")

elif user_choice==1 and computer_choice==0:
        print("Paper covers the rock so you won ")
elif user_choice==2 and computer_choice==1:
        print("Scissor crush the paper so you won")
elif user_choice==0 and computer_choice==2:
        print("Rock smash scissor so you won")
elif user_choice==computer_choice:
        print("Its draw play again")
else:
        print("Computer wins!")


