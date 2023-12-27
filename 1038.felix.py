a,b = list(map(int,input().split()))  
price = [0,4,4.5,5,2,1.5]
pay = price[a]*b
print(f"Total: R$ {pay:.2f}")

