# Imagine que você está em uma viagem para os Estados Unidos e precisa converter o valor em reais para dólares. Crie um programa que receba o valor em reais e a taxa de câmbio atual, e exiba o valor equivalente em dólares.
reais=float(input("quantos reais você tem?"))
taxac=0.18
conversao= (reais*taxac)
print(f"você tem U$ {conversao}")