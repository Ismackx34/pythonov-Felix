A,B,C,D = list(map(int,input().split()))
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
print(A,B,C,D)








# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())

# if B > C and D:
#     pass
# elif B > A:
#     pass
# elif (C + D) > (A + B):
#     pass
# elif C and D > 0:
#     pass
# elif A %2 == 0: 
#     pass
# else:
#     print("Valores nao aceitos")
# print("Valores aceitos")