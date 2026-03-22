nome = (input('Nome: '))
altura = float(input('Altura: '))
while True:
    sexo = str(input('Sexo: [m/f]')).strip().lower()
    if sexo in 'mf':
        break

if sexo == 'm':
    pideal = (72.7 * altura) - 58

else:
    pideal = (62.1 * altura) - 44.7
print(f'{nome}, o seu peso ideal é {pideal:.2f} kg.')
