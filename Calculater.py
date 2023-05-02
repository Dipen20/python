import math
def add(N1,N2):
        return (N1+N2)

def sub(N1,N2):
        return(N1-N2)


def mul(N1,N2):
        return(N1*N2)


def div(N1,N2):
        return(N1/N2)

def mod(N1,N2):
        return N1%N2

def exp(N1,N2):
        return math.pow(N1,N2)

N1=int(input("Enter the first number\n"))
N2=int(input("Enter the second number\n"))


operators=input("which operation do you want '+','-','*','/','%','^' \n")



if operators=='+':

       result=add(N1,N2)
       print(result)
elif operators=='-':
        result=sub(N1,N2)
        print(result)
elif operators=='*':
        result=mul(N1,N2)
        print(result)
elif operators=='/':
        result=div(N1,N2)
        print(result)
elif operators=='%':
        result=mod(N1,N2)
        print(result)
elif operators=='^':
        result=exp(N1,N2)
        print(result)
elif operators not in ['+','-','*','/','%']:
        print("Invalid operation! please enter valid operation")

