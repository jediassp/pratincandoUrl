'''
Desafio 1002, nome Área do Círculo
> Efetuar o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por n.
> Fórmula para calcular a área de uma circunferência:
área = n.raio2, considerando para este problema n = 3,14159.
> A entrada contém um valor de ponto flutuante, no caso, a variável 'raio'.
> Saída deve apresentar  mensagem "A=" seguida pelo valor área com 4 casas após o ponto decimal.
>1 crio a variável N = 3.14159.
>2 método de entrada de dados pelo teclado que recebe um str e apos converte para float.
>3 crio a variável 'área' que recebe o valor de N multiplicado
pelo valor do raio ao quadrado.
>4 imprimo a mensagem "A=" com o valor contido na variável 'área'
defino quantidade de casas decimais após o ponto sem espaços.
'''
N = 3.14159#valor da const N.
raio = float(input())#entrada de dados "2.00, 100.64, 150.00".
area = N*(raio**2)# variavel recebe valor de N vezes valor do raio ao quadrado.
print("A="f"{area:.4f}")#mensagem com o valor da variavel de 'area'  e define numero de  casas decimais após ponto.