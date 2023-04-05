#Fibonacci

n = int(input("Informe n: "))

if n <= 2:
    print(1)
else:
    anterior = 1
    atual = 1
    contador = 3
    
    while contador < n:
        prox = atual + anterior
        anterior = atual  
        atual = prox
        contador = contador + 1

print(atual)