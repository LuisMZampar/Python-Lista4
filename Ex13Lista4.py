import random

numero_sorteado = random.randint(1, 1000)
chutes = 0

while True:
    chute = int(input("Digite um número entre 1 e 1000: "))
    chutes += 1
    
    if chute == numero_sorteado:
        print(f"Parabéns, você acertou o número em {chutes} chutes!")
        break
    elif chute < numero_sorteado:
        print("O número sorteado é maior que o seu chute.")
        print("----------------")
    else:
        print("O número sorteado é menor que o seu chute.")
        print("----------------")
