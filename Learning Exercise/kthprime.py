#print kth prime from n:

def Isprime(n): 
    flag=True
    for i in range(2,n**1/2):
         if n%i==0:
             flag=False
             break
    return flag

def nprimes(N):
    count=0

    while(count!=k):
        N+=1
        if(Isprime(N)):
            print(N)
            count+=1
            
        
    
    
            
N=input("enter the number N:")
k=input("enter the value k:")
nprimes(N)