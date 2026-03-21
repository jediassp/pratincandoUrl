"""
Desafio: Cálculo de Salário de Funcionário

Descrição:
Este programa lê o número de matrícula de um funcionário, a quantidade de horas
trabalhadas e o valor recebido por hora. Em seguida, calcula o salário total
do funcionário.

Fórmula utilizada:
SALÁRIO = Horas Trabalhadas * Valor por Hora

Entrada:
- Um número inteiro representando a matrícula do funcionário
- Um número inteiro representando as horas trabalhadas
- Um número decimal representando o valor por hora trabalhada

Saída:
Exibe:
- O número da matrícula
- O salário calculado com duas casas decimais

Formato da saída:
NUMBER = <matricula>
SALARY = U$ <valor>

Exemplo:
Entrada:
25
100
5.50

Saída:
NUMBER = 25
SALARY = U$ 550.00
"""

# Leitura da matrícula do funcionário (inteiro)
matricula = int(input())

# Leitura da quantidade de horas trabalhadas (inteiro)
HoraTrab = int(input())

# Leitura do valor por hora (float)
valorHoraTrab = float(input())

# Exibe o número da matrícula
print('NUMBER = {}'.format(matricula))

# Calcula e exibe o salário com duas casas decimais
print('SALARY = U$ {:.2f}'.format(HoraTrab * valorHoraTrab))