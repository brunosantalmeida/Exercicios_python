# reajuste salarial

salário = float(input('Qual é o salário do Funcionario? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionario que ganhava R${}, com 15% de aumento passa a receber R${}'.format(salário, novo))