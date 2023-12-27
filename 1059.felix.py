def even(n):
    if n%2==0 and n!=100:
        print(n)
    if n == 100:
        return print(n)
    return even(n+1)

even(1)