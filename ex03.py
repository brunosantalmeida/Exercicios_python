# dissecando uma variavel

a = input('Digite algo: ')
print('O tipo primitivo de valor e ',type(a))
print('So tem espaço?', a.isspace())
print('E um numero?', a.isnumeric())
print('E um alfabeto?', a.isalpha())
print('E um alfanumerico',a.isalnum())
print('Estar em maiuscula',a.isupper())
print('Esta em minuscula',a.islower())
print('Estar capitalizada',a.istitle())