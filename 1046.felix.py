A,B = map(int, input().split())

if (A<B):
  print(f"O JOGO DUROU {B-A} HORA(S)")
else:
  print(f"O JOGO DUROU {(B+24)-A} HORA(S)")
  