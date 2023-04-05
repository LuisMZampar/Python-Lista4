
n = int(input("Digite o número de alunos na turma: "))  # recebe o número de alunos como input

notas = []  # cria uma lista vazia para armazenar as notas

for contador in range(n):
    nota = float(input(f"Digite a nota do aluno {contador+1}: "))  # recebe a nota de cada aluno como input
    notas.append(nota)  # adiciona a nota na lista de notas

media = sum(notas) / n  # calcula a média das notas da turma

print(f"A média da turma é: {media:.2f}")  # imprime a média com duas casas decimais

