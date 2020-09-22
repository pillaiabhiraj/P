# l=list(map(int,))
def fib(n):
    if n <= 1 :
       return n 
    else:
        return fib(n-1) + fib(n-2)

def SieveOfEratosthenes(): 
    n=100000
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 

                prime[i] = False
        p += 1
    c=[]  
    for p in range(2, n+1): 
        if prime[p]: 
            c.append(p)
    return c 


N=int(input())
arr=[]
prime2 = SieveOfEratosthenes() 
# print(prime2)
if(N%2&1):
    print(fib(N//2+1))
else:
    print(prime2[N//2-1])