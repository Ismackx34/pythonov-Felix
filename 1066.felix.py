p = 0
n=0
e=0
d=0

for i in range(5):
  m= float(input())
  if m>0:
    p=p+1
  if m<0:
    n=n+1
  if m%2==0:
    e=e+1
  if m%2!=0:
    d=d+1
    
print(f"{e} valor(es) par(es)")
print(f"{d} valor(es) impar(es)")   
print(f"{p} valor(es) positivo(s)")
print(f"{n} valor(es) negativo(s)")
