
def main(text:str)->None:
    d:dict = {}
    p : str = r'''!()-[]{};:'"|\,<>./?@#$%^&*_~'''
    
    text = text.lower()
    for i in text:
        if i in p:
            text = text.replace(i,'')
    
    for i in text.split():
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += 1
    
    for i,j in sorted(d.items(),key=lambda x: x[1],reverse=True):
        print(f'{i} -> {j}')
    
