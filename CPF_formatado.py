cpf = int(input("Informe o cpf: "))

controle = cpf % 100
nove_digitos = cpf // 100

ultimo_tres = nove_digitos % 1000
seis_digitos = nove_digitos // 1000
meio_tres = seis_digitos % 1000
inicio_tres = seis_digitos // 1000

print(f"{inicio_tres:03d}.{meio_tres:03d}.{ultimo_tres:03d}-{controle:02d}")


