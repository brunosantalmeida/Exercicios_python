# analisador de texto
 
nome = str(input('Digite seu nome completo:'))
print('analizando seu nome...')
print('seu nome em maiusculas e {}'.format(nome.upper()))
print('seu nome em minusculas e {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
nome.find(' ')