import random
def dies():
    a=random.randint(1,6);
    print(a);
i=1;
c=['yes','Yes','YES','S']
d=['NO','No','no','x']
while(i<10):
    a=input("give any input (YES /yes/Yes/S): ");
    if a in c:
        dies();
    else:
        if a in d:
            print("play again");
            break
    i=i+1;
   
