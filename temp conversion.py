#temperature fahrenheit and celcius 
print("Welcome to the fahrenheit, celcius temperatire calculator\n")
temp=float(input("Enter the temperature \n"))
unit=(input("Enter the unit of  the tempertaure('c or 'f')\n"))

if unit=='c':
        fahrenhit=(9/5) * temp + 32
        print(f"{temp}degree celciuse is equal to {fahrenhit}degree fahrenheit")
elif unit=='f':
        celcius=(temp - 32) * (5/9)
        print(f"{temp} degree fahrenheit is equal to {celcius} degree celcius")
else:
        print("You entered the invalid! temperature ..Please enter valid temperature")

        

