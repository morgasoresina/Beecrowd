# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

valor = input().split()
valorA = int(valor[0])
valorB = int(valor[1])
valorC = int(valor[2])

# Função "max" retorna o maior valor
print(f'{max(valorA,valorB,valorC)} eh o maior')
