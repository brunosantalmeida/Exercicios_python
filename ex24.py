# procurando uma string dentro de outra 

nome = str(input('Qual e seu nome completo? ')).strip()
print('Seu nome tem silva? {}'.format('Silva' in nome.lower()))