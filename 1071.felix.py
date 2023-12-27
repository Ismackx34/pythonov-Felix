x = int(input())
y = int(input())

sum=0
i=y+1

while i<x:
    if i%2!=0:
        sum=sum+i
    i = i+1

        

print(sum)