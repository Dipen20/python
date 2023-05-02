#prime checker
def prime_checker(number):

        if number%2==1: #if the remainder 1 then the number is prime 
                print("the number is prime number\n")
        else:           #if the remainder 0 then the numnber isnot prime number
                print("The number isnot a prime number")

n=int(input("Enter the number\n"))
prime_checker(number=n)