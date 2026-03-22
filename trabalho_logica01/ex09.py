morango = float(input('Kg de morango: '))
maca = float(input('Kg de maçã: '))

if morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total = (morango * preco_morango) + (maca * preco_maca)

peso_total = morango + maca

if peso_total > 8 or total > 25:
    total *= 0.9

print(f'Total a pagar: {total}')