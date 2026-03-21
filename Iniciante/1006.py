'''
Desafio ler tres notas, calcular o peso de cada nota a seguir a media, sendo que o resultado devera ter um ponto 
flutuante.
1 - criar as variaveis que recebem as notas e trasnformalas e tipo float.
2 - calcular  o peso de cada nota.
3 - calcular a media e imprimir-la.
'''
a = float(input())
b = float(input())
c = float(input())
media_1 = a*2
media_2 = b*3
media_3 = c*5
print('MEDIA = {:.1f}'.format((media_1+media_2+media_3)/10))