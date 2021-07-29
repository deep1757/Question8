for i in range(int(input())):
    a,b,c=map(int,input().split())

    if(c%2!=0):
            a=a*2
            b=b
            if(a>b):
                print(a//b)
            else:
                print(b//a)        
    else:
        a=a
        b=b
        if(a>b):
            print(a//b)
        else:
            print(b//a)