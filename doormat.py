def doormat(row,column):
    width=column
    
    for i in range(0,int(row/2)):
        pattern=".|." * (2*i+1)
        print(pattern.center(width,"-"))
        
    print("WELCOME".center(width,"-"))
    
    
    for i in range(int(row/2),0,-1):
        pattern=".|."*(2*i-1)
        print(pattern.center(width,"-"))
        

row,column=map(int,input().split())
if row%2!=0 and row>=1:
    column=row*3
    doormat(row,column)