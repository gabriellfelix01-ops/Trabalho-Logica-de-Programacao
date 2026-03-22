litros = float(input("Litros: "))
tipo = input("Tipo (A-álcool / G-gasolina): ").upper()

if tipo == "A":
    preco = 2.90
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
else:
    preco = 3.30
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

total = litros * preco
valor_final = total - (total * desconto)

print("Total a pagar:", valor_final)