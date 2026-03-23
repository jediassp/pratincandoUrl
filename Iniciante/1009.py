"""
Desafio calcula o salário total de um funcionário com base no salário fixo
    e em uma comissão de 15% sobre o total de vendas.

    Entradas:
        nome (str): Nome do funcionário (não utilizado no cálculo)
        salario (float): Salário fixo
        totalVendas (float): Valor total das vendas realizadas

    Saída:
        Exibe o salário total formatado com duas casas decimais.
"""

# Lê o nome do funcionário (não é usado no cálculo, mas pode ser útil para identificação)
nome = input()

# Lê o salário fixo do funcionário e converte para número decimal (float)
salario = float(input())

# Lê o total de vendas realizadas pelo funcionário e converte para float
totalVendas = float(input())

# Calcula o salário final:
# salário fixo + 15% de comissão sobre o total de vendas
aumentoSalario = salario + (totalVendas * 0.15)

# Exibe o resultado formatado com duas casas decimais
print('TOTAL = R$ {:.2f}'.format(aumentoSalario))