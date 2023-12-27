current = float(input())

if current <= 400:
    percentage = 15
elif current <= 800:
    percentage = 12
elif current <= 1200:
    percentage = 10
elif current <= 2000:
    percentage = 7
else:
    percentage = 4
    
earn = current*percentage/100
new = current+ earn

print(f'''Novo salario: {new:.2f}
Reajuste ganho: {earn:.2f}
Em percentual: {percentage} %''')
