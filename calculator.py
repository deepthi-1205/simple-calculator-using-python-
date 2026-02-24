while True:
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=input("enter the operation ( + - * % / ^):")

    if(c=="+"):
        print(a+b)
    if(c=="-"):
        print(a-b)
    if(c=="*"):
        print(a*b)
    if(c=="%"):
        print(a%b)
    if(c=="/"):
        if(b==0):
            print("invalid operation ")
            continue
        print(a/b)
    if(c=="^"):
        print(a**b)
    d=input("if you want to continue:(yes/no)")
    if(d!="yes"):
        print("Thank you")
        break
    
    
 

