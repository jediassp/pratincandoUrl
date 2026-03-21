"""
Desafio : Cálculo de Diferença de Produtos

Descrição:
Este programa lê quatro valores inteiros fornecidos pelo usuário (A, B, C e D)
e calcula a diferença entre o produto de A e B e o produto de C e D.

Fórmula utilizada:
DIFERENCA = (A * B) - (C * D)

Entrada:
Quatro números inteiros, um por linha.

Saída:
Exibe o resultado no formato:
DIFERENCA = <valor>

Exemplo:
Entrada:
5
6
7
8

Saída:
DIFERENCA = -26
"""

# Leitura dos valores de entrada (convertidos para inteiro)
a = int(input())  # Primeiro valor
b = int(input())  # Segundo valor
c = int(input())  # Terceiro valor
d = int(input())  # Quarto valor



# Exibição do resultado formatado com cálculo da diferença entre os produtos
print('DIFERENCA = {}'.format((a*b)-(c*d)))