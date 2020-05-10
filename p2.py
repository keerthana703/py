#prime numbers
a=int(input());
print('number:',a);
l = []
for a in range(0,a+1):
    if a>1:
    
        for i in (2,a):
            if a%i==0:
                break 
            else:
                print(a,end=" ")
                l.append(a)
                
print("\n{} prime numbers are there till {}".format(len(l),a) )              
                
