a1,b1 = list(map(float,input().split()))
a2,b2 = list(map(float,input().split()))
forml = (((a2 - a1)**2) +(b2 - b1)**2)**(1/2)
print(f"{forml:.4f}")
