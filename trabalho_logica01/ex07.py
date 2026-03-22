produto = input("Nome do produto: ")
qtd = int(input("Quantidade: "))
preco = float(input("Preço unitário: "))

total = qtd * preco

if qtd <= 5:
    desconto = 0.02
elif qtd <= 10:
    desconto = 0.03
else:
    desconto = 0.05

valor_final = total - (total * desconto)

print(f'Total : {total}')
print(f'Desconto: {total * desconto:.2f}')
print(f'Total a pagar: {valor_final}')