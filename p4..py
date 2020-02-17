import random;
a=random.randint(1,6)
def rans():
    i=1
    while(1<10):
        b=int(input("Enter any number"));
        if a==b:
            print("you win",a,'=',b);
        else:
            print("you lose",a,'not equal to',b);
            print("Try again...!")
            break
        i=i+1;
rans();
