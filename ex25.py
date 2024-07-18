# primeira e ultima ocorrencia de uma string

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra a aparecer {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posiçao {}'.format(frase.find('A')+1))
print('A uĺtima letra aparece na posiçao {}'.format(frase.rfind('A')+1))