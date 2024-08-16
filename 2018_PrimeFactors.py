N = 1
x = int(input('Enter number'))
while N<x:
##    N = int(input())

    def isPrime(n):
        if n==1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
                break
        else:
            return True
        
    def factNo(N, x):
        count = 0
        temp = N
        
        while True:
            if temp%x==0:
                count += 1
                temp//=x
            else:
                break
            
        return count

    result = f'{N} = '

    for i in range(1,N//2+1):
        if isPrime(i) and N%i==0:
            fact = factNo(N,i)
            if fact==1:
                result += f'{i} X '
            else:
                result += f'{i}^{fact} X '
          
    result = result[:-3]
    print(result)
    N+=1