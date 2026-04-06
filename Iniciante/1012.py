'''Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C.
Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor.
O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.'''

# Lê uma linha de entrada e separa os valores pelo espaço
T = input().split(' ')

# Converte os valores para float (números reais)
A = float(T[0])
B = float(T[1])
C = float(T[2])

# Define o valor de pi
pi = 3.14159

# Calcula a área do TRIÂNGULO (base A e altura C)
TRIANGULO = (A * C / 2)

# Calcula a área do CÍRCULO (raio C)
CIRCULO = pi * (C ** 2)

# Calcula a área do TRAPÉZIO (bases A e B, altura C)
TRAPEZIO = ((A + B) * C) / 2

# Calcula a área do QUADRADO (lado B)
QUADRADO = B ** 2

# Calcula a área do RETÂNGULO (lados A e B)
RETANGULO = A * B

# Imprime os resultados formatados com 3 casas decimais
print('TRIANGULO: {:.3f}'.format(TRIANGULO))
print('CIRCULO: {:.3f}'.format(CIRCULO))
print('TRAPEZIO: {:.3f}'.format(TRAPEZIO))
print('QUADRADO: {:.3f}'.format(QUADRADO))
print('RETANGULO: {:.3f}'.format(RETANGULO))