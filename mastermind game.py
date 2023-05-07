#welcome to the mastermind game
import random
num=random.randrange(10000,90000)
print(num)
user=int(input("Enter 5 digit numbers\n"))


if (user==num):
    print("Great! You have guessed in first try! You are mastermind\n")
else:
    ctr=0
    
    while (user!=num):
        ctr+=1
        count=0
        user=str(user)
        num=str(num)
        match=[]
        for i in range(0,5):
            if (user[i])==num[i]:
                count+=1
                match.append(user[i])
            else:
                continue
        if count<5 and count!=0:
            print(f"You havenot guessed all digita correct but you have guessed {count} digits correc\n")
            for k in match:
                print(k,end="")
            print()
            print()
            user=int(input("Enter your next choice number\n"))
        elif count==0:
            print("You have't guessed any digits correctr\n")
            user=int(input("Enter your next choice number"))

    if user==num:
        print("You have become mastermind")
        print(f"You have guessed all digits correct in {ctr} tries\n")


