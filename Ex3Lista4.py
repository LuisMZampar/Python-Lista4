n = int(input("Digite o número de alunos na turma: "))  # recebe o número de alunos como input

notas = []  # cria uma lista vazia para armazenar as notas
contagem_abaixo_5 = 0  # inicializa o contador de alunos abaixo de 5
contagem_acima_5 = 0  # inicializa o contador de alunos acima de 5

for contador in range(n):
    nota = float(input(f"Digite a nota do aluno {contador+1}: "))  # recebe a nota de cada aluno como input
    notas.append(nota)  # adiciona a nota na lista de notas
    
    if nota < 5.0:  # verifica se a nota é menor que 5.0
        contagem_abaixo_5 += 1  # adiciona 1 ao contador de alunos abaixo de 5
    elif nota >= 5.0:  # verifica se a nota é maior ou igual a 5.0
        contagem_acima_5 += 1  # adiciona 1 ao contador de alunos acima de 5

media = sum(notas) / n  # calcula a média das notas da turma

print(f"A média da turma é: {media:.2f}")
print(f"Número de alunos com nota abaixo de 5.0: {contagem_abaixo_5}")
print(f"Número de alunos com nota igual ou acima de 5.0: {contagem_acima_5}")