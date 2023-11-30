
a = int(input())
b = int(input())
c = float(input())
d = (b * c)
e = format(d, ".2f")
print(f"NUMBER = {a}\nSALARY = U$ {e}")

#optimizaed version 

a = int(input())
b = int(input())
c = float(input())
print(f"NUMBER = {a}\nSALARY = U$ {(b  * c):.2f}")

