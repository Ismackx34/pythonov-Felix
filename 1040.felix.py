A,B,C,D = map(float,input().split())
ag = (A*2+B*3+C*4+D*1)/(10)

print(f'Media: {ag:.1f}')
if ag >=7.0:
    print("Aluno aprovado.")
elif ag < 5.0:
    print("Aluno reprovado.")
elif ag >= 5.0 and ag < 7.0:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    ag2 = (ag+N)/2
    if ag2 >= 5.0:
        print("Aluno aprovado.")
        print(f'Media final: {ag2:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {ag2:.1f}')