salariofx = float(input('Salario fixo: '))
vendas = float(input('Valor das vendas: '))
comissão = 0
if vendas <= 1500:
    comissão += 1500 * 0.03
if vendas > 1500:
    extra = vendas - 1500
    comissão += 1500 * 0.03
    comissão += extra * 0.05
total = salariofx + comissão
print(f'O salario total é R${total:.2f}.')
