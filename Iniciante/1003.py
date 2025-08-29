'''
Desafio, criar duas variaveis que vao receber um valor intereiro cada, a seguir cria uma variavel que receba o
valor da soma, entao imprima a mensagem de saida 'SOMA = ' com o valor da variavel.
>Entrada 
duas a e b variaveis que recebem um valor por via teclado(input) e entao o converte para inteiro.
>Criar uma variavel que recebe a soma das variaveis.
>Saida
>Imprimir uma mensagem com a frase em maiusclo e um espaço entre soma, igualdade e apos igualdade 'SOMA = 'com a variavel.

>Valores de entrada.
> primeiro teste '30', '10'
> segundo '-30', '10'
> terceiro '0', '0'

'''
A = input("digite um valor")#entrada 
B = input("digite um valor")#entrada
SOMA = int(A)+int(B)#converte, soma e atribui a variavel soma 
print(f"SOMA = {SOMA}")# imprime a mensagem com o resultado.