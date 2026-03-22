quant = int(input('Quantidade de maçãs : '))
total = 0
if quant >= 12:
    total = quant * 1
else:
    total = quant * 1.3
print('--'*20)
print(f'Total da compra : R${total:.2f}')

