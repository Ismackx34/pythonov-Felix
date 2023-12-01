t = int(input())
cvt = 60
m = t // cvt
t %= cvt
h = m // cvt
m %= cvt
print(f"{h}:{m}:{t}")
