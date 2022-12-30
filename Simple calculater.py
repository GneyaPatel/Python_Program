#1.
a=int(input("enter first value : "))
b=int(input("enter second value : "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

#2.
a=int(input("enter first value : "))
b=int(input("enter second value : "))
operator=input("which operation you want")
if operator=="+":
    print(a," + ",b," = ",a+b)
elif operator=="-":
    print(a," - ",b," = ",a-b)
elif operator=="*":
    print(a," * ",b," = ",a*b)
elif operator=="/":
    print(a," / ",b," = ",a/b)
elif operator=="**":
    print(a," ** ",b," = ",a**b)
elif operator=="//":
    print(a," // ",b," = ",a//b)
    