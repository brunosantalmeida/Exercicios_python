# nome e sobrenome de uma pessoa 

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[-1]))