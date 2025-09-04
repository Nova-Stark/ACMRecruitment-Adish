
def main(text:str)->str:
    if not text:return ""
    
    p :str= ""
    
    def pp(l:int,r:int)->None:
        nonlocal p 
        while l>=0 and r < len(text) and text[l]== text[r]:
            if r-l+1 > len(p):
                p = text[l:r+1]
            l -= 1
            r += 1
            
    for i in range(len(text)):
        if len(text) & 1:
            pp(i,i)
        else:
            pp(i,i+1)
        
    return p 
