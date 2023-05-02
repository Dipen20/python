#blackjack games
import random
deck=(1,2,3,4,5,6,7,8,9,10,11)
print("First user show\n")
u1=random.choice(deck)
print(f"The first user card is: {u1}")
print("Its time to  show the dealer card\n")
d1=random.choice(deck)
print(f"The dealer card is: {d1}")
u2=random.choice(deck)

print(f"Your second card is {u2}")

choic=input("Do you want to 'hit' or 'stand'\n").lower()
d3=random.choice(deck)
u3=random.choice(deck)
d4=random.choice(deck)
if choic=='stand':
    print(d3)
    print(u3)
    td=d1+d3
    tuser=u1+u2

    
    print(f"Second card of dealer: {d3}")
   
    print(td,tuser)
    if tuser>td:
        print("you won")
    elif tuser<td:
        print("Dealer won")
    elif tuser>21 and td<=21:
        print("dealer won")
    elif tuser<=21 and td>21:
        print("You won")
    elif tuser==td:
        print("Its draw")       
if choic=='hit':
    u4=u1+u2+u3
    d5=d1+d3+d4
    
    
    if choic=='stand':
        print(d5)
        if u4>21 and d5<21:
            print('dealer won')
        elif u4<21 and d5>21:
            print("You won")
        elif u4>d5:
            print('you won')
        elif d5>u4:
            print('dealer won')
        elif u4==d5:
            print("it's draw")
        elif u4==21 and d5!=21:
            print("you won with the blackjack")
        elif d5==21 and u4!=21:
            print("Dealer won with black jack")
        print(f"your card is {u3} and your total card number is {u4}")




    






