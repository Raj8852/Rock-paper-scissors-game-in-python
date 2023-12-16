import random                
l =[0,1,2]                                      # Here 0 = paper , 1 = rock , 2 = caesar
c=[]
g=[]
try:
    a = list(map(int,(input( "Here 0 = paper , 1 = rock , 2 = caesar.Enter your choice ").split())))
    for i in range(0,len(a)):
          if a[i]>=3:
              raise ValueError("Please Enter number between 0 To 2")
    for y in range(0,len(a)):
        b = random.choice(l)
        c.append(b)
    
    for t in range(0,len(a)):
        if a[t] == int(c[t]):
            g.append("DROW")
        elif int(a[t])== 0 and int(c[t]) == 1 :
            g.append("WIN")
        elif int(a[t])==1 and int(c[t])==2:
            g.append("WIN")       
        elif int(a[t])==2 and int(c[t])==0:
            g.append("WIN")
        else:
            g.append("LOST")
    print("Y" ,"C" ,"R")        # Y = You , C = computer , R = result
    for z in range(0,len(a)):
        print(a[z] ,c[z] , g[z])        
except ValueError as c:
    print("Error code: ",c)
    
               
