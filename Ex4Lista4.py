n = int(input("Digite a quantidade de números da sequência: "))

numeros = []

for contador in range(n):
    numero = float(input(f"Digite o {contador+1}º número: "))
    numeros.append(numero)

qtd_positivos = 0
qtd_negativos = 0

for numero in numeros:
    if numero > 0:
        qtd_positivos += 1
    elif numero < 0:
        qtd_negativos += 1

print(f"Quantidade de números positivos: {qtd_positivos}")
print(f"Quantidade de números negativos: {qtd_negativos}")