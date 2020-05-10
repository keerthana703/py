def passw():
    s=k=p=0;
    h=['&','*','$','@','!','#','$','%','^']
    b=input("enter your password:");
    if b.isupper():
        p=p+1;
    elif b.islower():
        s=s+1;
    elif b in h:
        k=k+1;
        print("valid passwrd");
    else:
        print("invalid one");
            
def username():
    a=input("enter your email id:");
    if '@' and '.' in a:
        if a[0]=='@':
            print("invalid username")
        else :
            print("valid username");
            passw();
    else:
        print('pls do proper');


username();
