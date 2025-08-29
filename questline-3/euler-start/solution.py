#1#Question no. 2
def fib_sum()->int :
    a:int = 1
    b:int = 2
    sum:int = 2
    
    limit : int = 40_00_000
    
    while b <= limit :
        a,b = b,a+b 
        
        if not (b&1):
            sum += b 
        
    return sum 

#2# Question no. 9

def py_triplet()->int :
    
    for a in range(1,(1000//3)+1):
        b :int = (1000*(500-a))//(1000-a)
        c:int = 1000 - a - b 
        
        if a**2 + b**2 == c**2 :
            break 
    
    return a*b*c            #type:ignore

