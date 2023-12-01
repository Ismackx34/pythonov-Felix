#como pude omitir poner ",00" y  se ponen automaticamente los puntos decimales ".00"
a = int(input())
print(a)
for i in [100, 50, 20, 10, 5, 2, 1]:
    b = a//i
    print(f"{b} nota(s) de R$ {i:.2f}")
    a = a % i
    
#con como en vez de punto decimal // como lo solicita el ejercicio de la plataforma
a = int(input())
print(a)
for i in [100, 50, 20, 10, 5, 2, 1]:
    b = a//i
    print(f"{b} nota(s) de R$ {i},00")
    a = a % i