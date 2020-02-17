class bnk:
    def deposit(self,i=0):
        print("Let the initial amount be 0")
        c=int(input("enter the amount to be deposited:" ))
        self.i = i+c
        print("your account balance is:",self.i);
        return self.i
    def withdraw(self,i=0):
        print("withdrawal")
        d=int(input("enter the amount"))
        self.i =self.i-d
        print("your account balance is:",self.i)
        return self.i
k=1;
s=bnk()
print("1.deposit","2=withdraw");
while(k>=1):
    b=int(input("Enter your choice"));
    if b==1:
        s.deposit()
           
    elif b==2:
        s.withdraw()
        print("THANK YOU..! VISIT AGAIN")
        if s.i==0:
            print("No Balance...!")
    else :
        print("Enter the valid one")
k=k+1
