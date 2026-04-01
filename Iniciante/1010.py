'''
Desafio neste problema, deve-se ler o código de uma peça,  número de peças e o valor unitário de cada peça.

Entrada
O arquivo de entrada contém duas linhas de dados, em cada linha entrara os 3 valores, 1 a peça 2 quantidade e 3 preço da peça.
respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço
após os dois pontos um espaço após o "R$" mais um espaço conforme nos exemplo de saida. O valor deverá ser apresentado com 2 casas após o ponto decimal.

    >>> 12 1 5.30
    >>> 16 2 5.10
    VALOR A PAGAR: R$ 15.50

    >>> 13 2 15.30
    >>> 161 4 5.20
    VALOR A PAGAR: R$ 51.40

    >>> 1 1 15.10
    >>> 2 1 15.10
    VALOR A PAGAR: R$ 30.20
'''
# Lê a primeira linha de entrada e separa os valores por espaço
# Exemplo de entrada: "12 1 5.30"
entra1 = input().split()

# Lê a segunda linha de entrada e separa os valores por espaço
# Exemplo de entrada: "16 2 5.10"
entra2 = input().split()

# Cálculo do valor total:
# entra1[1] → quantidade do primeiro produto
# entra1[2] → preço do primeiro produto
# entra2[1] → quantidade do segundo produto
# entra2[2] → preço do segundo produto
#
# Multiplica quantidade × preço de cada produto e soma os resultados
result = float(entra1[1]) * float(entra1[2]) + float(entra2[1]) * float(entra2[2])

# Exibe o resultado formatado com duas casas decimais
print('VALOR A PAGAR: R$ {:.2f}'.format(result))