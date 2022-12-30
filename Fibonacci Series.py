a=int(input("enter no. for fibonacci :"))
def fibonacci(a):
    if a==1:
        return(0)
    elif a==2:
        return(1)
    else:
        return(fibonacci(a-2)+fibonacci(a-1))
for i in range(1,a+1):
    print(fibonacci(i))