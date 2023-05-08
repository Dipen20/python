#coffee machine
print("Welcome to coffee machine\n")
balance=int(input("How much money do you have\n"))
while balance>=60:
    name=input("Enter the coffee name\n")
    if name == "cappucino":
        price = 150
    elif name == 'latte':
        price = 60
    elif name == 'americano':
        price = 130
    else:
        print("Please enter correct name.")
        
    a=int(input("How much coffee do you want?\n"))
    if balance>=price*a:
        balance = balance - price*a
        print("There ois your coffee. Enjoy .🍵")
        print(f"Your remaining balance is: {balance}")
    else:
        print("Not enough money.")



    





  
          

