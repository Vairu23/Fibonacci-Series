num=eval(input("Enter a number"))
a=0
b=1
if (num==1):
    print(a,sep='\n')
elif (num==2):
    print(a,b,sep='\n')
else:
    print(a,b,sep='\n')
    for i in range(3,num+1):
        x=a+b
        print(x,sep='\n')
        a=b
        b=x
