
def rot_bin(bits:str,k:int)->int:#type:ignore
    
    l:int = len(bits)#type:ignore
    
    n : int = k%l 
    
    bits:str = bits[-n:]+bits[:-n]
    
    return int(bits,2)

print(rot_bin('10110',2))
print(rot_bin('1001',5))
