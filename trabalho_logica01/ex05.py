conta = int(input('Número da conta: '))
saldo = float(input('Saldo: '))
debito = float(input('Débito: '))
credito = float(input('Credito: '))
saldoatual = saldo - debito + credito
if saldoatual >= 0:
    print(f'O proprietário da conta: {conta}')
    print('\033[34mTem o SALDO POSITIVO.\033[m')
    print(F'R${saldoatual:.2f}')
else:
    print(f'O proprietário da conta: {conta}')
    print('\033[31mTem o SALDO NEGATIVO\033[m')
    print(F'R${saldoatual:.2f}')