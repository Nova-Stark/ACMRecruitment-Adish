
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
    
    
main('''Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 406 bytes | 406.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Nova-Stark/ACMRecruitment-Adish.git
   db8cfe6..c478974  main -> main''')