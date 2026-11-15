a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a>b:
    temp = a
    a=b
    b=temp
    
    if b>c:
       temp = b
       b=c
       c=temp
       
       if a>b:
        temp = a
        a=b
        b=temp
    
    print("Number in ascending ordr: ")