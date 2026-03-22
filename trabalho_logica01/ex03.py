horas_mes = float(input('Quantas horas total do mes: '))
salario_hr = float(input('Quanto vale a hora trabalhada?'))
total = 0
if horas_mes <= 160 :
    total = horas_mes * salario_hr

else:
    extra = horas_mes - 160
    acrescimo = salario_hr * 1.5
    total = (160 * salario_hr) + (extra * acrescimo)
print(f'O salário total do funcionario é R${total:.2f}.')

