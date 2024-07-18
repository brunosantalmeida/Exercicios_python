# conversor de moeda

real = float(input('Quanto dineiro voce tem na carteira? R$'))
dolar = real  / 3.27
print('Com R${:.2f}voce pode compra US${:.2f}'.format(real,dolar))