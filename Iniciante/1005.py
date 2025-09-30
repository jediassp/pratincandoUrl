'''
Desafio ler duas notas com ponto flutuante, calcular a media entre elas sendo que a primeira nota tera o peso 3.5 e a segunda tera o peso de 7.5 e os pontos somado correspondem ao valor de 11, o resultado deve ter a mensagem MEDIA =  com os espaços e 5 casas decimais apos a virgula.
1 - ler o valor com ponto flutuante.
2 - calculo o valor da nota com o peso da nota.
3 - somar o resultado das duas medias e dividir por 11 dentro da função de saida.
'''

a = float(input())
b = float(input())
media_1 = a*3.5
media_2 = b*7.5
print('MEDIA = {:.5f}'.format((media_1+media_2)/11))