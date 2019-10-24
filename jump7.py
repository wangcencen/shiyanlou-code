a=1
while a<=100:
    a = a+1
    if a%10==7:
        continue
    elif a//10==7:
        continue
    elif a%7==0:
        continue
    print(a)

