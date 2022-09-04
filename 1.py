n = int(input())
while n >= 10:
    m = 0
    while n != 0:
        k = n % 10
        n //= 10
        m += k
    n = m    
print(n)        
