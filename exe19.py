alunos, alunosa, alunose, alunosr = [], [], [], []
total = 0

for x in range(6):
    aluno = input("\nDigite o nome do aluno: ")
    alunos.append(aluno)
    n1 = int(input(f"Digite a N1 de {alunos[x]}: "))
    n2 = int(input(f"Digite a N2 de {alunos[x]}: "))
    media = (n1 + n2) / 2
    total += media
    print(f"\nA média de {alunos[x]} foi {media}")
    if media <= 3:
        alunosr.append(alunos[x])
        print(f"{alunos[x]} está reprovado(a)")
    elif media >= 4 and media <= 7:
        alunose.append(alunos[x])
        print(f"{alunos[x]} está de exame")
    else:
        alunosa.append(alunos[x])
        print(f"{alunos[x]} está aprovado(a)")

mediac = total / 6

print(f'''\nTotal de alunos aprovados: {len(alunosa)}
Total de alunos reprovados: {len(alunosr)}
Total de alunos de exame: {len(alunose)}
Média da classe: {mediac:.2f}''')