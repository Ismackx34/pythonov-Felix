a,b,c,d = map(int, input().split())

x=b + 60*a
y=d + 60*c
r= y-x

if r<=0:
  r=r+24*60

h= r//60
k=r%60

print(f"O JOGO DUROU {h} HORA(S) E {k} MINUTO(S)")
