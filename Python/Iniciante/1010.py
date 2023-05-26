# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

peca1 = input().split()
codigoPeca1 = int(peca1[0])
numeroPeca1 = int(peca1[1])
valorUnitario1 = float(peca1[2])

peca2 = input().split()
codigoPeca2 = int(peca2[0])
numeroPeca2 = int(peca2[1])
valorUnitario2 = float(peca2[2])

print(
    f'VALOR A PAGAR: R$ {(valorUnitario1 * numeroPeca1) + (valorUnitario2 * numeroPeca2):.2f}')
