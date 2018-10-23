#aashay-bhoyar
#gr no.-11810789
#roll no-04(M div.)
#factorial of a no.
num=int(input())
total=1
if num<0:
    print("invalid")
elif num==0:
    print("factorial is 1")
else:
    while num>0:
        total=num*total
        num=num-1
    print("factorial is total",total)
