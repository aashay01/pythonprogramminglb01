#Aashay Bhoyar
#grno-11810789
rollno-04(M div)
#outcome of rolling of a dice using function
# #import random
from random import randint as rt
out=0
faces=6
dice=3
for roll in range(0,dice):
    out+=rt(1,faces)
print(out)