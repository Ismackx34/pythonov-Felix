d = int(input())
a = d // 365
d %= 365
m = d // 30
d %= 30
print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")

