cpf = int(input("Informe cpf 9: "))

soma = 0
mult = 2
cpf_copia = cpf

while cpf > 0:
    digito = cpf % 10
    soma = soma + digito * mult
    cpf = cpf // 10
    mult = mult + 1

resto = soma % 11
if resto < 2:
    digito_controle_1 = 0
else:
    digito_controle_1 = 11 - resto

    print(cpf_copia)
    print(digito_controle_1)

#juntando o cpf9 com o 1 digito de controle 
cpf = cpf_copia * 10 + digito_controle_1

mult = 2
soma = 0
while cpf > 0:
    digito = cpf % 10
    soma = soma + digito * mult
    cpf = cpf // 10
    mult = mult + 1

resto = soma % 11
if resto < 2:
    digito_controle_2 = 0
else:
    digito_controle_2 = 11 - resto

print("{}{}".format(digito_controle_1, digito_controle_2))