import random

a=['a','b','c','1','4','6','8']
b=random.choice(a)
a=input("enter the alphabets\n")
if a==b:
    print(b)
    print("Your guess it right\n")
else:
    print(b)
    print("Sorry try again")