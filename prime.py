# Hello World program in Python
    
N = int(raw_input())
b = [True]*(N-1)
p = 2
multiples = 1

while p <= int(N**(0.5)):
    
    multiplier = 2

    while multiples <= N:
        multiples = p * multiplier
        
        if multiples > N:
            break
        
        
        print(multiples)
        
        b[multiples - 2] = False
        print(b)
        
        multiplier += 1
        
    p += 1
    multiples = 1

print(b)

for x in range(len(b)):
    if b[x] == True:
        print(x+2)
        
        
        
  
