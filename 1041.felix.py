x,y = list(map(float,input().split()))
if (x==0 and y==0):
  print("Origem")
elif (x==0 or y==0):
  print("Eixo X") if  y==0 else print("Eixo Y")
elif x>0:
  print("Q1") if y>0 else print( "Q4")
else:
    print("Q2") if y>0 else print("Q3")
    