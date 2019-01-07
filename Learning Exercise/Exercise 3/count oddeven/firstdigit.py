# First digit of the given integer:


def Firstdigit(N):

    count=0
    A=N
    while(N>0):
        N%10
        count+=1
        N=N//10

    count-=1
    X=(A//(10**count))

    return X


# Last digit of the given integer

def Lastdigit(N):

    X=N%10
    return X

if(Firstdigit(N)==Lastdigit(N)):
        print("First and last digit are same")


N=input("Enter the value of N: ")
Firstdigit(N)
Lastdigit(N)



    







